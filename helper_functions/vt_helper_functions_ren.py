import renpy
from game.major_game_classes.character_related.Person_ren import Person
from game.main_character.MainCharacter_ren import mc
from typing import Union
from renpy import persistent, basestring

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 900 python:
"""
import math
import builtins

# helper function; if the person has a sex skill, she must have gotten it with someone
# returns name either random, SO_name, or MC
def _vt_cherry_popper(person, sex_kind: str) -> str | None:
    # was already assigned by something else
    if hasattr(person, sex_kind.lower() + "_first") and getattr(person, sex_kind.lower() + "_first") is not None:
        return getattr(person, sex_kind.lower() + "_first")
    # person is in a relationship with MC
    elif person.relationship != "Single" and person.SO_name is mc.name:
        return mc.name
    # person has a partner
    elif person.relationship != "Single" and person.SO_name:
        return person.SO_name
    # generate random value
    else:
        return Person.get_random_male_name()

def _vt_bounded_gaussian_int(lower=2, upper=8, mean=3.4, stdev=10/3) -> int:
    # NOTE: smaller window between lower and upper
    # (i.e. less area under the curve)
    # means (exponentially) longer while-loop
    value = int(lower) - 1
    while value < lower or value > upper:
        value = int(renpy.random.gauss(mean, stdev))
    return value

def _vt_is_virgin(person: Person, sex_kind: str) -> bool:
    if person.title == "Clone":
        # all clones are total virgins
        return True
    elif hasattr(person, sex_kind.lower() + "_first"):
        # if the person has e.g. "oral_first"=="some name", then is not virgin
        return getattr(person, sex_kind.lower() + "_first") is None
    elif hasattr(person, sex_kind.lower() + "_virgin"):
        # if person has e.g. "anal_virgin" > 0, then is not virgin
        # NOTE: vaginal_virgin == 1 is treated as virgin ("just the tip")
        return getattr(person, sex_kind.lower() + "_virgin") <= (1 if sex_kind=="Vaginal" else 0)
    elif person.type != "random":
        # story/unique characters might have sex skill assigned; base virginality on that
        return person.sex_skills[sex_kind] == (1 if sex_kind=="Vaginal" else 0)
    elif sex_kind == "Vaginal" and person.kids > 0:
        return False
    else:
        # TODO: make virginity likelihood granular
        # TODO: ADD a flag to enable defining person opinion on virgin likelihood in a VTMOD startup screen
        # TODO: Allow player to say min floor is 100%, 19 being 100%, etc... etc..
        # based on sex type (oral/vaginal/anal)?
        VIRGINITY_LIKELIHOOD_BY_AGE: dict[tuple[int | float], dict[str, float]] = {
            # (min age, max age):
            #     {sex kind, virginity probability},
            (-math.inf, Person.get_age_floor()):
                {"Oral": 1.0, "Vaginal": 1.0, "Anal": 1.0},
            ((Person.get_age_floor()+1), 19):
                {"Oral": 0.3, "Vaginal": 0.3, "Anal": 0.3},
            (20, 30):
                {"Oral": 0.3, "Vaginal": 0.3, "Anal": 0.3},
            (31, math.inf):
                {"Oral": 0.1, "Vaginal": 0.1, "Anal": 0.1},
        }
        for (min_age, max_age), virginity_probability in VIRGINITY_LIKELIHOOD_BY_AGE.items():
            if min_age <= person.age <= max_age:
                return renpy.random.random() < virginity_probability[sex_kind]
        # NOTE: should never get this far
        # FIXME: VIRGINITY_LIKELIHOOD_BY_AGE should be rigorously tested/validated
        raise ValueError(f"Could not assess whether {person.fname} (aged {person.age}) is a(n) {sex_kind} virgin")

def _vt_threshold_to_reroll(person: Person) -> int:
    # story/unique/mod characters get a boost
    return 2 if person.type != "random" else 0

def _vt_reroll_lower_bound(person: Person, sex_kind: str, sex_cap: int) -> int:
    # story/unique/mod characters get a boost
    ret_val = 2 if person.type != "random" else 1

    # mothers get a boost
    ret_val += person.kids if sex_kind=="Vaginal" else 0

    # ensure to return a value no greater than sex_cap
    # else the randint lower/upper bounds would be reversed
    # and it would raise a ValueError
    return builtins.min(sex_cap, ret_val)

def _vt_virginity_stats(person: Person, sex_kind: str, sex_cap: int) -> dict:
    stats: dict[str, int | str | None] = {}
    # vaginal "just the tip" (skill=1) counts as virgin
    if _vt_is_virgin(person, sex_kind):
        # IN THIS BRANCH: IS A VIRGIN (for that sex kind)
        # TL;DR lock all values to 0/None (or in case "just the tip" vaginal_virgin can be 1)
        # set name of first partner in sex kind to None
        stats[sex_kind.lower() + "_first"] = None

        # if vaginal virgin/"just the tip" set hymen to sealed
        # TODO: is there a scenario where sex_skills[sex_kind] should be untouched?
        if sex_kind == "Vaginal":
            stats["hymen"] = 0
            person.sex_skills["Vaginal"] = (1 if person.sex_skills["Vaginal"] == 1 else 0)
        else:
            person.sex_skills[sex_kind] = 0

        # set sex_kind virginality to 0
        stats[sex_kind.lower() + "_virgin"] = 0

        # set (oral/vaginal/anal)_cum to 0
        stats[sex_kind.lower() + "_cum"] = 0
    else:
        # IN THIS BRANCH: DEFLOWERED (for that sex kind)
        # TL;DR set appropriate values
        # set name of first partner in sex kind
        stats[sex_kind.lower() + "_first"] = _vt_cherry_popper(person, sex_kind)

        # if vaginal, set hymen to normal (unless it's already set to torn)
        if sex_kind=="Vaginal" and getattr(person, "hymen", 0) < 1:
            stats["hymen"] = 2

        # set the person's skill
        if person.sex_skills[sex_kind] <= _vt_threshold_to_reroll(person): #threshold is 0 if random, 2 otherwise
            # reroll = _vt_bounded_gaussian_int(_vt_reroll_lower_bound(person), sex_cap)
            # TODO: if using bounded gaussian, should shift the median too
            person.sex_skills[sex_kind] = renpy.random.randint(_vt_reroll_lower_bound(person, sex_kind, sex_cap), sex_cap)

        # ensure that _virgin is in the range [3..10] and matches the sex_skill if possible
        stats[sex_kind.lower() + "_virgin"] = 3

        # allow cum storage at character creation
        # if the value exists, don't overwrite it
        if not hasattr(person, sex_kind.lower() + "_cum"):
            # set (oral/vaginal/anal)_cum to 0
            stats[sex_kind.lower() + "_cum"] = 0

    return stats

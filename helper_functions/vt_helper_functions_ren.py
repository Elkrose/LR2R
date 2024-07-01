import renpy
from game.major_game_classes.character_related.Person_ren import Person
from game.main_character.MainCharacter_ren import mc
from typing import Union
from renpy import persistent, basestring
from VTrandom_lists_ren import VT_AGE_RANGES, VT_Settings

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 900 python:
"""
import math
import builtins

def _vt_internal_age_tag(age_tag_repr: str) -> str:
    internal, *other = VT_Settings["Population"].get(age_tag_repr)
    if not internal:
        # sanity check; should not reach this
        raise ValueError(f"{age_tag_repr} not described in VirginTracker age ranges")
    return internal

def _vt_repr_age_tag(age_tag: str) -> str:
    for repr, (internal, *other) in VT_Settings["Population"].items():
        if age_tag == internal:
            return repr
    # sanity check; should not reach this
    raise ValueError(f"{age_tag} not described in VirginTracker age ranges")

def _vt_get_person_age_tag(person: Person) -> str:
    for tag, (lower, upper) in VT_AGE_RANGES.items():
        if lower <= person.age <= upper:
            return tag
    # sanity check; should not reach this
    raise ValueError(f"{person.name} age value {person.age} not found in VirginTracker age ranges")

# helper function; if the person has a sex skill, she must have gotten it with someone
# returns name either random, SO_name, or MC
def _vt_cherry_popper(person, sex_kind: str) -> str | None:
    # TODO: for girls in relationships, someone before their current partner might have popped their cherry?
    # could factor in presumed/random relationship length, loyalty/desire to save for marriage, etc.

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
    elif sex_kind == "Vaginal" and (person.kids > 0 or person.is_pregnant):
        return False
    elif person.type != "random":
        # story/unique characters might have sex skill assigned; base virginality on that
        return person.sex_skills[sex_kind] <= (1 if sex_kind=="Vaginal" else 0)
    else:
        # TODO: mixin age/relationship status? e.g. 19 w/ boyfriend might likely have tried oral, 25 w/ fiancee likely tried it all (but might be saving for marriage)
        age_tag = _vt_get_person_age_tag(person)
        age_tag_repr = _vt_repr_age_tag(age_tag)

        # get the value from persistent settings store if available, else from default mod value
        virginity_probability = getattr(persistent, age_tag + "_" + sex_kind.lower(), VT_Settings["Virgin Stats"].get(age_tag_repr + " - " + sex_kind)[1])
        return renpy.random.randint(1,100) <= virginity_probability

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

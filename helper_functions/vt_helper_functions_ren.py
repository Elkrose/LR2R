import renpy
from game.major_game_classes.character_related.Person_ren import Person
from game.main_character.MainCharacter_ren import mc
from typing import Union

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 900 python:
"""
import math
import builtins

# helper function; if the person has a sex skill, she must have gotten it with someone
# returns name either random, SO_name, or MC
def _vt_cherry_popper(person) -> str | None:
    if person.relationship != "Single" and person.SO_name is mc.name:
        return mc.name
    elif person.relationship != "Single" and person.SO_name:
        return person.SO_name
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
    if person.type in ("story", "unique"):
        return person.sex_skills[sex_kind] == 0 or (sex_kind=="Vaginal" and person.sex_skills[sex_kind] == 1)
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
        # FIXME: should never get this far
        return False

def _vt_virginal_stats(person: Person, sex_kind: str, sex_cap: int) -> dict:
    stats: dict[str, int | str | None] = {}
    # vaginal "just the tip" (skill=1) counts as virgin
    if _vt_is_virgin(person, sex_kind):
        # IN THIS BRANCH: IS A VIRGIN (for that sex kind)
        # set name of first partner in sex kind to None
        stats[sex_kind.lower() + "_first"] = None

        # if vaginal virgin/"just the tip" set hymen to sealed
        if sex_kind == "Vaginal":
            stats["hymen"] = 0
            person.sex_skills["Vaginal"] = 1 if person.sex_skills["Vaginal"] == 1 else 0
        else:
            person.sex_skills[sex_kind] = 0

        # set sex_kind virginality to 0
        stats[sex_kind.lower() + "_virgin"] = 0
    else:
        # IN THIS BRANCH: DEFLOWERED (for that sex kind)
        # set name of first partner in sex kind
        stats[sex_kind.lower() + "_first"] = _vt_cherry_popper(person)

        # if vaginal, set hymen to normal
        if sex_kind=="Vaginal":
            stats["hymen"] = 2

        # with this mod, non-virginal means skill >= 2
        if person.sex_skills[sex_kind] <= 2:
            reroll = _vt_bounded_gaussian_int(2, sex_cap)
            #reroll = renpy.random.randint(2, sex_cap)
            person.sex_skills[sex_kind] = reroll
            stats[sex_kind.lower() + "_virgin"] = reroll
        else:
            stats[sex_kind.lower() + "_virgin"] = builtins.min(10, person.sex_skills[sex_kind])
            if sex_kind == "Vaginal" and person.kids != 0 and person.sex_skills[sex_kind] <= 10:
                # FIXME: shouldn't this be setting sex_skills["Vaginal"]
                # instead of "vaginal_virgin"?
                stats[sex_kind.lower() + "_virgin"] = 7 # give mothers an edge

    # always set (oral/vaginal/anal)_cum to 0
    stats[sex_kind.lower() + "_cum"] = 0

    return stats

from __future__ import annotations
import builtins
import renpy
from renpy import persistent
from typing import TypeVar
from collections import OrderedDict
from game.major_game_classes.character_related.Person_ren import Person
import math
T = TypeVar('T')
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

VT_Settings = {}

VT_AGE_RANGES = {
    "preteen":          (0, 12),
    "teen":             (13, 15),
    "adolescent":       (16, 18),
    "young_adult":      (19, 25),
    "early_adult":      (26, 30),
    "middle_adult":     (31, 46),
    "late_adult":       (47, 52),
    "senior":           (53, 60),
    "elderly":          (61, 95),
}

VT_Settings["Population"] = {
    "Adolescent":   ["adolescent",      5, 0],
    "Young Adult":  ["young_adult",     30, 1],
    "Millennial":   ["early_adult",     30, 2],
    "Adult":        ["middle_adult",    20, 3],
    "Middle Age":   ["late_adult",      10, 4],
    "Seniors":      ["senior",          4, 5],
    "Elderly":      ["elderly",         1, 6],
    "Teen":         ["teen",            0, 7],
    "Preteen":      ["preteen",         0, 8],
}

VT_Settings["Virgin Stats"] = {
    "Adolescent - Oral":    ["adolescent_oral",    100,  0],
    "Adolescent - Vaginal": ["adolescent_vaginal", 100,  1],
    "Adolescent - Anal":    ["adolescent_anal",    100,  2],
    "Young Adult - Oral":   ["young_adult_oral",    30,  3],
    "Young Adult - Vaginal":["young_adult_vaginal", 30,  4],
    "Young Adult - Anal":   ["young_adult_anal",    30,  5],
    "Millennial - Oral":    ["early_adult_oral",    20,  6],
    "Millennial - Vaginal": ["early_adult_vaginal", 20,  7],
    "Millennial - Anal":    ["early_adult_anal",    20,  8],
    "Adult - Oral":         ["middle_adult_oral",   10,  9],
    "Adult - Vaginal":      ["middle_adult_vaginal",10, 10],
    "Adult - Anal":         ["middle_adult_anal",   10, 11],
    "Middle Age - Oral":    ["late_adult_oral",     10, 12],
    "Middle Age - Vaginal": ["late_adult_vaginal",  10, 13],
    "Middle Age - Anal":    ["late_adult_anal",     10, 14],
    "Seniors - Oral":       ["senior_oral",          5, 15],
    "Seniors - Vaginal":    ["senior_vaginal",       5, 16],
    "Seniors - Anal":       ["senior_anal",          5, 17],
    "Elderly - Oral":       ["elderly_oral",          5, 18],
    "Elderly - Vaginal":    ["elderly_vaginal",       5, 19],
    "Elderly - Anal":       ["elderly_anal",          5, 20],
    "Teen - Oral":          ["teen_oral",          100, 21],
    "Teen - Vaginal":       ["teen_vaginal",       100, 22],
    "Teen - Anal":          ["teen_anal",          100, 23],
    "Preteen - Oral":       ["preteen_oral",          100, 24],
    "Preteen - Vaginal":    ["preteen_vaginal",       100, 25],
    "Preteen - Anal":       ["preteen_anal",          100, 26],
}

VT_Settings["Trackers"] = {
    "Favorites":                ["fullstar",       1, 0],
    "Story Characters":         ["labbook",         1, 1],
    "Polycule":                 ["polyamorous",           1, 2],
    "Polycule - Paramour":      ["parapoly",        1, 3],
    "Polycule - Familia":       ["familypoly",            1, 4],
    "Girlfriend":               ["girlfriend",              1, 5],
    "Girlfriend - Paramour":    ["paramour",        1, 6],
    "Girlfriend - Familia":     ["familylove",            1, 7],
    "Familia":                  ["familycircle",          1, 8],
    "Slave":                    ["slave",                 1, 9],
    "Slave - Polyamorous":      ["polyslave",             1, 10],
    "Slave - Poly Paramour":    ["parapolyslave",         1, 11],
    "Slave - Poly Familia":     ["polyfamiliaslave",      1, 12],
    "Slave - Paramour":         ["paraslave",             1, 13],
    "Slave - GF Familia":       ["gffamiliaslave",        1, 14],
    "Slave - Girlfriend":       ["gfslave",               1, 15],
    "Slave - Familia":          ["familiaslave",          1, 16],
    "Lotus - White":            ["whitelotus",            1, 17],
    "Lotus - Red":              ["redlotus",              1, 18],
    "Lotus - Pink":             ["pinklotus",             1, 19],
    "Lotus - Blue":             ["bluelotus",             1, 20],
    "Lotus - Gold":             ["goldlotus",             1, 21],
    "Virgin - Vaginal":         ["virgin_image_marker",          1, 22],
    "Virgin - Anal":            ["virgin_image_marker",          1, 23],
    "Virgin - Oral":            ["virgin_image_marker",          1, 24],
    "Pregnant":                 ["feeding_bottle",  1, 25],
    "Trance - Very Heavy":      ["ahegaotrance",    1, 26],
    "Trance - Heavy":           ["heavytrance",     1, 27],
    "Trance - Available":       ["starttrance",     1, 28],
    "Arousal":                  ["arousal",         1, 29],
    "Serums":                   ["serum_vial",      1, 30],
    "Infractions":              ["infraction",      1, 31],
    "Clone":                    ["dna_sequence",    1, 32],
    "Fertility Bee":            ["beezee",          1, 33],
    "Had Sex Today":            ["hadsextoday",     1, 34],
    "Stripper":                 ["stripper",        1, 35],
    "Prostitute":                ["cashpanties",     1, 36],
    }

# update defaults when not exist
for pref in VT_Settings.values():
    for setting in pref.values():
        if not (getattr(persistent, setting[0]) or isinstance(getattr(persistent, setting[0]), int)):
            setattr(persistent, setting[0], setting[1])

def _vt_build_weighted_list(options_dict: dict[str, list[str | int]], start = None, end = None):
    weighted_list = []
    if start is None:
        start = 0
    if end is None:
        end = len(options_dict)

    pref_dict = OrderedDict(options_dict)
    for idx, x in enumerate(pref_dict):
        if idx < start or idx > end:
            continue
        if getattr(persistent, options_dict[x][0], options_dict[x][1]) > 0:
            weighted_list.append((options_dict[x][0], getattr(persistent, options_dict[x][0], options_dict[x][1])))
    return weighted_list

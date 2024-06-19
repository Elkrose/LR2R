from __future__ import annotations
import builtins
import renpy
from renpy import persistent
from game.helper_functions.list_functions_ren import get_random_from_list
from typing import TypeVar
T = TypeVar('T')
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
#TO DO Make sliders not care about 100% totals only on its row, some rows are %, some are Months/week/turns


VT_Settings = {}
#TO-DO Have the total 100% at the bottom to set the Age Population they wish to see more of.
#TO-DO allow players to choose whatever Ages they wish to see etc.
#TO-DO Don't think there is a weighted list for ages.
VT_Settings["Population"] = {
    "Adolescence": ["VT_Settings_Adolescence", 5, 0],
    "Young Adult": ["VT_Settings_PRE_Adult", 30, 1],
    "Millennial": ["VT_Settings_Adult", 30, 2],
    "Adult": ["VT_Settings_Mature_Adult", 20, 3],
    "Middle Age": ["VT_Settings_Elder", 10, 4],
    "Seniors": ["VT_Settings_Ancient", 5, 5],
}

#TO DO - allow the settings to each be set by 100% ie teen to 20 1-100% Virgins but starts at 30% as recommended
#TO DO - recommended already set... might need a button to reload the defaults if they need to?
VT_Settings["Virgin Stats"] = {
    "Adolescence - Oral": ["VT_Settings_Adolescence", 100, 0],
    "Adolescence - Anal": ["VT_Settings_Adolescence", 100, 1],
    "Adolescence - Vaginal": ["VT_Settings_Adolescence", 100, 2],
    "Young Adult - Oral": ["VT_Settings_PRE_Adult", 30, 3],
    "Young Adult - Anal": ["VT_Settings_PRE_Adult", 30, 4],
    "Young Adult - Vaginal": ["VT_Settings_PRE_Adult", 30, 5],
    "Millennial - Oral": ["VT_Settings_Adult", 20, 6],
    "Millennial - Anal": ["VT_Settings_Adult", 20, 7],
    "Millennial - Vaginal": ["VT_Settings_Adult", 20, 8],
    "Adult - Oral": ["VT_Settings_Mature_Adult", 10, 9],
    "Adult - Anal": ["VT_Settings_Mature_Adult", 10, 10],
    "Adult - Vaginal": ["VT_Settings_Mature_Adult", 10, 11],
    "Middle Age - Oral": ["VT_Settings_Elder", 10, 12],
    "Middle Age - Anal": ["VT_Settings_Elder", 10, 13],
    "Middle Age - Vaginal": ["VT_Settings_Elder", 10, 14],
    "Seniors - Oral": ["VT_Settings_Ancient", 5, 15],
    "Seniors - Anal": ["VT_Settings_Ancient", 5, 16],
    "Seniors - Vaginal": ["VT_Settings_Ancient", 5, 17],
}
#TO DO - Pregnancy  BunTimer (weeks in labor) 100% = 9 months x 3.5 weeks x 7 days x 7 turns, max (1544), min(172) 3.5 weeks, recommend(344)
#TO DO - Type of pregnancy Natural / C-Section = 100% so its either 40% natural or 100% natural setting, recommended 50% to choose between them
#To DO -  Postsex (sex wait period due to medical recovery usually 6 weeks).
#TO DO - PostSex max 6 weeks = 6x7x7 = 294 turns, min 2 weeks = 98 turns, recommended 3 weeks=147, 
VT_Settings["Pregnancy"] = {
    "Bun in the Oven Timer": ["VT_BunTimer", 4, 0],
    "Natural Delivery": ["VT_NatDelivery", 8, 1],
    "C-Section Delivery": ["VT_CSecDelivery", 15, 2],
    "Post-Sex Timer": ["VT_Postsex", 20, 3],
    }

# update defaults when not exist
for pref in VT_Settings.values():
    for setting in pref.values():
        if not (getattr(persistent, setting[0]) or isinstance(getattr(persistent, setting[0]), int)):
            setattr(persistent, setting[0], setting[1])

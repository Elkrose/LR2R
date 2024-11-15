# GENERIC LIST OF ROLES AND ACTIONS ASSOCIATED WITH THAT ROLE
from __future__ import annotations
import renpy
from renpy import persistent
from game.random_lists_ren import get_random_from_weighted_list
from game.major_game_classes.character_related.Person_ren import Person, mc, cousin, lily, aunt, ashley, alexia, ellie, sarah, candace, nora, kaya, city_rep
from game.people.Rebecca.aunt_definition_ren import aunt_unemployed_job
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import dungeon

day = 0
time_of_day = 0
TIER_1_TIME_DELAY = 0
THREESOME_BASE_SLUT_REQ = 80
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

################
# Fetish Roles #
################
def fetish_anal_staylate_requirement(person: Person):
    if mc.is_at_office and mc.business.is_open_for_business and person.is_employee:
        return True
    return False

def get_anal_fetish_role_actions():
    fetish_anal_staylate = Action("See me after work", fetish_anal_staylate_requirement, "fetish_anal_staylate_label",
        menu_tooltip = "Ask her to stay late after work day is over.", priority = 10)

    return [fetish_anal_staylate]

def breeding_fetish_role_on_day(person: Person):
    if person.knows_pregnant or person.is_lactating:
        person.change_happiness(2, add_to_log = False)
    elif person.is_highly_fertile and person.arousal_perc < 50: #Always aroused when fertile.
        person.arousal = person.max_arousal * .5

def breeding_fetish_bend_her_over_requirement(person: Person):
    if not person.known_opinion("creampies") and not person.known_opinion("vaginal sex") and not person.known_opinion("bareback"):
        return False
    if person.energy < 50:
        return "She's too tired"
    if mc.energy < 50:
        return "You're too tired"
    return True

def breeding_fetish_fuck_requirement(person: Person):
    if persistent.pregnancy_pref == 0:
        return False
    if person.knows_pregnant:
        return False
    if not person.known_opinion("creampies") and not person.known_opinion("vaginal sex") and not person.known_opinion("bareback"):
        return False
    return True

def get_breeding_fetish_role_actions():
    breeding_fetish_fuck_action = Action("Offer to knock her up", breeding_fetish_fuck_requirement, "breeding_fetish_fuck",
        menu_tooltip = "She wants to get pregnant, you could help with that.", priority = 10)
    breeding_fetish_bend_her_over_action = Action("Bend her over", breeding_fetish_bend_her_over_requirement, "breeding_fetish_bend_her_over_label",
        menu_tooltip = "Bend her over right here and give your breeding stock a creampie", priority = 10)

    return [breeding_fetish_fuck_action, breeding_fetish_bend_her_over_action]

def cum_fetish_get_dosage_requirement(person: Person):
    if not (person.known_opinion("anal creampies") or person.known_opinion("creampies") or person.known_opinion("being covered in cum")):
        return False
    if mc.energy < 40 or time_of_day >= 4:
        return "You're too tired"
    return True

def get_cum_fetish_role_actions():
    cum_fetish_get_dosage = Action("Give her a cum dosage", cum_fetish_get_dosage_requirement, "cum_fetish_get_dosage_label",
        menu_tooltip = "Give her cum, right here, right now.", priority = 10)

    return [cum_fetish_get_dosage]

from __future__ import annotations
from game.clothing_lists_ren import fuck_doll_collar
from game.fetish.fetish_action_ren import Fetish_Action
from game.fetish.fetish_serum_quests_ren import fetish_add_collar
from game.helper_functions.list_functions_ren import get_random_from_list, known_people_in_the_game
from game.bugfix_additions.ActionMod_ren import ActionMod
from game.game_roles._role_definitions_ren import anal_fetish_role
from game.major_game_classes.character_related.Person_ren import Person, mc, lily, mom, starbuck, stephanie

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
def get_random_pussy_position():
    return get_random_from_list(["back_peek", "standing_doggy", "doggy", "walking_away"])

def vaginal_fetish_employee_evening_approach_requirement():
    if time_of_day == 3 and mc.is_at_office and mc.business.is_open_for_business:
        return not get_vaginal_fetish_employee() is None
    return False

def aggressive_vaginal_fetish_non_employee_requirement():
    if time_of_day in (1, 2, 3):
        return not get_needy_vaginal_fetish_non_employee() is None
    return False

def aggressive_vaginal_employee_requirement():
    if mc.is_at_office and mc.business.is_open_for_business:
        return not get_needy_vaginal_fetish_employee() is None
    return False

def get_vaginal_fetish_employee():
    return get_random_from_list([
        x for x in mc.business.employees_availabe
        if x.has_vaginal_fetish
        and not x.event_triggers_dict.get("vaginal_fetish_crisis_disabled", False)
    ])

def get_needy_vaginal_fetish_employee(): #If it's been a while
    return get_random_from_list([
        x for x in mc.business.employees_availabe
        if x.has_vaginal_fetish
        and x.days_since_event("LastVaginalFetish") > 10
        and not x.event_triggers_dict.get("vaginal_fetish_crisis_disabled", False)
        and not x.is_at(mc.current_location_hub)
    ])

def get_needy_vaginal_fetish_non_employee():
    return get_random_from_list([
        x for x in known_people_in_the_game(excluded_people = mc.business.employee_list + [mom, lily, starbuck, stephanie])
        if x.is_available
        and x.has_vaginal_fetish
        and x.days_since_event("LastVaginalFetish") > 10
        and not x.event_triggers_dict.get("vaginal_fetish_crisis_disabled", False)
    ])

# TODO: Write needy anal fetish events for family?
# def get_anal_fetish_family():
#     return get_random_from_list([
#         x for x in known_people_in_the_game()
#         if x.is_available
#         and x.has_anal_fetish
#         and x.is_family
#         and not x.event_triggers_dict.get("anal_fetish_crisis_disabled", False)
#     ])

aggressive_vaginal_fetish_employee = ActionMod("Vaginal Fetish: Employee", aggressive_vaginal_employee_requirement, "aggressive_vaginal_fetish_employee_label",
    menu_tooltip = "An employee needs her vaginal fetish fulfilled", category = "VT Natural Fetish", is_crisis = True)

aggressive_vaginal_fetish_non_employee = ActionMod("Vaginal Fetish: Someone", aggressive_vaginal_fetish_non_employee_requirement, "aggressive_vaginal_fetish_non_employee_label",
    menu_tooltip = "Someone needs her vaginal fetish fulfilled", category = "VT Natural Fetish", is_crisis = True)

vaginal_fetish_employee_evening_approach = ActionMod("Vaginal Fetish: Employee evening", vaginal_fetish_employee_evening_approach_requirement, "vaginal_fetish_employee_evening_approach_label",
    menu_tooltip = "An employee asks for vaginal after the office closes", category = "VT Natural Fetish", is_crisis = True)

def add_vaginal_fetish(person: Person):
    person.max_opinion_score("vaginal sex")
    person.max_opinion_score("creampies")
    person.add_role(vaginal_fetish_role)
    if person.vaginal_sex_skill < 6:
        person.update_sex_skill("Vaginal", 6)
    person.set_event_day("LastVaginalFetish")
    fetish_add_collar(person, fuck_doll_collar)
    person.unlock_spanking()

def get_vaginal_fetish_unique_dialogue_list():
    vaginal_list = [lily, starbuck, mom, stephanie]
    return vaginal_list

def debug_set_stats_for_vaginal_fetish_mins(person: Person):
    person.arousal = 0
    person.energy = person.max_energy
    person.max_opinion_score("vaginal sex")
    person._sluttiness = 70
    person._obedience = 100
    person.happiness = 100
    person.love = 0

def abort_vaginal_fetish_intro(person: Person): #Use this function to exit a vaginal fetish scene for whatever reason (something fails, MC choice, etc.)
    person.event_triggers_dict["vaginal_fetish_start"] = False
    person.remove_role(vaginal_fetish_role)

def fetish_vaginal_staylate_event_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business

def add_fetish_vaginal_staylate_event(person: Person):
    mc.business.add_mandatory_crisis(
        Fetish_Action("Employee stays late", fetish_vaginal_staylate_event_requirement, "fetish_vaginal_staylate_event_label", args = person, priority = 10, fetish_type = "vaginal")
    )

#This is a list of positions that show off a person's pussy. Can grab one randomly for when a girl wants to show off pussy specifically
def SB_get_random_pussy_position():
    return get_random_from_list(["back_peek", "standing_doggy", "doggy", "walking_away"])


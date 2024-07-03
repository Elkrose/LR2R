from __future__ import annotations
#from game.clothing_lists_ren import cum_slut_collar
# from game.fetish.fetish_serum_quests_ren import fetish_add_collar
from game.helper_functions.list_functions_ren import get_random_from_list, known_people_in_the_game
from game.bugfix_additions.ActionMod_ren import ActionMod
from game.game_roles._role_definitions_ren import cum_fetish_role
from game.major_game_classes.character_related.Person_ren import Person, mc, lily, mom
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""

def VT_cum_fetish_morning_shower_requirement():
    if time_of_day == 0 and mc.is_home:
        return not VT_get_fetish_shower_cum_girl() is None
    return False

def VT_cum_fetish_employee_dosage_request_requirement():
    if mc.business.is_open_for_business and mc.is_at_office:
        return not VT_get_fetish_cum_dosage_employee() is None
    return False

def VT_cum_fetish_non_employee_dosage_request_requirement():
    if time_of_day in (1, 2, 3):
        return not VT_get_fetish_cum_dosage_non_employee() is None
    return False

def VT_get_fetish_shower_cum_girl():
    return get_random_from_list([x for x in (mom, lily) if x.has_cum_fetish and not x.has_queued_event("sleeping_walk_in_label") and x.days_since_event("LastCumFetish") > 10])

def VT_get_fetish_cum_dosage_employee():
    return get_random_from_list([x for x in mc.business.employees_at_office if x.has_cum_fetish and x.days_since_event("LastCumFetish") > 10])

def VT_get_fetish_cum_dosage_non_employee():
    return get_random_from_list([x for x in known_people_in_the_game(excluded_people = mc.business.employee_list + [mom, lily]) if x.has_cum_fetish and x.days_since_event("LastCumFetish") > 10])

VT_cum_fetish_morning_shower_crisis = ActionMod("Morning shower with company", VT_cum_fetish_morning_shower_requirement, "VT_cum_fetish_morning_shower_label",
    menu_tooltip = "You are taking a shower when a family member joins you.", category = "Fetish", is_crisis = True)
VT_cum_fetish_employee_dosage_request_crisis = ActionMod("Employee asks for cum", VT_cum_fetish_employee_dosage_request_requirement, "VT_cum_fetish_employee_dosage_request_label",
    menu_tooltip = "An employee is thirsty for cum.", category = "Fetish", is_crisis = True)
VT_cum_fetish_non_employee_dosage_request_crisis = ActionMod("Someone asks for cum", VT_cum_fetish_non_employee_dosage_request_requirement, "VT_cum_fetish_non_employee_dosage_request_label",
    menu_tooltip = "Someone calls and asks for a favour.", category = "Fetish", is_crisis = True)


def VT_add_cum_fetish(person: Person):
    person.max_opinion_score("drinking cum")
    person.max_opinion_score("being covered in cum")
    person.add_role(cum_fetish_role)
    if person.oral_sex_skill <6:
        person.update_sex_skill("Oral", 6)
    person.set_event_day("LastCumFetish")
    #fetish_add_collar(person, cum_slut_collar)

def VT_get_cum_fetish_unique_dialogue_list():
    cum_list = [lily, mom]
    return cum_list

# def VT_abort_cum_fetish_intro(person: Person): #Use this function to exit a anal fetish scene for whatever reason (something fails, MC choice, etc.)
    # person.event_triggers_dict["VT_cum_fetish_start"] = False
    # person.remove_role(cum_fetish_role)

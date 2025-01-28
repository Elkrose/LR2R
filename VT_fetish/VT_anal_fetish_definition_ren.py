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
def VT_anal_fetish_employee_evening_approach_requirement():
    if time_of_day == 3 and mc.is_at_office and mc.business.is_open_for_business:
        return not VT_get_anal_fetish_employee() is None
    return False

def VT_aggressive_anal_fetish_non_employee_requirement():
    if time_of_day in (1, 2, 3):
        return not VT_get_needy_anal_fetish_non_employee() is None
    return False

def VT_aggressive_anal_employee_requirement():
    if mc.is_at_office and mc.business.is_open_for_business:
        return not VT_get_needy_anal_fetish_employee() is None
    return False

def VT_get_anal_fetish_employee():
    return get_random_from_list([x for x in mc.business.employee_list if x.has_anal_fetish])

def VT_get_needy_anal_fetish_employee(): #If it's been a while
    return get_random_from_list([x for x in mc.business.employee_list if x.has_anal_fetish and x.days_since_event("LastAnalFetish") > 10 and x.current_location_hub != mc.current_location_hub])

def VT_get_anal_fetish_non_employee():
    return get_random_from_list([x for x in known_people_in_the_game(excluded_people = mc.business.employee_list + [mom, lily, starbuck, stephanie]) if x.has_anal_fetish and x.days_since_event("LastAnalFetish") > 10])

def VT_get_needy_anal_fetish_non_employee():
    return get_random_from_list([x for x in known_people_in_the_game(excluded_people = mc.business.employee_list + [mom, lily, starbuck, stephanie]) if x.has_anal_fetish and x.days_since_event("LastAnalFetish") > 10])

def VT_get_anal_fetish_family():
    return get_random_from_list([x for x in known_people_in_the_game() if x.is_family and x.has_anal_fetish])

VT_aggressive_anal_fetish_employee = ActionMod("Anal Fetish: Employee", VT_aggressive_anal_employee_requirement, "VT_aggressive_anal_fetish_employee_label",
    menu_tooltip = "An employee needs her anal fetish fulfilled", category = "VT Natural Fetish", is_crisis = True)

VT_aggressive_anal_fetish_non_employee = ActionMod("Anal Fetish: Someone", VT_aggressive_anal_fetish_non_employee_requirement, "VT_aggressive_anal_fetish_non_employee_label",
    menu_tooltip = "Someone needs her anal fetish fulfilled", category = "VT Natural Fetish", is_crisis = True)

VT_anal_fetish_employee_evening_approach = ActionMod("Anal Fetish: Employee evening", VT_anal_fetish_employee_evening_approach_requirement, "VT_anal_fetish_employee_evening_approach_label",
    menu_tooltip = "An employee asks for anal after the office closes", category = "VT Natural Fetish", is_crisis = True)

#TODO - anal fetish family, generic non employee, mom, lily, starbuck and stephanie

def VT_add_anal_fetish(person: Person):
    person.max_opinion_score("anal sex")
    person.max_opinion_score("anal creampies")
    person.add_role(anal_fetish_role)
    if person.anal_sex_skill <6:
        person.update_sex_skill("Anal", 6)
    person.set_event_day("LastAnalFetish")
    #fetish_add_collar(person, fuck_doll_collar)
    person.unlock_spanking()

def VT_get_anal_fetish_unique_dialogue_list():
    anal_list = [lily, starbuck, mom, stephanie]
    return anal_list

# def VT_abort_anal_fetish_intro(person: Person): #Use this function to exit a anal fetish scene for whatever reason (something fails, MC choice, etc.)
    # person.event_triggers_dict["VT_anal_fetish_start"] = False
    # person.remove_role(anal_fetish_role)

def VT_fetish_anal_staylate_event_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business

def VT_add_fetish_anal_staylate_event(person: Person):
    mc.business.add_mandatory_crisis(
        Fetish_Action("Employee stays 'behind'", VT_fetish_anal_staylate_event_requirement, "fetish_anal_staylate_event_label", args = person, priority = 10, fetish_type = "anal")
    )

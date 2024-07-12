from __future__ import annotations
from game.clothing_lists_ren import breed_collar
from game.fetish.fetish_serum_quests_ren import fetish_add_collar
from game.helper_functions.list_functions_ren import get_random_from_list, known_people_in_the_game
from game.bugfix_additions.ActionMod_ren import ActionMod
from game.game_roles._role_definitions_ren import breeding_fetish_role
from game.major_game_classes.character_related.Person_ren import Person, mc

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""

def VT_get_breeding_fetish_list():
    return [x for x in known_people_in_the_game() if x.has_breeding_fetish and x.is_available and x.days_since_event("LastBreedingFetish") > 12]

def VT_get_highly_fertile_breeder():
    return get_random_from_list([x for x in VT_get_breeding_fetish_list() if x.is_highly_fertile and not x.is_employee])

def VT_get_highly_fertile_employee_breeder():
    return get_random_from_list([x for x in VT_get_breeding_fetish_list() if x.is_highly_fertile and x.is_employee])

def VT_get_pregnant_breeder():
    return get_random_from_list([x for x in VT_get_breeding_fetish_list() if x.knows_pregnant])

def VT_get_family_breeder():
    return get_random_from_list([x for x in VT_get_breeding_fetish_list() if x.is_family])

def VT_breeding_fetish_high_fertility_crisis_requirement():
    if time_of_day == 4 and mc.is_home:
        return not VT_get_highly_fertile_breeder() is None
    return False

def VT_breeding_fetish_happy_breeder_crisis_requirement():
    if time_of_day == 4 and mc.is_home:
        return not VT_get_pregnant_breeder() is None
    return False

def VT_breeding_fetish_family_sleep_crisis_requirement():
    if time_of_day == 4 and mc.is_home:
        return not VT_get_family_breeder() is None
    return False

def VT_breeding_fetish_employee_high_fertility_crisis_requirement():
    if mc.business.is_open_for_business and mc.is_at_office:
        return not VT_get_highly_fertile_employee_breeder() is None
    return False

def update_breeding_fetish_state(person: Person):
    person.energy = max(person.energy, 80)
    mc.energy = max(mc.energy, 80)
    if person.arousal_perc <= 20:
        person.change_arousal(30)

VT_breeding_fetish_high_fertility_crisis = ActionMod("Highly fertile breeding desperation", VT_breeding_fetish_high_fertility_crisis_requirement, "VT_breeding_fetish_high_fertility_crisis_label",
    menu_tooltip = "You are visited by a highly fertile breeder.", category = "VT Natural Fetish", is_crisis = True)
VT_breeding_fetish_happy_breeder_crisis = ActionMod("Breeding fetish desperation", VT_breeding_fetish_happy_breeder_crisis_requirement, "VT_breeding_fetish_happy_breeder_crisis_label",
    menu_tooltip = "You are visited by a highly fertile breeder.", category = "VT Natural Fetish", is_crisis = True)
VT_breeding_fetish_family_sleep_crisis = ActionMod("Familial night time breeding", VT_breeding_fetish_family_sleep_crisis_requirement, "VT_breeding_fetish_family_sleep_crisis_label",
    menu_tooltip = "You are visited at night by a thirsty family member.", category = "VT Natural Fetish", is_crisis = True)
VT_breeding_fetish_employee_high_fertility_crisis = ActionMod("Highly fertile employee needs breeding", VT_breeding_fetish_employee_high_fertility_crisis_requirement, "VT_breeding_fetish_employee_high_fertility_crisis_label",
    menu_tooltip = "An employee surprises you in your office", category = "VT Natural Fetish", is_crisis = True)

def VT_add_breeding_fetish(person: Person):
    person.add_role(breeding_fetish_role)
    if person.vaginal_sex_skill <6:
        person.update_sex_skill("Vaginal", 6)
    person.set_event_day("LastBreedingFetish")
    #fetish_add_collar(person, breed_collar)
    person.change_baby_desire(500)

# def VT_abort_breeding_fetish_intro(person: Person): #Use this function to exit a anal fetish scene for whatever reason (something fails, MC choice, etc.)
    # person.event_triggers_dict["VT_breeding_fetish_start"] = False
    # person.remove_role(breeding_fetish_role)

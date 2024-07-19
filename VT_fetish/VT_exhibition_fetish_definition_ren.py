from __future__ import annotations
from game.game_roles._role_definitions_ren import exhibition_fetish_role
from game.major_game_classes.character_related.Person_ren import Person

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""

def debug_set_stats_for_exhibition_fetish_mins(person: Person):
    person.arousal = 0
    person.energy = person.max_energy
    person.max_opinion_score("anal sex")
    person._sluttiness = 70
    person._obedience = 100
    person.happiness = 100
    person.love = 0

# def abort_exhibition_fetish_intro(person: Person): #Use this function to exit a anal fetish scene for whatever reason (something fails, MC choice, etc.)
    # person.event_triggers_dict["exhibition_fetish_start"] = False
    # person.remove_role(exhibition_fetish_role)


# sb_free_strip_pose_list = [("Turn around","walking_away"), ("Turn around and look back", "back_peek"), ("Hands down, ass up","standing_doggy"), ("Be flirty","stand2"), ("Be casual","stand3"), ("Strike a pose", "stand4"), ("Move your hands out of the way", "stand5")]

# def sb_free_strip_build_strip_menu(person: Person, must_be_naked: bool):
#     option_list = []
#     option_list.append("Choose Strip Action")
#     for item in person.outfit.get_unanchored():
#         if not item.is_extension:
#             test_outfit = person.outfit.get_copy()
#             test_outfit.remove_clothing(item)

#             display_string = "Strip " + item.name
#             option_list.append((display_string, [item, 0]))

#     option_list.append(("Just watch", "Watch"))
#     option_list.append(("Tell her to pose", "Pose"))
#     if not must_be_naked or person.outfit.has_full_access:
#         option_list.append(("Finish the show", "Finish"))
#     return option_list

# def sb_free_strip_build_pose_menu(current_pose):
#     option_list = []
#     option_list.append("Choose Pose")
#     for pose in sb_free_strip_pose_list:
#         if not pose[1] == current_pose:
#             option_list.append(pose)
#     option_list.append(("Never mind", None))
#     return option_list


def VT_add_exhibition_fetish(person: Person):
    person.add_role(exhibition_fetish_role)
    person.set_opinion("public sex", 2, True)
    person.set_event_day("LastExhibitionFetish")


def VT_exhibition_fetish_morning_shower_requirement():
    if time_of_day == 0 and mc.is_home:
        return not VT_get_fetish_shower_cum_girl() is None
    return False

def VT_exhibition_fetish_employee_dosage_request_requirement():
    if mc.business.is_open_for_business and mc.is_at_work:
        return not VT_get_fetish_cum_dosage_employee() is None
    return False

def VT_exhibition_fetish_non_employee_dosage_request_requirement():
    if time_of_day in (1, 2, 3):
        return not VT_get_fetish_cum_dosage_non_employee() is None
    return False

def VT_get_fetish_shower_cum_girl():
    return get_random_from_list([x for x in (mom, lily) if x.has_exhibition_fetish and not x.has_queued_event("sleeping_walk_in_label") and x.days_since_event("LastExhibitionFetish") > 10])

def VT_get_fetish_cum_dosage_employee():
    return get_random_from_list([x for x in mc.business.employees_at_office if x.has_exhibition_fetish and x.days_since_event("LastExhibitionFetish") > 10])

def VT_get_fetish_cum_dosage_non_employee():
    return get_random_from_list([x for x in known_people_in_the_game(excluded_people = mc.business.employee_list + [mom, lily]) if x.has_exhibition_fetish and x.days_since_event("LastExhibitionFetish") > 10])


VT_exhibition_fetish_morning_shower_crisis = ActionMod("Morning shower with company", VT_exhibition_fetish_morning_shower_requirement, "VT_exhibition_fetish_morning_shower_label",
    menu_tooltip = "You are taking a shower when a family member joins you.", category = "VT Natural Fetish", is_crisis = True)
VT_exhibition_fetish_employee_dosage_request_crisis = ActionMod("Employee Casually asks for cum", VT_exhibition_fetish_employee_dosage_request_requirement, "VT_exhibition_fetish_employee_casual_request_label",
    menu_tooltip = "An employee is thirsty for cum.", category = "VT Natural Fetish", is_crisis = True)
VT_exhibition_fetish_non_employee_dosage_request_crisis = ActionMod("Someone asks for cum", VT_exhibition_fetish_non_employee_dosage_request_requirement, "VT_exhibition_fetish_non_employee_dosage_request_label",
    menu_tooltip = "Someone calls and asks for a favour.", category = "VT Natural Fetish", is_crisis = True)





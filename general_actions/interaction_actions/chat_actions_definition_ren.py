from __future__ import annotations
import builtins
from game.general_actions.interaction_actions.command_descriptions_definition_ren import demand_strip_naked_requirement, demand_strip_tits_requirement, demand_strip_underwear_requirement
from game.helper_functions.heart_formatting_functions_ren import get_gold_heart
from game.helper_functions.list_functions_ren import get_random_from_list
from game.business_policies.serum_policies_ren import mandatory_unpaid_serum_testing_policy, mandatory_paid_serum_testing_policy
from game.game_roles._role_definitions_ren import onlyfans_role
from game.game_roles.stripclub._stripclub_role_definitions_ren import get_strip_club_foreclosed_stage
from game.game_roles.relationship_role_definition_ren import ask_girlfriend_requirement, evening_date_trigger
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.ActionList_ren import ActionList
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import strip_club, bdsm_room
from renpy import persistent
import renpy

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

def hug_requirement(person: Person):
    love_requirement = 10
    if person.sluttiness < 5:
        return False #Don't show the option at all at minimal sluttiness.
    if mc.energy < 5:
        return "Requires: {energy=5}"
    if person.love < love_requirement:
        return f"Requires: {love_requirement} Love"
    return True

def kiss_requirement(person: Person):
    love_requirement = 30
    if person.has_relation_with_mc == False :
        return False  #Don't show if not a girlfriend
    if person.sluttiness < 5:
        return False #Don't show the option at all at minimal sluttiness.
    if mc.energy < 5:
        return "Requires: {energy=5}"
    if person.love < love_requirement:
        return f"Requires: {love_requirement} Love"
    return True

#Default "aggressive" actions that are displayed when talking to a girl.
specific_actions = ActionList([
    Action("Hug goodbye  {energy=-5}", requirement = hug_requirement, effect = "hug_person",
    menu_tooltip = "Be \"friendly\"! A good hug goes a long way."),
    Action("Kiss goodbye  {energy=-5}", requirement = kiss_requirement, effect = "kiss_person",
    menu_tooltip = "Give your sweet gal some loving."),
    Action("Grope her  {energy=-5}", requirement = grope_requirement, effect = "grope_person",
        menu_tooltip = 'Be "friendly" and see how far she is willing to let you take things. May make her more comfortable with physical contact, but at the cost of her opinion of you.'),
    Action("Give her a command", requirement = command_requirement, effect = "command_person",
        menu_tooltip = "Leverage her obedience and command her to do something."),
])

def sort_display_list(the_item): #Function to use when sorting lists of actions (and potentially people or strings)
    extra_args = None
    if isinstance(the_item, list): #If it's a list it's actually an item of some sort with extra args. Break those out and continue.
        extra_args = the_item[1]
        the_item = the_item[0]

    if isinstance(the_item, Action):
        if the_item.is_action_enabled(extra_args):
            return the_item.priority
        return the_item.priority - 1000 #Apply a ranking penalty to disabled items. They will appear in priority order but below enabled events (Unless something has a massive priority).

    if isinstance(the_item, Person):
        return the_item.sluttiness #Order people by sluttiness? Love? Something else?
    return 0

def build_specific_action_list(person: Person, keep_talking = True):
    specific_actions_list = ["Say goodbye"]
    for act in specific_actions:
        if keep_talking or act.is_fast:
            specific_actions_list.append((act, person))

    specific_actions_list.sort(key = sort_display_list, reverse = True)
    specific_actions_list.insert(0, "Do something specific")
    return specific_actions_list

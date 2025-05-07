from __future__ import annotations

from game.bugfix_additions.ActionMod_ren import limited_time_event_pool
from game.game_roles._role_definitions_ren import mother_role, sister_role
from game.helper_functions.heart_formatting_functions_ren import get_gold_heart
from game.major_game_classes.character_related.Person_ren import Person, mc, mom
from game.major_game_classes.game_logic.Action_ren import Action, Limited_Time_Action

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def build_sleep_climax_menu_options(person: Person, straddle = False, stomach_allowed = False, face_allowed = False, tits_allowed = False, throat_allowed = False, inside_allowed = False, pussy_allowed = False):
    climax_options = [("Cum in your hand", "air")]

    if person.vagina_available:
        pussy_allowed = True

    if stomach_allowed:
        climax_options.append(("Cum on her stomach", "body"))

    if tits_allowed:
        if person.effective_sluttiness() >= 30:
            climax_options.append(("Cum on her tits", "tits"))
        else:
            climax_options.append((f"Cum on her tits\n{{menu_red}}Requires: {get_gold_heart(30)}{{/menu_red}} (disabled)", "tits"))

    if face_allowed:
        if person.effective_sluttiness() >= 40:
            climax_options.append(("Cum on her face", "face"))
        else:
            climax_options.append((f"Cum on her face\n{{menu_red}}Requires: {get_gold_heart(40)}{{/menu_red}} (disabled)", "face"))

    if throat_allowed:
        if person.effective_sluttiness() >= 55:
            climax_options.append(("Cum down her throat", "throat"))
        else:
            climax_options.append((f"Cum down her throat\n{{menu_red}}Requires: {get_gold_heart(55)}{{/menu_red}} (disabled)", "throat"))

    if pussy_allowed:
       if person.effective_sluttiness() >= 30:
            climax_options.append(("Cum on her pussy", "pussy"))
       else:
            climax_options.append((f"Cum on her pussy\n{{menu_red}}Requires: {get_gold_heart(30)}{{/menu_red}} (disabled)", "pussy"))

    if inside_allowed:
        if person.effective_sluttiness() >= 65 or mc.condom:
            climax_options.append(("Cum inside her", "pussy"))
        else:
            climax_options.append((f"Cum inside her\n{{menu_red}}Requires: {get_gold_heart(65)}{{/menu_red}} (disabled)", "pussy"))
    return climax_options

from __future__ import annotations
import builtins
from game.main_character.perks.Perks_ren import Ability_Perk, perk_system
from game.major_game_classes.game_logic.ClimaxController_ren import ClimaxController
from game.major_game_classes.character_related.Person_ren import mc
from renpy import persistent

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def oral_virgin_perception_perk_unlock():
    if not perk_system.has_ability_perk("Oral Virgin Perception") and number_of_sucking_cock_broken > 3:
        perk_system.add_ability_perk(Ability_Perk(description = "See or interact with a girl, you gain the ability to know if she's an oral virgin.", active = True, togglable = False, usable = False), "Oral Virgin Perception")
        return True
    return False

def anal_virgin_perception_perk_unlock():
    if not perk_system.has_ability_perk("Anal Virgin Perception") and number_of_anal_sex_broken > 3:
        perk_system.add_ability_perk(Ability_Perk(description = "See or interact with a girl, you gain the ability to know if she's an anal virgin.", active = True, togglable = False, usable = False), "Anal Virgin Perception")
        return True
    return False

def vaginal_virgin_perception_perk_unlock():
    if not perk_system.has_ability_perk("Vaginal Virgin Perception") and number_of_vaginal_sex_broken > 3:
        perk_system.add_ability_perk(Ability_Perk(description = "See or interact with a girl, you gain the ability to know if she's an vaginal virgin.", active = True, togglable = False, usable = False), "Vaginal Virgin Perception")
        return True
    return False

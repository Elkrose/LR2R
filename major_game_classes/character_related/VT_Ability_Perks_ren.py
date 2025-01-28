import renpy
import renpy.store
from renpy import persistent, basestring
from __future__ import annotations
import builtins
from game.random_lists_ren import get_random_from_weighted_list
from game.major_game_classes.game_logic.Person_ren import Person, list_of_people, mom, lily, aunt, cousin
from game.main_character.perks.Perks_ren import Ability_Perk, perk_system
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.character_related.StatTracker_ren import StatTracker, number_of_sucking_cock_broken, number_of_anal_sex_broken, number_of_vaginal_sex_broken

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 900 python:
"""

def oral_virgin_perception_perk_unlock():
    if not perk_system.has_ability_perk("Lip Lock Intuition") and mc.stats.number_of_sucking_cock_broken > 3:
        perk_system.add_ability_perk(Ability_Perk(description = "A subtle perception that senses a girl's oral intimacy experience. It reads the cues of her lips and energies, granting a quiet understanding of her intimate encounters. With Lip Lock Intuition, the user discerns her oral experience, perceiving the unspoken truth behind her smile and gaining insight into her desires and boundaries.", active = True, togglable = False, usable = False), "Lip Lock Intuition")
        return True
    return False

def anal_virgin_perception_perk_unlock():
    if not perk_system.has_ability_perk("Midnight Mirage") and mc.stats.number_of_anal_sex_broken > 3:
        perk_system.add_ability_perk(Ability_Perk(description = "A shadowy perception that senses a girl's anal intimacy experience. This dark intuition navigates her hidden desires and experiences, granting a veiled understanding of her guarded secrets. With Midnight Mirage, the user discerns her anal experience, perceiving the unseen truth hidden from the light and gaining insight into her deepest desires.", active = True, togglable = False, usable = False), "Midnight Mirage")
        return True
    return False

def vaginal_virgin_perception_perk_unlock():
    if not perk_system.has_ability_perk("Rose Petal Insight") and mc.stats.number_of_vaginal_sex_broken > 3:
        perk_system.add_ability_perk(Ability_Perk(description = "A delicate perception that allows the user to sense whether a girl has experienced vaginal intimacy or remains untouched. This gentle intuition picks up on the subtlest energies and auras, granting the user a quiet understanding of her most private and personal history. With the Rose Petal Insight, the user can discern the presence or absence of vaginal experience, perceiving the unspoken truth that lies beneath her surface.", active = True, togglable = False, usable = False), "Rose Petal Insight")
        return True
    return False

def bald_eagle_perception_perk_unlock():
    if not perk_system.has_ability_perk("Bald Eagle Perception") and mc.stats.number_of_bare_pussy_broken > 3:
        perk_system.add_ability_perk(Ability_Perk(description = "A supernatural ability that grants the user insight into a girl's most intimate secret: whether she's wearing panties or not. With a single glance, the user can sense the presence or absence of undergarments, revealing a hidden truth that's invisible to the naked eye. This X-ray-like vision pierces through clothing, allowing the user to uncover a secret that's normally reserved for the most intimate of relationships. The ability is both thrilling and unsettling, offering a forbidden glimpse into a girl's private world and leaving the user with a sense of power and intrigue.", active = True, togglable = False, usable = False), "Bald Eagle Perception")
        return True
    return False

def strap_sense_perk_unlock():
    if not perk_system.has_ability_perk("Strap Sense") and mc.stats.number_of_bare_tits_broken > 3:
        perk_system.add_ability_perk(Ability_Perk(description = "A unique perception that allows the user to detect the presence or absence of a bra on a girl. This specialized intuition focuses on the subtle signs of straps, cups, and clasps, giving the user a clear sense of whether she's wearing a bra or going au naturel. With the Strap Sense ability, the user can instantly know whether a girl's curves are supported by lingerie or not.", active = True, togglable = False, usable = False), "Strap Sense")
        return True
    return False

def condomless_sex_perk_unlock():
    if not perk_system.has_ability_perk("Skin Deep Sense") and mc.stats.number_of_condomless_sex_broken > 3:
        perk_system.add_ability_perk(Ability_Perk(description = "A primal perception that allows the user to sense whether a girl has engaged in unprotected sex or always prioritizes protection. This raw intuition taps into the unspoken energies of her intimate encounters, granting the user a visceral understanding of her most private choices. With the Skin Deep Sense, the user can discern the presence or absence of condomless experiences, perceiving the unguarded truth that lies beneath her surface.", active = True, togglable = False, usable = False), "Skin Deep Sense")
        return True
    return False

def personality_insight_perk_unlock():
    if not perk_system.has_ability_perk("Social Sage") and len(known_people_in_the_game()) == 20:
        perk_system.add_ability_perk(Ability_Perk(description = "A keen understanding of human nature that allows the user to discern the underlying personalities of those they meet. This intuitive insight taps into the subtle cues and behaviors of others, granting the user a profound comprehension of their motivations, values, and desires. With the Social Sage, the user can perceive the intricate tapestry of personalities that surrounds them, navigating social situations with ease and finesse.", active = True, togglable = False, usable = False), "Social Sage")
        return True
    return False
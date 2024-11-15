import renpy # @UnresolvedImport
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.game_roles.business_roles._business_role_definitions_ren import clone_role
from game.game_roles.role_pregnant_definition_ren import become_pregnant
from game.bugfix_additions.SerumTraitMod_ren import SerumTraitMod
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.serums._serum_traits_T0_ren import basic_med_app

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
import inspect
from typing import Callable

list_of_instantiation_functions.append("init_Virginal_Serum")
##VIRGINITY##
## Virginity Tracker ##
#hymen = None, vaginal_virgin = 0, anal_virgin = 0, oral_virgin = 0, vaginal_first = None, anal_first = None, oral_first = None
#hymen is 0 = sealed, 1=recently torn bleeding(negative number instead?), 2=normal - serum to regenerate vaginal and hymen
#person.vaginal_virgin is None: #0=virgin, 1=just the tip, 2=full penetration, 3-10 is degree of tightness to loose, longer they go without sex usually returns to 7=normal if had kids
#anal_virgin is None: #0=virgin, 1=just the tip, 2=full penetration, 3-10 is degree of tightness to loose -placeholder atm
#oral_virgin is None: #0=virgin, 1=just the tip, 2=full penetration, 3-10 is degree of tightness to loose -placeholder atm

### Virgin ON APPLY ####
def hymen_restore_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log=add_to_log)
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Vaginal Stimulation started", "float_text_pink")
    if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
        renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god my....it itches!")

def anal_restore_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log=add_to_log)
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Anal Stimulation Started", "float_text_pink")
    if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
        renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god! Excuse me! How embarrassing!")

def oral_restore_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log=add_to_log)
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Throat Stimulation started", "float_text_pink")
    if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
        renpy.say(f"{person.title or person.create_formatted_title('???')}", "Ugh, why am I drooling???!")

def clone_womb_restore_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log=add_to_log)
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Clone Womb Stimulation started", "float_text_blue")
    if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
        renpy.say(f"{person.title or person.create_formatted_title('???')}", "Ugh, my tummy feels weird... I think I need to go throw up!? *turns pale* OMG out of my way! *hic*")

def true_virgin_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-10, add_to_log=add_to_log)
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Virgin Purity Stimulation started", "float_text_pink")
    if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
        renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god my....it itches! Ugh, why am I drooling???! Oh my god! Excuse me! How embarrassing!")

### Virgin ON TURN ###
def hymen_restore_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log=add_to_log)
    if person.vaginal_virgin >= 1:
        person.vaginal_virgin -= 1
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god my....it itches!")
    elif person.vaginal_virgin == 0:
        if person.hymen == 2:
            person.hymen = 1
            person.restore_taboo('vaginal_sex')
            if add_to_log:
                mc.log_event(f"{person.title or person.create_formatted_title('???')}: Hymen 50% Restored", "float_text_grey")
        if person.hymen == 1:
            person.hymen = 0
            person.restore_taboo('vaginal_sex')
            if add_to_log:
                mc.log_event(f"{person.title or person.create_formatted_title('???')}: Vaginal Stimulation Ended", "float_text_pink")

def anal_restore_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log=add_to_log)
    if person.anal_virgin >= 1:
        person.anal_virgin -= 1
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god! Excuse me! How embarrassing!")
    if person.anal_virgin == 0:
        person.restore_taboo('anal_sex')
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Anal Stimulation Ended", "float_text_pink")

def oral_restore_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log=add_to_log)
    if person.oral_virgin >= 1:
        person.oral_virgin -= 1
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "Ugh, why am I drooling???!")
    if person.oral_virgin == 0:
        person.restore_taboo('sucking cock')
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Throat Stimulation Ended", "float_text_pink")

def true_virgin_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log=add_to_log)
    if person.vaginal_virgin >= 1:
        person.vaginal_virgin -= 1
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god my....it itches!")
    elif person.vaginal_virgin == 0:
        if person.hymen == 2:
            person.hymen = 1
            person.restore_taboo('vaginal_sex')
            if add_to_log:
                mc.log_event(f"{person.title or person.create_formatted_title('???')}: Hymen 50% Restored", "float_text_grey")
        if person.hymen == 1:
            person.hymen = 0
            person.restore_taboo('vaginal_sex')
            if add_to_log:
                mc.log_event(f"{person.title or person.create_formatted_title('???')}: True Vaginal Stimulation Ended", "float_text_pink")
    if person.anal_virgin >= 1:
        person.anal_virgin -= 1
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god! Excuse me! How embarrassing!")
    if person.anal_virgin == 0:
        person.restore_taboo('anal_sex')
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: True Anal Stimulation Ended", "float_text_pink")
    if person.oral_virgin >= 1:
        person.oral_virgin -= 1
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "Ugh, why am I drooling???!")
    if person.oral_virgin == 0:
        person.restore_taboo('sucking cock')
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: True Throat Stimulation Ended", "float_text_pink")

def clone_womb_restore_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log=add_to_log)
    if person.vaginal_virgin >= 1:
        person.vaginal_virgin -= 1
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "Ugh, my tummy feels weird... I think I need to... *turns pale* OMG out of my way! *hic*")
    if person.vaginal_virgin == 0:
        person.vaginal_first = None
        person.hymen = 0
        person.restore_taboo('vaginal_sex')
        if person.is_clone:
            person.clone_womb_revived = True
            # used as flag from become_pregnant, so as not to override is_clone elsewhere
            # probably a better way to do this (global variable?)
            person.clone_can_become_pregnant = False

        person._baby_desire = 100
        person.restore_taboo('vaginal_sex')
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Clone Womb Stimulation Ended", "float_text_blue")

### Virgin ON REMOVE ###
def hymen_restore_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Vaginal Stimulation Completed", "float_text_pink")

def anal_restore_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Anal Stimulation Completed", "float_text_pink")

def oral_restore_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Throat Stimulation Completed", "float_text_pink")

def true_virgin_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Virgin Purity Stimulation Completed", "float_text_blue")

def clone_womb_restore_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Clone Womb Stimulation Completed", "float_text_blue")

#Rose Blossom Stims
def rose_blossom_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    #basically to give a one quick shot, then daily small increases over time
    if person.suggestibility <= 30:
        person.change_suggest(30, add_to_log = add_to_log)
    if person.happiness <= 30:
        person.change_happiness(30, add_to_log = add_to_log)
    if person.sluttiness <= 30:
        person.change_slut(30, 30, add_to_log = add_to_log)
    if person.arousal <= 30:
        person.change_arousal(30, add_to_log = add_to_log)
    if person.obedience <= 160:
        person.change_obedience(30, add_to_log = add_to_log)
    if person.love <= 70:
        person.change_love(30, add_to_log = add_to_log)
    if person.charisma <= 4:
        person.change_cha(2, add_to_log = add_to_log)
    if person.focus <= 4:
        person.change_focus(2, add_to_log = add_to_log)
    if person.int <= 4:
        person.change_int(2, add_to_log = add_to_log)

    return
def rose_blossom_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    #basically to give a one quick shot, then daily small increases over time
    if person.suggestibility <= 95:
        person.change_suggest(5, add_to_log = add_to_log)
    if person.happiness <= 295:
        person.change_happiness(5, add_to_log = add_to_log)
    if person.sluttiness <= 95:
        person.change_slut(5, add_to_log = add_to_log)
    if person.arousal <= 65:
        person.change_arousal(5, add_to_log = add_to_log)
    if person.obedience <= 295:
        person.change_obedience(5, add_to_log = add_to_log)
    if person.love <= 95:
        person.change_love(5, add_to_log = add_to_log)
    if person.charisma <= 19:
        person.change_cha(1, add_to_log = add_to_log)
    if person.focus <= 19:
        person.change_focus(1, add_to_log = add_to_log)
    if person.int <= 19:
        person.change_int(1, add_to_log = add_to_log)
    return
def rose_blossom_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    #if on Rose Blossoms, the suggestion should always be above 50
    #remove_suggest_effect(50)
    return
def red_roses_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: R3D R0535 injested", "float_text_red")
    if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
        renpy.say(f"{person.title or person.create_formatted_title('???')}", "mmmMM tastes like cherries!")
    #basically to give a one quick shot, then daily small increases over time
    if person.suggestibility <= 95:
        person.change_suggest(5, add_to_log = add_to_log)
    if person.happiness <= 300:
        person.change_happiness(5, add_to_log = add_to_log)
    if person.sluttiness <= 95:
        person.change_slut(5, add_to_log = add_to_log)
    if person.arousal <= 65:
        person.change_arousal(5, add_to_log = add_to_log)
    if person.obedience <= 295:
        person.change_obedience(5, add_to_log = add_to_log)
    if person.love <= 80:
        person.change_love(5, add_to_log = add_to_log)
    return
def red_roses_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
   #basically to give a one quick shot, then daily small increases over time
    if person.suggestibility <= 95:
        person.change_suggest(5, add_to_log = add_to_log)
    if person.happiness <= 300:
        person.change_happiness(5, add_to_log = add_to_log)
    if person.sluttiness <= 95:
        person.change_slut(5, add_to_log = add_to_log)
    if person.arousal <= 65:
        person.change_arousal(5, add_to_log = add_to_log)
    if person.obedience <= 295:
        person.change_obedience(5, add_to_log = add_to_log)
    if person.love <= 80:
        person.change_love(5, add_to_log = add_to_log)
    return
def red_roses_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_focus(2, add_to_log = add_to_log)
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: R3D R0535 Completed", "float_text_red")
    return

def fertile_rose_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: F3RT1L3 R053 injested", "float_text_red")
    #Sluttiness
    person.add_situational_slut("F3RT1L3 R053 5LUT", 50, "F3RT1L3 R053 5LUT!")
    #Arousal/Novelty
    person.change_arousal(30, add_to_log = add_to_log)
    person.change_novelty(69, add_to_log = add_to_log)
    #Obedience
    if person.obedience<=160:
        person.change_obedience(100, add_to_log=add_to_log)
    else:
        person.add_situational_obedience("F3RT1L3 R053 0B3Y", 300, "You will 0B3Y!")
    #suggestibility
    person.add_suggest_effect(80, add_to_log = add_to_log)
    #happiness
    if person.happiness<=200:
        person.change_happiness(50, add_to_log=add_to_log)
    #love
    if person.love <=50:
        person.change_love(10, add_to_log=add_to_log)
    #fertile Security Locker and story locker
    if person not in (erica, camila):
        if person.on_birth_control:
            person.fertility_percent = 0.001
            if add_to_log: 
                display_name = person.create_formatted_title("???")
                if person.title: display_name = person.title
                mc.log_event(display_name + ":F3RT1L3 R053 3GG PR0T3CT3D!", "float_text_red")
        else:
            person.fertility_percent = person.fertility_percent + 100
            if person.baby_desire < 500:
                person.change_baby_desire(person.baby_desire + 50)
            if add_to_log: 
                display_name = person.create_formatted_title("???")
                if person.title: display_name = person.title
                mc.log_event(display_name + ":F3RT1L3 R053 3GG H4XX3D!", "float_text_red")
            #to show that the first effects are kicking in
            person.ideal_fertile_day = ((day+1) % 30)
            if add_to_log: 
                    display_name = person.create_formatted_title("???")
                    if person.title: display_name = person.title
                    mc.log_event(f"{person.title or person.create_formatted_title('???')}: ovum is maturing...", "float_text_red")
        if person in mc.location.people:
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "mmmMM tastes like watermelon!")
    else:
        if add_to_log: 
                display_name = person.create_formatted_title("???")
                if person.title: display_name = person.title
                mc.log_event(display_name + ":F3RT1L3 R053 5T0RY PR0T3CT3D!", "float_text_red")
        if person in mc.location.people:
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "ew! tastes like lemons!")
    return
def fertile_rose_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    #ensures the person will eventually get horny... soon
    if person.happiness<=150:
        person.change_happiness(15, add_to_log=add_to_log)
    else:
        person.change_happiness(5, add_to_log=add_to_log)
    person.change_novelty(5, add_to_log = add_to_log)
    #love
    if person.love <=90:
        person.change_love(5, add_to_log=add_to_log)
    if person.arousal < 100: 
        person.change_arousal(5, add_to_log = add_to_log)
        if add_to_log and person.arousal>70: 
            display_name = person.create_formatted_title("???")
            if person.title: display_name = person.title
            mc.log_event(display_name + ":F3RT1L3 R053 getting her wet...", "float_text_pink")
    #fertile Security story locker
    if person not in (erica, camila):
        if not person.on_birth_control:
            person.fertility_percent = person.fertility_percent + 100
            if person.baby_desire < 500:
                person.change_baby_desire(person.baby_desire + 10)
            #if add_to_log: 
            display_name = person.create_formatted_title("???")
            if person.title: display_name = person.title
            mc.log_event(display_name + f":3GG H4XX3D! {person.effective_fertility:.1f}%", "float_text_red")
    return
def fertile_rose_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    #Sluttiness
    person.clear_situational_slut("F3RT1L3 R053 5LUT")
    #Arousal/Novelty
    person.reset_arousal()
    #Obedience
    person.clear_situational_obedience("F3RT1L3 R053 0B3Y")
    #Suggestibility
    person.remove_suggest_effect(80)
    #fertile Security Locker and story locker
    if person not in (erica, camila):
        if person.on_birth_control:
            #the BC helps regulate the fertility back to normal ranges
            person.fertility_percent = 20.0 - ((person.age - Person.get_age_floor()) / 3.0)
        else:
            #Fertility Restored but permanently damaged due to F3RT1L3 R053
            person.fertility_percent = renpy.random.randint(50, 100)
    #to show the serum expired
    #if add_to_log: 
    display_name = person.create_formatted_title("???")
    if person.title: display_name = person.title
    mc.log_event(display_name + ":F3RT1L3 R053 3XP1R3D!", "float_text_red")
    return

def crimson_roses_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    #basically to give a one quick shot, then daily small increases over time
    person.fertility_percent += 70
    person.bc_penalty += 40
    display_name = person.create_formatted_title("???")
    if person.title:
        display_name = person.title
    if add_to_log:
        mc.log_event(display_name + ": Birth control effectiveness reduced by 40%", "float_text_grey")
    if person.arousal < person.suggestibility:
        person.change_arousal(65,add_to_log = False)
    if person.suggestibility <= 95:
        person.add_suggest_effect(55, add_to_log = add_to_log)
    if person.happiness <= 300:
        person.change_happiness(55, add_to_log = add_to_log)
    if person.sluttiness <= 95:
        person.change_slut(55, add_to_log = add_to_log)
    if person.arousal <= 65:
        person.change_arousal(55, add_to_log = add_to_log)
    if person.obedience <= 295:
        person.change_obedience(55, add_to_log = add_to_log)
    if person.love <= 80:
        person.change_love(55, add_to_log = add_to_log)
    return
def crimson_roses_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    #ensures the person will eventually get horny... soon
    person.change_happiness(10, add_to_log = add_to_log)
    person.change_happiness(5, add_to_log=add_to_log)
    if person.arousal < 90: 
        person.change_arousal(15, add_to_log = False)
        #if add_to_log and person.arousal>70:
        if person.arousal>70:
            display_name = person.create_formatted_title("???")
            if person.title: display_name = person.title
            mc.log_event(display_name + ":CR1M50N R053 is making her wet...", "float_text_pink")
    return
def crimson_roses_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    #person.change_focus(2, add_to_log = add_to_log)
    return

def smart_roses_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    #first dose brings them up to base good stats
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: 5M4RT R053 injested", "float_text_blue")
    if person.charisma < 4:
        person.charisma = 4
    else:
        person.charisma +=1
    if person.int < 4:
        person.int = 4
    else:
        person.int +=1
    if person.focus < 4:
        person.focus = 4
    else:
        person.focus +=1
    return
def smart_roses_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.charisma < 20:
        person.charisma +=1
    if person.int < 20:
        person.int +=1
    if person.focus < 20:
        person.focus +=1
    return
def smart_roses_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    display_name = person.create_formatted_title("???")
    if person.title: display_name = person.title
    mc.log_event(display_name + ":5M4RT R0535 finished...", "float_text_blue")
    return

def rose_gardens_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.happiness <= 300:
        person.change_happiness(35, add_to_log = add_to_log)
    if not person.has_role(pregnant_role):
        return
    if person.event_triggers_dict.get("preg_announce_day", day) -1 > day:
        person.event_triggers_dict["preg_announce_day"] = person.event_triggers_dict.get("preg_announce_day", day) - 1
    if person.event_triggers_dict.get("preg_tits_date", day) - 1 > day:
        if person.event_triggers_dict.get("preg_tits_date", day) -1 > person.event_triggers_dict.get("preg_announce_day", 9999):
            person.event_triggers_dict["preg_tits_date"] = person.event_triggers_dict.get("preg_tits_date", day) - 1
    if person.event_triggers_dict.get("preg_transform_day", day) - 1 > day:
        if person.event_triggers_dict.get("preg_transform_day", day)-1 > person.event_triggers_dict.get("preg_tits_date", 9999):
            person.event_triggers_dict["preg_transform_day"] = person.event_triggers_dict.get("preg_transform_day", day) - 1
    if person.event_triggers_dict.get("preg_finish_announce_day", day) - 1 > day:
        if person.event_triggers_dict.get("preg_finish_announce_day", day) -1 > person.event_triggers_dict.get("preg_transform_day", 9999):
            person.event_triggers_dict["preg_finish_announce_day"] = person.event_triggers_dict.get("preg_finish_announce_day", day) - 1
    return
def rose_gardens_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.happiness <= 300:
        person.change_happiness(15, add_to_log = add_to_log)
    if not person.has_role(pregnant_role):
        return
    if person.event_triggers_dict.get("preg_announce_day", day) -5 > day:
        person.event_triggers_dict["preg_announce_day"] = person.event_triggers_dict.get("preg_announce_day", day) - 5
    if person.event_triggers_dict.get("preg_tits_date", day) - 5 > day:
        if person.event_triggers_dict.get("preg_tits_date", day) -5 > person.event_triggers_dict.get("preg_announce_day", 9999):
            person.event_triggers_dict["preg_tits_date"] = person.event_triggers_dict.get("preg_tits_date", day) - 5
    if person.event_triggers_dict.get("preg_transform_day", day) - 5 > day:
        if person.event_triggers_dict.get("preg_transform_day", day)-5 > person.event_triggers_dict.get("preg_tits_date", 9999):
            person.event_triggers_dict["preg_transform_day"] = person.event_triggers_dict.get("preg_transform_day", day) - 5
    if person.event_triggers_dict.get("preg_finish_announce_day", day) - 5 > day:
        if person.event_triggers_dict.get("preg_finish_announce_day", day) -5 > person.event_triggers_dict.get("preg_transform_day", 9999):
            person.event_triggers_dict["preg_finish_announce_day"] = person.event_triggers_dict.get("preg_finish_announce_day", day) - 5
    return
def rose_gardens_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    display_name = person.create_formatted_title("???")
    if person.title: display_name = person.title
    mc.log_event(display_name + ":R053 G4RD3N5 finished...", "float_text_blue")
    return
    
## Override/inject into core code
def _vt_is_clone_override(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        self = args[0] if len(args) > 0 and isinstance(args[0], Person) else (kwargs["person"] if kwargs.get("person") else None)
        if not self:
            raise ValueError
        # wrapped_func (is_clone) returns True iff has_role(clone_role)
        #
        # if clone has been given "Clone Womb Revival Stim", then
        # `not self.clone_can_become_pregnant` == False, so that `become_pregnant` proceeds as if `person.is_clone == False`
        return wrapped_func(*args, **kwargs) \
            and not getattr(self, "clone_can_become_pregnant", False)

    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    # NOTE: because is_clone is a property, this is different than other injections
    return property(wrapping_func)

def _vt_become_pregnant_override(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        # variable initialization; get the `person` variable
        person = args[0] if len(args) > 0 and isinstance(args[0], Person) else (kwargs["person"] if kwargs.get("person") else None)
        if not person:
            raise ValueError

        # set the "being called from `become_pregnant`" flag
        if hasattr(person, "clone_can_become_pregnant") and getattr(person, "clone_womb_revived", False):
            person.clone_can_become_pregnant = True

        # call core code (has side-effects)
        wrapped_func(*args, **kwargs)

        # reset the "being called from `become_pregnant`" flag
        # so that any other functions using is_clone get the un-modified value
        if hasattr(person, "clone_can_become_pregnant"):
            person.clone_can_become_pregnant = False
        return
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

# set the injections
# TODO: should be called from an instantiation function?
setattr(Person, "is_clone", _vt_is_clone_override(Person.is_clone.__get__))
become_pregnant = _vt_become_pregnant_override(become_pregnant)

### Virginal SerumDesign ###
def init_Virginal_Serum():
    SerumTraitMod(name = "Vaginal Muscle Stim",
        desc = "A special serum trait developed to restore the muscles around the vaginal cavity. Requires a week to fully stimulate",
        positive_slug = "Vaginal muscles will be stimulated",
        negative_slug = "Stimulation is not a comfortable process. Stimulation may cause the hymen to regrow.",
        research_added = 300,
        base_side_effect_chance = 50,
        duration_added = 3,
        on_turn = hymen_restore_on_turn,
        on_apply = hymen_restore_on_apply,
        on_remove = hymen_restore_on_remove,
        requires = [basic_med_app],
        tier = 2,
        start_researched = False,
        research_needed = 750,
        clarity_cost = 500,
        hidden_tag = "Medical",
        mental_aspect = 2, physical_aspect = 2, sexual_aspect = 2, medical_aspect = 6, flaws_aspect = 0, attention = 2)

    SerumTraitMod(name = "Anal Muscle Stim",
        desc = "A special serum trait developed to restore the muscles around the anal cavity. Requires a week to fully stimulate.",
        positive_slug = "Anal muscles will be stimulated",
        negative_slug = "Stimulation is not a comfortable process, may cause excessive methane production.",
        research_added = 300,
        base_side_effect_chance = 50,
        duration_added = 3,
        on_turn = anal_restore_on_turn,
        on_apply = anal_restore_on_apply,
        on_remove = anal_restore_on_remove,
        requires = [basic_med_app],
        tier = 2,
        start_researched = False,
        research_needed = 750,
        clarity_cost = 500,
        hidden_tag = "Medical",
        mental_aspect = 2, physical_aspect = 2, sexual_aspect = 2, medical_aspect = 6, flaws_aspect = 0, attention = 1)

    SerumTraitMod(name = "Throat Muscle Stim",
        desc = "A special serum trait developed to restore the muscles around the throat cavity. Requires a week to fully stimulate.",
        positive_slug = "Throat muscles will be stimulated",
        negative_slug = "Stimulation is not a comfortable process, may cause excessive saliva production.",
        research_added = 300,
        base_side_effect_chance = 50,
        duration_added = 3,
        on_turn = oral_restore_on_turn,
        on_apply = oral_restore_on_apply,
        on_remove = oral_restore_on_remove,
        requires = [basic_med_app],
        tier = 2,
        start_researched = False,
        research_needed = 750,
        clarity_cost = 500,
        hidden_tag = "Medical",
        mental_aspect = 2, physical_aspect = 2, sexual_aspect = 2, medical_aspect = 6, flaws_aspect = 0, attention = 1)

    SerumTraitMod(name = "Virginity Purity Stim",
        desc = "A special serum trait developed to restore the muscles around the throat, anal, and vaginal cavity. Requires a week to fully stimulate.",
        positive_slug = "Throat, anal and vaginal muscles will be stimulated",
        negative_slug = "Stimulation is not a comfortable process and may cause excessive saliva and methane production. Stimulation may also cause the hymen to regrow.",
        research_added = 300,
        base_side_effect_chance = 100,
        duration_added = 3,
        on_turn = true_virgin_on_turn,
        on_apply = true_virgin_on_apply,
        on_remove = true_virgin_on_remove,
        requires = [basic_med_app],
        tier = 2,
        start_researched = False,
        research_needed = 2000,
        clarity_cost = 2000,
        hidden_tag = "Medical",
        mental_aspect = 5, physical_aspect = 5, sexual_aspect = 9, medical_aspect = 9, flaws_aspect = 0, attention = 5)

    SerumTraitMod(name = "Clone Womb Revival Stim",
        desc = "A special serum trait developed to restore the womb of the infertile clone. Requires a week to fully stimulate.",
        positive_slug = "Womb muscles will be stimulated, vitamins and regrowth of fallopian tubes, egg growth.",
        negative_slug = "Stimulation is not a comfortable process, may cause excessive upset stomache aches and pains.",
        research_added = 300,
        base_side_effect_chance = 50,
        duration_added = 3,
        on_turn = clone_womb_restore_on_turn,
        on_apply = clone_womb_restore_on_apply,
        on_remove = clone_womb_restore_on_remove,
        requires = [basic_med_app],
        tier = 3,
        start_researched = False,
        research_needed = 1450,
        clarity_cost = 1500,
        hidden_tag = ["Reproduction", "Medical"],
        mental_aspect = 4, physical_aspect = 2, sexual_aspect = 4, medical_aspect = 6, flaws_aspect = 0, attention = 5)

    SerumTraitMod(name = "R3D R0535",
        desc = "Red Rose formula, meant to hugely stimulate neural pathways positively, in theory.",
        positive_slug = "Permanently icreases suggest, happiness, sluttiness, arousal, obedience and love.",
        negative_slug = "One dose lasts 7 durations. Arousal",
        research_added = 20,
        base_side_effect_chance = 35,
        duration_added = 7,
        on_turn = red_roses_on_turn,
        on_apply = red_roses_on_apply,
        on_remove = red_roses_on_remove,
        requires = [basic_med_app],
        tier = 0,
        start_researched = False,
        research_needed = 50,
        clarity_cost = 50,
        hidden_tag = ["Obedience", "Slut"],
        mental_aspect = 50, physical_aspect = 50, sexual_aspect = 50, medical_aspect = 50, flaws_aspect = 0, attention = 5)

    SerumTraitMod(name = "F3RT1L3 R053",
        desc = "Sexual stimulator, an increase arousal and urge to copulate. Security Lock with Birth Control (will not affect Camila or Erica Story)",
        positive_slug = "One dose instant reaction, on turn +happiness and arousal",
        negative_slug = "Will interfer with ovum cycles. Might cause cramping and baby desire.",
        research_added = 2000,
        base_side_effect_chance = 75,
        duration_added = 5,
        on_turn = fertile_rose_on_turn,
        on_apply = fertile_rose_on_apply,
        on_remove = fertile_rose_on_remove,
        requires = [basic_med_app],
        tier = 0,
        start_researched = False,
        research_needed = 500,
        clarity_cost = 500,
        hidden_tag = ["Reproduction", "Unique"],
        mental_aspect = 69, physical_aspect = 69, sexual_aspect = 69, medical_aspect = 69, flaws_aspect = 0, attention = 5)

    SerumTraitMod(name = "CR1M50N R053",
        desc = "A more silent R3D R053, which leads to rose petals on beds, of course.",
        positive_slug = "7 durations +15 Arousal/turn",
        negative_slug = "BC -40%",
        research_added = 2000,
        base_side_effect_chance = 75,
        duration_added = 7,
        on_turn = crimson_roses_on_turn,
        on_apply = crimson_roses_on_apply,
        on_remove = crimson_roses_on_remove,
        requires = [basic_med_app],
        tier = 0,
        start_researched = False,
        research_needed = 500,
        clarity_cost = 500,
        exclude_tags = "Suggest",
        hidden_tag = ["Obedience", "Slut", "Suggest"],
        mental_aspect = 50, physical_aspect = 50, sexual_aspect = 50, medical_aspect = 50, flaws_aspect = 0, attention = 5)

    SerumTraitMod(name = "SM4RT R053",
        desc = "Permanently increase base stats, and slowly increases per turn.",
        positive_slug = "7 durations CHA/INT/FOC+ Max 20",
        negative_slug = "",
        research_added = 2000,
        base_side_effect_chance = 75,
        duration_added = 7,
        on_turn = smart_roses_on_turn,
        on_apply = smart_roses_on_apply,
        on_remove = smart_roses_on_remove,
        requires = [basic_med_app],
        tier = 0,
        start_researched = False,
        research_needed = 500,
        clarity_cost = 500,
        hidden_tag = "Skill",
        mental_aspect = 50, physical_aspect = 50, sexual_aspect = 50, medical_aspect = 50, flaws_aspect = 0, attention = 5)

    SerumTraitMod(name = "R053 BL0550M5",
        desc = "Company secret Rose Blossom formula, specially brewed to ensure the user will never feel alone nor incompetent.",
        positive_slug = "Permanently increases in Int/Focus/Charisma, suggest, happiness, sluttiness, arousal, obedience and love.",
        negative_slug = "One dose lasts 7 durations (max 20 Int/Foc/Cha)",
        research_added = 2000,
        base_side_effect_chance = 75,
        duration_added = 7,
        on_turn = rose_blossom_on_turn,
        on_apply = rose_blossom_on_apply,
        on_remove = rose_blossom_on_remove,
        requires = [basic_med_app],
        tier = 0,
        start_researched = False,
        research_needed = 500,
        clarity_cost = 500,
        hidden_tag = ["Obedience", "Slut", "Love"],
        mental_aspect = 55, physical_aspect = 55, sexual_aspect = 55, medical_aspect = 55, flaws_aspect = 0, attention = 5)

    SerumTraitMod(name = "R053 G4RD3N5",
        desc = "Company secret Rose Blossom formula, specially brewed to promote a healthy speedy, spectacular pregnancy! With Sparkles!",
        positive_slug = "7 durations, increases in Int/Focus/Charisma, suggest, happiness, sluttiness, arousal, obedience and love.",
        negative_slug = "One dose lasts 7 durations",
        research_added = 2000,
        base_side_effect_chance = 75,
        duration_added = 7,
        on_turn = rose_gardens_on_turn,
        on_apply = rose_gardens_on_apply,
        on_remove = rose_gardens_on_remove,
        requires = [basic_med_app],
        tier = 0,
        start_researched = False,
        research_needed = 500,
        clarity_cost = 500,
        exclude_tags = "Pregnancy",
        hidden_tag = ["Pregnancy", "Medical", "Unique"],
        mental_aspect = 55, physical_aspect = 55, sexual_aspect = 55, medical_aspect = 55, flaws_aspect = 0, attention = 5)

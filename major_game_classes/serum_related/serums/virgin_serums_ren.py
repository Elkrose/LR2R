import copy
from game.bugfix_additions.SerumTraitMod_ren import SerumTraitMod
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.serums._serum_traits_T0_ren import basic_med_app

"""renpy
init -1 python:
"""
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
    person.change_happiness(-5, add_to_log = add_to_log)
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Vaginal Stimulation started", "float_text_pink")
    if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
        renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god my....it itches!")
def anal_restore_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log = add_to_log)
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Anal Stimulaltion Started", "float_text_pink")
    if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
        renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god! Excuse me! How embarrassing!")
def oral_restore_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log = add_to_log)
    if add_to_log:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Throat Stimulation started", "float_text_pink")
    if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
        renpy.say(f"{person.title or person.create_formatted_title('???')}", "Ugh, why am I drooling???!")
### Virgin ON TURN ###
def hymen_restore_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log = add_to_log)
    if person.vaginal_virgin>=1: 
        person.vaginal_virgin -=1
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god my....it itches!")
    elif person.vaginal_virgin ==0:
        if person.hymen==2: 
            person.hymen=1
            if add_to_log:
                mc.log_event(f"{person.title or person.create_formatted_title('???')}: Hymen 50% Restored", "float_text_grey")
        if person.hymen==1:
            person.hymen=0
            if add_to_log:
                mc.log_event(f"{person.title or person.create_formatted_title('???')}: Vaginal Stimulation Ended", "float_text_pink")
def anal_restore_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log = add_to_log)
    if person.anal_virgin>=1: 
        person.anal_virgin -=1
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "Oh my god! Excuse me! How embarrassing!")
    if person.anal_virgin==0:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Anal Stimulation Ended", "float_text_pink")
def oral_restore_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-5, add_to_log = add_to_log)
    if person.oral_virgin>=1: 
        person.oral_virgin -=1
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.title or person.create_formatted_title('???')}", "Ugh, why am I drooling???!")
    if person.oral_virgin==0:
        mc.log_event(f"{person.title or person.create_formatted_title('???')}: Throat Stimulation Ended", "float_text_pink")
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
        mental_aspect = 2, physical_aspect = 2, sexual_aspect = 2, medical_aspect = 6, flaws_aspect = 0, attention = 1)
    

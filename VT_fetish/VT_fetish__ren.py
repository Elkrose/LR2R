from __future__ import annotations
import builtins
import renpy
from renpy import persistent
from game.helper_functions.list_functions_ren import get_random_from_list
from game.fetish.fetish_action_ren import Fetish_Action
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc, lily, mom, aunt, starbuck, stephanie, erica, candace, sarah, myra
from game.major_game_classes.game_logic.Room_ren import lily_bedroom, aunt_apartment, gym
from game.sex_positions._position_definitions_ren import missionary, doggy_anal
from game.people.Erica.erica_role_definition_ren import erica_get_progress, erica_has_given_morning_handjob
from game.people.Myrabelle.myra_role_definition_ren import myra_lewd_game_fuck_avail
from game.people.Sarah.sarah_definition_ren import sarah_threesomes_unlocked
from game.people.Starbuck.starbuck_role_definition_ren import get_shop_investment_rate, sex_shop_stage
from virgin_tracker_ren import NewPerson
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -50 python:
"""
FETISH_BASIC_OPINION_LIST = ["giving handjobs", "giving tit fucks", "being fingered", "kissing", "masturbating", "big dicks", "getting head", "lingerie"]
FETISH_ANAL_OPINION_LIST = ["anal sex", "doggy style sex", "anal creampies", "showing her ass"]
FETISH_CUM_OPINION_LIST = ["being covered in cum", "drinking cum", "cum facials", "giving blowjobs", "anal creampies", "creampies"]
FETISH_BREEDING_OPINION_LIST = ["bareback sex", "vaginal sex", "creampies", "missionary style sex"]
FETISH_EXHIBITION_OPINION_LIST = ["public sex", "not wearing underwear", "not wearing anything", "showing her tits", "showing her ass", "skimpy outfits", "skimpy uniforms", "sex standing up", "threesomes"]
#common tools
#$ VT_fetish_timer_reset(the_person, "breeding", 0)
def VT_fetish_timer_reset(person: Person, fetish_type:str, VT_fetishtimer=0, VT_fetish_Intro=True):
    person.set_event_day(f"{fetish_type}_fetish_locked", day+VT_fetishtimer)
    if VT_fetish_Intro:
        person.event_triggers_dict[f"VT_{fetish_type}_fetish_start"] = False
        person.remove_role(f"{fetish_type}_fetish_role")

####  VAGINAL FETISH
def VT_vaginal_fetish_employee_intro_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business and mc.is_at_office

def VT_vaginal_fetish_family_intro_requirement(person: Person):
    if person.home == harem_mansion:
        return person.is_available
    else:
        return person.is_home and person.location.person_count == 1

def VT_vaginal_fetish_generic_intro_requirement(person: Person):
    return person.location != person.home and person.is_available

def VT_vaginal_fetish_mom_intro_requirement():
    return mc.is_in_bed and mc.energy > 80 and mom.is_available

def VT_vaginal_fetish_lily_intro_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business and mc.is_at_office and lily.is_available

def VT_vaginal_fetish_rebecca_intro_requirement():
    return False

def VT_vaginal_fetish_gabrielle_intro_requirement():
    return False

def VT_vaginal_fetish_stephanie_intro_requirement():
    if mc.business.is_open_for_business and mc.is_at_office and renpy.random.randint(0, 100) < 20:
        return stephanie.is_available
    return False

def VT_vaginal_fetish_alex_intro_requirement():
    return False

def VT_vaginal_fetish_nora_intro_requirement():
    return False

def VT_vaginal_fetish_emily_intro_requirement():
    return False

def VT_vaginal_fetish_christina_intro_requirement():
    return False

def VT_vaginal_fetish_starbuck_intro_requirement():
    return time_of_day == 3 and mc.is_at_office and starbuck.is_available

def VT_vaginal_fetish_sarah_intro_requirement():
    return False

def VT_vaginal_fetish_ophelia_intro_requirement():
    return False

def VT_vaginal_fetish_candace_intro_requirement():
    return False

def VT_vaginal_fetish_dawn_intro_requirement():
    return False

def VT_vaginal_fetish_erica_intro_requirement():
    return day % 7 == 6 and erica.is_available

def VT_vaginal_fetish_ashley_intro_requirement():
    return False

def VT_vaginal_fetish_kaya_intro_requirement():
    return False

def VT_vaginal_fetish_ellie_intro_requirement():
    return False

def VT_vaginal_fetish_camila_intro_requirement():
    return False

def VT_vaginal_fetish_sakari_intro_requirement():
    return False

def VT_vaginal_fetish_myra_intro_requirement():
    return False

def VT_start_vaginal_fetish_quest(person: NewPerson):
    if (person.has_taboo("vaginal_sex") \
            or person.vaginal_sex_skill < 4 \
            or (person.opinion.vaginal_sex < 2 and person.opinion.creampies < 2 ) \
            or not person.is_willing(missionary) \
            or person.sluttiness < 60 \
            or person.opinion.showing_her_ass < 2
            or (person.vaginal_sex_count < 10 and person.vaginal_creampie_count <10)):
        return False

    if person.VT_has_started_vaginal_fetish:
        return False
    
    # when blocking the fetish gain, prevent repeat triggering for a while
    if day < person.get_event_day("vaginal_fetish_locked"):
        return False

    person.set_event_day("vaginal_fetish_locked", day + renpy.random.randint(5, 7) + person.opinion.being_submissive - person.opinion.taking_control)

    if person == lily:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Lily Vaginal Fetish Intro", VT_vaginal_fetish_lily_intro_requirement, "VT_vaginal_fetish_lily_intro_label", fetish_type = "vaginal")
        )
        return True
    if person == mom:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Jennifer Vaginal Fetish Intro", VT_vaginal_fetish_mom_intro_requirement, "VT_vaginal_fetish_mom_intro_label", fetish_type = "vaginal")
        )
        return True
    if person == starbuck:
        if get_shop_investment_rate() >= 6.0:
            mc.business.add_mandatory_crisis(
                Fetish_Action("Starbuck Vaginal Fetish Intro", VT_vaginal_fetish_starbuck_intro_requirement, "VT_vaginal_fetish_starbuck_intro_label", fetish_type = "vaginal")
            )
            return True
        return False
    if person == stephanie:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Stephanie Vaginal Fetish Intro", VT_vaginal_fetish_stephanie_intro_requirement, "VT_vaginal_fetish_stephanie_intro_label", fetish_type = "vaginal")
        )
        return True
    # elif person == emily and False:
    #     pass
    # elif person == christina and False:
    #     pass
    # elif person == sarah and False:
    #     pass
    # elif person == salon_manager and False:
    #     pass
    if person == erica:
        if erica_has_given_morning_handjob():
            mc.business.add_mandatory_morning_crisis(
                Fetish_Action("Erica Vaginal Fetish Intro", VT_vaginal_fetish_erica_intro_requirement, "VT_vaginal_fetish_erica_intro_label", fetish_type = "vaginal")
            )
            return True
        return False
    # if person == candace and False:
    #     pass
    # elif person == ashley and False:
    #     pass
    # elif person == alexia and False:
    #     pass
    # elif person == kaya and False:
    #     pass
    # elif person == ellie and False:
    #     pass
    # elif person == camila and False:
    #     pass
    # elif person == sakari and False:
    #     pass
    # if person == myra:
    #     Fetish_Action("Myra Anal Fetish Intro", anal_fetish_myra_intro_requirement, "anal_fetish_myra_intro_label", fetish_type = "anal")
    if person.is_employee and not person in (erica, lily, mom, stephanie, starbuck):
        mc.business.add_mandatory_crisis(
            Fetish_Action("Employee Vaginal Fetish Intro", VT_vaginal_fetish_employee_intro_requirement, "VT_vaginal_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "vaginal")
        )
        return True
    if person.is_family and not person in (erica, lily, mom, stephanie, starbuck):
        person.add_unique_on_room_enter_event(
            Fetish_Action("Family Vaginal Fetish Intro", VT_anal_fetish_family_intro_requirement, "VT_vaginal_fetish_family_intro_label", fetish_type = "vaginal", priority = 30)
        )
        return True

    if not person in (erica, lily, mom, stephanie, starbuck):
        person.add_unique_on_talk_event(
            Fetish_Action("Generic Vaginal Fetish Intro", VT_vaginal_fetish_generic_intro_requirement, "VT_vaginal_fetish_generic_intro_label", fetish_type = "vaginal")
        )
        return True
    return False


####  ANAL FETISH
def VT_anal_fetish_employee_intro_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business and mc.is_at_office

def VT_anal_fetish_family_intro_requirement(person: Person):
    if person.home == harem_mansion:
        return person.is_available
    else:
        return person.is_home and person.location.person_count == 1

def VT_anal_fetish_generic_intro_requirement(person: Person):
    return person.location != person.home and person.is_available

def VT_anal_fetish_mom_intro_requirement():
    return mc.is_in_bed and mc.energy > 80 and mom.is_available

def VT_anal_fetish_lily_intro_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business and mc.is_at_office and lily.is_available

def VT_anal_fetish_rebecca_intro_requirement():
    return False

def VT_anal_fetish_gabrielle_intro_requirement():
    return False

def VT_anal_fetish_stephanie_intro_requirement():
    if mc.business.is_open_for_business and mc.is_at_office and renpy.random.randint(0, 100) < 20:
        return stephanie.is_available
    return False

def VT_anal_fetish_alex_intro_requirement():
    return False

def VT_anal_fetish_nora_intro_requirement():
    return False

def VT_anal_fetish_emily_intro_requirement():
    return False

def VT_anal_fetish_christina_intro_requirement():
    return False

def VT_anal_fetish_starbuck_intro_requirement():
    return time_of_day == 3 and mc.is_at_office and starbuck.is_available

def VT_anal_fetish_sarah_intro_requirement():
    return False

def VT_anal_fetish_ophelia_intro_requirement():
    return False

def VT_anal_fetish_candace_intro_requirement():
    return False

def VT_anal_fetish_dawn_intro_requirement():
    return False

def VT_anal_fetish_erica_intro_requirement():
    return day % 7 == 6 and erica.is_available

def VT_anal_fetish_ashley_intro_requirement():
    return False

def VT_anal_fetish_kaya_intro_requirement():
    return False

def VT_anal_fetish_ellie_intro_requirement():
    return False

def VT_anal_fetish_camila_intro_requirement():
    return False

def VT_anal_fetish_sakari_intro_requirement():
    return False

def VT_anal_fetish_myra_intro_requirement():
    return False

def VT_start_anal_fetish_quest(person: NewPerson):
    if (person.has_taboo("anal_sex") \
            or person.anal_sex_skill < 4 \
            or (person.opinion.anal_sex < 2 and person.opinion.anal_creampies < 2 ) \
            or not person.is_willing(doggy_anal) \
            or person.sluttiness < 60 \
            or (person.anal_sex_count < 10 and person.anal_creampie_count <10)):
        return False

    if person.VT_has_started_anal_fetish:
        return False
    
    # when blocking the fetish gain, prevent repeat triggering for a while
    if day < person.get_event_day("anal_fetish_locked"):
        return False

    person.set_event_day("anal_fetish_locked", day + renpy.random.randint(5, 7) + person.opinion.being_submissive - person.opinion.taking_control)

    if person == lily:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Lily Anal Fetish Intro", VT_anal_fetish_lily_intro_requirement, "VT_anal_fetish_lily_intro_label", fetish_type = "anal")
        )
        return True
    if person == mom:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Jennifer Anal Fetish Intro", VT_anal_fetish_mom_intro_requirement, "VT_anal_fetish_mom_intro_label", fetish_type = "anal")
        )
        return True
    if person == starbuck:
        if get_shop_investment_rate() >= 6.0:
            mc.business.add_mandatory_crisis(
                Fetish_Action("Starbuck Anal Fetish Intro", VT_anal_fetish_starbuck_intro_requirement, "VT_anal_fetish_starbuck_intro_label", fetish_type = "anal")
            )
            return True
        return False
    if person == stephanie:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Stephanie Anal Fetish Intro", VT_anal_fetish_stephanie_intro_requirement, "VT_anal_fetish_stephanie_intro_label", fetish_type = "anal")
        )
        return True
    # elif person == emily and False:
    #     pass
    # elif person == christina and False:
    #     pass
    # elif person == sarah and False:
    #     pass
    # elif person == salon_manager and False:
    #     pass
    if person == erica:
        if erica_has_given_morning_handjob():
            mc.business.add_mandatory_morning_crisis(
                Fetish_Action("Erica Anal Fetish Intro", VT_anal_fetish_erica_intro_requirement, "VT_anal_fetish_erica_intro_label", fetish_type = "anal")
            )
            return True
        return False
    # if person == candace and False:
    #     pass
    # elif person == ashley and False:
    #     pass
    # elif person == alexia and False:
    #     pass
    # elif person == kaya and False:
    #     pass
    # elif person == ellie and False:
    #     pass
    # elif person == camila and False:
    #     pass
    # elif person == sakari and False:
    #     pass
    # if person == myra:
    #     Fetish_Action("Myra Anal Fetish Intro", anal_fetish_myra_intro_requirement, "anal_fetish_myra_intro_label", fetish_type = "anal")
    if person.is_employee and not person in (erica, lily, mom, stephanie, starbuck):
        mc.business.add_mandatory_crisis(
            Fetish_Action("Employee Anal Fetish Intro", VT_anal_fetish_employee_intro_requirement, "VT_anal_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "anal")
        )
        return True
    if person.is_family and not person in (erica, lily, mom, stephanie, starbuck):
        person.add_unique_on_room_enter_event(
            Fetish_Action("Family Anal Fetish Intro", VT_anal_fetish_family_intro_requirement, "VT_anal_fetish_family_intro_label", fetish_type = "anal", priority = 30)
        )
        return True

    if not person in (erica, lily, mom, stephanie, starbuck):
        person.add_unique_on_talk_event(
            Fetish_Action("Generic Anal Fetish Intro", VT_anal_fetish_generic_intro_requirement, "VT_anal_fetish_generic_intro_label", fetish_type = "anal")
        )
        return True
    return False

##### BREEDING FETISH
def VT_breeding_fetish_employee_intro_requirement():
    if time_of_day == 3 and mc.business.is_open_for_business and mc.is_at_office:
        return True
    return False

def VT_breeding_fetish_generic_intro_requirement(person: Person):
    if person.location != person.home and person.is_available:
        return True
    return False

def VT_breeding_fetish_family_intro_requirement(person: Person):
    if person.home == harem_mansion:
        if person.location == person.home and person.is_available and time_of_day >= 3:
            return True
    else:
        if person.is_home and person.location.person_count == 1 and time_of_day >= 3 and person.is_available: #She is alone in her bedroom
            return True
    return False

def VT_breeding_fetish_mom_intro_requirement(): #TODO this should be a morning mandatory crisis event.
    return True #??? Is this right?

def VT_breeding_fetish_lily_intro_requirement(person: Person):
    return lily.location == lily.home and lily_bedroom.person_count == 1

def VT_breeding_fetish_rebecca_intro_requirement():
    return aunt.location == aunt.home and aunt.is_available

def VT_breeding_fetish_gabrielle_intro_requirement():
    return cousin.location == cousin.home and cousin.is_available

def VT_breeding_fetish_stephanie_intro_requirement():
    if mc.business.is_open_for_business and stephanie.is_at_work and renpy.random.randint(0, 100) < 25:
        return True
    return False

def VT_breeding_fetish_emily_intro_requirement():
    return False

def VT_breeding_fetish_christina_intro_requirement():
    return False

def VT_breeding_fetish_starbuck_intro_requirement():
    return time_of_day == 3 and sex_shop_stage() > 0 and starbuck.is_available

def VT_breeding_fetish_sarah_intro_requirement():
    return day % 7 != 5 and mc.is_in_bed and sarah_threesomes_unlocked() and sarah.is_available

def VT_breeding_fetish_ophelia_intro_requirement():
    return False

def VT_breeding_fetish_erica_intro_requirement():
    return mc.is_in_bed and day % 7 != 6 and erica.is_available

def VT_breeding_fetish_erica_unsuccessful_followup_requirement():
    return True

def VT_breeding_fetish_candace_intro_requirement(person: Person):
    return candace.is_at_work and mc.is_at_office and candace.is_available

def VT_breeding_fetish_ashley_intro_requirement():
    return False

def VT_breeding_fetish_kaya_intro_requirement():
    return False

def VT_breeding_fetish_ellie_intro_requirement():
    return False

def VT_breeding_fetish_camila_intro_requirement():
    return False

def VT_breeding_fetish_sakari_intro_requirement():
    return False

def VT_breeding_fetish_myra_intro_requirement():
    return time_of_day == 4 and mc.energy > 80 and myra.energy > 80 and myra.is_available

def VT_start_breeding_fetish_quest(person: Person):
    #Determine who it is, then add the appropriate quest.
    if (persistent.pregnancy_pref == 0 \
        or person.vaginal_creampie_count < 10
        or person.vaginal_sex_skill < 4 \
        or person.is_willing(missionary) \
        or person.has_taboo("condomless_sex") \
        or person.has_taboo("vaginal_sex") \
        or person.sluttiness < 60 \
        or person.opinion.bareback_sex < 2 \
        or person.opinion.showing_her_ass < 2 \
        or person.opinion.vaginal_sex < 2 \
        or person.opinion.creampies < 2 ) :
        return False
    
    if person.VT_has_started_breeding_fetish:
        return False
        
    # when blocking the fetish gain, prevent repeat triggering for a while
    if day < person.get_event_day("breeding_fetish_locked"):
        return False

    person.set_event_day("breeding_fetish_locked", day + renpy.random.randint(5, 7) + person.opinion.being_submissive - person.opinion.taking_control)

    if person == mom:
        mc.business.add_mandatory_morning_crisis(
            Fetish_Action("Mom breeding fetish intro", VT_breeding_fetish_mom_intro_requirement, "VT_breeding_fetish_mom_intro_label", fetish_type = "breeding")
        )
        return True
    if person == lily:
        lily.add_unique_on_room_enter_event(
            Fetish_Action("Lily breeding fetish intro", VT_breeding_fetish_lily_intro_requirement, "VT_breeding_fetish_lily_intro_label", fetish_type = "breeding", priority = 30)
        )
        return True
    if person == aunt:
        aunt.add_unique_on_room_enter_event(
            Fetish_Action("Rebecca breeding fetish intro", VT_breeding_fetish_rebecca_intro_requirement, "VT_breeding_fetish_rebecca_intro_label", fetish_type = "breeding", priority = 30)
        )
        return True
    if person == cousin:
        cousin.add_unique_on_room_enter_event(
            Fetish_Action("Gabrielle breeding fetish intro", VT_breeding_fetish_gabrielle_intro_requirement, "VT_breeding_fetish_gabrielle_intro_label", fetish_type = "breeding", priority = 30)
        )
        return True
    if person == stephanie:
        mc.business.add_mandatory_morning_crisis(
            Fetish_Action("Stephanie breeding fetish intro", VT_breeding_fetish_stephanie_intro_requirement, "VT_breeding_fetish_stephanie_intro_label", fetish_type = "breeding")
        )
        return True
    # elif person == emily:
    #     Fetish_Action("Emily breeding fetish intro", breeding_fetish_emily_intro_requirement, "breeding_fetish_emily_intro_label", fetish_type = "breeding")
    # elif person == christina:
    #     Fetish_Action("Christina breeding fetish intro", breeding_fetish_christina_intro_requirement, "breeding_fetish_christina_intro_label", fetish_type = "breeding")
    if person == starbuck:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Starbuck breeding fetish intro", VT_breeding_fetish_starbuck_intro_requirement, "VT_breeding_fetish_starbuck_intro_label", fetish_type = "breeding")
        )
        return True
    if person == sarah:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Sarah breeding fetish intro", VT_breeding_fetish_sarah_intro_requirement, "VT_breeding_fetish_sarah_intro_label", fetish_type = "breeding")
        )
        return True
    # elif person is salon_manager and False:
    #     Fetish_Action("Ophelia breeding fetish intro", breeding_fetish_ophelia_intro_requirement, "breeding_fetish_ophelia_intro_label", fetish_type = "breeding")
    if person == erica:
        if erica_get_progress() >= 4:
            mc.business.add_mandatory_crisis(
                Fetish_Action("Erica breeding fetish intro", VT_breeding_fetish_erica_intro_requirement, "VT_breeding_fetish_erica_intro_label", fetish_type = "breeding")
            )
            return True
        return False
    if person == candace:
        candace.add_unique_on_room_enter_event(
            Fetish_Action("Candace breeding fetish intro", VT_breeding_fetish_candace_intro_requirement, "VT_breeding_fetish_candace_intro_label", fetish_type = "breeding", priority = 30)
        )
        return True
    # elif person == ashley:
    #     Fetish_Action("Ashley breeding fetish intro", breeding_fetish_ashley_intro_requirement, "breeding_fetish_ashley_intro_label", fetish_type = "breeding")
    # elif person == alexia:
    #     pass
    # elif person == kaya:
    #     pass
    # elif person == ellie:
    #     pass
    # elif person == camila:
    #     pass
    # elif person == sakari:
    #     pass
    if person == myra:
        if myra_lewd_game_fuck_avail():
            mc.business.add_mandatory_crisis(
                Fetish_Action("Myra Breeding Fetish Intro", VT_breeding_fetish_myra_intro_requirement, "VT_breeding_fetish_myra_intro_label", fetish_type = "breeding")
            )
            return True
        return False
    if person.is_employee and not person in (erica, lily, mom, stephanie, starbuck, sarah, erica, candance, myra):
        mc.business.add_mandatory_crisis(
            Fetish_Action("Employee breeding fetish intro", VT_breeding_fetish_employee_intro_requirement, "VT_breeding_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "breeding")
        )
        return True
    if person.is_family and not person in (erica, lily, mom, stephanie, starbuck, sarah, erica, candance, myra):
        person.add_unique_on_room_enter_event(
            Fetish_Action("Family Member breeding fetish intro", VT_breeding_fetish_family_intro_requirement, "VT_breeding_fetish_family_intro_label", fetish_type = "breeding", priority = 30)
        )
        return True
    if not person in (erica, lily, mom, stephanie, starbuck, sarah, erica, candance, myra):
        person.add_unique_on_talk_event(
            Fetish_Action("Non Employee breeding fetish intro", VT_breeding_fetish_generic_intro_requirement, "VT_breeding_fetish_generic_intro_label", fetish_type = "breeding")
        )
        return True

def VT_cum_fetish_employee_intro_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business and mc.is_at_office

def VT_cum_fetish_family_intro_requirement(person: Person):
    if person.home == harem_mansion:
        return person.location == person.home and person.is_available
    else:
        return person.is_home and person.location.person_count == 1 and person.is_available

def cum_fetish_generic_intro_requirement():
    return mc.is_in_bed and mc.energy > 70

def VT_cum_fetish_mom_intro_requirement():
    return mc.is_in_bed and mc.energy > 70 and mom.is_available

def VT_cum_fetish_lily_intro_requirement():
    return day % 7 != 5 and mc.is_home and lily.is_available

def VT_cum_fetish_rebecca_intro_requirement(person: Person):
    return time_of_day == 3 and mc.energy > 70 and person in aunt_apartment.people

def VT_cum_fetish_gabrielle_intro_requirement():
    return False

def VT_cum_fetish_stephanie_intro_requirement():
    return False

def VT_cum_fetish_alex_intro_requirement():
    return False

def VT_cum_fetish_nora_intro_requirement():
    return False

def VT_cum_fetish_emily_intro_requirement():
    return False

def VT_cum_fetish_christina_intro_requirement():
    return False

def VT_cum_fetish_starbuck_intro_requirement():
    return False

def VT_cum_fetish_sarah_intro_requirement():
    if time_of_day == 2 and day % 7 != 0:
        return mc.is_at_office and mc.business.is_open_for_business and sarah.is_at_work and sarah.is_available
    return False

def VT_cum_fetish_ophelia_intro_requirement():
    return False

def VT_cum_fetish_candace_intro_requirement():
    return False

def VT_cum_fetish_dawn_intro_requirement():
    return False

def VT_cum_fetish_erica_intro_requirement(person: Person):
    return person.location == gym and person.energy >= 80 and mc.energy >= 80 and person.is_available

def VT_cum_fetish_ashley_intro_requirement():
    return False

def VT_cum_fetish_kaya_intro_requirement():
    return False

def VT_cum_fetish_ellie_intro_requirement():
    return False

def VT_cum_fetish_camila_intro_requirement():
    return False

def VT_cum_fetish_sakari_intro_requirement():
    return False

def VT_cum_fetish_myra_intro_requirement(person: Person):
    return False

def VT_start_cum_fetish_quest(person: Person):
    if (not person.has_taboo(["sucking_cock", "condomless_sex"]) \
            or person.cum_exposure_count < 20 \
            or person.oral_sex_skill < 4 \
            or person.sluttiness <  60 \
            or person.opinion.giving_blowjobs < 2 \
            or person.opinion.being_covered_in_cum < 2 \
            or person.opinion.cum_facials < 2 \
            or person.opinion.drinking_cum < 2 \
            or person.opinion.showing_her_tits < 2 \
            or person.opinion.creampies < 2 \
            or person.opinion.anal_creampies < 2 \
            or person.opinion.bareback_sex < 2 \
            or person.opinion.giving_handjobs < 2 ):
        return False
    
    if person.VT_has_started_cum_fetish:
        return False
    # when blocking the fetish gain, prevent repeat triggering for a while
    if day < person.get_event_day("cum_fetish_locked"):
        return False

    person.set_event_day("cum_fetish_locked", day + renpy.random.randint(5, 7) + person.opinion.being_submissive - person.opinion.taking_control)

    if person == lily:
        mc.business.add_mandatory_morning_crisis(
            Fetish_Action("Lily Cum Fetish Intro", VT_cum_fetish_lily_intro_requirement, "VT_cum_fetish_lily_intro_label", fetish_type = "cum")
        )
        return True
    if person == mom:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Jennifer Cum Fetish Intro", VT_cum_fetish_mom_intro_requirement, "VT_cum_fetish_mom_intro_label", fetish_type = "cum")
        )
        return True
    if person == aunt:
        person.add_unique_on_room_enter_event(
            Fetish_Action("Rebecca Cum Fetish Intro", VT_cum_fetish_rebecca_intro_requirement, "VT_cum_fetish_rebecca_intro_label", fetish_type = "cum", priority = 30)
        )
        return True
    # elif person is stephanie and person.has_role(head_researcher) and person.personality != bimbo_personality and False:
    #     pass
    if person == sarah:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Sarah Cum Fetish Intro", VT_cum_fetish_sarah_intro_requirement, "VT_cum_fetish_sarah_intro_label", fetish_type = "cum")
        )
        return True
    if person == erica:
        if erica_get_progress() >= 4:
            erica.add_unique_on_room_enter_event(
                Fetish_Action("Erica Cum Fetish Intro", VT_cum_fetish_erica_intro_requirement, "VT_cum_fetish_erica_intro_label", fetish_type = "cum", priority = 30)
            )
            return True
        return False
    # if person == myra:
    #     myra.add_unique_on_room_enter_event(
    #         cum_fetish_myra_intro = Fetish_Action("Myra Cum Fetish Intro", cum_fetish_myra_intro_requirement, "cum_fetish_myra_intro_label", fetish_type = "cum")
    #     )
    #     return True
    # elif person is kaya and False:
    #     pass
    # elif person is ellie and False:
    #     pass
    # elif person is camila and False:
    #     pass
    # elif person is sakari and False:
    #     pass
    if person.is_employee and not person in (erica, lily, mom, aunt, sarah):
        mc.business.add_mandatory_crisis(
            Fetish_Action("Employee cum fetish intro", VT_cum_fetish_employee_intro_requirement, "VT_cum_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "cum")
        )
        return True
    if person.is_family and not person in (erica, lily, mom, aunt, sarah):
        person.add_unique_on_room_enter_event(
            Fetish_Action("Family Cum Fetish Intro", VT_cum_fetish_family_intro_requirement, "VT_cum_fetish_family_intro_label", fetish_type = "cum", priority = 30)
        )
        return True
    
    if not person in (erica, lily, mom, aunt, sarah):
        mc.business.add_mandatory_crisis(
            Fetish_Action("Someone needs cum", VT_cum_fetish_generic_intro_requirement, "VT_cum_fetish_generic_intro_label", args = person, priority = 10, fetish_type = "cum")
        )
        return True

def VT_exhibition_fetish_employee_intro_requirement():
    return time_of_day == 2 and mc.business.is_open_for_business and mc.is_at_office

def VT_exhibition_fetish_family_intro_requirement(person: Person):
    if person.home == harem_mansion:
        return time_of_day == 3 and person.location == person.home and person.is_available
    else:
        return time_of_day == 3 and person.location == person.home and person.location.person_count == 1 #She is alone in her bedroom

def VT_exhibition_fetish_generic_intro_requirement(person: Person):
    return person.location == mall and mc.is_at_office and time_of_day == 3

def VT_exhibition_fetish_mom_intro_requirement():
    return False

def VT_exhibition_fetish_lily_intro_requirement():
    return False

def VT_exhibition_fetish_rebecca_intro_requirement():
    return False

def VT_exhibition_fetish_gabrielle_intro_requirement():
    return False

def VT_exhibition_fetish_stephanie_intro_requirement():
    return False

def VT_exhibition_fetish_alex_intro_requirement():
    return False

def VT_exhibition_fetish_nora_intro_requirement():
    return False

def VT_exhibition_fetish_emily_intro_requirement():
    return False

def VT_exhibition_fetish_christina_intro_requirement():
    return False

def VT_exhibition_fetish_starbuck_intro_requirement():
    return False

def VT_exhibition_fetish_sarah_intro_requirement():
    return False

def VT_exhibition_fetish_ophelia_intro_requirement():
    return False

def VT_exhibition_fetish_candace_intro_requirement():
    return False

def VT_exhibition_fetish_dawn_intro_requirement():
    return False

def VT_exhibition_fetish_erica_intro_requirement():
    return False

def VT_exhibition_fetish_ashley_intro_requirement():
    return False

def VT_exhibition_fetish_myra_intro_requirement():
    return False


def VT_start_exhibition_fetish_quest(person: Person):
    if (not person.has_taboo(["sucking_cock", "vaginal_sex", "anal_sex", "bare_tits", "bare_pussy"])
            or person.sex_record.get("Public Sex", 0) < 20 \
            or person.oral_sex_skill < 4 \
            or person.vaginal_sex_skill < 4 \
            or person.anal_sex_skill < 4 \
            or person.sluttiness < 60 \
            or person.opinion.public_sex < 2 \
            or person.opinion.not_wearing_anything < 2 \
            or person.opinion.not_wearing_underwear < 2 \
            or person.opinion.showing_her_ass < 2 \
            or person.opinion.showing_her_tits < 2 \
            or person.opinion.skimpy_outfits < 2 \
            or person.opinion.skimpy_uniforms < 2 \
            or person.opinion.masturbating < 2 ):
        return False

    if person.VT_has_started_exhibition_fetish:
        return False

    # when blocking the fetish gain, prevent repeat triggering for a while
    if day < person.get_event_day("exhibition_fetish_locked"):
        return False

    person.set_event_day("exhibition_fetish_locked", day + renpy.random.randint(5, 7) + person.opinion.being_submissive - person.opinion.taking_control)

    # if person == myra:
    #     Fetish_Action("Myra Exhibitionism Fetish Intro", exhibition_fetish_myra_intro_requirement, "exhibition_fetish_myra_intro_label", fetish_type = "exhibition")
    if person.is_employee and not person in (aunt, lily, mom, cousin):
        mc.business.add_mandatory_crisis(
            Fetish_Action("Employee exhibition fetish intro", VT_exhibition_fetish_employee_intro_requirement, "VT_exhibition_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "exhibition")
        )
        return True
    if person.is_family:
        person.add_unique_on_room_enter_event(
            Fetish_Action("Family Member exhibition fetish intro", VT_exhibition_fetish_family_intro_requirement, "VT_exhibition_fetish_family_intro_label", fetish_type = "exhibition", priority = 30)
        )
        return True
    if not person in (lily, mom, cousin, aunt):
        person.add_unique_on_talk_event(
            Fetish_Action("Non Employee exhibition fetish intro", VT_exhibition_fetish_generic_intro_requirement, "VT_exhibition_fetish_generic_intro_label", fetish_type = "exhibition")
        )
        return True
        
    #return False #None of them are written yet

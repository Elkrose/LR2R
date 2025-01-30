from __future__ import annotations
import builtins
from renpy.text.text import Text
from game.major_game_classes.character_related.Person_ren import Person, list_of_people
from game.major_game_classes.game_logic.Room_ren import Room, list_of_places
from game.game_roles._role_definitions_ren import affair_role, girlfriend_role, harem_role
from game.people.Myrabelle.myra_definition_ren import myra
from game.helper_functions.list_functions_ren import known_people_at_location
from game.major_game_classes.game_logic.Action_ren import Limited_Time_Action
from game.major_game_classes.character_related.Progression_Scene_ren import list_of_progression_scenes
from game.map.HomeHub_ren import HomeHub
from game.map.MapHub_ren import MapHub
from VTrandom_lists_ren import VT_Settings

list_of_hubs: list[MapHub] = []
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
from functools import lru_cache

GRID_MAP_POS = [[1, 1], [0, 1], [2, 1], [0, 2], [2, 2], [1, 0], [1, 2]]

def mall_is_open():
    return time_of_day not in (0, 4)

def gym_is_open():
    return time_of_day not in (0, 4)

def sex_shop_is_open():
    return time_of_day in (1, 2, 3) and day % 7 != 6    # closed on sundays

def university_is_open():
    return time_of_day in (1, 2, 3) and day % 7 != 6    # closed on sundays

def coffee_shop_is_open():
    return time_of_day not in (0, 4)

def hair_salon_is_open():
    return time_of_day in (1, 2, 3) and day % 7 != 6    # closed on sundays

def downtown_bar_is_open():
    return time_of_day in (2, 3, 4) and day % 7 != 0    # closed on mondays

def strip_club_is_open():
    return time_of_day > 2

def mom_office_is_open():
    return time_of_day in (1, 2) and day % 7 not in (5, 6)

def gaming_cafe_is_open():
    return (myra.event_triggers_dict.get("gaming_cafe_open", False)
        and ((day % 7 in (2, 3, 4) and time_of_day in (2, 3))
             or (day % 7 in (5, 6) and time_of_day in (1, 2, 3))))

def clear_map_cache():
    calculate_hub_offsets.cache_clear()
    get_location_tooltip.cache_clear()
    get_hub_tile_text.cache_clear()
    get_location_on_enter_events.cache_clear()

def create_tooltip_dictionary(locations: list[Room]) -> dict[str, str]:
    # start_time = time.time()
    # only create this once for each build-up
    active_progression_scene_names = tuple(y.progression_scene_action.name for y in list_of_progression_scenes if y.progression_available)

    result = {place.name: (get_location_tooltip(place), *get_location_on_enter_events(place, active_progression_scene_names)) for place in locations}
    # if debug_log_enabled: # disable log for now
    #    add_to_debug_log("Map build-up time: {total_time:.3f}", start_time)
    return result

@lru_cache(100)
def get_location_tooltip(location: Room) -> str:
    known_people = sorted(known_people_at_location(location), key = lambda x: x.name)
    if builtins.len(known_people) == 0:
        return ""
    tooltip = f"You know {builtins.len(known_people)} {('person' if builtins.len(known_people) == 1 else 'people')} here:\n"
    for person in known_people:
        info = []
        #added girlfriend statuses to beginning
        if person.is_favourite and getattr(persistent, "fullstar")==1:
            info.append("{image=full_star_token_small}")
        else:
            info.append("{image=empty_token_small}")
        if person.type=="story" and getattr(persistent, "labbook")==1:
            info.append("{image=labbook_token_small}")
        else:
            info.append("{image=empty_token_small}")
        info.append(" ")
        info.append(person.name)
        info.append(" ")
        info.append(person.last_name)
        info.append(" ")
        if any(not isinstance(x, Limited_Time_Action) for x in person.on_talk_event_list.enabled_actions(person) if not x.silent):
            info.append("{image=speech_bubble_exclamation_token_small}")
        elif any(x for x in person.on_talk_event_list.enabled_actions(person) if not x.silent):
            info.append("{image=speech_bubble_token_small}")
        #made to sort through girlfriend faster
        if person.has_relation_with_mc:
            if person.is_slave and getattr(persistent, "slave")==1:
                if person.has_role(harem_role) and getattr(persistent, "polyamorous")==1 and getattr(persistent, "polyslave")==1:
                    if person.has_role(affair_role) and getattr(persistent, "parapoly")==1 and getattr(persistent, "parapolyslave")==1:
                        info.append("{image=parapolyslave_small}")
                    else:
                        if person.is_family and getattr(persistent, "familypoly")==1 and getattr(persistent, "familycircle")==1 and getattr(persistent, "polyfamiliaslave")==1:
                            info.append("{image=polyfamiliaslave_small}")
                        else:
                            info.append("{image=polyslave_small}")
                else:
                    if person.has_role(affair_role) and getattr(persistent, "paraslave")==1:
                        info.append("{image=paraslave_small}")
                    else:
                        if person.is_family and getattr(persistent, "familycircle")==1 and getattr(persistent, "gffamiliaslave")==1:
                            info.append("{image=gffamiliaslave_small}")
                        else:
                            if getattr(persistent, "girlfriend")==1 and getattr(persistent, "gfslave")==1:
                                info.append("{image=gfslave_small}")
            else:
                if person.has_role(harem_role) and getattr(persistent, "polyamorous")==1:
                    if person.has_role(affair_role) and getattr(persistent, "parapoly")==1:
                        info.append("{image=parapoly_token_small}")
                    else:
                        if person.is_family and getattr(persistent, "familypoly")==1 and getattr(persistent, "familycircle")==1:
                            info.append("{image=familypoly_small}")
                        else:
                            if getattr(persistent, "polyamorous")==1:
                                info.append("{image=harem_token_small}")
                else:
                    if person.has_role(affair_role) and getattr(persistent, "paramour")==1:
                        info.append("{image=paramour_token_small}")
                    else:
                        if person.is_family and getattr(persistent, "familylove")==1 and getattr(persistent, "familycircle")==1:
                            info.append("{image=familylove_small}")
                        else:
                            if getattr(persistent, "girlfriend")==1:
                                info.append("{image=gf_token_small}")
        else:
            if person.is_family and getattr(persistent, "familycircle")==1:
                if person.is_slave and getattr(persistent, "slave")==1 and getattr(persistent, "familiaslave")==1:
                    info.append("{image=familiaslave_small}")
                else:
                    info.append("{image=familycircle_small}")
            else:
                if person.is_slave and getattr(persistent, "slave")==1:
                    info.append("{image=slave_small}")
        #### AGE ####
        if person.has_cum_fetish and (person.has_breeding_fetish or person.has_anal_fetish) and person.has_exhibition_fetish and person.opinion.polyamory>1:
            if getattr(persistent, "goldlotus")==1:
                info.append("{image=goldlotus_small}")
        else:
            if getattr(persistent, "whitelotus")==1:
                if person.age <= 19:
                    info.append("{image=whitelotus_small}")
            if getattr(persistent, "redlotus")==1:
                if person.age >19 and person.age <=29:
                    info.append("{image=redlotus_small}")
            if getattr(persistent, "pinkllotus")==1:
                if person.age >29 and person.age <31:
                    info.append("{image=pinklotus_small}")
            if getattr(persistent, "bluellotus")==1:
                if person.age >=31:
                    if person.sluttiness>30:
                        info.append("{image=cougar_small}")
                    else:
                        info.append("{image=bluelotus_small}")
 
            if  (getattr(persistent, "virgin_vaginal")==1 and  getattr(persistent, "virgin_anal")==1 and  getattr(persistent, "virgin_oral")==1) and (person.hymen==0 and person.anal_virgin==0 and person.oral_virgin==0) and  perk_system.has_ability_perk("Lip Lock Intuition") and  perk_system.has_ability_perk("Midnight Mirage") and  perk_system.has_ability_perk("Rose Petal Insight"):
               info.append("{image=virgin_token_small}")
            else:
                if getattr(persistent, "virgin_vaginal")==1 and  perk_system.has_ability_perk("Rose Petal Insight"):
                    if person.hymen == 0:
                        info.append("{image=virgin_vaginal_small}")
                if getattr(persistent, "virgin_anal")==1 and  perk_system.has_ability_perk("Midnight Mirage"):
                    if person.anal_virgin == 0:
                        info.append("{image=virgin_anal_small}")
                if getattr(persistent, "virgin_oral")==1 and  perk_system.has_ability_perk("Lip Lock Intuition"):
                    if person.oral_virgin == 0:
                        info.append("{image=virgin_oral_small}")
 
        if getattr(persistent, "dna_sequence")==1:
            if person.is_clone:
                info.append("{image=dna_token_small}")
        if getattr(persistent, "feeding_bottle")==1:
            if person.knows_pregnant and person.is_mc_father:
                info.append("{image=feeding_bottle_token_small}")
        if getattr(persistent, "serum_vial")==1:
            if person.serum_effects:
                if person.active_serum_count > person.serum_tolerance:
                    info.append("{image=vial3_token_small}")
                elif person.active_serum_count == person.serum_tolerance:
                    info.append("{image=vial2_token_small}")
                else:
                    info.append("{image=vial_token_small}")
        if getattr(persistent, "infraction")==1:
            if person.infractions and person.is_at_office:
                info.append("{image=infraction_token_small}")
        if person.trance_training_available:
            if person.has_exact_role(very_heavy_trance_role):
                if getattr(persistent, "ahegaotrance")==1:
                    info.append("{image=ahegaotrance_token_small}")
            else:
                if person.has_exact_role(heavy_trance_role):
                    if getattr(persistent, "heavytrance")==1:
                        info.append("{image=heavytrance_token_small}")
                else:
                    if person.has_exact_role(trance_role):
                        if getattr(persistent, "starttrance")==1:
                            info.append("{image=starttrance_token_small}")
        if getattr(persistent, "arousal")==1:
            if person.arousal_perc >= 60:
                info.append("{image=arousal_token_small}")
        if getattr(persistent, "hadsextoday")==1:
            if person.had_sex_today:
                info.append("{image=hadsex_token_small}")
        if getattr(persistent, "beezee")==1:
            if person.bc_status_known and person.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception"):
                info.append("{image=beezee_token_small}")
        if getattr(persistent, "stripper")==1:
            if person.has_role(stripper_role) and person.is_job_known:
                info.append("{image=stripper_small}")
        if getattr(persistent, "cashpanties")==1:
            if person.has_role(prostitute_role) and person.is_job_known:
                info.append("{image=cashpanties_small}")
        if getattr(persistent, "employee")==1:
            if person.is_employee:
                info.append("{image=employee_small}")
        if getattr(persistent, "intern")==1:
            if person.is_intern:
                info.append("{image=intern_small}")

        info.append("\n")
        tooltip += "".join(info)

    global debug_log_enabled
    if debug_log_enabled:
        room_event_list = [y.name for x in location.people for y in x.on_room_enter_event_list.enabled_actions(x)]
        if room_event_list:
            tooltip += "\nLocation Events:\n"
            for event in room_event_list:
                tooltip += f"  {event}\n"
        person_event_list = [(x.name, y.name) for x in location.people for y in x.on_talk_event_list.enabled_actions(x)]
        if person_event_list:
            tooltip += "\nPerson Events:\n"
            for (person, event) in person_event_list:
                tooltip += f"  {person}: {event}\n"

    return tooltip

@lru_cache(100)
def get_location_on_enter_events(location: Room, scene_names: tuple) -> tuple[bool, bool]:
    room_event_list = [y for x in location.people for y in x.on_room_enter_event_list.enabled_actions(x) if not y.silent]
    on_enter_event = room_event_list or any(x for x in location.on_room_enter_event_list.enabled_actions() if not x.silent)
    progression_event = any(x for x in room_event_list if x.name in scene_names)
    return (on_enter_event, progression_event)

def get_location_tile_text(location: Room, tt_dict: dict[str, str]) -> str:
    #added to show icons in tile text to bring attention that there is something there worth checking out etc
    known_people = known_people_at_location(location)
    return build_tile_information(known_people, location.person_count, location.formal_name, tt_dict[location.name][1], tt_dict[location.name][2])

@lru_cache(100)
def get_hub_tile_text(hub: MapHub) -> str:
    active_progression_scene_names = tuple(y.progression_scene_action.name for y in list_of_progression_scenes if y.progression_available)
    known_people = []
    total_people = 0
    has_event = False
    has_progress = False
    for location in (x for x in hub.visible_locations if x.is_accessible):
        known_people.extend(known_people_at_location(location))
        total_people += location.person_count
        (loc_event, loc_progress) = get_location_on_enter_events(location, active_progression_scene_names)
        if loc_event:
            has_event = True
        if loc_progress:
            has_progress = True

    return build_tile_information(known_people, total_people, hub.formal_name, has_event, has_progress)

def build_tile_information(known_people: list[Person], total_people: int, location_name: str, has_event: bool, has_progress: bool) -> str:
    #setting the catches
    extra_info = []
    if getattr(persistent, "fullstar")==1:
        if any(x for x in known_people if x.is_favourite):
            extra_info.append("{image=full_star_token_small}")
    if getattr(persistent, "labbook")==1:
        if any(x for x in known_people if x.type=="story"):
            extra_info.append("{image=labbook_token_small}")
    #relationships
    #Polycule
    if getattr(persistent, "polyamorous")==1:
        if any(x for x in known_people if x.has_relation_with_mc and not x.is_slave and x.has_exact_role(harem_role) and not x.has_exact_role(affair_role) and not x.is_family):
            extra_info.append("{image=harem_token_small}")
    #Polycule - Paramour
    if getattr(persistent, "parapoly")==1:
        if any(x for x in known_people if x.has_relation_with_mc and not x.is_slave and x.has_exact_role(harem_role) and x.has_exact_role(affair_role) and not x.is_family):
            extra_info.append("{image=parapoly_token_small}")
    #Polycule - Familia
    if getattr(persistent, "familypoly")==1:
        if any(x for x in known_people if x.has_relation_with_mc and not x.is_slave and x.has_exact_role(harem_role) and not x.has_exact_role(affair_role) and x.is_family):
            extra_info.append("{image=familypoly_small}")

    #Girlfriend
    if getattr(persistent, "girlfriend")==1:
        if any(x for x in known_people if x.has_relation_with_mc and not x.is_slave and not x.has_exact_role(harem_role) and not x.has_exact_role(affair_role) and not x.is_family):
            extra_info.append("{image=gf_token_small}")
    #Girlfriend - Paramour
    if getattr(persistent, "paramour")==1:
        if any(x for x in known_people if x.has_relation_with_mc and not x.is_slave and not x.has_exact_role(harem_role) and x.has_exact_role(affair_role) and not x.is_family):
            extra_info.append("{image=paramour_token_small}")
    #Girlfriend - Familia
    if getattr(persistent, "familylove")==1:
        if any(x for x in known_people if x.has_relation_with_mc and not x.is_slave and not x.has_exact_role(harem_role) and not x.has_exact_role(affair_role) and x.is_family):
            extra_info.append("{image=familylove_small}")

    #Familia
    if getattr(persistent, "familycircle")==1:
        if any(x for x in known_people if not x.has_relation_with_mc and not x.is_slave and x.is_family):
            extra_info.append("{image=familycircle_small}")

    #Slave
    if getattr(persistent, "slave")==1:
        if any(x for x in known_people if not x.has_relation_with_mc and x.is_slave and not x.has_exact_role(harem_role) and not x.has_exact_role(affair_role) and not x.is_family):
            extra_info.append("{image=slave_small}")
    #Slave - Polyamorous
    if getattr(persistent, "polyslave")==1:
        if any(x for x in known_people if x.has_relation_with_mc and x.is_slave and x.has_exact_role(harem_role) and x.has_exact_role(affair_role) and not x.is_family):
            extra_info.append("{image=polyslave_small}")
    #Slave - Poly Paramour
    if getattr(persistent, "parapolyslave")==1:
        if any(x for x in known_people if x.has_relation_with_mc and x.is_slave and x.has_exact_role(harem_role) and x.has_exact_role(affair_role)):
            extra_info.append("{image=parapolyslave_small}")
    #Slave - Poly Familia
    if getattr(persistent, "polyfamiliaslave")==1:
        if any(x for x in known_people if x.has_relation_with_mc and x.is_slave and x.has_exact_role(harem_role) and not x.has_exact_role(affair_role) and x.is_family):
            extra_info.append("{image=polyfamiliaslave_small}")
    #Slave - Paramour
    if getattr(persistent, "paraslave")==1:
        if any(x for x in known_people if x.has_relation_with_mc and x.is_slave and not x.has_exact_role(harem_role) and x.has_exact_role(affair_role) and not x.is_family):
            extra_info.append("{image=paraslave_small}")
    #Slave - GF Familia
    if getattr(persistent, "gffamiliaslave")==1:
        if any(x for x in known_people if x.has_relation_with_mc and x.is_slave and not x.has_exact_role(harem_role) and not x.has_exact_role(affair_role) and x.is_family):
            extra_info.append("{image=gffamiliaslave_small}")
    #Slave - Girlfriend
    if getattr(persistent, "gfslave")==1:
        if any(x for x in known_people if x.has_relation_with_mc and x.is_slave and  not x.has_exact_role(harem_role) and not x.has_exact_role(affair_role) and not x.is_family):
            extra_info.append("{image=gfslave_small}")
    #Slave - Familia
    if getattr(persistent, "familiaslave")==1:
        if any(x for x in known_people if not x.has_relation_with_mc and x.is_slave and x.is_family):
            extra_info.append("{image=familiaslave_small}")

    #Lotuses
    if getattr(persistent, "whitelotus")==1:
        if any(x for x in known_people if x.age <=19):
            extra_info.append("{image=whitelotus_small}")
    if getattr(persistent, "redlotus")==1:
        if any(x for x in known_people if x.age >19 and x.age <=29):
            extra_info.append("{image=redlotus_small}")
    if getattr(persistent, "pinkllotus")==1:
        if any(x for x in known_people if x.age >29 and x.age <=31):
            extra_info.append("{image=pinklotus_small}")
    if getattr(persistent, "bluellotus")==1:
        if any(x for x in known_people if x.age >31 and x.sluttiness>=30):
            extra_info.append("{image=cougar_small}")
        if any(x for x in known_people if x.age >31 and x.sluttiness<30):
            extra_info.append("{image=bluelotus_small}")
    if getattr(persistent, "goldlotus")==1:
        if any(x for x in known_people if x.has_cum_fetish and (x.has_breeding_fetish or x.has_anal_fetish) and x.has_exhibition_fetish and x.opinion.polyamory>1):
            extra_info.append("{image=goldlotus_small}")

    #Virginal
    if  (getattr(persistent, "virgin_vaginal")==1 and  getattr(persistent, "virgin_anal")==1 and  getattr(persistent, "virgin_oral")==1) and any(x for x in known_people if x.hymen==0 and x.anal_virgin==0 and x.oral_virgin==0 and  perk_system.has_ability_perk("Lip Lock Intuition") and  perk_system.has_ability_perk("Midnight Mirage") and  perk_system.has_ability_perk("Rose Petal Insight")):
            extra_info.append("{image=virgin_token_small}")
    else:
        if getattr(persistent, "virgin_vaginal")==1 and  perk_system.has_ability_perk("Rose Petal Insight"):
            if any(x for x in known_people if x.hymen == 0):
                extra_info.append("{image=virgin_vaginal_small}")
        if getattr(persistent, "virgin_anal")==1 and  perk_system.has_ability_perk("Midnight Mirage"):
            if any(x for x in known_people if x.anal_virgin == 0):
                extra_info.append("{image=virgin_anal_small}")
        if getattr(persistent, "virgin_oral")==1 and  perk_system.has_ability_perk("Lip Lock Intuition"):
            if any(x for x in known_people if x.oral_virgin == 0):
                extra_info.append("{image=virgin_oral_small}")

    #Pregnant
    if getattr(persistent, "feeding_bottle")==1:
        if any(x for x in known_people if x.knows_pregnant and x.is_mc_father):
            extra_info.append("{image=feeding_bottle_token_small}")

    #Trance - Very Heavy
    if getattr(persistent, "ahegaotrance")==1:
        if any(x for x in known_people if x.has_exact_role(very_heavy_trance_role) and x.trance_training_available):
            extra_info.append("{image=ahegaotrance_token_small}")
    #Trance - Heavy
    if getattr(persistent, "heavytrance")==1:
        if any(x for x in known_people if x.has_exact_role(heavy_trance_role) and x.trance_training_available):
            extra_info.append("{image=heavytrance_token_small}")
    #Trance - Available
    if getattr(persistent, "starttrance")==1:
        if any(x for x in known_people if x.has_exact_role(trance_role) and x.trance_training_available):
            extra_info.append("{image=starttrance_token_small}")

    if any(y for y in known_people if any(not isinstance(x, Limited_Time_Action) for x in y.on_talk_event_list.enabled_actions(y) if not x.silent)):
        extra_info.append("{image=speech_bubble_exclamation_token_small}")
    if any(y for y in known_people if any(x for x in y.on_talk_event_list.enabled_actions(y) if not x.silent)):
        extra_info.append("{image=speech_bubble_token_small}")

    #Arousal
    if getattr(persistent, "arousal")==1:
        if any(x for x in known_people if x.arousal >= 60):
            extra_info.append("{image=arousal_token_small}")

    #Serums
    if getattr(persistent, "serum_vial")==1:
        if any(x for x in known_people if x.serum_effects):
            extra_info.append("{image=vial_token_small}")

    #Infractions
    if getattr(persistent, "infraction")==1:
        if any(x for x in known_people if x.infractions and x.is_at_office):
            extra_info.append("{image=infraction_token_small}")

    #Clone Available
    if getattr(persistent, "dna_sequence")==1:
        if any(x for x in known_people if x.is_clone):
            extra_info.append("{image=dna_token_small}")

    #Fertility Bee
    if getattr(persistent, "beezee")==1:
        if any(x for x in known_people if (x.bc_status_known and x.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception"))):
            extra_info.append("{image=beezee_token_small}")

    #Had Sex Today
    if getattr(persistent, "hadsextoday")==1:
        if any(x for x in known_people if x.had_sex_today):
            extra_info.append("{image=hadsex_token_small}")

    if getattr(persistent, "stripper")==1:
        if any(x for x in known_people if x.has_exact_role(stripper_role) and x.is_job_known):
            extra_info.append("{image=stripper_small}")

    if getattr(persistent, "cashpanties")==1:
        if any(x for x in known_people if x.has_exact_role(prostitute_role) and x.is_job_known):
            extra_info.append("{image=cashpanties_small}")

    if getattr(persistent, "employee")==1:
        if any(x for x in known_people if x.is_employee):
            extra_info.append("{image=employee_small}")
    if getattr(persistent, "intern")==1:
        if any(x for x in known_people if x.is_intern):
            extra_info.append("{image=intern_small}")
    # if len(extra_info) > 6:
        # break_insert = int((len(extra_info) + 1) / 2.0)
        # print("Insert tile break at {break_insert}")
        # extra_info.insert(break_insert, "\n")

    info = []
    if extra_info:
        info.append(f"{''.join(extra_info)}\n")
    info.append(Text(location_name.replace(" ", "\n", 2), substitute = True).get_all_text())
    info.append(f"\n({len(known_people)}/{total_people})")
    if has_event:
        info.append("\n{color=#FFFF00}Event!{/color}")
    if has_progress:
        info.append("\n{image=progress_token_small}")
    return "".join(info)

def change_page(page: int, distance: int, max_page: int) -> int:
    page += distance
    if page > max_page:
        page = 1
    if page < 1:
        page = max_page
    return page

@lru_cache(40)
def calculate_hub_offsets(hub: MapHub, idx: int, location: Room) -> tuple[int, int]:
    hex_offset = (75 if isinstance(hub, HomeHub) and hub.visible_count > 7 and hub.position.Y < 540 else 0)

    if not hub.is_expandable:    # location hub with 1 POI
        offset_x, offset_y = (0, 0)
    elif not isinstance(hub, HomeHub) and hub.visible_count < 8:
        # fully controlled position by location map_pos
        offset_x = 132 * location.map_pos[0]
        offset_y = (150 * location.map_pos[1]) - 75
        if location.map_pos[0] % 2 == 1:
            offset_y += 75
    elif isinstance(hub, HomeHub) and hub.visible_count < 8:
        offset_x = 132 * GRID_MAP_POS[(idx % 7)][0]
        offset_y = (150 * GRID_MAP_POS[(idx % 7)][1]) - 75
        if GRID_MAP_POS[(idx % 7)][0] % 2 == 1:
            offset_y += 75
    elif hub.position.Y < 540:
        row_idx = idx // 3
        offset_x = 132 * GRID_MAP_POS[(idx % 3)][0]
        offset_y = ((150 * GRID_MAP_POS[(idx % 3)][1]) + (row_idx * 150)) - 75
        if GRID_MAP_POS[(idx % 3)][0] % 2 != 1:
            offset_y += 75
    else:
        row_idx = 3 - (idx // 3) # inverted fill
        offset_x = 132 * GRID_MAP_POS[(idx % 3)][0]
        offset_y = ((150 * GRID_MAP_POS[(idx % 3)][1]) + (row_idx * 150)) - 75
        if GRID_MAP_POS[(idx % 3)][0] % 2 == 1:
            offset_y += 75
    return (offset_x, offset_y - hex_offset)

def check_for_any_room_events():
    return (any(y for x in list_of_people for y in x.on_room_enter_event_list.enabled_actions(x) if x.location.visible and x.location.is_accessible and not y.silent)
        or any(y for x in list_of_places for y in x.on_room_enter_event_list.enabled_actions() if x.visible and x.is_accessible and not y.silent))

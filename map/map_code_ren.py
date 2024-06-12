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

    result = {}
    for place in locations:
        result[place.name] = [get_location_tooltip(place)]
        result[place.name].extend(get_location_on_enter_events(place, active_progression_scene_names))

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
        if person.is_favourite:
            info.append("{image=full_star_token_small}")
        else:
            info.append("{image=empty_token_small}")
        if person.type=="story":
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
            if person.has_role(harem_role):
                if person.has_role(affair_role):
                    info.append("{image=parapoly_token_small}")
                else:
                    info.append("{image=harem_token_small}")
            else:
                if person.has_role(affair_role):
                    info.append("{image=paramour_token_small}")
                else:
                    info.append("{image=gf_token_small}")
        if person.age <= 18:
            info.append("{image=matureteen_token_small}")
        if person.is_clone:
            info.append("{image=dna_token_small}")
        if person.knows_pregnant:
            info.append("{image=feeding_bottle_token_small}")
        if person.serum_effects:
            info.append("{image=vial_token_small}")
        if person.infractions and person.is_at_office:
            info.append("{image=infraction_token_small}")
        if person.trance_training_available:
            if person.has_exact_role(very_heavy_trance_role):
                info.append("{image=ahegaotrance_token_small}")
            else:
                if person.has_exact_role(heavy_trance_role):
                    info.append("{image=heavytrance_token_small}")
                else:
                    if person.has_exact_role(trance_role):
                        info.append("{image=starttrance_token_small}")
        if person.arousal_perc >= 60:
            info.append("{image=arousal_token_small}")
        if person.had_sex_today:
            info.append("{image=hadsex_token_small}")
        if person.bc_status_known and person.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception"):
            info.append("{image=beezee_token_small}")
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
    if any(x for x in known_people if x.is_favourite):
        extra_info.append("{image=full_star_token_small}")
    if any(x for x in known_people if x.type=="story"):
        extra_info.append("{image=labbook_token_small}")
    if any(x for x in known_people if x.has_exact_role(harem_role) and x.has_exact_role(affair_role)==False):
        extra_info.append("{image=harem_token_small}")
    if any(x for x in known_people if x.has_exact_role(harem_role) and x.has_exact_role(affair_role)):
        extra_info.append("{image=parapoly_token_small}")
    if any(x for x in known_people if x.has_exact_role(affair_role) and x.has_exact_role(harem_role)==False):
        extra_info.append("{image=paramour_token_small}")
    if any(x for x in known_people if x.has_exact_role(girlfriend_role)):
        extra_info.append("{image=gf_token_small}")
    if any(x for x in known_people if x.age <=18):
        extra_info.append("{image=matureteen_token_small}")
    if any(x for x in known_people if x.knows_pregnant):
        extra_info.append("{image=feeding_bottle_token_small}")
    if any(x for x in known_people if x.has_exact_role(very_heavy_trance_role) and x.trance_training_available):
        extra_info.append("{image=ahegaotrance_token_small}")
    if any(x for x in known_people if x.has_exact_role(heavy_trance_role) and x.trance_training_available):
        extra_info.append("{image=heavytrance_token_small}")
    if any(x for x in known_people if x.has_exact_role(trance_role) and x.trance_training_available):
        extra_info.append("{image=starttrance_token_small}")
    if any(y for y in known_people if any(not isinstance(x, Limited_Time_Action) for x in y.on_talk_event_list.enabled_actions(y) if not x.silent)):
        extra_info.append("{image=speech_bubble_exclamation_token_small}")
    if any(y for y in known_people if any(x for x in y.on_talk_event_list.enabled_actions(y) if not x.silent)):
        extra_info.append("{image=speech_bubble_token_small}")
    if any(x for x in known_people if x.arousal >= 60):
        extra_info.append("{image=arousal_token_small}")
    if any(x for x in known_people if x.serum_effects):
        extra_info.append("{image=vial_token_small}")
    if any(x for x in known_people if x.infractions and x.is_at_office):
        extra_info.append("{image=infraction_token_small}")
    if any(x for x in known_people if x.is_clone):
        extra_info.append("{image=dna_token_small}")
    if any(x for x in known_people if (x.bc_status_known and x.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception"))):
        extra_info.append("{image=beezee_token_small}")
    if any(x for x in known_people if x.had_sex_today):
        extra_info.append("{image=hadsex_token_small}")

    if len(extra_info) > 6:
        break_insert = int((len(extra_info) + 1) / 2.0)
        print("Insert tile break at {break_insert}")
        extra_info.insert(break_insert, "\n")

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

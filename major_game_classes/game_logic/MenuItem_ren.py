from __future__ import annotations
import builtins
import renpy
from renpy import basestring
from renpy.text.text import Text
from game.bugfix_additions.debug_info_ren import validate_texture_memory
from game.helper_functions.convert_to_string_ren import format_titles
from game.helper_functions.heart_formatting_functions_ren import get_heart_image_list
from game.game_roles._role_definitions_ren import employee_freeuse_role
from game.game_roles.relationship_role_definition_ren import girlfriend_role, affair_role, harem_role
from game.main_character.perks.Perks_ren import perk_system
from game.major_game_classes.character_related.Person_ren import Person, scale_person, mc, character_right
from game.major_game_classes.clothing_related.Facial_Accessories_ren import Facial_Accessory
from game.major_game_classes.game_logic.Action_ren import Action, Limited_Time_Action

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""
import re

menu_item_substitution_regex = re.compile(r"\[[^]]*\]")

def build_menu_items(elements_list, draw_hearts_for_people = True, draw_person_previews = True, show_location = False, person_preview_args = None,
        draw_insta = False, draw_onlyfans = False, draw_dikdok = False):
    result = []
    for count, _ in enumerate(elements_list):
        if builtins.len(elements_list[count]) > 1:
            if not isinstance(elements_list[count][1], MenuItem):
                result.append(build_menu_item_list(elements_list[count], draw_person_previews, draw_hearts_for_people, show_location, person_preview_args, draw_insta, draw_onlyfans, draw_dikdok))
            else:
                result.append(elements_list[count])
    return result

def build_menu_item_list(element_list, draw_hearts_for_people = True, draw_person_previews = True, show_location = False, person_preview_args = None,
        draw_insta = False, draw_onlyfans = False, draw_dikdok = False):
    def find_and_replace_tooltip_property(item, extra_args):
        groups = menu_item_substitution_regex.search(item.menu_tooltip)
        if groups and isinstance(extra_args, Person):
            if ".title" in groups.group(0):
                return menu_item_substitution_regex.sub(extra_args.title, item.menu_tooltip)
            if ".name" in groups.group(0):
                return menu_item_substitution_regex.sub(extra_args.name, item.menu_tooltip)
        return item.menu_tooltip

    result = []
    result.append(element_list[0])

    column_elements = element_list[1:]
    for item in column_elements:
        mi = MenuItem()

        if isinstance(item, (list, tuple, set)): #It's a title/return value pair. Show the title, return the value.
            if isinstance(item[0], Action): #It's an action with extra arguments.
                mi.extra_args = item[1]
                item = item[0] #Rename item so that this is caught by the action section below.

            else: #It's (probably) a title/return string pair. Show the title, return the value
                mi.title = item[0]
                mi.return_value = item[1]

        if isinstance(item, Person): #It's a person. Format it for a person list.
            # Pre-load early
            if not (renpy.mobile or renpy.android): # don't load person on mobile
                renpy.exports.invoke_in_thread(mi.preload)

            info = []
            if item.is_favourite:
                info.append("{image=full_star_token_small}")
            if item.type=="story":
                info.append("{image=labbook_token_small}")
            if item.has_relation_with_mc:
                if item.has_role(harem_role):
                    if item.has_role(affair_role):
                        info.append("{image=parapoly_token_small}")
                    else:
                        info.append("{image=harem_token_small}")
                else:
                    if item.has_role(affair_role):
                        info.append("{image=paramour_token_small}")
                    else:
                        info.append("{image=gf_token_small}")
            if item.age <= 18:
                info.append("{image=matureteen_token_small}")
            if any(not isinstance(x, Limited_Time_Action) for x in item.on_talk_event_list.enabled_actions(item) if not x.silent):
                info.append("{image=speech_bubble_exclamation_token_small}")
            elif any(x for x in item.on_talk_event_list.enabled_actions(item) if not x.silent):
                info.append("{image=speech_bubble_token_small}")

            info.append(format_titles(item))

            if any((draw_insta, draw_dikdok, draw_onlyfans)):
                if ((draw_insta and item.has_instapic_post)
                        or (draw_dikdok and item.has_dikdok_post)
                        or (draw_onlyfans and item.has_onlyfan_post)):
                    info.append("{image=phone_token_small}")
            else:
                if item.is_clone:
                    info.append("{image=dna_token_small}")
                if item.knows_pregnant:
                    info.append("{image=feeding_bottle_token_small}")
                if item.is_free_use:
                    if item.has_role(employee_freeuse_role):
                        info.append("{image=doggy_style_token_small}")
                    else:
                        info.append("{image=stocking_token_small}")
                if item.serum_effects:
                    if len(item.serum_effects) > item.serum_tolerance:
                        info.append("{image=vial3_token_small}")
                    elif len(item.serum_effects) > 1:
                        info.append("{image=vial2_token_small}")
                    else:
                        info.append("{image=vial_token_small}")
                if item.infractions and item.is_at_office:    # only when at work
                    info.append("{image=infraction_token_small}")
                if item.trance_training_available:
                    if item.has_exact_role(very_heavy_trance_role):
                        info.append("{image=ahegaotrance_token_small}")
                    else:
                        if item.has_exact_role(heavy_trance_role):
                            info.append("{image=heavytrance_token_small}")
                        else:
                            if item.has_exact_role(trance_role):
                                info.append("{image=starttrance_token_small}")
                if item.arousal_perc >= 60:
                    info.append("{image=arousal_token_small}")
                if item.bc_status_known and item.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception"):
                    info.append("{image=beezee_token_small}")
                if item.had_sex_today:
                    info.append("{image=hadsex_token_small}")
                if show_location:
                    info.append("\n{size=15}<" + Text(item.location.formal_name, substitute = True).get_all_text() + ">{/size}")
                if draw_hearts_for_people:
                    info.append("\n" + get_heart_image_list(item.sluttiness, item.effective_sluttiness()))

            if person_preview_args is None:
                person_preview_args = {}

            mi.title = " ".join(info)
            mi.return_value = item
            mi.person_preview_args = person_preview_args
            mi.display_key = str(item.identifier)
            mi.display_scale = scale_person(item.height)
            if draw_person_previews:
                mi.display_func = item.build_person_displayable

        if isinstance(item, Action):
            mi.title = ""
            mi.return_value = item
            mi.display = False #Default display state for an action is to hide it unless it is enabled or has a disabled slug
            if item.is_action_enabled(mi.extra_args):
                mi.title = item.name
                mi.display = True

            elif item.is_disabled_slug_shown(mi.extra_args):
                mi.title = item.get_disabled_slug_name(mi.extra_args)
                mi.display = True

            if item.menu_tooltip:
                mi.the_tooltip = Text(find_and_replace_tooltip_property(item, mi.extra_args), substitute=True).get_all_text()

        if isinstance(item, basestring): #It's just text. Display the text and return the text.
            mi.title = item
            mi.return_value = item

        if " (tooltip)" in mi.title:
            mi.the_tooltip = mi.title.split(" (tooltip)", 1)[1]
            mi.title = mi.title.replace(" (tooltip)" + mi.the_tooltip, "")

        if " (disabled)" in mi.title:
            mi.title = mi.title.replace(" (disabled)", "")
            parts = mi.title.split("\n")
            if builtins.len(parts) > 1: # color and size disable reason
                parts[-1] = "{color=#ff0000}{size=16}" + parts[-1] + "{/color}{/size}"
                mi.title = "\n".join(parts)
            mi.is_sensitive = False

        if mi.display:
            if isinstance(item, Person) and isinstance(item.title, basestring) and isinstance(mi.the_tooltip, basestring):
                mi.the_tooltip = mi.the_tooltip.replace("[the_person.title]", item.title)
            result.append(mi)
    return result


class MenuItem():
    def __init__(self, title = "", return_value = None, the_tooltip = None, extra_args = None, display = True, is_sensitive = True, display_key = None, display_func = None, person_preview_args = None):
        self.title = title
        self.display_func = display_func
        self.the_tooltip = the_tooltip
        self.extra_args = extra_args
        self.display = display
        self.is_sensitive = is_sensitive
        self.display_key = display_key
        self.display_scale: float | None = None
        self.person_preview_args = person_preview_args
        self.return_value = return_value

    def __hash__(self) -> int:
        return hash((self.title, self.display_key))

    def __eq__(self, other: MenuItem) -> bool:
        if not isinstance(other, MenuItem):
            return NotImplemented
        return self.title == other.title and self.display_key == other.display_key

    def __del__(self):
        try:
            self.return_value = None
            self.display_func = None
        except:
            pass # just ignore error

    def show_person(self):
        if not self.display_func:
            return

        # check if we are not running out of memory
        validate_texture_memory()

        renpy.exports.show(self.display_key, at_list=[character_right, self.display_scale], layer = "extra", what= self.display_func(lighting = mc.location.get_lighting_conditions(), **self.person_preview_args), tag = self.display_key)
        return

    def hide_person(self):
        if self.display_key:
            renpy.exports.hide(self.display_key, layer = "extra")

    def preload(self):
        def load_image(file):
            if file and "empty_holder.png" not in file.filename:
                file.load()

        def actual_body_type(person, cloth):
            if not cloth.body_dependant:
                return "standard_body"
            return person.body_type

        def actual_tit_size(person, cloth):
            if cloth.draws_breasts:
                return person.tits
            return "AA"

        if not self.display_func:
            return

        # pre-load clothing items
        person = self.return_value
        for cloth in person.outfit:
            if isinstance(cloth, Facial_Accessory):
                load_image(cloth.position_sets[person.idle_pose].get_image(person.face_style, person.get_emotion()))
            else:
                load_image(cloth.position_sets[person.idle_pose].get_image(actual_body_type(person, cloth), actual_tit_size(person, cloth)))
        return

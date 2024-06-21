import inspect

import renpy
from renpy.exports import write_log
from game.helper_functions.random_generation_functions_ren import create_random_person, make_person, create_party_schedule, get_premade_character
from game.major_game_classes.game_logic.Room_ren import Room, list_of_places, strip_club, bdsm_room, downtown_bar, downtown_hotel, downtown, hospital
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from helper_functions.vt_helper_functions_ren import _vt_virginity_stats
from renpy import persistent, basestring
from game.major_game_classes.clothing_related.wardrobe_builder_ren import WardrobeBuilder
from typing import Optional, Callable, Iterable

day: int
#last_name: str
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 900 python:
"""

VIRGIN_TRACKER_DEBUG = True
# TO DO: Need to capture pros and adjust sluttiness to appropriate levels
# TO DO: NOT SURE how to hook into the _map_definitions to edit the harem name

def _vt_prefix_person_init(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        # if age (args[3]) <= core game min age (default 18)
        if args[3] <= Person.get_age_floor() and kwargs["type"]=="random":
            # ensure single with no kids
            kwargs["relationship"] = "Single"
            kwargs["kids"] = 0
        return wrapped_func(*args, **kwargs)
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_run_turn(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        # TODO: make mod install compatible with existing savegames (person doesn't have VT attributes)
        # Call core code; has core side effects
        ret_val = wrapped_func(*args, **kwargs)

        self = args[0]
        #VirginTracker cum tracker dealing with cum in orifices
        # NOTE: vaginal_cum has floor 1, other two have floor 0
        if self.oral_cum > 0 and (day -self.sex_record.get("Last Oral Day", -1)) >= 0:
            self.oral_cum -= 1
        if self.anal_cum > 0 and (day -self.sex_record.get("Last Anal Day", -1)) >= 0:
            self.anal_cum -= 1
        if self.vaginal_cum > 1 and (day -self.sex_record.get("Last Vaginal Day", -1)) >= 0:
            self.vaginal_cum -= 1

        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_run_day(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        # TODO: make mod install compatible with existing savegames (person doesn't have VT attributes)
        # Call core code; has core side effects
        ret_val = wrapped_func(*args, **kwargs)

        self = args[0]
        # dealing with virgin hymen healing, 0-seal 1-bleeding/torn 2-normalized
        # only heal hymen at day end if haven't had vaginal sex for at least 3 days
        if self.hymen == 1 and (day - self.sex_record.get("Last Vaginal Day", -1)) >= 3:
            self.hymen = 2
        # dealing with muscles relaxing and stretching back to normal levels
        # virgin is None: #0=virgin, 1=just the tip, 2=full penetration, 3-10 is degree of tightness
        # 3 is the normal tightness of the muscles, higher would be from trauma ie, baby -> 5-7
        # will always return to normal after a few days depending on the trauma
        if self.vaginal_virgin > 3 and (day - self.sex_record.get("Last Vaginal Day", -1)) >= 3:
            self.vaginal_virgin -= 1
        if self.oral_virgin > 3 and (day - self.sex_record.get("Last Oral Day", -1)) >= 3:
            self.oral_virgin -= 1
        if self.anal_virgin > 3 and (day - self.sex_record.get("Last Anal Day", -1)) >= 3:
            self.anal_virgin -= 1
        # remove up to one level vaginal cum (only way to remove last level)
        if self.vaginal_cum > 0 and (day - self.sex_record.get("Last Vaginal Day", -1)) >= 4:
            self.vaginal_cum -= 1

        # auto-develop fetishes without serum
        #if (not self.has_anal_fetish and self.anal_sex_skill >= 5
        #        and self.opinion.anal_sex >= 2 and self.opinion.anal_creampies >= 2
        #        and (self.anal_sex_count > 19 or self.anal_creampie_count > 19)):
            #if VT_start_anal_fetish_quest(self):
                #self.event_triggers_dict["VT_anal_fetish_start"] = True

        #if (not self.has_cum_fetish and self.oral_sex_skill >= 5
        #        and self.opinion.giving_blowjobs >= 2 and (self.opinion.drinking_cum >= 2 or self.opinion.cum_facials >= 2)
        #        and self.cum_exposure_count > 19):
            #if VT_start_cum_fetish_quest(self):
                #self.event_triggers_dict["VT_cum_fetish_start"] = True

       # if (not self.has_breeding_fetish and self.vaginal_sex_skill >= 5
                #and self.opinion.vaginal_sex >= 2 and self.opinion.creampies >= 2
                #and self.vaginal_creampie_count > 19):
           # if VT_start_breeding_fetish_quest(self):
                #self.event_triggers_dict["VT_breeding_fetish_start"] = True

        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_cum_in_mouth(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        # TODO: make mod install compatible with existing savegames (person doesn't have VT attribute oral_cum)
        ret_val = wrapped_func(*args, **kwargs)

        self = args[0]
        self.oral_cum += 1

        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_cum_in_vagina(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        # TODO: make mod install compatible with existing savegames (person doesn't have VT attribute vaginal_cum)
        ret_val = wrapped_func(*args, **kwargs)

        self = args[0]
        self.vaginal_cum += 1

        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_cum_in_ass(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        # TODO: make mod install compatible with existing savegames (person doesn't have VT attribute anal_cum)
        ret_val = wrapped_func(*args, **kwargs)

        self = args[0]
        self.anal_cum += 1

        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_update_sex_record(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        # TODO: make mod install compatible with existing savegames (person doesn't have VT attributes)
        ret_val = wrapped_func(*args, **kwargs)

        self, report_log = args
        types_seen = set(position_type.record_class for position_type in report_log.get("positions_used", []))

        # .get(, default=Foreplay) is necessary because standing_grope and drysex_cowgirl do not have record_class
        sex_classes = set(Person._record_skill_map.get(sex_type, "Foreplay") for sex_type in types_seen)
        sex_classes.discard("Foreplay")

        # at this point, sex_classes is guaranteed to be some subset of
        # {"Oral", "Vaginal", "Anal"}
        for sex_class in sex_classes:
            # make the appropriate strings, e.g. "oral_virgin" and "oral_first"
            # using these strings with setattr/getattr allows same code in loop
            _sex_type_first = sex_class.lower() + "_first"
            _sex_type_virgin = sex_class.lower() + "_virgin"

            # set last day had this kind of sex
            self.sex_record["Last " + sex_class + " Day"] = day

            # if _virgin is 0
            if getattr(self, _sex_type_virgin, 3) == 0:
                # set _first name
                setattr(self, _sex_type_first, mc.name)
                # and if vaginal
                if sex_class == "Vaginal":
                    # tear hymen
                    self.hymen = 1

            # if _virgin <= 9 (NOTE: this condition is always evaluated,
            # whether or not the previous `if _virgin == 0`` was True)
            if getattr(self, _sex_type_virgin) <= 9:
                # increase it by one
                setattr(self, _sex_type_virgin, getattr(self, _sex_type_virgin, 3) + 1)

        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

Person.__init__         = _vt_prefix_person_init(Person.__init__)
Person.run_turn         = _vt_postfix_person_run_turn(Person.run_turn)
Person.run_day          = _vt_postfix_person_run_day(Person.run_day)
Person.cum_in_mouth     = _vt_postfix_person_cum_in_mouth(Person.cum_in_mouth)
Person.cum_in_vagina    = _vt_postfix_person_cum_in_vagina(Person.cum_in_vagina)
Person.cum_in_ass       = _vt_postfix_person_cum_in_ass(Person.cum_in_ass)
Person.update_person_sex_record = _vt_postfix_person_update_sex_record(Person.update_person_sex_record)

def _vt_create_random_person_override(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs) -> Person:
        virgin_tracker_args: tuple[str] = (
            "oral_virgin",
            "oral_first",
            "oral_cum",
            "hymen",
            "vaginal_virgin",
            "vaginal_first",
            "vaginal_cum",
            "anal_virgin",
            "anal_first",
            "anal_cum",
        )

        # use sex_cap arg if passed, else get_sex_skill_ceiling to keep core balance
        sex_cap = kwargs.get("sex_cap", Person.get_sex_skill_ceiling())
        kwargs.pop("sex_cap", None)

        # grab any provided VirginTracker keyword args
        # remove them from the kwargs dict
        given_vt_kwargs: dict[str, int | None] = {}
        for arg_name in virgin_tracker_args:
            if arg_name in kwargs:
                given_vt_kwargs[arg_name] = kwargs[arg_name]
                kwargs.pop(arg_name, None)

        # force kids=0 if hymen is sealed or recently torn
        if given_vt_kwargs.get("hymen", None) in (0, 1):
            kwargs["kids"] = 0

        ######################
        #### Call to core code
        ######################
        person = wrapped_func(*args, **kwargs)

        #TO DO write appropriate code to catch and set Clone virginities in create_random_person
        if VIRGIN_TRACKER_DEBUG:
            write_log("Overriding create_random_person; adding attributes")

        # NOTE: first assign any parameters passed by the calling location
        # this may set any combination of VT parameters
        for key, value in given_vt_kwargs.items():
            # set the values directly
            setattr(person, key, value)

        # NOTE: then fill in the remaining stats
        virginity_types = ["Oral", "Vaginal", "Anal"]
        for sex_type in virginity_types:
            # compute the values
            stats = _vt_virginity_stats(person, sex_type, sex_cap)
            # and apply them
            for key, value in stats.items():
                setattr(person, key, value)

        return person

    # don't override the signature, because modded code might provide VT kwargs
    #wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

create_random_person = _vt_create_random_person_override(create_random_person)

def _vt_optional_get_premade(**kwargs) -> Optional[Person]:
    if kwargs.get("type")=="random" and kwargs.get("allow_premade") and renpy.random.randint(1,100) < 20:
        return get_premade_character(kwargs.get("age_range"),
                                     kwargs.get("tits_range"),
                                     kwargs.get("height_range"),
                                     kwargs.get("kids_range"),
                                     kwargs.get("relationship_list"),
        )
    return None

def _vt_apply_opinions_makeup_and_schedule(person: Person, forced_opinions: Optional[list | tuple | set], forced_sexy_opinions: Optional[list | tuple | set]) -> Person:
    # apply forced opinions after we 'update opinions', so we don't override them there
    if forced_opinions and isinstance(forced_opinions, (list, tuple, set)):
        for opinion in forced_opinions:
            person.opinions[opinion[0]] = [opinion[1], opinion[2]]

    if forced_sexy_opinions and isinstance(forced_sexy_opinions, (list, tuple, set)):
        for opinion in forced_sexy_opinions:
            person.sexy_opinions[opinion[0]] = [opinion[1], opinion[2]]

    if config.version not in ("2024.05B"):
        if person.base_outfit and len(person.base_outfit.accessories) == 0 and person.opinion.makeup > 0:
            WardrobeBuilder.add_make_up_to_outfit(person, person.base_outfit)

    if person.type == 'random':
        create_party_schedule(person)

    # not strictly necessary to return the person object
    # because all the above modified the provided object directly
    # but still, good practice
    return person

def _vt_make_person_override(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args,
                      ## DO NOT PASS THESE THRU TO CREATE_RANDOM_PERSON
                      forced_opinions=None,
                      forced_sexy_opinions=None,
                      allow_premade=False,
                      ## MUST PASS THESE THRU TO CREATE_RANDOM_PERSON
                      type="random",
                      age_range=None,
                      tits_range=None,
                      height_range=None,
                      kids_range=None,
                      relationship_list=None,
                      **kwargs) -> Person:

        return_character = _vt_optional_get_premade(type=type, allow_premade=allow_premade,
            age_range=age_range, tits_range=tits_range,
            height_range=height_range, kids_range=kids_range,
            relationship_list=relationship_list,
        )

        if not return_character:
            return_character = create_random_person(*args,
                                                    type=type,
                                                    age_range=age_range,
                                                    tits_range=tits_range,
                                                    height_range=height_range,
                                                    kids_range=kids_range,
                                                    relationship_list=relationship_list,
                                                    **kwargs)

        return_character = _vt_apply_opinions_makeup_and_schedule(return_character, forced_opinions, forced_sexy_opinions)

        return return_character
    #wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

make_person = _vt_make_person_override(make_person)

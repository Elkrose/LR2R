import inspect

import renpy
from renpy.exports import write_log
from game.helper_functions.random_generation_functions_ren import create_random_person
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.character_related.Person_ren import Person
from vt_helper_functions_ren import _vt_virginal_stats
day: int

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 900 python:
"""
VIRGIN_TRACKER_DEBUG = True

def _vt_prefix_person_init(wrapped_func):
    def wrapping_func(*args, **kwargs):
        # hack
        # if age (args[3]) <= core game min age (default 18)
        if args[3] <= Person.get_age_floor() and kwargs["type"] not in ("story", "unique"):
            # ensure single with no kids
            kwargs["relationship"] = "Single"
            kwargs["kids"] = 0
        return wrapped_func(*args, **kwargs)
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_run_turn(wrapped_func):
    def wrapping_func(*args, **kwargs):
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

def _vt_postfix_person_run_day(wrapped_func):
    def wrapping_func(*args, **kwargs):
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

        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_cum_in_mouth(wrapped_func):
    def wrapping_func(*args, **kwargs):
        ret_val = wrapped_func(*args, **kwargs)

        self = args[0]
        self.oral_cum += 1

        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_cum_in_vagina(wrapped_func):
    def wrapping_func(*args, **kwargs):
        ret_val = wrapped_func(*args, **kwargs)

        self = args[0]
        self.vaginal_cum += 1

        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_cum_in_ass(wrapped_func):
    def wrapping_func(*args, **kwargs):
        ret_val = wrapped_func(*args, **kwargs)

        self = args[0]
        self.anal_cum += 1

        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_person_update_sex_record(wrapped_func):
    def wrapping_func(*args, **kwargs):
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

def _vt_create_random_person_override(wrapped_func):
    def wrapping_func(*args, **kwargs):
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

        # use this line to keep core game balance
        sex_cap = Person.get_skill_ceiling()

        # else uncomment this line for uniform distribution from 2-8
        #sex_cap = 8

        # override above sex_cap if passed as keyword arg
        if "sex_cap" in kwargs:
            sex_cap = kwargs["sex_cap"]
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

        if VIRGIN_TRACKER_DEBUG:
            write_log("Overriding create_random_person; adding attributes")

        # NOTE: this is all-or-nothing; if some but not all of the VT kwargs are provided
        # the provided values will be ignored, and instead all values estimated based on sex skills
        # if create_random_person was called with all the VirginTracker keyword args
        if set(virgin_tracker_args) == set(given_vt_kwargs.keys()):
            for key, value in given_vt_kwargs.items():
                # set the values directly
                setattr(person, key, value)
        else:
            virginity_types = ["Oral", "Vaginal", "Anal"]
            for sex_type in virginity_types:
                # compute the values
                stats = _vt_virginal_stats(person, sex_type, sex_cap)
                # and apply them
                for key, value in stats.items():
                    setattr(person, key, value)

        return person

    # don't override the signature, because modded code might provide VT kwargs
    #wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

create_random_person = _vt_create_random_person_override(create_random_person)
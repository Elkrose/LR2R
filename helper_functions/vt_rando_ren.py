import builtins
import copy
import renpy
from math import floor
from renpy import persistent, basestring
from renpy.exports import write_log
from game.helper_functions.random_generation_functions_ren import make_person, create_hooker, create_old_hooker_with_daughter, create_stripper
from game.major_game_classes.character_related.Person_ren import Person, generate_daughter, generate_home, home
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition, prostitute_job, stripper_job

day: int
#last_name: str
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 900 python:
"""
VIRGIN_TRACKER_DEBUG = True

# TO DO: NOT SURE how to hook into the _map_definitions to edit the harem name
# mansion_name = last_name +" Mansion"
# harem_mansion = Room("harem_mansion", str(mansion_name), harem_mansion_background, harem_objects,
# map_pos =[1, 1], visible = False, lighting_conditions = standard_indoor_lighting)
# harem_hub = MapHub("mansion", str(mansion_name), icon = "POI_Brothel", position = Point(120, 660), locations = [harem_mansion])

def _vt_create_hooker_override(wrapped_func):
    def wrapping_func(*args, **kwargs):
        hooker = make_person( sluttiness = renpy.random.randint(80, 100),
            sex_skill_array = [renpy.random.randint(4,8),renpy.random.randint(3,8),renpy.random.randint(2,8),renpy.random.randint(2,8)],
            job = prostitute_job,
            type="unique",
            forced_opinions = [
                ["flirting", 2, False],
                ["high heels", 2, False],
                ["makeup", 1, False],
                ["pants", -2, False],
                ["skirts", 2, False],
            ],
            forced_sexy_opinions = [
                ["bareback sex", -2, False],
                ["being submissive", 1, False],
                ["giving blowjobs", 2, False],
                ["public sex", 2, False],
                ["showing her tits", 1, False],
                ["skimpy outfits", 2, False],
                ["vaginal sex", 2, False],
            ])
        hooker.set_mc_title("Honey")
        if (len(args) > 0 and args[0]) or kwargs.get("add_to_game"):
            hooker.generate_home()
            hooker.home.add_person(hooker)
        return hooker
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_create_stripper_override(wrapped_func):
    def wrapping_func(*args, **kwargs):
        # change sluttiness range, type="unique", sex_skill_array ranges
        stripper = make_person(sluttiness = renpy.random.randint(25, 55),
            sex_skill_array = [renpy.random.randint(4,8),renpy.random.randint(3,8),renpy.random.randint(2,8),renpy.random.randint(2,8)],
            job = stripper_job,
            type="unique",
            forced_opinions = [
                ["small talk", 1, False],
                ["conservative outfits", -2, False],
                ["flirting", 2, False],
                ["high heels", 2, False],
                ["work uniforms", 1, False],
            ], forced_sexy_opinions = [
                ["showing her tits", 2, False],
                ["showing her ass", 2, False],
                ["skimpy outfits", 2, False],
                ["taking control", 2, False],
            ])
        stripper.set_mc_title("Honey")
        stripper.generate_home()
        stripper.home.add_person(stripper)
        return stripper
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_create_old_hooker_with_daughter_override(wrapped_func):
    def wrapping_func(*args, **kwargs):
        person = create_hooker()
        person.age = renpy.random.randint(40, 49)
        daughter = person.generate_daughter(job = prostitute_job)
        daughter.set_mc_title("Daddy")
        daughter._sluttiness = renpy.random.randint(40, 60)
        return daughter
    # don't override the signature, because modded code might provide VT kwargs
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

create_hooker = _vt_create_hooker_override(create_hooker)
create_stripper = _vt_create_stripper_override(create_stripper)
create_old_hooker_with_daughter = _vt_create_old_hooker_with_daughter_override(create_old_hooker_with_daughter)

import inspect
import renpy
import renpy.store
from renpy import persistent, basestring
from renpy.exports import write_log
from game.helper_functions.random_generation_functions_ren import create_random_person, make_person, create_party_schedule, get_premade_character, update_person_opinions, ensure_opinion_on_subject,fix_opinion_contradiction,set_work_opinion
from game.major_game_classes.game_logic.Room_ren import Room, list_of_places, strip_club, bdsm_room, downtown_bar, downtown_hotel, downtown, hospital
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.character_related.Person_ren import mc
from game.major_game_classes.character_related.StatTracker_ren import StatTracker
from game.major_game_classes.game_logic.Person_ren import Person, list_of_people, mom, lily, aunt, cousin
from helper_functions.vt_helper_functions_ren import _vt_virginity_stats, _vt_get_person_age_tag
from game.major_game_classes.clothing_related.wardrobe_builder_ren import WardrobeBuilder
from typing import Optional, Callable, Iterable
from VTrandom_lists_ren import VT_AGE_RANGES, VT_Settings, _vt_build_weighted_list
from game.random_lists_ren import get_random_from_weighted_list
from game.major_game_classes.character_related.Person_ren import Person, list_of_patreon_characters, tan_images_dict
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition, university_professor_job, student_job, doctor_job, waitress_job, unemployed_job, stripper_job, stripclub_stripper_job, stripclub_bdsm_performer_job, stripclub_mistress_job, stripclub_waitress_job, stripclub_manager_job, prostitute_job, secretary_job, office_worker_job, lawyer_job, architect_job, interior_decorator_job, fashion_designer_job
from game.main_character.perks.Perks_ren import Ability_Perk, perk_system
from game.major_game_classes.character_related.configuration.opinion_lists_ren import init_list_of_opinions, init_list_of_sexy_opinions
from game.major_game_classes.character_related.Opinion_ren import Opinion

day: int
#last_name: str
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 900 python:
"""
# TODO: on release, set False?
VIRGIN_TRACKER_DEBUG = True

def vt_init_list_of_sexy_opinions() -> list[str]:
    return [
        "anal creampies",  # Has gameplay effect
        "anal sex",  # Has gameplay effect
        "bareback sex",  # Has gameplay effect.
        "being covered in cum",  # Has gameplay effect
        "being fingered",  # Has gameplay effect
        "being submissive",  # Has gameplay effect
        "big dicks",
        "cheating on men",  # Has gameplay effect
        "creampies",  # Has gameplay effect
        "cum facials",  # Has gameplay effect
        "doggy style sex",  # Has gameplay effect
        "drinking cum",  # Has gameplay effect
        "flashing",  # Has gameplay effect
        "getting head",  # Has gameplay effect
        "giving blowjobs",  # Has gameplay effect
        "giving handjobs",  # Has gameplay effect
        "giving tit fucks",  # Has gameplay effect
        "incest",  # Has gameplay effect
        "kissing",  # Has gameplay effect
        "likes men", # Has gameplay effect
        "likes women",  # Has gameplay effect
        "lingerie",  # Has gameplay effect
        "masturbating",  # Has gameplay effect
        "missionary style sex",  # Has gameplay effect
        "not wearing anything",  # Has gameplay effect
        "not wearing underwear",  # Has gameplay effect
        "open relationships",  # Has gameplay effect
        "peeping",  # Has gameplay effect
        "polyamory", # Has gameplay effect
        "public sex",  # Has gameplay effect
        "sex standing up",  # Has gameplay effect
        "showing her ass",  # Has gameplay effect
        "showing her tits",  # Has gameplay effect
        "skimpy outfits",  # Has gameplay effect
        "skimpy uniforms",  # Has gameplay effect
        "taking control",  # Has gameplay effect
        "threesomes",
        "vaginal sex",  # Has gameplay effect
    ]

class VTPerson(Person):

    _initial_age_floor = 18
    _initial_age_ceiling = 50
    _final_age_floor = 18
    _final_age_ceiling = 70
    _teen_age_ceiling = 19
    _old_age_floor = 70

    _sexy_opinions_list = vt_init_list_of_sexy_opinions()

    _record_opinion_map = {
        "Handjobs": ["giving handjobs", "sex standing up", "flashing", "likes men"],
        "Kissing": ["kissing"],
        "Fingered": ["masturbating", "being fingered", "sex standing up", "flashing", "peeping"],
        "Tit Fucks": ["giving tit fucks", "showing her tits"],
        "Blowjobs": ["giving blowjobs", "likes men"],
        "Cunnilingus": ["getting head", "likes women"],
        "Vaginal Sex": ["vaginal sex", "missionary style sex", "lingerie", "likes men"],
        "Anal Sex": ["anal sex", "doggy style sex", "bareback sex", "likes men", "flashing"],
        "Cum Facials": ["cum facials", "flashing", "likes men"],
        "Cum in Mouth": ["drinking cum", "flashing", "likes men"],
        "Cum Covered": ["being covered in cum", "flashing", "likes men"],
        "Vaginal Creampies": ["creampies", "likes men"],
        "Anal Creampies": ["anal creampies", "likes men"],
        "Threesomes": ["not wearing anything", "skimpy outfits", "skimpy uniforms", "flashing", "peeping"],
        "Spankings": ["not wearing underwear", "showing her ass", "flashing", "peeping"],
        "Insertions": ["big dicks", "public sex", "sex standing up", "flashing"],
        "Public Sex": ["flashing", "peeping", "public sex", "sex standing up", "skimpy outfits", "skimpy uniforms"]
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def weight(self) -> float:
        if not hasattr(self, "_weight"):
            check_type = self.event_triggers_dict.get("pre_preg_body", self.body_type)
            if check_type == "thin_body":
                self._weight = 51 * self.height
            elif check_type == "standard_body":
                self._weight = 58 * self.height
            else:
                self._weight = 67 * self.height
        #old values 60, 75, 90
        extra_modifier = 0
        if self.is_pregnant:
            extra_modifier = max(self.days_since_event("preg_start_date") - 25, 0) * .17
        return self._weight + extra_modifier    

    @weight.setter
    def weight(self, value: float):
        self._weight = value

    def change_weight(self, amount: float, chance: int = 100) -> bool:
        if amount == 0:
            return False

        if renpy.random.randint(0, 100) <= chance:
            self._weight += amount

        # maximum and minimum weight are dependent on height
        max_weight = (self.height) * 100
        min_weight = (self.height) * 50
        switch_point_low = (self.height) * 68 #68
        switch_point_high = (self.height) * 83

        if amount > 0:
            if self.weight > switch_point_low + 3 and self.body_type == "thin_body":
                self.body_type = "standard_body"
                return True
            if self.weight > switch_point_high + 3 and self.body_type == "standard_body":
                self.body_type = "curvy_body"
                return True
            if self.weight > max_weight: #Maximum weight
                self._weight = max_weight
            return False

        if amount < 0:
            if self.weight < min_weight:  #Minimum weight
                self._weight = min_weight
                return False
            if self.weight < switch_point_low - 3 and self.body_type == "standard_body":
                self.body_type = "thin_body"
                return True
            if self.weight < switch_point_high - 3 and self.body_type == "curvy_body":
                self.body_type = "standard_body"
                return True
            return False

    @property
    def fetish_count(self) -> int:
        return builtins.len([x for x in self.special_role if x in (anal_fetish_role, cum_fetish_role, breeding_fetish_role, exhibition_fetish_role, vaginal_fetish_role)])

    @property
    def has_vaginal_fetish(self) -> bool:
        return self.has_role(vaginal_fetish_role)

    @property
    def VT_has_started_cum_fetish(self) -> bool:
        return self.event_triggers_dict.get("VT_cum_fetish_start", False)

    @property
    def VT_has_started_vaginal_fetish(self) -> bool:
        return self.event_triggers_dict.get("VT_vaginal_fetish_start", False)

    @property
    def VT_has_started_anal_fetish(self) -> bool:
        return self.event_triggers_dict.get("VT_anal_fetish_start", False)

    @property
    def VT_has_started_breeding_fetish(self) -> bool:
        return self.event_triggers_dict.get("VT_breeding_fetish_start", False)

    @property
    def VT_has_started_exhibition_fetish(self) -> bool:
        return self.event_triggers_dict.get("VT_exhibition_fetish_start", False)

    @property
    def is_family(self) -> bool:
        return self in (mom, lily, aunt, cousin) or hasattr(self, 'is_daughter_of_mc') or self.has_role(clone_role)

    @property
    def relation_possessive_title(self) -> str:
        '''
        Returns the possessive title always as family relationship if person is family.
        When person is not family will return appropriate relationship reference.
        Usage: for dialogues where you specifically want to refer to your family relationship
        '''
        if not self.is_family:
            if self.is_girlfriend:
                if self.has_role(harem_role):
                    return "your polygirl"
                return "your girlfriend"
            if self.is_affair:
                if self.has_role(harem_role):
                    return "your polyamour"
                return "your mistress"
            if self.vaginal_sex_count > 9:
                if self.has_role(harem_role):
                    return "your polypussy"
                return "your booty call"
            return "your friend"
        if self == mom:
            return "your mother"
        if self == lily:
            return "your sister"
        if self == aunt:
            return "your aunt"
        if self == cousin:
            return "your cousin"
        if hasattr(self, 'is_daughter_of_mc'):
            return "your daughter"
        if self.has_role(clone_role):
            return "your cloned daughter"
        return "your family"

    # @property
    # def on_birth_control(self) -> bool:
        # return self.is_infertile or self._birth_control

Person         = VTPerson

def init_vt_generic_roles():
    global vaginal_fetish_role
    vaginal_fetish_role = Role(role_name ="Vaginal Fetish", actions = get_vaginal_fetish_role_actions())
    return
init_vt_generic_roles()

#to add property for likes women/men and flashing/peeping as well as open relationships
class VTOpinion(Opinion):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def likes_women(self) -> int:
        return self.get_func("likes women") #Has gameplay effect

    @property
    def likes_men(self) -> int:
        return self.get_func("likes men") #Has gameplay effect

    @property
    def flashing(self) -> int:
        return self.get_func("flashing") #Has gameplay effect

    @property
    def peeping(self) -> int:
        return self.get_func("peeping") #Has gameplay effect

Opinion     = VTOpinion

#keep an eye on the vanilla stats, likes to change them alot, so might need to bring them here to keep stability
class VTStatTracker(StatTracker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    #### total Polycules
    @property
    def polycules(self) -> int:
        return sum(1 for x in list_of_people if x.has_role(harem_role))
    ##### Seperate the harem girlfriends from girlfriends
    @property
    def polycule_girlfriends(self) -> int:
        return sum(1 for x in list_of_people if x.is_girlfriend and x.has_role(harem_role) and not x.is_family and not x.is_affair)
    ##### Seperate the harem paramour from paramours
    @property
    def polycule_paramours(self) -> int:
        return sum(1 for x in list_of_people if x.is_affair and x.has_role(harem_role))
    #### Poly Familia
    @property
    def polycule_familia(self) -> int:
        return sum(1 for x in list_of_people if x.is_girlfriend and x.has_role(harem_role) and x.is_family)

    #### total girlfriends not in polycule
    @property
    def girlfriends(self) -> int:
        return sum(1 for x in list_of_people if (x.is_girlfriend or x.is_affair) and not x.has_role(harem_role))
    #### total girlfriends sans familia not in polycule and not affair
    @property
    def girlfriends_sansfamilia(self) -> int:
        return sum(1 for x in list_of_people if x.is_girlfriend and not x.has_role(harem_role) and not x.is_family and not x.is_affair)
    #### total familia not in polycule
    @property
    def familia(self) -> int:
        return sum(1 for x in list_of_people if x.is_girlfriend and not x.has_role(harem_role) and x.is_family)
    #### total paramours not in polycule
    @property
    def paramours(self) -> int:
        return sum(1 for x in list_of_people if x.is_affair and not x.has_role(harem_role))

    #### total slaves
    @property
    def slaves(self) -> int:
        return sum(1 for x in list_of_people if x.is_slave)
    #### total slaves no relations
    @property
    def slaves_norel(self) -> int:
        return sum(1 for x in list_of_people if x.is_slave and not x.is_family and not x.has_relation_with_mc)
    #### total girlfriend slaves
    @property
    def slaves_girlfriends(self) -> int:
        return sum(1 for x in list_of_people if x.is_slave and x.is_girlfriend and not x.is_family and not x.is_affair and not x.has_role(harem_role))
    #### total paramour slaves
    @property
    def slaves_paramour(self) -> int:
        return sum(1 for x in list_of_people if x.is_slave and not x.is_family and x.is_affair and not x.has_role(harem_role))
    
    #### famila slaves
    @property
    def slaves_familia(self) -> int:
        return sum(1 for x in list_of_people if x.is_slave and x.is_family and not x.is_girlfriend and not x.has_role(harem_role))
    #### famila gf slaves
    @property
    def slaves_gffamilia(self) -> int:
        return sum(1 for x in list_of_people if x.is_slave and x.is_family and x.is_girlfriend and not x.has_role(harem_role))
    #### famila poly slaves
    @property
    def slaves_polyfamilia(self) -> int:
        return sum(1 for x in list_of_people if x.is_slave and x.has_role(harem_role))

    @property
    def number_of_sucking_cock_broken(self) -> int:
        return sum(1 for x in list_of_people if x.has_broken_taboo("sucking_cock"))

    @property
    def number_of_vaginal_sex_broken(self) -> int:
        return sum(1 for x in list_of_people if x.has_broken_taboo("vaginal_sex"))

    @property
    def number_of_anal_sex_broken(self) -> int:
        return sum(1 for x in list_of_people if x.has_broken_taboo("anal_sex"))

    @property
    def number_of_bare_pussy_broken(self) -> int:
        return sum(1 for x in list_of_people if x.has_broken_taboo("bare_pussy"))

    @property
    def number_of_bare_tits_broken(self) -> int:
        return sum(1 for x in list_of_people if x.has_broken_taboo("bare_tits"))

    @property
    def number_of_condomless_sex_broken(self) -> int:
        return sum(1 for x in list_of_people if x.has_broken_taboo("condomless_sex"))

StatTracker     = VTStatTracker

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



def _vt_postfix_break_taboo(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        # TODO: make more virgin taboo break dialogs for personalities
        ret_val = wrapped_func(*args, **kwargs)
        self = args[0]
        the_taboo = args[1]
        #VirginTracker virginity taboo breaks
        def get_blood_item(clothing):
            #print("get_blood_item called")
            item = clothing.get_copy()
            item.colour = [.71, .1, .1, 0.8]
            item.layer = 0
            return item
        if the_taboo == "vaginal_sex":
            vt_bloodshow = int(persistent.virgin_blood)
            #print( "vt_bloodshow =" + str(vt_bloodshow))
            if self.hymen==0:
                if vt_bloodshow > 0:
                    vt_bloodrando = renpy.random.randint(1,100)
                    #vt_bloodrando = 33
                    #print( "vt_bloodrando =" + str(vt_bloodrando))
                    if vt_bloodrando <= vt_bloodshow:
                        print("Bloodshow is occurring")
                        self.outfit.add_accessory(get_blood_item(creampie_cum))
                        self.outfit.add_accessory(get_blood_item(ass_cum))
                self.event_triggers_dict["given_virginity"] = True
                self.vaginal_first = mc.name
                self.vaginal_virgin = 1
                self.hymen = 1
                if self.opinion.vaginal_sex < 1:
                    self.update_opinion_with_score("vaginal sex", 1)
            renpy.call("evaluate_virgin_tracker_perks")
            # print( "after evaluate virgin tracker perks...")
        if the_taboo == "sucking_cock":
            if self.oral_virgin == 0:
                self.oral_virgin = 1
                self.oral_first = mc.name
                if self.opinion.giving_blowjobs < 1:
                    self.update_opinion_with_score("giving blowjobs", 1)
            renpy.call("evaluate_virgin_tracker_perks")
        if the_taboo == "anal_sex":
            if self.anal_virgin==0:
                self.anal_virgin =1
                self.anal_first = mc.name
                if self.opinion.anal_sex < 1:
                    self.update_opinion_with_score("anal sex", 1)
            renpy.call("evaluate_virgin_tracker_perks")
        if the_taboo=="condomless_sex":
            renpy.call("evaluate_virgin_tracker_perks")
        if the_taboo=="bare_tits":
            renpy.call("evaluate_virgin_tracker_perks")
        if the_taboo=="bare_pussy":
            renpy.call("evaluate_virgin_tracker_perks")

        #return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

def _vt_postfix_restore_taboo(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        ret_val = wrapped_func(*args, **kwargs)
        self = args[0]
        the_taboo = args[1]

        if the_taboo not in self.broken_taboos:
            return False
        while the_taboo in self.broken_taboos:
            self.broken_taboos.remove(the_taboo)
        #virginity taboo restores
        if the_taboo == "vaginal_sex" and self.vaginal_virgin<=1:
            #restore_virginity(self)
            #self.restore_taboo('vaginal_sex')
            self.vaginal_virgin = 0
            self.hymen = 0
            self.vaginal_first = None
            #self.event_triggers_dict.pop("given_virginity", None)

        if the_taboo == "sucking_cock" and self.oral_virgin==0:
            #self.restore_taboo('sucking_cock')
            self.oral_virgin = 0
            self.oral_first = None

        if the_taboo == "anal_sex" and self.anal_virgin==0:
            #self.restore_taboo('anal_sex')
            self.anal_virgin = 0
            self.anal_first = None

        if add_to_log:
            mc.log_event(f"Taboo reasserted with {self.display_name}!", "float_text_red")
        return True
        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

# def _vt_postfix_advance_time_run_move(wrapped_func: Callable) -> Callable:
    # def wrapping_func(*args, **kwargs):
        # ret_val = wrapped_func(*args, **kwargs)
        # #self = args[0]

        # # #Add the  background switch here if needed
        # if time_of_day == 0:
            # park.background_name = "Park_Early_Morning_Background"
        # elif time_of_day == 1:
            # park.background_name = "Park_Morning_Background"
        # elif time_of_day == 2:
            # park.background_name = "Park_Afternoon_Background"
        # elif time_of_day >3:
            # park.background_name = "Park_Evening_Background"


        # return ret_val # probably None, but core could change
    # wrapping_func.__signature__ = inspect.signature(wrapped_func)
    # return wrapping_func

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

        #return  # probably None, but core could change
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
        # auto-develop natural fetishes without serums or nanos
        if (not self.has_exhibition_fetish \
            and self.sex_record.get("Public Sex", 0) > 19 \
            and self.has_broken_taboo("sucking_cock") \
            and self.has_broken_taboo("vaginal_sex") \
            and self.has_broken_taboo("anal_sex") \
            and self.has_broken_taboo("bare_tits") \
            and self.has_broken_taboo("bare_pussy") \
            and self.sluttiness >= 60 \
            and self.oral_sex_skill >= 4 \
            and self.anal_sex_skill >= 4 \
            and self.vaginal_sex_skill >= 4 \
            and self.opinion.public_sex >= 2 \
            and self.opinion.not_wearing_anything >= 2 \
            and self.opinion.not_wearing_underwear >= 2 \
            and self.opinion.showing_her_ass >= 2 \
            and self.opinion.showing_her_tits >= 2 \
            and self.opinion.skimpy_outfits >= 2 \
            and self.opinion.skimpy_uniforms >= 2 \
            and self.opinion.masturbating >= 2 ):
            if VT_start_exhibition_fetish_quest(self):
                self.event_triggers_dict["VT_exhibition_fetish_start"] = True

        if (not self.has_cum_fetish \
            and self.cum_exposure_count >=20 \
            and self.has_broken_taboo("sucking_cock") \
            and self.has_broken_taboo("condomless_sex") \
            and self.has_broken_taboo("anal_sex") \
            and self.has_broken_taboo("vaginal_sex") \
            and self.has_broken_taboo("bare_tits") \
            and self.has_broken_taboo("bare_pussy") \
            and self.oral_sex_skill >= 4 \
            and self.sluttiness >= 60 \
            and self.opinion.giving_blowjobs >= 2 \
            and self.opinion.being_covered_in_cum >= 2 \
            and self.opinion.cum_facials >= 2 \
            and self.opinion.drinking_cum >= 2 \
            and self.opinion.showing_her_tits >= 2 \
            and self.opinion.creampies >= 2 \
            and self.opinion.anal_creampies >= 2 \
            and self.opinion.bareback_sex >= 2 \
            and self.opinion.giving_handjobs >= 2 ):
            if VT_start_cum_fetish_quest(self):
                self.event_triggers_dict["VT_cum_fetish_start"] = True

        if (not self.has_vaginal_fetish \
            and (self.vaginal_sex_count >=10 or self.vaginal_creampie_count >= 10) \
            and self.vaginal_sex_skill >=4 \
            and self.is_willing(missionary) \
            and self.has_broken_taboo("vaginal_sex") \
            and self.sluttiness >=60 \
            and (self.opinion.vaginal_sex >=2 or self.opinion.creampies >=2) \
            and self.opinion.bareback_sex >= 2 \
            and self.opinion.showing_her_ass >= 2 \
            and self.opinion.missionary_style >= 2 ):
            if VT_start_vaginal_fetish_quest(self):
                self.event_triggers_dict["VT_vaginal_fetish_start"] = True

        if (not self.has_anal_fetish \
                and (self.anal_sex_count >= 10 or self.anal_creampie_count >= 10) \
                and self.anal_sex_skill >= 4 \
                and self.is_willing(doggy_anal) \
                and self.has_broken_taboo("anal_sex") \
                and self.sluttiness >= 60 \
                and (self.opinion.anal_sex >= 2 or self.opinion.anal_creampies >= 2 ) \
                and self.opinion.doggy_style >= 2 \
                and self.opinion.showing_her_ass >= 2 ):
            if VT_start_anal_fetish_quest(self):
                self.event_triggers_dict["VT_anal_fetish_start"] = True

        if (not self.has_breeding_fetish \
                and persistent.pregnancy_pref > 0 \
                and self.vaginal_creampie_count >= 10 \
                and self.vaginal_sex_skill >= 4 \
                and self.is_willing(missionary) \
                and self.has_broken_taboo("condomless_sex") \
                and self.has_broken_taboo("vaginal_sex") \
                and self.sluttiness >=60 \
                and self.opinion.bareback_sex >=2 \
                and self.opinion.showing_her_ass >= 2 \
                and self.opinion.vaginal_sex >= 2 \
                and self.opinion.missionary_style >= 2 \
                and self.opinion.creampies >= 2 ):
            if VT_start_breeding_fetish_quest(self):
                self.event_triggers_dict["VT_breeding_fetish_start"] = True

        #run randomizer for girls
        VT_shuffle_and_update()

        #use run day 1 to set the harem mansion name
        if day == 1:
            harem_mansion.formal_name = str(mc.last_name) + " Mansion"
            #harem_mansion.visible = True
            harem_hub.formal_name = str(mc.last_name) + " Mansion"
        #do a check on end of day to see if  any of the perks popped
        if len(known_people_in_the_game()) == 20:
            renpy.call("evaluate_virgin_tracker_perks")
        
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
            
            if sex_class == "Vaginal":
                self.set_event_day("Last Vaginal Day")
            if sex_class == "Oral":
                self.set_event_day("Last Oral Day")
            if sex_class == "Anal":
                self.set_event_day("Last Anal Day")
            # if _virgin <= 9 (NOTE: this condition is always evaluated,
            # whether or not the previous `if _virgin == 0`` was True)
            if getattr(self, _sex_type_virgin) <= 9:
                # increase it by one
                setattr(self, _sex_type_virgin, getattr(self, _sex_type_virgin, 3) + 1)
        if report_log.get("was_public", False):
            self.set_event_day("LastExhibitionDay")
        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

# advance_time_run_move         = _vt_postfix_advance_time_run_move(advance_time_run_move)

Person.__init__         = _vt_prefix_person_init(Person.__init__)
Person.break_taboo      = _vt_postfix_break_taboo(Person.break_taboo)
Person.restore_taboo    = _vt_postfix_restore_taboo(Person.restore_taboo)
Person.run_turn         = _vt_postfix_person_run_turn(Person.run_turn)
Person.run_day          = _vt_postfix_person_run_day(Person.run_day)
Person.cum_in_mouth     = _vt_postfix_person_cum_in_mouth(Person.cum_in_mouth)
Person.cum_in_vagina    = _vt_postfix_person_cum_in_vagina(Person.cum_in_vagina)
Person.cum_in_ass       = _vt_postfix_person_cum_in_ass(Person.cum_in_ass)
Person.update_person_sex_record = _vt_postfix_person_update_sex_record(Person.update_person_sex_record)

def _vt_postfix_update_person_opinions(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):
        # TODO: make mod install compatible with existing savegames (person doesn't have VT attribute anal_cum)
        ret_val = wrapped_func(*args, **kwargs)
        person = args[0]
        ensure_opinion_on_subject(person, ["dresses", "pants", "skirts"])
        ensure_opinion_on_subject(person, ["boots", "high heels"])
        ensure_opinion_on_subject(person, ["classical music", "heavy metal music", "jazz", "punk music", "pop music"])
        ensure_opinion_on_subject(person, ["Mondays", "Fridays", "the weekend"])
        ensure_opinion_on_subject(person, ["hiking", "sports", "yoga"])

        ensure_sexy_opinion_on_subject(person, ["lingerie", "showing her tits", "showing her ass"])
        ensure_sexy_opinion_on_subject(person, ["skimpy outfits", "not wearing underwear", "skimpy uniforms"])

        # skew anal sex to negative
        if person.anal_sex_skill > 2:
            person.sex_skills["Anal"] -= 2

        # by default there is a negative skew opinion on incest / threesomes / cheating (66%)
        if person.opinion.incest == 0 and renpy.random.randint(0, 2) != 1:
            person.set_opinion("incest", renpy.random.choice([-2, -1]), False)

        if person.opinion.threesomes == 0 and renpy.random.randint(0, 2) != 1:
            person.set_opinion("threesomes", renpy.random.choice([-2, -1]), False)

        if person.opinion.cheating_on_men == 0 and renpy.random.randint(0, 2) != 1:
            person.set_opinion("cheating on men", renpy.random.choice([-2, -1]), False)

        # do we have sexual preferences / dislikes?
        ensure_opinion_on_sexual_preference(person, "Foreplay", ["kissing", "being fingered", "giving handjobs"])
        ensure_opinion_on_sexual_preference(person, "Oral", ["giving blowjobs", "getting head", "drinking cum"])
        ensure_opinion_on_sexual_preference(person, "Vaginal", ["missionary style sex", "vaginal sex", "creampies"])
        ensure_opinion_on_sexual_preference(person, "Anal", ["anal sex", "anal creampies", "doggy style sex"])

        # fix opinion contradictions (one cannot exclude other)
        fix_opinion_contradiction(person, "drinking cum", ["giving blowjobs", "giving handjobs", "giving tit fucks", "like men"])
        fix_opinion_contradiction(person, "bareback sex", ["creampies", "anal creampies", "like men"])
        fix_opinion_contradiction(person, "skimpy outfits", ["showing her tits", "showing her ass", "high heels", "flashing"])
        fix_opinion_contradiction(person, "masturbating", ["being fingered", "peeping", "flashing"])
        fix_opinion_contradiction(person, "vaginal sex", ["creampies", "like men"])
        fix_opinion_contradiction(person, "anal sex", ["anal creampies", "like men"])
        fix_opinion_contradiction(person, "cheating on men", ["flashing", "peeping", "like men", "like women", "open relationships"])
        fix_opinion_contradiction(person, "being covered in cum", ["flashing", "like men"])
        fix_opinion_contradiction(person, "giving blowjobs", ["flashing", "like men"])
        fix_opinion_contradiction(person, "likes women", ["getting head", "masturbating", "being fingered"])
        
        # choose at least three colours for an opinion (one from primary, one from b/w, one from secondary)
        ensure_opinion_on_subject(person, ["the colour red", "the colour green", "the colour blue"])
        ensure_opinion_on_subject(person, ["the colour black", "the colour white"])
        ensure_opinion_on_subject(person, ["the colour pink", "the colour purple", "the colour orange", "the colour yellow", "the colour brown"])

        # fix opinion exclusion (one excludes other)
        fix_opinion_exclusion(person, "lingerie", ["not wearing underwear", "not wearing anything"])
        fix_opinion_exclusion(person, "skimpy outfits", ["not wearing anything", "conservative outfits"])
        fix_opinion_exclusion(person, "the colour red", ["the colour pink", "the colour purple"]) # red and pink/purple clash
        fix_opinion_exclusion(person, "the colour pink", ["the colour purple", "the colour red"]) # pink and purple/red clash
        fix_opinion_exclusion(person, "the colour purple", ["the colour pink", "the colour red", "the colour blue"]) # purple and pink/red/blue clash
        fix_opinion_exclusion(person, "the colour blue", ["the colour purple"]) # pink and purple clash
        fix_opinion_exclusion(person, "the colour orange", ["the colour yellow"]) # orange and yellow clash
        fix_opinion_exclusion(person, "the colour yellow", ["the colour orange"]) # yellow and orange clash

        # set work opinions (based on stats / skills)
        if not person.is_unique:
            set_work_opinion(person, "research work", person.int, person.research_skill)
            set_work_opinion(person, "marketing work", person.charisma, person.market_skill)
            set_work_opinion(person, "HR work", person.charisma, person.hr_skill)
            set_work_opinion(person, "supply work", person.focus, person.supply_skill)
            set_work_opinion(person, "production work", person.focus, person.production_skill)
        
        
        
        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

update_person_opinions = _vt_postfix_update_person_opinions(update_person_opinions)

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
        # use sex_cap arg if passed, else get_sex_skill_ceiling
        sex_cap = kwargs.pop("sex_cap", Person.get_sex_skill_ceiling())
        # grab any provided VirginTracker keyword args
        given_vt_kwargs: dict[str, Optional[Union[int, None]]] = {}
        for arg_name in virgin_tracker_args:
            if arg_name in kwargs:
                given_vt_kwargs[arg_name] = kwargs.pop(arg_name, None)
  
        # force kids=0 if hymen is sealed or recently torn
        if given_vt_kwargs.get("hymen", None) in (0, 1):
            kwargs["kids"] = 0

        #try to grab the age_range
        age_range = kwargs.get("age_range", None)

        # Determine job assignment
        # if not kwargs.get("age") and not "age_range" and type and (kwargs.get("job") == None or kwargs.get("job").age_range == None):
            # age_range = VT_AGE_RANGES[get_random_from_weighted_list(_vt_build_weighted_list(VT_Settings["Population"]))]
        # set age_range based on VT preferences
        #if not kwargs.get("age") and not kwargs.get("age_range") and kwargs.get("type")=="random" and (kwargs.get("job") == None or hasattr(kwargs.get("job"), 'age_range') == None):
        if not kwargs.get("age") and not kwargs.get("age_range") and kwargs.get("type")=="random" and (kwargs.get("job") == None or hasattr(kwargs.get("job"), 'age_range') == None):
            kwargs["age_range"] = VT_AGE_RANGES[get_random_from_weighted_list(_vt_build_weighted_list(VT_Settings["Population"]))]
            age_range = kwargs["age_range"]
        ######################
        #### Call to core code
        ######################
        person = wrapped_func(*args, **kwargs)

        # NOTE: first assign any parameters passed by the calling location
        # this may set any combination of VT parameters
        for key, value in given_vt_kwargs.items():
            # set the values directly
            setattr(person, key, value)

        # NOTE: then fill in the remaining stats
        for sex_type in ["Oral", "Vaginal", "Anal"]:
        # compute the values
            # NOTE: this has side-effects; it affects the person's sex skills
            stats = _vt_virginity_stats(person, sex_type, sex_cap)
            # and apply them (if they don't already exist)
            for key, value in stats.items():
                if not hasattr(person, key):
                    setattr(person, key, value)

        if VIRGIN_TRACKER_DEBUG:
            write_log(f"Added VT Attributes - Virgins: {[getattr(person, sex_kind+'_virgin') for sex_kind in ('oral','vaginal','anal')]},"\
                      + f" Firsts: {[getattr(person, sex_kind+'_first') for sex_kind in ('oral','vaginal','anal')]})")
            if person.type=="random":
                age_tag = _vt_get_person_age_tag(person)
                write_log(f"Random char | Age range: {age_tag} | Virginity chances: {[getattr(persistent, age_tag + '_' + sex_kind.lower()) for sex_kind in ['Oral','Vaginal','Anal']]}")

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
                      job: JobDefinition = None, 
                      job_list: list[JobDefinition] = None,
                      **kwargs) -> Person:

        # Determine job assignment
        if not kwargs.get("age") and not "age_range" and type and (kwargs.get("job") == None or kwargs.get("job").age_range == None):
            age_range = VT_AGE_RANGES[get_random_from_weighted_list(_vt_build_weighted_list(VT_Settings["Population"]))]

        # if VIRGIN_TRACKER_DEBUG:
            # if type=="random":
                # write_log(f"make_person_override-after age chk-RANDOM: {age_range} Job: {job}")
            # else:
                # write_log(f"make_person_override-after age chk: {age_range} Job: {job} ")

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
                                                    job = job,
                                                    job_list = job_list,
                                                    **kwargs)

        return_character = _vt_apply_opinions_makeup_and_schedule(return_character, forced_opinions, forced_sexy_opinions)

        return return_character
    #wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func

make_person = _vt_make_person_override(make_person)

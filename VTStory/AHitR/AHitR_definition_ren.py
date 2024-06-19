import renpy
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.personality_types._personality_definitions_ren import wild_personality, relaxed_personality, bimbo_personality,reserved_personality,introvert_personality,cougar_personality
from game.clothing_lists_ren import twintail, shaved_pubes, colourful_bracelets
from game.major_game_classes.character_related.Job_ren import Job
from game.major_game_classes.character_related._job_definitions_ren import unemployed_job, night_nurse_job, bartender_job
from game.major_game_classes.character_related.JobDefinition_ren import JobDefinition, student_job, market_job, supply_job, production_job, hr_job
from game.game_roles._role_definitions_ren import generic_student_role
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions, mc, lily, mom
day = 0
time_of_day = 0
"""renpy
init 3 python:
"""
list_of_instantiation_functions.append("create_AHitR_characters")

def create_AHitR_characters():
    # Azraesha - Rae - sensual arts - auburn/purple hair - purple eyes - pale - shorter than Lyriel
    #   short crop top, jean pants
    ### Azraesha ###
    Azraesha_wardrobe = wardrobe_from_xml("AHitR_Azraesha_Wardrobe")

    # Azraesha_personality = Personality("wild", wild_personality.default_prefix,
        # common_likes = ["the colour white", "flirting", "skirts", "makeup", "the colour yellow", "high heels", "working" "yoga"],
        # common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        # common_dislikes = ["pants", "conservative outfits"],
        # common_sexy_dislikes = ["cheating on men"],
        # titles_function = AHitR_titles, possessive_titles_function = AHitR_possessive_titles, player_titles_function = AHitR_player_titles,
        # insta_chance = 0, dikdok_chance = 0)

    global Azraesha_role
    Azraesha_role = Role("Azraesha", [], hidden = True) #Used to hold any Stephanie specific actions not tied to another role, and to guarantee this is Steph even if she undergoes a personality change.

    global Azraesha
    Azraesha = make_person(name = "Azraesha", last_name = "Lilitu", age = 24, body_type = "thin_body", face_style = "Face_7", tits="C", height = 0.8,
        hair_colour = ["purple", [0.69, 0.05, 0.61, 0.95]], hair_style = twintail, pubes_style = shaved_pubes, skin = "white",
        eyes = ["purple", [0.69, 0.05, 0.61, 0.95]], personality = relaxed_personality, name_color = "#6600cc", dial_color = "#9900cc", starting_wardrobe = Azraesha_wardrobe,
        stat_array = [20,20,20], skill_array = [20,20,20,20,20], sex_skill_array = [20,20,20,20], sluttiness = 95, obedience = 280, happiness = 200, love = 100, suggestibility=100,
        title = "Rae", possessive_title = "Your Succubus", mc_title = "Honey", relationship = "Single", kids = 0, job = unemployed_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["skirts", 2, True],
            ["dresses", 2, True],
            ["flirting", 1, True],
            ["makeup", 2, True],
            ["pants", -2, True],
            ["the colour red", 2, True],
            ["the colour purple", 2, True],
            ["working", 2, True],
            ["yoga", 2, True]
        ], forced_sexy_opinions = [
            ["bareback sex", 2, True],
            ["skimpy outfits", 2, True],
            ["showing her ass", 1, True],
            ["masturbating", 2, True],
            ["creampies", 2, True],
            ["giving blowjobs", 2, True],
            ["drinking cum", 1, True],
            ["incest", 2, True],
            ["polyamory", 2, True],
            ["threesomes", 2, True]
        ])

    Azraesha.generate_home().add_person(Azraesha)
    Azraesha.home.add_person(Azraesha)
    Azraesha.add_role(Azraesha_role)
    Azraesha.home.background_name = "AHitR_downstairslobby"
    mc.phone.register_number(Azraesha)
    mc.known_home_locations.append(Azraesha.home)
    Azraesha.on_birth_control = False
    Azraesha.change_job(market_job)
    Azraesha.change_job(stripper_job, is_primary = False)
    strip_club.add_person(Azraesha)

    ### Naomi ### Needs own titles etc
# Naomi - wild - tanned - brown hair short - brown eyes - tall
#   Red top, black jogging pants
    Naomi_wardrobe = wardrobe_from_xml("AHitR_Naomi_Wardrobe")
    
    # Naomi_personality = Personality("alpha", introvert_personality.default_prefix,
        # common_likes = ["dresses", "flirting", "skirts", "makeup", "the colour red", "high heels", "working" "yoga"],
        # common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        # common_dislikes = ["pants", "conservative outfits"],
        # common_sexy_dislikes = ["cheating on men"],
        # titles_function = AHitR_titles, possessive_titles_function = AHitR_possessive_titles, player_titles_function = AHitR_player_titles,
        # insta_chance = 0, dikdok_chance = 0)

    global Naomi_role
    Naomi_role = Role("Naomi", [], hidden = True) #Used to hold any Stephanie specific actions not tied to another role, and to guarantee this is Steph even if she undergoes a personality change.
    
    global Naomi
    Naomi = make_person(name = "Naomi", last_name = "Foringi", age = 32, body_type = "standard_body", face_style = "Face_5", tits="F", height = 1.1,
        hair_colour = ["brown", [0.21, 0.105, 0.06, 0.95]], hair_style = messy_ponytail, pubes_style = default_pubes, skin = "tan",
        eyes = ["brown", [0.62, 0.42, 0.29, 0.9]], personality = cougar_personality, name_color = "#cc3300", dial_color = "#ff531a", starting_wardrobe = Naomi_wardrobe,
        stat_array = [20,20,20], skill_array = [20,20,20,20,20], sex_skill_array = [20,20,20,20], sluttiness = 95, obedience = 280, happiness = 200, love = 100, suggestibility=100,
        title = "Captain", possessive_title = "Your Pirate", mc_title = "Mate", relationship = "Single", kids = 0, job = unemployed_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["skirts", 2, True],
            ["dresses", 2, True],
            ["flirting", 1, True],
            ["makeup", 2, True],
            ["pants", -2, True],
            ["the colour red", 2, True],
            ["the colour purple", 2, True],
            ["working", 2, True],
            ["yoga", 2, True]
        ], forced_sexy_opinions = [
            ["bareback sex", 2, True],
            ["skimpy outfits", 2, True],
            ["showing her ass", 1, True],
            ["masturbating", 2, True],
            ["creampies", 2, True],
            ["giving blowjobs", 2, True],
            ["drinking cum", 1, True],
            ["incest", 2, True],
            ["polyamory", 2, True],
            ["threesomes", 2, True]
        ])

    Azraesha.home.add_person(Naomi)
    Naomi.home = Azraesha.home
    Naomi.set_schedule(Naomi.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 1, 2, 3, 4])
    Naomi.add_role(Naomi_role)
    Naomi.home.add_person(Naomi)
    mc.phone.register_number(Naomi)
    mc.known_home_locations.append(Naomi.home)
    Naomi.on_birth_control = False
    Naomi.change_job(hr_job)
    Naomi.change_job(bartender_job, is_primary = False)

### Lyriel ###
# Lyriel - blond long hair - green eyes - pale - well endowed - bitchy elf - not as tall as Naomi/Yona
#   green top - white/blue shorts
    Lyriel_wardrobe = wardrobe_from_xml("AHitR_Lyriel_Wardrobe")
    
#    Lyriel_personality = Personality("bimbo", bimbo_personality.default_prefix,
#        common_likes = ["dresses", "flirting", "skirts", "makeup", "the colour red", "high heels", "working" "yoga"],
#        common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
#        common_dislikes = ["pants", "conservative outfits"],
#        common_sexy_dislikes = ["cheating on men"],
#        titles_function = AHitR_titles, possessive_titles_function = AHitR_possessive_titles, player_titles_function = AHitR_player_titles,
#        insta_chance = 0, dikdok_chance = 0)

    global Lyriel_role
    Lyriel_role = Role("Lyriel", [], hidden = True) #Used to hold any Stephanie specific actions not tied to another role, and to guarantee this is Steph even if she undergoes a personality change.
    
    global Lyriel
    Lyriel = make_person(name = "Lyriel", last_name = "Edhel", age = 19, body_type = "thin_body", face_style = "Face_4", tits="C", height = 0.8,
        hair_colour = ["golden blonde", [0.895, 0.781, 0.656, 0.95]], hair_style = long_hair, pubes_style = diamond_pubes, skin = "white",
        eyes = ["green", [0.35, 0.68, 0.40, 0.9]], personality = bimbo_personality, name_color = "#33cc00", dial_color = "#66ff33", starting_wardrobe = Lyriel_wardrobe,
        stat_array = [20,20,20], skill_array = [20,20,20,20,20], sex_skill_array = [20,20,20,20], sluttiness = 95, obedience = 280, happiness = 200, love = 100, suggestibility=100,
        title = "Daisy", possessive_title = "Your Elven Lover", mc_title = "Yeah", relationship = "Single", kids = 0, job = student_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["skirts", 2, True],
            ["dresses", 2, True],
            ["flirting", 1, True],
            ["makeup", 2, True],
            ["pants", -2, True],
            ["the colour red", 2, True],
            ["the colour purple", 2, True],
            ["working", 2, True],
            ["yoga", 2, True]
        ], forced_sexy_opinions = [
            ["bareback sex", 2, True],
            ["skimpy outfits", 2, True],
            ["showing her ass", 1, True],
            ["masturbating", 2, True],
            ["creampies", 2, True],
            ["giving blowjobs", 2, True],
            ["drinking cum", 1, True],
            ["incest", 2, True],
            ["polyamory", 2, True],
            ["threesomes", 2, True]
        ])
    Azraesha.home.add_person(Lyriel)
    Lyriel.home = Azraesha.home
    Lyriel.set_schedule(Lyriel.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 1, 2, 3, 4])
    Lyriel.add_role(Lyriel_role)
    Lyriel.home.add_person(Lyriel)
    mc.phone.register_number(Lyriel)
    mc.known_home_locations.append(Lyriel.home)
    Lyriel.on_birth_control = False
    Lyriel.change_job(production_job)
    Lyriel.change_job(night_nurse_job, is_primary = False)
   
# Caitlin
### Caitlin ###
# Caitlin - red hair orange - blue eyes - well endowed - laid back relaxed_personality - shy student - pale - short as Lyriel
#   white dress top, black skirt
    Caitlin_wardrobe = wardrobe_from_xml("AHitR_Caitlin_Wardrobe")
    
    # Caitlin_personality = Personality("bimbo", bimbo_personality.default_prefix,
        # common_likes = ["dresses", "flirting", "skirts", "makeup", "the colour red", "high heels", "working" "yoga"],
        # common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        # common_dislikes = ["pants", "conservative outfits"],
        # common_sexy_dislikes = ["cheating on men"],
        # titles_function = AHitR_titles, possessive_titles_function = AHitR_possessive_titles, player_titles_function = AHitR_player_titles,
        # insta_chance = 0, dikdok_chance = 0)

    global Caitlin_role
    Caitlin_role = Role("Caitlin", [], hidden = True) #Used to hold any Stephanie specific actions not tied to another role, and to guarantee this is Steph even if she undergoes a personality change.
    
    global Caitlin
    Caitlin = make_person(name = "Caitlin", last_name = "Mystica", age = 19, body_type = "thin_body", face_style = "Face_4", tits="C", height = 0.8,
        hair_colour = ["vivid red", [1.0, 0.23, 0.00, 0.95]], hair_style = messy_short_hair, pubes_style = diamond_pubes, skin = "white",
        eyes = ["green", [0.35, 0.68, 0.40, 0.9]], personality = reserved_personality, name_color = "#ff531a", dial_color = "#ff8c67", starting_wardrobe = Caitlin_wardrobe,
        stat_array = [20,20,20], skill_array = [20,20,20,20,20], sex_skill_array = [20,20,20,20], sluttiness = 95, obedience = 280, happiness = 200, love = 100, suggestibility=100,
        title = "Sunflower", possessive_title = "Your Librarian", mc_title = "Sir", relationship = "Single", kids = 0, job = student_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["skirts", 2, True],
            ["dresses", 2, True],
            ["flirting", 1, True],
            ["makeup", 2, True],
            ["pants", -2, True],
            ["the colour red", 2, True],
            ["the colour purple", 2, True],
            ["working", 2, True],
            ["yoga", 2, True]
        ], forced_sexy_opinions = [
            ["bareback sex", 2, True],
            ["skimpy outfits", 2, True],
            ["showing her ass", 1, True],
            ["masturbating", 2, True],
            ["creampies", 2, True],
            ["giving blowjobs", 2, True],
            ["drinking cum", 1, True],
            ["incest", 2, True],
            ["polyamory", 2, True],
            ["threesomes", 2, True]
        ])
    Azraesha.home.add_person(Caitlin)
    Caitlin.home = Azraesha.home
    Caitlin.set_schedule(Caitlin.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 1, 2, 3, 4])
    Caitlin.add_role(Caitlin_role)
    Caitlin.home.add_person(Caitlin)
    mc.phone.register_number(Caitlin)
    mc.known_home_locations.append(Caitlin.home)
    Caitlin.on_birth_control = False

# Blair
### Blair ###
# Blair - feisty dwarf - independent - red/auburn hair - hazel eyes - big boobs - shortest and curvy - tanned
#   white open top with blue vest, blue jean shorts
    Blair_wardrobe = wardrobe_from_xml("AHitR_Blair_Wardrobe")
    
    # Blair_personality = Personality("bimbo", bimbo_personality.default_prefix,
        # common_likes = ["dresses", "flirting", "skirts", "makeup", "the colour red", "high heels", "working" "yoga"],
        # common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        # common_dislikes = ["pants", "conservative outfits"],
        # common_sexy_dislikes = ["cheating on men"],
        # titles_function = AHitR_titles, possessive_titles_function = AHitR_possessive_titles, player_titles_function = AHitR_player_titles,
        # insta_chance = 0, dikdok_chance = 0)

    global Blair_role
    Blair_role = Role("Blair", [], hidden = True) #Used to hold any Stephanie specific actions not tied to another role, and to guarantee this is Steph even if she undergoes a personality change.
    
    global Blair
    Blair = make_person(name = "Blair", last_name = "Mjolnir", age = 22, body_type = "curvy_body", face_style = "Face_6", tits="E", height = 0.6,
        hair_colour = ["dark auburn", [0.367, 0.031, 0.031, 0.95]], hair_style = ponytail, pubes_style = diamond_pubes, skin = "tan",
        eyes = ["brown", [0.62, 0.42, 0.29, 0.9]], personality = introvert_personality, name_color = "#996633", dial_color = "#996633", starting_wardrobe = Blair_wardrobe,
        stat_array = [20,20,20], skill_array = [20,20,20,20,20], sex_skill_array = [20,20,20,20], sluttiness = 95, obedience = 280, happiness = 200, love = 100, suggestibility=100,
        title = "Dwarven Lass", possessive_title = "Your Stout rock", mc_title = "Mister", relationship = "Single", kids = 0, job = student_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["skirts", 2, True],
            ["dresses", 2, True],
            ["flirting", 1, True],
            ["makeup", 2, True],
            ["pants", -2, True],
            ["the colour red", 2, True],
            ["the colour purple", 2, True],
            ["working", 2, True],
            ["yoga", 2, True]
        ], forced_sexy_opinions = [
            ["bareback sex", 2, True],
            ["skimpy outfits", 2, True],
            ["showing her ass", 1, True],
            ["masturbating", 2, True],
            ["creampies", 2, True],
            ["giving blowjobs", 2, True],
            ["drinking cum", 1, True],
            ["incest", 2, True],
            ["polyamory", 2, True],
            ["threesomes", 2, True]
        ])
    Azraesha.home.add_person(Blair)
    Blair.home = Azraesha.home
    Blair.set_schedule(Blair.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 1, 2, 3, 4])
    Blair.add_role(Blair_role)
    Blair.home.add_person(Blair)
    mc.phone.register_number(Blair)
    mc.known_home_locations.append(Blair.home)
    Blair.on_birth_control = False
    Blair.change_job(production_job)
    
# Yona
### Yona ###
# Yona Flotnar- strong stoic orc - braided long dark red hair ponytail - hazel gold eyes - green skinned/tanned - tall as Naomi
#   tight black top, black hot shorts
    Yona_wardrobe = wardrobe_from_xml("AHitR_Yona_Wardrobe")
    
    # Yona_personality = Personality("bimbo", bimbo_personality.default_prefix,
        # common_likes = ["dresses", "flirting", "skirts", "makeup", "the colour red", "high heels", "working" "yoga"],
        # common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        # common_dislikes = ["pants", "conservative outfits"],
        # common_sexy_dislikes = ["cheating on men"],
        # titles_function = AHitR_titles, possessive_titles_function = AHitR_possessive_titles, player_titles_function = AHitR_player_titles,
        # insta_chance = 0, dikdok_chance = 0)

    global Yona_role
    Yona_role = Role("Yona", [], hidden = True) #Used to hold any Stephanie specific actions not tied to another role, and to guarantee this is Steph even if she undergoes a personality change.
    
    global Yona
    Yona = make_person(name = "Yona", last_name = "Mjolnir", age = 22, body_type = "curvy_body", face_style = "Face_6", tits="E", height = 1.1,
        hair_colour = ["dark auburn", [0.367, 0.031, 0.031, 0.95]], hair_style = ponytail, pubes_style = diamond_pubes, skin = "tan",
        eyes = ["dark auburn", [0.367, 0.031, 0.031, 0.95]], personality = introvert_personality, name_color = "#333333", dial_color = "#505050", starting_wardrobe = Yona_wardrobe,
        stat_array = [20,20,20], skill_array = [20,20,20,20,20], sex_skill_array = [20,20,20,20], sluttiness = 95, obedience = 280, happiness = 200, love = 100, suggestibility=100,
        title = "Amazon", possessive_title = "Your Amazon", mc_title = "Chief", relationship = "Single", kids = 0, job = student_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["skirts", 2, True],
            ["dresses", 2, True],
            ["flirting", 1, True],
            ["makeup", 2, True],
            ["pants", -2, True],
            ["the colour red", 2, True],
            ["the colour purple", 2, True],
            ["working", 2, True],
            ["yoga", 2, True]
        ], forced_sexy_opinions = [
            ["bareback sex", 2, True],
            ["skimpy outfits", 2, True],
            ["showing her ass", 1, True],
            ["masturbating", 2, True],
            ["creampies", 2, True],
            ["giving blowjobs", 2, True],
            ["drinking cum", 1, True],
            ["incest", 2, True],
            ["polyamory", 2, True],
            ["threesomes", 2, True]
        ])
    Azraesha.home.add_person(Yona)
    Yona.home = Azraesha.home
    Yona.set_schedule(Yona.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 1, 2, 3, 4])
    Yona.add_role(Yona_role)
    Yona.home.add_person(Yona)
    mc.phone.register_number(Yona)
    mc.known_home_locations.append(Yona.home)
    Yona.on_birth_control = False
    Yona.change_job(production_job)
    
    ####define relationships after
    town_relationships.update_relationship(Naomi, Azraesha, "Sister")
    town_relationships.update_relationship(Lyriel, Azraesha, "Sister")
    town_relationships.update_relationship(Lyriel, Naomi, "Sister")
    town_relationships.update_relationship(Caitlin, Azraesha, "Sister")
    town_relationships.update_relationship(Caitlin, Naomi, "Sister")
    town_relationships.update_relationship(Caitlin, Lyriel, "Sister")
    town_relationships.update_relationship(Blair, Azraesha, "Sister")
    town_relationships.update_relationship(Blair, Naomi, "Sister")
    town_relationships.update_relationship(Blair, Lyriel, "Sister")
    town_relationships.update_relationship(Blair, Caitlin, "Sister")
    town_relationships.update_relationship(Yona, Azraesha, "Sister")
    town_relationships.update_relationship(Yona, Naomi, "Sister")
    town_relationships.update_relationship(Yona, Lyriel, "Sister")
    town_relationships.update_relationship(Yona, Caitlin, "Sister")
    town_relationships.update_relationship(Yona, Blair, "Sister")


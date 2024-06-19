import renpy
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.personality_types._personality_definitions_ren import wild_personality, relaxed_personality, bimbo_personality
from game.clothing_lists_ren import twintail, shaved_pubes, colourful_bracelets
from game.major_game_classes.character_related.Job_ren import Job
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition, nora_professor_job, university_professor_job, doctor_job, waitress_job, unemployed_job, stripper_job, stripclub_stripper_job, stripclub_bdsm_performer_job, stripclub_mistress_job, stripclub_waitress_job, stripclub_manager_job, prostitute_job
from game.game_roles._role_definitions_ren import generic_student_role
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions, mc, lily

"""renpy
init 3 python:
"""
list_of_instantiation_functions.append("create_tmnt_characters")

def tmnt_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)
    valid_titles.append("Turtle")
    valid_titles.append("Quiet One")
    valid_titles.append("Pizza Girl")
    valid_titles.append("Plucky")
    valid_titles.append("Ninja")
    valid_titles.append("Sprout")
    if person.has_breeding_fetish:
        valid_titles.append("Cowabunga Breeder Bunny")
    if person.has_anal_fetish:
        valid_titles.append("Star Ninja")
    return valid_titles

def tmnt_possessive_titles(person: Person):
    valid_possessive_titles = ["your shadow girl", person.title]
    if person.effective_sluttiness() > 60:
        valid_possessive_titles.append("your shadow slut")
    if person.effective_sluttiness() > 80:
        valid_possessive_titles.append("your ninja cumdump")
    if person.has_breeding_fetish:
        valid_possessive_titles.append("your shadow breeder")
    if person.has_anal_fetish:
        valid_possessive_titles.append("your anal ninja")
    return valid_possessive_titles

def tmnt_player_titles(person: Person):
    valid_mc_titles = [mc.name]
    valid_mc_titles.append("Dude")
    valid_mc_titles.append("Mutant")
    valid_mc_titles.append("Polymath")
    valid_mc_titles.append("Sensei")
    valid_mc_titles.append("Mouser")
    valid_mc_titles.append("Plucky")
    if person.has_breeding_fetish:
        valid_mc_titles.append("Shadow Breeder")
    return valid_mc_titles

def create_tmnt_characters():
    ### Yoshi Hamato ###
    yoshitmnt_wardrobe = wardrobe_from_xml("TMNTSplinter_Wardrobe")
    yoshitmnt_base = Outfit("Splinter Casuals") #TODO: Decide what accessories we want her to haven
    
    yoshitmnt_personality = Personality("athlete", reserved_personality.default_prefix,
        common_likes = ["pants", "flirting", "conservative outfits", "makeup", "the colour purple", "the color yellow", "working", "yoga"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "showing her ass", "drinking cum", "taking control", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        common_dislikes = ["skirts", "dresses", "makeup", "the colour pink", "dresses", "high heels"],
        common_sexy_dislikes = ["cheating on men","lingerie", "being submissive", "skimpy outfits"],
        titles_function = tmnt_titles, possessive_titles_function = tmnt_possessive_titles, player_titles_function = tmnt_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global yoshitmnt_role
    yoshitmnt_role = Role("Yoshi", [], hidden = True)

    global yoshitmnt
    yoshitmnt = make_person(name = "Yoshi", last_name = "Hamato", age = 42, body_type = "thin_body", face_style = "Face_12", tits="E", height = 0.86,
        hair_colour = ["rat grey", [0.15, 0.15, 0.15, 0.95]], hair_style = messy_short_hair, pubes_style = shaved_pubes, skin = "tan",
        eyes = "dark brown", personality = yoshitmnt_personality, name_color = "#611F26", dial_color = "#611F26", starting_wardrobe = yoshitmnt_wardrobe, base_outfit = yoshitmnt_base,
        stat_array = [7,5,3], skill_array = [8,1,3,4,4], sex_skill_array = [7,7,7,7], sluttiness = 40, obedience = 160, happiness = 120, love = 80, suggestibility=40,
        relationship = "Single", kids = 5, job = unemployed_job,
        sex_cap=10, 
        work_experience = 8, type="unique",
        forced_opinions = [
            ["classical music", 2, False],
            ["heavy metal music", -2, False],
            ["jazz", 2, False],
            ["pop music", -2, False],
            ["punk music", -2, False],
            ["hr work", 2, True],
            ["marketing work", 2, False],
            ["production work", -2, False],
            ["research work", -2, False],
            ["supply work", -2, False],
            ["flirting", 2, False],
            ["small talk", 2, False],
            ["sports", 2, False],
            ["the colour blue", -2, False],
            ["the colour brown", 2, True],
            ["the colour green", -2, False],
            ["the colour orange", -2, False],
            ["the colour purple", 2, True],
            ["the colour red", -2, False],
            ["working", 2, False],
            ["yoga", 2, False]
        ], forced_sexy_opinions = [
            ["taking control", 2, False],
            ["being submissive", -2, False],
            ["cheating on men", -2, False],
            ["masturbating", 2, False],
            ["creampies", 2, False],
            ["giving blowjobs", -2, False],
            ["giving handjobs", 2, False],
            ["getting head", 2, False],
            ["incest", 2, False],
            ["polyamory", 2, False],
            ["threesomes", 2, False]
        ])

    yoshitmnt.generate_home().add_person(yoshitmnt)
    yoshitmnt.home.add_person(yoshitmnt)
    yoshitmnt.add_role(yoshitmnt_role)
    yoshitmnt.home.background_name = "sewerlair"
    yoshitmnt.add_role(yoshitmnt_role)
    yoshitmnt.change_job(hr_job)
    mc.phone.register_number(yoshitmnt)
    mc.known_home_locations.append(yoshitmnt.home)
    ### April ###
    #reporter for channel 6 News - new york newstation - Burne Thompson boss, Vernon Fenwick co-worker, Irma receptionist and friend
    # Shredder, Footsoldiers, new organized crime syndicate, The Foot Clan, Technodrome (underground)
    #Splinter mutated, Mousers droids, Baxter Stockman, Krang, Titanus, Krakus
    #April -red hair - confident, courageous, benevolent, intelligent, outgoing human, upbeat, quick-witted and adventurius, go with the flow. REPORTER
    apriltmnt_wardrobe = wardrobe_from_xml("TMNTApril_Wardrobe")
    apriltmnt_base = Outfit("April Casuals") #TODO: Decide what accessories we want her to haven

    apriltmnt_personality = Personality("relaxed", relaxed_personality.default_prefix,
        common_likes = ["pants", "flirting", "conservative outfits", "makeup", "the colour red", "the color yellow", "working", "yoga"],
        common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        common_dislikes = ["skirts", "dresses", "high heels"],
        common_sexy_dislikes = ["cheating on men"],
        titles_function = tmnt_titles, possessive_titles_function = tmnt_possessive_titles, player_titles_function = tmnt_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global apriltmnt_role
    apriltmnt_role = Role("April", [], hidden = True) 

    global apriltmnt
    apriltmnt = make_person(name = "April", last_name = "O'Neil", age = 28, body_type = "thin_body", face_style = "Face_12", tits="E", height = 0.86,
        hair_colour = ["knight red", [0.48, 0.09, 0.07, 0.95]], hair_style = messy_short_hair, pubes_style = shaved_pubes, skin = "tan",
        eyes = "green", personality = apriltmnt_personality, name_color = "#E34233", dial_color = "#E34233", starting_wardrobe = apriltmnt_wardrobe, base_outfit = apriltmnt_base,
        stat_array = [5,5,7], skill_array = [2,8,4,2,2], sex_skill_array = [7,7,0,0], sluttiness = 55, obedience = 120, happiness = 120, love = 80, suggestibility=20,
        relationship = "Single", kids = 0, job = unemployed_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["classical music", -2, False],
            ["heavy metal music", 2, False],
            ["jazz", -2, False],
            ["pop music", 2, False],
            ["punk music", -2, False],
            ["hr work", 2, False],
            ["marketing work", 2, True],
            ["production work", -2, False],
            ["research work", -2, False],
            ["supply work", -2, False],
            ["flirting", 2, False],
            ["small talk", 2, False],
            ["sports", -2, False],
            ["the colour yellow", 2, True],
            ["the colour brown", -2, False],
            ["the colour green", -2, False],
            ["the colour orange", 2, True],
            ["the colour purple", -2, False],
            ["the colour red", 2, True],
            ["working", 2, False],
            ["yoga", 2, False]
        ], forced_sexy_opinions = [
            ["taking control", 1, False],
            ["being submissive", 1, False],
            ["cheating on men", -2, False],
            ["masturbating", 2, False],
            ["creampies", 2, False],
            ["giving blowjobs", 2, False],
            ["giving handjobs", 2, False],
            ["getting head", 2, False],
            ["incest", 2, False],
            ["polyamory", 2, False],
            ["threesomes", 2, False]
        ])
    yoshitmnt.home.add_person(apriltmnt)
    apriltmnt.home = yoshitmnt.home
    apriltmnt.set_schedule(apriltmnt.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 1, 2, 3, 4])
    apriltmnt.add_role(apriltmnt_role)
    apriltmnt.home.add_person(apriltmnt)
    apriltmnt.change_job(market_job)
    apriltmnt.change_job(bartender_job, is_primary = False)

    ### Donna ###
    #Donna - purple - Respinsible, organized, creator, inventor, rule follower, conservative, straight arrow - IT Support, programmer, web developer 
    #- I'm just Donnie, your friendly IT tech support...here to help you 24 hours a day, sir. [Pause] Yeah, I'm sorry. Ma'am.
    
    donnatmnt_wardrobe = wardrobe_from_xml("TMNTDonna_Wardrobe")
    donnatmnt_base = Outfit("Donna Casuals") #TODO: Decide what accessories we want her to haven

    donnatmnt_personality = Personality("relaxed", relaxed_personality.default_prefix,
        common_likes = ["pants", "flirting", "conservative outfits", "makeup", "the colour red", "the color yellow", "working", "yoga"],
        common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        common_dislikes = ["skirts", "dresses", "high heels"],
        common_sexy_dislikes = ["cheating on men"],
        titles_function = tmnt_titles, possessive_titles_function = tmnt_possessive_titles, player_titles_function = tmnt_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global donnatmnt_role
    donnatmnt_role = Role("Donna", [], hidden = True) 

    global donnatmnt
    donnatmnt = make_person(name = "Donna", last_name = "Hamato", age = Person._initial_age_floor, body_type = "thin_body", face_style = "Face_12", tits="E", height = 0.86,
        hair_colour = ["sunset purple", [0.45, 0.31, 0.59, 0.95]], hair_style = shaved_side_hair, pubes_style = shaved_pubes, skin = "tan",
        eyes = "blue", personality = donnatmnt_personality, name_color = "#692961", dial_color = "#692961", starting_wardrobe = donnatmnt_wardrobe, base_outfit = donnatmnt_base,
        stat_array = [8,7,2], skill_array = [5,3,8,8,3], sex_skill_array = [7,0,0,0], sluttiness = 45, obedience = 120, happiness = 120, love = 80, suggestibility=20,
        relationship = "Single", kids = 0, job = unemployed_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["classical music", 2, False],
            ["heavy metal music", -2, False],
            ["jazz", 2, False],
            ["pop music", -2, False],
            ["punk music", -2, False],
            ["hr work", -2, False],
            ["marketing work", 2, False],
            ["production work", 2, False],
            ["research work", 2, True],
            ["supply work", 2, False],
            ["flirting", -2, False],
            ["small talk", -2, False],
            ["sports", -2, False],
            ["the colour blue", -2, False],
            ["the colour brown", -2, False],
            ["the colour green", 2, True],
            ["the colour orange", -2, False],
            ["the colour purple", 2, True],
            ["the colour red", -2, False],
            ["working", 2, False],
            ["yoga", 2, False]
        ], forced_sexy_opinions = [
            ["taking control", -1, False],
            ["being submissive", 1, False],
            ["cheating on men", -2, False],
            ["masturbating", 2, False],
            ["creampies", 2, False],
            ["giving blowjobs", 2, False],
            ["giving handjobs", 2, False],
            ["getting head", 2, False],
            ["incest", 2, False],
            ["polyamory", 2, False],
            ["threesomes", 2, False]
        ])

    yoshitmnt.home.add_person(donnatmnt)
    donnatmnt.home = yoshitmnt.home
    donnatmnt.set_schedule(donnatmnt.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 1, 2, 3, 4])
    donnatmnt.add_role(donnatmnt_role)
    donnatmnt.home.add_person(donnatmnt)
    donnatmnt.change_job(rd_job)
    donnatmnt.change_job(stripper_job, is_primary = False)
    strip_club.add_person(donnatmnt)

    ### Racheal ###
    #Racheal - red - Bold, insensitive, rational practical, impatien, original, risk-prone, perceptive, unstructured, 
    #direct, miss the big picture, sociable, defiant, hot-headed, naturall social - Comic Book seller, antique dealer, grease monkey, 
    #Belle Motorbike, Nightwatcher crimefighter, personal trainer
    
    rachealtmnt_wardrobe = wardrobe_from_xml("TMNTRacheal_Wardrobe")
    rachealtmnt_base = Outfit("Racheal Casuals") #TODO: Decide what accessories we want her to haven

    rachealtmnt_personality = Personality("wild", wild_personality.default_prefix,
        common_likes = ["pants", "flirting", "conservative outfits", "makeup", "the colour red", "the color yellow", "working", "yoga"],
        common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        common_dislikes = ["skirts", "dresses", "high heels"],
        common_sexy_dislikes = ["cheating on men"],
        titles_function = tmnt_titles, possessive_titles_function = tmnt_possessive_titles, player_titles_function = tmnt_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global rachealtmnt_role
    rachealtmnt_role = Role("Racheal", [], hidden = True) 

    global rachealtmnt
    rachealtmnt = make_person(name = "Racheal", last_name = "Hamato", age = Person._initial_age_floor, body_type = "thin_body", face_style = "Face_12", tits="E", height = 0.86,
        hair_colour = ["sunset harvest", [0.78, 0.03, 0.08, 0.95]], hair_style = shaved_side_hair, pubes_style = shaved_pubes, skin = "tan",
        eyes = "steel blue", personality = rachealtmnt_personality, name_color = "#C70814", dial_color = "#C70814", starting_wardrobe = rachealtmnt_wardrobe, base_outfit = rachealtmnt_base,
        stat_array = [2,2,5], skill_array = [0,0,0,8,8], sex_skill_array = [7,0,0,0], sluttiness = 45, obedience = 120, happiness = 120, love = 80, suggestibility=20,
        relationship = "Single", kids = 0, job = unemployed_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["classical music", -2, False],
            ["heavy metal music", 2, False],
            ["jazz", -2, False],
            ["pop music", -2, False],
            ["punk music", 2, False],
            ["hr work", -2, False],
            ["marketing work", -2, False],
            ["production work", 2, True],
            ["research work", -2, False],
            ["supply work", 2, False],
            ["flirting", 1, False],
            ["small talk", -1, False],
            ["sports", 2, False],
            ["the colour blue", -2, False],
            ["the colour brown", -2, False],
            ["the colour green", 2, True],
            ["the colour orange", -2, False],
            ["the colour purple", -2, False],
            ["the colour red", 2, True],
            ["working", 2, False],
            ["yoga", 2, False]
        ], forced_sexy_opinions = [
            ["taking control", 2, False],
            ["being submissive", -2, False],
            ["cheating on men", -2, False],
            ["masturbating", 2, False],
            ["creampies", 2, False],
            ["giving blowjobs", -2, False],
            ["giving handjobs", -2, False],
            ["getting head", 2, False],
            ["incest", 2, False],
            ["polyamory", 2, False],
            ["threesomes", 2, False]
        ])

    yoshitmnt.home.add_person(rachealtmnt)
    rachealtmnt.home = yoshitmnt.home
    rachealtmnt.set_schedule(rachealtmnt.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 1, 2, 3, 4])
    rachealtmnt.add_role(rachealtmnt_role)
    rachealtmnt.home.add_person(rachealtmnt)
    rachealtmnt.change_job(production_job)
    rachealtmnt.change_job(stripper_job, is_primary = False)
    strip_club.add_person(rachealtmnt)

    ### Michelle ###
    #Michelle - orange - party animal, passionate, creative, agile, expressive, curious, emotional intensity, easily bored by details. 
    #PIZZA Delivery, birthday party entertainer,  "freakin' lot of cash" COWABUNGA CARLA

    michelletmnt_wardrobe = wardrobe_from_xml("TMNTMichelle_Wardrobe")
    michelletmnt_base = Outfit("Michelle Casuals") #TODO: Decide what accessories we want her to haven

    michelletmnt_personality = Personality("bimbo", bimbo_personality.default_prefix,
        common_likes = ["pants", "flirting", "conservative outfits", "makeup", "the colour red", "the color yellow", "working", "yoga"],
        common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        common_dislikes = ["skirts", "dresses", "high heels"],
        common_sexy_dislikes = ["cheating on men"],
        titles_function = tmnt_titles, possessive_titles_function = tmnt_possessive_titles, player_titles_function = tmnt_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global michelletmnt_role
    michelletmnt_role = Role("Michelle", [], hidden = True) 

    global michelletmnt
    michelletmnt = make_person(name = "Michelle", last_name = "Hamato", age = Person._initial_age_floor, body_type = "thin_body", face_style = "Face_12", tits="E", height = 0.86,
        hair_colour = ["sunset orange", [0.80, 0.33, 0.00, 0.95]], hair_style = shaved_side_hair, pubes_style = shaved_pubes, skin = "tan",
        eyes = "green", personality = michelletmnt_personality, name_color = "#FF9E00", dial_color = "#FF9E00", starting_wardrobe = michelletmnt_wardrobe, base_outfit = michelletmnt_base,
        stat_array = [2,2,8], skill_array = [5,2,2,7,8], sex_skill_array = [7,0,0,0], sluttiness = 55, obedience = 120, happiness = 120, love = 80, suggestibility=20,
        relationship = "Single", kids = 0, job = unemployed_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["classical music", 2, False],
            ["heavy metal music", 2, False],
            ["jazz", 2, False],
            ["pop music", 2, False],
            ["punk music", 2, False],
            ["hr work", -2, False],
            ["marketing work", 2, False],
            ["production work", 2, False],
            ["research work", -2, False],
            ["supply work", 2, True],
            ["flirting", 2, False],
            ["small talk", 2, False],
            ["sports", 2, False],
            ["the colour blue", -2, False],
            ["the colour brown", -2, False],
            ["the colour green", 2, True],
            ["the colour orange", 2, True],
            ["the colour purple", -2, False],
            ["the colour red", -2, False],
            ["working", 2, False],
            ["yoga", 2, False]
        ], forced_sexy_opinions = [
            ["taking control", -2, False],
            ["being submissive", 2, False],
            ["cheating on men", -2, False],
            ["masturbating", 2, False],
            ["creampies", 2, False],
            ["giving blowjobs", 2, False],
            ["giving handjobs", 2, False],
            ["getting head", 2, False],
            ["incest", 2, False],
            ["polyamory", 2, False],
            ["threesomes", 2, False]
        ])

    yoshitmnt.home.add_person(michelletmnt)
    michelletmnt.home = yoshitmnt.home
    michelletmnt.set_schedule(michelletmnt.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 1, 2, 3, 4])
    michelletmnt.add_role(michelletmnt_role)
    michelletmnt.home.add_person(michelletmnt)
    michelletmnt.change_job(supply_job)
    michelletmnt.change_job(stripper_job, is_primary = False)
    strip_club.add_person(michelletmnt)


    ### Leona ###
    #Leona - blue - Organized, want what is best for others, focused on values and visions, passionate about otherse, optimistic, 
    #forward thinking, always improving, resposible, leader, humanitarian, Catering, courier work, barista, gym teacher, martial art Tai Chi

    leonatmnt_wardrobe = wardrobe_from_xml("TMNTLeona_Wardrobe")
    leonatmnt_base = Outfit("Leona Casuals") #TODO: Decide what accessories we want her to haven

    leonatmnt_personality = Personality("alpha", alpha_personality.default_prefix,
        common_likes = ["pants", "flirting", "conservative outfits", "makeup", "the colour red", "the color yellow", "working", "yoga"],
        common_sexy_likes = ["bareback sex", "creampies", "giving blowjobs", "drinking cum", "incest", "public sex", "doggy style sex", "public sex", "not wearing underwear", "threesomes", "vaginal sex", "missionary style sex"],
        common_dislikes = ["skirts", "dresses", "high heels"],
        common_sexy_dislikes = ["cheating on men"],
        titles_function = tmnt_titles, possessive_titles_function = tmnt_possessive_titles, player_titles_function = tmnt_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global leonatmnt_role
    leonatmnt_role = Role("Leona", [], hidden = True) 

    global leonatmnt
    leonatmnt = make_person(name = "Leona", last_name = "Hamato", age = Person._initial_age_floor, body_type = "thin_body", face_style = "Face_12", tits="E", height = 0.86,
        hair_colour = ["sky blue", [0.36, 0.68, 0.93, 0.95]], hair_style = shaved_side_hair, pubes_style = shaved_pubes, skin = "tan",
        eyes = "dark blue", personality = leonatmnt_personality, name_color = "#5CADED", dial_color = "#5CADED", starting_wardrobe = leonatmnt_wardrobe, base_outfit = leonatmnt_base,
        stat_array = [2,8,3], skill_array = [5,2,2,8,5], sex_skill_array = [7,0,0,0], sluttiness = 45, obedience = 120, happiness = 120, love = 80, suggestibility=20,
        relationship = "Single", kids = 0, job = unemployed_job,
        sex_cap = 20, oral_virgin = 0, oral_first = None, oral_cum = 0, hymen = 0, vaginal_virgin = 0, vaginal_first = None, vaginal_cum = 0, anal_virgin = 0, anal_first = None, anal_cum = 0,
        work_experience = 8, type="unique",
        forced_opinions = [
            ["classical music", -2, False],
            ["heavy metal music", 2, False],
            ["jazz", -2, False],
            ["pop music", 2, False],
            ["punk music", -2, False],
            ["hr work", 2, False],
            ["marketing work", -2, False],
            ["production work", 2, True],
            ["research work", -2, False],
            ["supply work", 2, False],
            ["flirting", 2, False],
            ["small talk", 2, False],
            ["sports", 2, False],
            ["the colour blue", 2, True],
            ["the colour brown", -2, False],
            ["the colour green", 2, True],
            ["the colour orange", -2, False],
            ["the colour purple", -2, False],
            ["the colour red", -2, False],
            ["working", 2, False],
            ["yoga", 2, False]
        ], forced_sexy_opinions = [
            ["taking control", 2, False],
            ["being submissive", -2, False],
            ["cheating on men", -2, False],
            ["masturbating", 2, False],
            ["creampies", 2, False],
            ["giving blowjobs", -2, False],
            ["giving handjobs", -2, False],
            ["getting head", 2, False],
            ["incest", 2, False],
            ["polyamory", 2, False],
            ["threesomes", 2, False]
        ])

    yoshitmnt.home.add_person(leonatmnt)
    leonatmnt.home = yoshitmnt.home
    leonatmnt.set_schedule(leonatmnt.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 1, 2, 3, 4])
    leonatmnt.add_role(leonatmnt_role)
    leonatmnt.home.add_person(leonatmnt)
    leonatmnt.change_job(production_job)
    leonatmnt.change_job(stripper_job, is_primary = False)
    strip_club.add_person(leonatmnt)

    ####define relationships after
    town_relationships.update_relationship(yoshitmnt, apriltmnt, "Daughter", "Mother")
    town_relationships.update_relationship(yoshitmnt, donnatmnt, "Daughter", "Mother")
    town_relationships.update_relationship(yoshitmnt, rachealtmnt, "Daughter", "Mother")
    town_relationships.update_relationship(yoshitmnt, michelletmnt, "Daughter", "Mother")
    town_relationships.update_relationship(yoshitmnt, leonatmnt, "Daughter", "Mother")
    town_relationships.update_relationship(donnatmnt, apriltmnt, "Sister")
    town_relationships.update_relationship(apriltmnt, rachealtmnt, "Sister")
    town_relationships.update_relationship(rachealtmnt, michelletmnt, "Sister")
    town_relationships.update_relationship(michelletmnt, leonatmnt, "Sister")
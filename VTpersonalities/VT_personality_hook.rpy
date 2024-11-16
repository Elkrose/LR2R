# VT Personality Hook by Elkrose - Original created by Trist


init 901 python: # add to stack later then other mods (;ast to load)
    add_label_hijack("normal_start", "activate_VT_personality")
    #add_label_hijack("after_load", "update_generic_personality")

    config.label_overrides["wild_introduction"] = "vt_wild_introduction"
    config.label_overrides["wild_greetings"] = "vt_wild_greetings"
    config.label_overrides["wild_sex_responses_foreplay"] = "vt_wild_sex_responses_foreplay"
    config.label_overrides["wild_sex_responses_oral"] = "vt_wild_sex_responses_oral"
    config.label_overrides["wild_sex_responses_vaginal"] = "vt_wild_sex_responses_vaginal"
    config.label_overrides["wild_sex_responses_anal"] = "vt_wild_sex_responses_anal"
    config.label_overrides["wild_climax_responses_foreplay"] = "vt_wild_climax_responses_foreplay"
    config.label_overrides["wild_climax_responses_oral"] = "vt_wild_climax_responses_oral"
    config.label_overrides["wild_climax_responses_vaginal"] = "vt_wild_climax_responses_vaginal"
    config.label_overrides["wild_climax_responses_anal"] = "vt_wild_climax_responses_anal"
    config.label_overrides["wild_clothing_accept"] = "vt_wild_clothing_accept"
    config.label_overrides["wild_clothing_reject"] = "vt_wild_clothing_reject"
    config.label_overrides["wild_clothing_review"] = "vt_wild_clothing_review"
    config.label_overrides["wild_strip_reject"] = "vt_wild_strip_reject"
    config.label_overrides["wild_strip_obedience_accept"] = "vt_wild_strip_obedience_accept"
    config.label_overrides["wild_grope_body_reject"] = "vt_wild_grope_body_reject"
    config.label_overrides["wild_sex_accept"] = "vt_wild_sex_accept"
    config.label_overrides["wild_sex_obedience_accept"] = "vt_wild_sex_obedience_accept"
    config.label_overrides["wild_sex_gentle_reject"] = "vt_wild_sex_gentle_reject"
    config.label_overrides["wild_sex_angry_reject"] = "vt_wild_sex_angry_reject"
    config.label_overrides["wild_seduction_response"] = "vt_wild_seduction_response"
    config.label_overrides["wild_seduction_accept_crowded"] = "vt_wild_seduction_accept_crowded"
    config.label_overrides["wild_seduction_accept_alone"] = "vt_wild_seduction_accept_alone"
    config.label_overrides["wild_seduction_refuse"] = "vt_wild_seduction_refuse"
    config.label_overrides["wild_compliment_response"] = "vt_wild_compliment_response"
    config.label_overrides["wild_compliment_response_girlfriend"] = "vt_wild_compliment_response_girlfriend"
    config.label_overrides["wild_compliment_response_affair"] = "vt_wild_compliment_response_affair"
    config.label_overrides["wild_flirt_response"] = "vt_wild_flirt_response"
    config.label_overrides["wild_flirt_response_employee_uniform_low"] = "vt_wild_flirt_response_employee_uniform_low"
    config.label_overrides["wild_flirt_response_employee_uniform_mid"] = "vt_wild_flirt_response_employee_uniform_mid"
    config.label_overrides["wild_flirt_response_low"] = "vt_wild_flirt_response_low"
    config.label_overrides["wild_flirt_response_low1"] = "vt_wild_flirt_response_low1"
    config.label_overrides["wild_flirt_response_mid"] = "vt_wild_flirt_response_mid"
    config.label_overrides["wild_flirt_response_mid1"] = "vt_wild_flirt_response_mid1"
    config.label_overrides["wild_flirt_response_high"] = "vt_wild_flirt_response_high"
    config.label_overrides["wild_flirt_response_low_energy"] = "vt_wild_flirt_response_low_energy"
    config.label_overrides["wild_flirt_response_girlfriend"] = "vt_wild_flirt_response_girlfriend"
    config.label_overrides["wild_flirt_response_affair"] = "vt_wild_flirt_response_affair"
    config.label_overrides["wild_flirt_response_text"] = "vt_wild_flirt_response_text"
    config.label_overrides["wild_condom_demand"] = "vt_wild_condom_demand"
    config.label_overrides["wild_condom_ask"] = "vt_wild_condom_ask"
    config.label_overrides["wild_condom_bareback_ask"] = "vt_wild_condom_bareback_ask"
    config.label_overrides["wild_condom_bareback_demand"] = "vt_wild_condom_bareback_demand"
    config.label_overrides["wild_cum_face"] = "vt_wild_cum_face"
    config.label_overrides["wild_cum_mouth"] = "vt_wild_cum_mouth"
    config.label_overrides["wild_cum_pullout"] = "vt_wild_cum_pullout"
    config.label_overrides["wild_cum_condom"] = "vt_wild_cum_condom"
    config.label_overrides["wild_cum_vagina"] = "vt_wild_cum_vagina"
    config.label_overrides["wild_cum_anal"] = "vt_wild_cum_anal"
    config.label_overrides["wild_surprised_exclaim"] = "vt_wild_surprised_exclaim"
    config.label_overrides["wild_talk_busy"] = "vt_wild_talk_busy"
    config.label_overrides["wild_sex_strip"] = "vt_wild_sex_strip"
    config.label_overrides["wild_sex_watch"] = "vt_wild_sex_watch"
    config.label_overrides["wild_being_watched"] = "vt_wild_being_watched"
    config.label_overrides["wild_work_enter_greeting"] = "vt_wild_work_enter_greeting"
    config.label_overrides["wild_date_seduction"] = "vt_wild_date_seduction"
    config.label_overrides["wild_sex_end_early"] = "vt_wild_sex_end_early"
    config.label_overrides["wild_sex_take_control"] = "vt_wild_sex_take_control"
    config.label_overrides["wild_sex_beg_finish"] = "vt_wild_sex_beg_finish"
    config.label_overrides["wild_sex_review"] = "vt_wild_sex_review"
    config.label_overrides["wild_improved_serum_unlock"] = "vt_wild_improved_serum_unlock"
    config.label_overrides["wild_kissing_taboo_break"] = "vt_wild_kissing_taboo_break"
    config.label_overrides["wild_touching_body_taboo_break"] = "vt_wild_touching_body_taboo_break"
    config.label_overrides["wild_touching_penis_taboo_break"] = "vt_wild_touching_penis_taboo_break"
    config.label_overrides["wild_touching_vagina_taboo_break"] = "vt_wild_touching_vagina_taboo_break"
    config.label_overrides["wild_sucking_cock_taboo_break"] = "vt_wild_sucking_cock_taboo_break"
    config.label_overrides["wild_licking_pussy_taboo_break"] = "vt_wild_licking_pussy_taboo_break"
    config.label_overrides["wild_vaginal_sex_taboo_break"] = "vt_wild_vaginal_sex_taboo_break"
    config.label_overrides["wild_anal_sex_taboo_break"] = "vt_wild_anal_sex_taboo_break"
    config.label_overrides["wild_condomless_sex_taboo_break"] = "vt_wild_condomless_sex_taboo_break"
    config.label_overrides["wild_underwear_nudity_taboo_break"] = "vt_wild_underwear_nudity_taboo_break"
    config.label_overrides["wild_bare_tits_taboo_break"] = "vt_wild_bare_tits_taboo_break"
    config.label_overrides["wild_bare_pussy_taboo_break"] = "vt_wild_bare_pussy_taboo_break"
    config.label_overrides["wild_creampie_taboo_break"] = "vt_wild_creampie_taboo_break"
    config.label_overrides["wild_anal_creampie_taboo_break"] = "vt_wild_anal_creampie_taboo_break"
    config.label_overrides["wild_dual_penetration_taboo_break"] = "vt_wild_dual_penetration_taboo_break"
    config.label_overrides["wild_sleepover_yourplace_response"] = "vt_wild_sleepover_yourplace_response"
    config.label_overrides["wild_sleepover_herplace_response"] = "vt_wild_sleepover_herplace_response"
    config.label_overrides["wild_sleepover_yourplace_sex_start"] = "vt_wild_sleepover_yourplace_sex_start"
    config.label_overrides["wild_sleepover_herplace_sex_start"] = "vt_wild_sleepover_herplace_sex_start"
    config.label_overrides["wild_sleepover_impressed_response"] = "vt_wild_sleepover_impressed_response"
    config.label_overrides["wild_sleepover_good_response "] = "vt_wild_sleepover_good_response "
    config.label_overrides["wild_sleepover_bored_response "] = "vt_wild_sleepover_bored_response "


init 900 python:

    def create_breeder_fetish_npc():
        #add one breederfetish to the game (on start of game)
        #VT_add_breeding_fetish #Nakadashi
        person = make_person(last_name = "Nakadashi", age=renpy.random.randint(21, 35), tits="E", face_style = "Face_4", skin = "tan", 
            stat_array = [8, 4, 5], skill_array = [6,5,5,5,5], sex_skill_array = [4,0,5,0],
            sluttiness = 45, obedience = 180, suggestibility=40, relationship = "Single", kids = 0,
            hair_colour = ["platinum blonde", [.789, .746, .691, 1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = breeder_personality,
            name_color = "#2475fa", dial_color = "#1f5fca", type="unique",
            forced_opinions = [
            ["high heels", 2, False],
            ["skirts", 2, False],
            ["dresses", 2, False],
            ["flirting", 2, False],
            ["makeup", 2, False],
            ["pants", -2, False],
            ["the colour blue", 2, False],
            ["the colour purple", 2, False],
            ["yoga", 2, False]],
            forced_sexy_opinions = [
            ["bareback sex", 2, False],
            ["not wearing underwear", 2, False],
            ["public sex", 2, False],
            ["skimpy uniforms", 2, False],
            ["skimpy outfits", 2, False],
            ["showing her ass", 2, False],
            ["masturbating", 2, False],
            ["creampies", 2, False],
            ["polyamory", 2, False],
            ["threesomes", 2, False]])
        person.generate_home().add_person(person)
        person.on_birth_control = False
        VT_add_breeding_fetish(person)
        person.add_opinion("missionary style sex", 2, False)
        person.add_opinion("vaginal sex", 2, False)
        person.add_opinion("creampies", 2, False)
        person.add_opinion("being submissive", 2, False)
        person.add_opinion("bareback sex", 2, False)
        return

    def make_person_breeder(self):
        #self.sex_record["Vaginal Sex"] += 10
        #self.sex_record["Vaginal Creampies"] += 10
        #self.sex_skills["Vaginal"] += 5
        self.on_birth_control = False
        VT_add_breeding_fetish(self)
        self.add_opinion("missionary style sex", 2, False)
        self.add_opinion("vaginal sex", 2, False)
        self.add_opinion("creampies", 2, False)
        self.add_opinion("being submissive", 2, False)
        self.add_opinion("bareback sex", 2, False)
        return

    def create_anal_fetish_npc():
        #VT_add_anal_fetish()
        #koumonseikou
        person = make_person(last_name = "Koumonseikou", age=renpy.random.randint(21, 35), tits="DD", face_style = "Face_7", skin = "tan", 
            stat_array = [8, 4, 5], skill_array = [6,5,5,5,5], sex_skill_array = [4,0,0,5],
            sluttiness = 35, obedience = 180, suggestibility=40,
            hair_colour = ["dark auburn", [0.745, 0.117, 0.235, 0.95]], hair_style = twintail, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = alluring_personality,
            name_color = "#e34037", dial_color = "#c43830", type="unique",
            forced_opinions = [
            ["high heels", 2, False],
            ["skirts", 2, False],
            ["dresses", 2, False],
            ["flirting", 2, False],
            ["makeup", 2, False],
            ["pants", -2, False],
            ["the colour red", 2, False],
            ["the colour purple", 2, False],
            ["yoga", 2, False]],
            forced_sexy_opinions = [
            ["anal sex", 2, False],
            ["anal creampies", 2, False],
            ["bareback sex", 2, False],
            ["not wearing underwear", 2, False],
            ["public sex", 2, False],
            ["skimpy uniforms", 2, False],
            ["skimpy outfits", 2, False],
            ["showing her ass", 2, False],
            ["masturbating", 2, False],
            ["polyamory", 2, False],
            ["threesomes", 2, False]])
        person.generate_home().add_person(person)
        VT_add_anal_fetish(person)
        person.add_opinion("doggy style sex", 2, False)
        person.add_opinion("anal sex", 2, False)
        person.add_opinion("anal creampies", 2, False)
        person.add_opinion("being submissive", 2, False)
        person.add_opinion("bareback sex", 2, False)
        return
    
    def create_cum_fetish_npc():
        #VT_add_cum_fetish
        #Ikuwareme / Sukebe
        person = make_person(last_name = "Sukebe", age=renpy.random.randint(21, 35), tits="E", face_style = "Face_4", skin = "tan", 
            stat_array = [8, 4, 5], skill_array = [6,5,5,5,5], sex_skill_array = [4,5,0,0],
            sluttiness = 35, obedience = 180,
            hair_colour = ["platinum blonde", [.789, .746, .691, 1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = wild_personality,
            name_color = "#dfddae", dial_color = "#c0be99", type="unique",
            forced_opinions = [
            ["flirting", 2, False],
            ["makeup", 2, False],
            ["the colour yellow", 2, False],
            ["the colour white", 2, False],
            ["yoga", 2, False]],
            forced_sexy_opinions = [
            ["bareback sex", 2, False],
            ["being covered in cum", 2, False],
            ["not wearing anything", 2, False],
            ["not wearing underwear", 2, False],
            ["public sex", 2, False],
            ["skimpy uniforms", 2, False],
            ["skimpy outfits", 2, False],
            ["masturbating", 2, False],
            ["giving handjobs", 2, False],
            ["giving blowjobs", 2, False],
            ["drinking cum", 2, False],
            ["cum facials", 2, False],
            ["polyamory", 2, False],
            ["threesomes", 2, False]])
        person.generate_home().add_person(person)
        VT_add_cum_fetish(person)
        person.add_opinion("giving blowjobs", 2, False)
        person.add_opinion("drinking cum", 2, False)
        person.add_opinion("being covered in cum", 2, False)
        person.add_opinion("cum facials", 2, False)
        person.add_opinion("bareback sex", 2, False)
        return
    
    def create_exhibition_fetish_npc():
        #VT_add_exhibition_fetish
        #Kimochi -feeling/pillow
        person = make_person(last_name = "Kimochi", age=renpy.random.randint(21, 35), tits="E", face_style = "Face_4", skin = "tan", 
            stat_array = [8, 4, 5], skill_array = [6,5,5,5,5], sex_skill_array = [4,0,0,5],
            sluttiness = 35, obedience = 180, 
            hair_colour = ["platinum blonde", [.789, .746, .691, 1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = cosplay_personality,
            name_color = "#6bd265", dial_color = "#4f9b4b", type="unique",
            forced_opinions = [
            ["high heels", 2, False],
            ["skirts", 2, False],
            ["dresses", 2, False],
            ["flirting", 2, False],
            ["the colour green", 2, False],
            ["the colour brown", 2, False],
            ["yoga", 2, False]],
            forced_sexy_opinions = [
            ["not wearing anything", 2, False],
            ["not wearing underwear", 2, False],
            ["public sex", 2, False],
            ["showing her tits", 2, False],
            ["skimpy uniforms", 2, False],
            ["skimpy outfits", 2, False],
            ["showing her ass", 2, False],
            ["masturbating", 2, False],
            ["polyamory", 2, False]])
        person.generate_home().add_person(person)
        VT_add_exhibition_fetish(person)
        person.add_opinion("giving blowjobs", 2, False)
        person.add_opinion("anal sex", 2, False)
        person.add_opinion("vaginal sex", 2, False)
        person.add_opinion("public sex", 2, False)
        person.add_opinion("bareback sex", 2, False)
        return
        
    def create_creampie_fetish_npc():
        #breeding/anal fetish #Ikuwareme
        person = make_person(last_name = "Ikuwareme", age=renpy.random.randint(21, 35), tits="E", face_style = "Face_4", skin = "tan", 
            stat_array = [8, 4, 5], skill_array = [6,5,5,5,5], sex_skill_array = [4,5,5,5],
            sluttiness = 35, obedience = 180,
            hair_colour = ["platinum blonde", [.789, .746, .691, 1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = slutty_personality,
            name_color = "#9361c4", dial_color = "#734b9b", type="unique",
            forced_opinions = [
            ["high heels", 2, False],
            ["skirts", 2, False],
            ["dresses", 2, False],
            ["flirting", 2, False],
            ["makeup", 2, False],
            ["pants", -2, False],
            ["the colour blue", 2, False],
            ["the colour red", 2, False],
            ["the colour purple", 2, False]
            ],
            forced_sexy_opinions = [
            ["anal sex", 2, False],
            ["anal creampies", 2, False],
            ["bareback sex", 2, False],
            ["not wearing underwear", 2, False],
            ["public sex", 2, False],
            ["skimpy outfits", 2, False],
            ["showing her ass", 2, False],
            ["masturbating", 2, False],
            ["creampies", 2, False],
            ["vaginal sex", 2, False],
            ["polyamory", 2, False],
            ["threesomes", 2, False]
            ])
        person.generate_home().add_person(person)
        #the analist
        VT_add_anal_fetish(person)
        person.add_opinion("doggy style sex", 2, False)
        person.add_opinion("anal sex", 2, False)
        person.add_opinion("anal creampies", 2, False)
        person.add_opinion("being submissive", 2, False)
        person.add_opinion("bareback sex", 2, False)
        #the vaginalist
        person.on_birth_control = False
        VT_add_breeding_fetish(person)
        person.add_opinion("missionary style sex", 2, False)
        person.add_opinion("vaginal sex", 2, False)
        person.add_opinion("creampies", 2, False)
        person.add_opinion("being submissive", 2, False)
        person.add_opinion("bareback sex", 2, False)
        return
        
    def create_golden_lotus_npc():
        #she has it all mate... a true pokemon #Yariman/Warugaki
        person = make_person(last_name = "Warugaki", age=renpy.random.randint(21, 35), tits="E", face_style = "Face_4", skin = "tan", 
            stat_array = [8, 7, 7], skill_array = [7,7,7,7,7], sex_skill_array = [7,7,7,7],
            sluttiness = 75, suggestibility=50,
            hair_colour = ["orange haze", [1, 0.42, 0.0, 1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = pornstar_personality,
            name_color = "#fae42b", dial_color = "#dcc928", type="unique",
            forced_opinions = [
            ["high heels", 2, False],
            ["skirts", 2, False],
            ["dresses", 2, False],
            ["flirting", 2, False],
            ["makeup", 2, False],
            ["pants", -2, False],
            ["the colour red", 2, False],
            ["the colour purple", 2, False],
            ["working", 2, False],
            ["yoga", 2, False]],
            forced_sexy_opinions = [
            ["polyamory", 2, False],
            ["threesomes", 2, False]])
        person.generate_home().add_person(person)
        #the analist
        VT_add_anal_fetish(person)
        person.add_opinion("doggy style sex", 2, False)
        person.add_opinion("anal sex", 2, False)
        person.add_opinion("anal creampies", 2, False)
        #the vaginalist
        person.on_birth_control = False
        VT_add_breeding_fetish(person)
        person.add_opinion("missionary style sex", 2, False)
        person.add_opinion("vaginal sex", 2, False)
        person.add_opinion("creampies", 2, False)
        person.add_opinion("being submissive", 2, False)
        person.add_opinion("bareback sex", 2, False)
        #the cummalist
        VT_add_cum_fetish(person)
        person.add_opinion("giving blowjobs", 2, False)
        person.add_opinion("drinking cum", 2, False)
        person.add_opinion("being covered in cum", 2, False)
        person.add_opinion("cum facials", 2, False)
        #the skinlist
        VT_add_exhibition_fetish(person)
        person.add_opinion("not wearing anything", 2, False)
        person.add_opinion("not wearing underwear", 2, False)
        person.add_opinion("showing her tits", 2, False)
        person.add_opinion("public sex", 2, False)
        person.add_opinion("showing her ass", 2, False)
        person.add_opinion("skimpy uniforms", 2, False)
        person.add_opinion("skimpy outfits", 2, False)
        return
    
    #### THE Personalities ####
    def create_dandere_npc():
        # add one dandere to the game (on start of game)
        # based on Shouko Komi from Komi Can't Communicate
        person = make_person(name = "Shouko", last_name = "Komi", age=renpy.random.randint(Person.get_age_floor(), 21), tits="E", face_style = "Face_4", skin = "white", 
            stat_array = [8, 4, 5], skill_array = [6,5,10,5,5], sex_skill_array = [4,0,0,0], body_type = "thin_body", height = 0.978,
            sluttiness = 25, obedience = 180, happiness = 200, love = 10, suggestibility=10, relationship = "Single", kids = 0,
            hair_colour = ["purple black", [0.0, 0.0, 0.06, 0.9]], hair_style = long_hair, eyes = ["dark purple", [0.0, 0.0, 0.15, 0.9]], personality = dandere_personality,
            name_color = "#8200ae", dial_color = "#9f00ae", type="unique",
            forced_opinions = [
            ["the colour purple", 2, False],
            ["the colour white", 2, False],
            ["research work", 2, False],
            ["working", 2, False]
            ],
            forced_sexy_opinions = [
            ["bareback sex", 2, False]
            ])
        person.generate_home().add_person(person)
        person.on_birth_control = False
        VT_add_breeding_fetish(person)
        person.add_opinion("doggy style sex", 2, False)
        person.add_opinion("anal sex", 2, False)
        person.add_opinion("creampies", 2, False)
        person.add_opinion("being submissive", 2, False)
        person.add_opinion("bareback sex", 2, False)
        person.change_job(student_job)

        return

    def create_goudere_npc():
        # add one goudere to the game (on start of game)
        # based on Albedo from Overlord
        person = make_person(name = "Albedo", last_name = "Smaragdina", age=renpy.random.randint(19, 25), tits="E", face_style = "Face_4", skin = "white", 
            stat_array = [10, 10, 10], skill_array = [20,5,5,5,5], sex_skill_array = [4,0,0,0], relationship = "Single", kids = 0,
            sluttiness = 65, obedience = 200, happiness = 200, love = 10, suggestibility=20,  body_type = "curvy_body", height = 1.002,
            hair_colour = ["raven black", [0.0, 0.0, 0.0, 1]], hair_style = long_hair, eyes = ["golden", [0.95, 0.95, 0.20, 0.9]], personality = goudere_personality,
            name_color = "#fae42b", dial_color = "#dcc928", type="unique",
            forced_opinions = [
            ["the colour black", 2, False],
            ["the colour white", 2, False],
            ["hr work", 2, False],
            ["heavy metal music", 2, False],
            ["working", 2, False]
            ],
            forced_sexy_opinions = [
            ["bareback sex", 2, False]
            ])
        person.generate_home().add_person(person)
        person.on_birth_control = False
        VT_add_breeding_fetish(person)
        person.add_opinion("doggy style sex", 2, False)
        person.add_opinion("anal sex", 2, False)
        person.add_opinion("creampies", 2, False)
        person.add_opinion("being submissive", 2, False)
        person.add_opinion("bareback sex", 2, False)
        return

    def create_kuudere_npc():
        # add one kuudere to the game (on start of game)Reina Aharen
        person = make_person(name = "Reina", last_name = "Aharen", age=renpy.random.randint(Person.get_age_floor(), 18), tits="B", face_style = "Face_4", skin = "white", 
            stat_array = [5, 7, 5], skill_array = [5,5,5,5,5], sex_skill_array = [4,0,0,0], relationship = "Single", kids = 0,
            body_type = "thin_body", height = 0.817,
            hair_colour = ["silver", [0.92, 1.00, 1.00, 0.9]], hair_style = long_hair, eyes = ["deep blue", [0.00, 0.17, 0.56, 0.9]], personality = kuudere_personality,
            name_color = "#a2a7ae", dial_color = "#b0b4ba", type="unique",
            forced_opinions = [
            ["the colour purple", 2, False],
            ["working", 2, False]
            ],
            forced_sexy_opinions = [
            ["bareback sex", 2, False]
            ])
        person.generate_home().add_person(person)
        person.on_birth_control = False
        person.add_opinion("doggy style sex", 2, False)
        person.add_opinion("anal sex", 2, False)
        person.add_opinion("creampies", 2, False)
        person.add_opinion("being submissive", 2, False)
        person.add_opinion("bareback sex", 2, False)
        return person
# update all the following the_person and actions with tsundere personality. Remember the_person is female, and mc.name is male. Use Asuka Langley from Neon Genesis Evangelion for ideas, keep to the structure and don't use the same dialogs:```
    def create_tsundere_npc():
        # add one tsundere to the game (on start of game) Asuka Langley from Neon Genesis Evangelion 
        person = make_person(name = "Asuka", last_name = "Langley", age=renpy.random.randint(19, 28), tits="B", face_style = "Face_9", skin = "white", 
            stat_array = [7, 8, 7], skill_array = [5,5,5,5,5], sex_skill_array = [4,0,0,0], relationship = "Single", kids = 0,
            sluttiness = 20, obedience = 180, happiness = 200, body_type = "standard_body", height = 0.922,
            hair_colour = ["orange haze", [1, 0.42, 0.0, 1]], hair_style = twintail, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = tsundere_personality,
            name_color = "#fae42b", dial_color = "#dcc928", type="unique",
            forced_opinions = [
            ["the colour red", 2, False],
            ["the colour orange", 2, False],
            ["the colour yellow", 2, False],
            ["working", 2, False]
            ],
            forced_sexy_opinions = [
            ["bareback sex", 2, False]
            ])
        person.generate_home().add_person(person)
        person.on_birth_control = False
        person.add_opinion("doggy style sex", 2, False)
        person.add_opinion("anal sex", 2, False)
        person.add_opinion("creampies", 2, False)
        person.add_opinion("being submissive", 2, False)
        person.add_opinion("bareback sex", 2, False)
        return person

# update all the following the_person and actions with yandere personality. Remember the_person is female, and mc.name is male. Use Yuno Gasai from Future Diary for ideas, keep to the structure and don't use the same dialogs:```
    def create_yandere_npc():
        # add one tsundere to the game (on start of game) Yuno Gasai from Future Diary
        person = make_person(name = "Yuno", last_name = "Gasai", age=renpy.random.randint(Person.get_age_floor(), 25), tits="B", face_style = "Face_4", skin = "white", 
            stat_array = [7, 10, 6], skill_array = [2,7,5,5,5], sex_skill_array = [4,0,0,0], relationship = "Single", kids = 0,
            sluttiness = 75, obedience = 180, happiness = 200, love = 15, suggestibility=80, body_type = "thin_body", height = 0.95,
            hair_colour = ["cotton candy", [1, 0.66, 0.81, 0.9]], hair_style = long_hair, eyes = ["cotton candy", [1, 0.66, 0.81, 0.9]], personality = yandere_personality,
            name_color = "#f394da", dial_color = "#f8c2ea", type="unique",
            forced_opinions = [
            ["the colour pink", 2, False],
            ["working", 2, False]
            ],
            forced_sexy_opinions = [
            ["bareback sex", 2, False]
            ])
        person.generate_home().add_person(person)
        person.on_birth_control = False
        person.add_opinion("doggy style sex", 2)
        person.add_opinion("anal sex", 2)
        person.add_opinion("creampies", 2)
        person.add_opinion("being submissive", 2)
        person.add_opinion("bareback sex", 2)
        return person

    def create_gothic_npc():
        person = make_person(name = "Calantha", last_name = "Cairnwall", age=renpy.random.randint(19, 25), tits="D", face_style = "Face_4", skin = "white", 
            stat_array = [10, 10, 10], skill_array = [5,5,10,5,5], relationship = "Single", kids = 0,
            sluttiness = 35, suggestibility=20, body_type = "thin_body", height = 0.87,
            hair_colour = ["raven black", [0.0, 0.0, 0.0, 1]], hair_style = long_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = gothic_personality,
            name_color = "#6A0DAD", dial_color = "#A44CE6", type="unique", 
            forced_opinions = [
            ["the colour black", 2, False],
            ["the colour purple", 2, False],
            ["hr work", 2, False],
            ["heavy metal music", 2, False],
            ["working", -2, False]
            ],
            forced_sexy_opinions = [
            ["bareback sex", 2, False],
            ["taking control", 2, False]
            ])
        person.generate_home().add_person(person)
        person.add_opinion("public sex", 2, False)
        person.add_opinion("anal sex", 2, False)
        person.add_opinion("being submissive", -2, False)
        return

    def create_tomboy_npc():
        person = make_person(last_name = "Rowan", age=renpy.random.randint(19, 25), tits="AA", face_style = "Face_4", skin = "tan", 
            stat_array = [7, 7, 7], skill_array = [5,5,5,10,5], relationship = "Single", kids = 0,
            body_type = "thin_body", height = 0.87,
            hair_colour = ["raven black", [0.0, 0.0, 0.0, 1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = tomboy_personality,
            name_color = "#7E7E2A", dial_color = "#B5B238", type="unique",
            forced_opinions = [
            ["the colour black", 2, False],
            ["the colour blue", 2, False],
            ["production work", 2, False],
            ["heavy metal music", 2, False],
            ["working", -2, False]
            ],
            forced_sexy_opinions = [
            ["getting head", 2, False],
            ["taking control", 2, False]
            ])
        person.generate_home().add_person(person)
        person.add_opinion("anal sex", 2, False)
        person.add_opinion("being submissive", -2, False)
        return

    def create_foodie_npc():
        person = make_person(name="Colette", last_name = "Fournier", age=renpy.random.randint(19, 29), tits="FF", face_style = "Face_9", skin = "tan", 
            stat_array = [7, 7, 7], skill_array = [7,5,10,5,5], 
            body_type = "curvy_body", height = 1.27,
            hair_colour = ["raven black", [0.0, 0.0, 0.0, 1]], hair_style = long_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = foodie_personality,
            name_color = "#7E7E2A", dial_color = "#B5B238", type="unique",
            forced_opinions = [
            ["the colour purple", 2, False],
            ["the colour red", 2, False],
            ["research work", 2, False],
            ["classical music", 2, False],
            ["working", -2, False]
            ],
            forced_sexy_opinions = [
            ["taking control", 2, False]
            ])
        person.generate_home().add_person(person)
        person.add_opinion("getting head", 2, False)
        person.add_opinion("being submissive", -2, False)
        return

label activate_VT_personality(stack):
    python:
        
        #create random personalities
        create_dandere_npc()
        create_goudere_npc()
        create_kuudere_npc()
        create_tsundere_npc()
        create_yandere_npc()
        create_gothic_npc()
        create_tomboy_npc()
        create_foodie_npc()
        #for i in builtins.range(2):
        create_anal_fetish_npc()
        create_cum_fetish_npc()
        create_creampie_fetish_npc()
        create_exhibition_fetish_npc()
        create_golden_lotus_npc()
        create_breeder_fetish_npc()
        # add two random hookers to the game (on start of game)
        for i in builtins.range(3):
            create_hooker()

        update_main_character_actions()

        generate_random_mothers_and_daughters()

        generate_random_sisters_cousins_nieces()

        generate_random_sisters()

        generate_random_studying_daughters()

        create_old_hooker_with_daughter()

        # final routine to create initial party schedules and set special personalities
        update_characters()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
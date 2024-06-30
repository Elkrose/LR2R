#Counter VT01

#tweaked start
define config.name = _("Lab Rats 2 Reformuate - Cherries Edition")
define config.window_icon = "VTimages/mod_icon.png"

init -1 python:
    gui.main_menu_background = Image(get_file_handle("VTimages/background_images/LR2_Title.png"))
    gui.game_menu_background = Image(get_file_handle("VTimages/background_images/LR2_Title.png"))

init 5 python:
    config.label_overrides["start"] = "improved_start"

label improved_start():
    scene bg paper_menu_background with fade
    "Lab Rats 2 contains adult content. If you are not over 18 or your country's equivalent age you should not view this content."
    menu:
        "I am over 18":
            "Excellent, let's continue then."

        "I am not over 18":
            $renpy.full_restart()

    "[config.version] represents an early iteration of Lab Rats 2. Expect to run into limited content, unexplained features, and unbalanced game mechanics."

    "Lab Rats 2 contains content related to impregnation and pregnancy. These settings may be changed in the menu at any time."
    menu:
        "No pregnancy content\n{size=16}Girls never become pregnant. Most pregnancy content hidden.{/size}":
            $ persistent.pregnancy_pref = 0

        "Predictable pregnancy content\n{size=16}Birth control is 100%% effective. Girls always default to taking birth control.{/size}":
            $ persistent.pregnancy_pref = 1

        "Semi-Realistic pregnancy content\n{size=16}Birth control is not 100%% effective. Girls may not be taking birth control.{/size}":
            $ persistent.pregnancy_pref = 2

        "Realistic pregnancy content\n{size=16}Realistic cycles. Girls know their fertile times. Pulling out not 100%% effective. Girls don't want to get pregnant.{/size}":
            $ persistent.pregnancy_pref = 3

    "How quickly would you like stories from the game to play out? This will affect spacing between story events."
    menu:
        "Quick":
            $ update_game_speed(0)
        "Standard":
            $ update_game_speed(1)
        "Epic":
            $ update_game_speed(2)
        "Marathon":
            $ update_game_speed(3)

    $ easy_mode = False
    $ kina_mode = False
    $ cherry_mode = False
    "Choose a Game Mode..."
    menu:
        "Default Game Play":
            pass
        "Higher Max Stats for MC":
            "Default gameplay but higher max ceiling for MC. And unlocked theoretical research policy at start."
            $ kina_mode = True
        "Easier Game Play":
            "All options for making the game easier will be applied after character creation."
            $ easy_mode = True
        "Super Cheat":
            "Easier Game Play + Higher Max Stats for MC. All options for making the game easier will be applied after character creation."
            $ kina_mode = True
            $ easy_mode = True
        "Easy Cherries":
            "Easy Cherries! Easy Mode + Higher Stats, everything set to just have fun"
            $ cherry_mode = True

    "Finally, the game uses random generated characters, the mod offers you the ability to control the random generation."
    "We will now open that screen for you, so you can set it to your preferences."

    call screen generic_preference_ui()
    call screen VTMOD_setup_ui()

    "That's all, the game will now initialize, this might take a moment."

    $ renpy.block_rollback()
    if persistent.stats:
        $ name = persistent.stats['name']
        $ l_name = persistent.stats['l_name']
        $ b_name = persistent.stats['b_name']
    call screen character_create_screen()
    $ return_arrays = _return #These are the stat, skill, and sex arrays returned from the character creator.
    $ setattr(persistent, "stats", {})
    $ [[persistent.stats["cha"],persistent.stats["int"],persistent.stats["foc"]], [persistent.stats["h_skill"],persistent.stats["m_skill"],persistent.stats["r_skill"],persistent.stats["p_skill"],persistent.stats["s_skill"]], [persistent.stats["F_skill"],persistent.stats["O_skill"],persistent.stats["V_skill"],persistent.stats["A_skill"]]] = _return
    $ [persistent.stats["name"],persistent.stats["l_name"],persistent.stats["b_name"]] = [store.name,store.l_name,store.b_name]


    python:
        renpy.show("Loading", layer = "solo", at_list = [truecenter], what = Image(get_file_handle("VTimages/background_images/creating_world.png")))
        renpy.pause(0.5)
        renpy.game.interface.timeout(30)
        if easy_mode:
            for array in range(0, builtins.len(return_arrays)):
                for val in range(0, builtins.len(return_arrays[array])):
                    return_arrays[array][val] += 2

    call initialize_game_state(store.name,store.b_name,store.l_name,return_arrays[0],return_arrays[1],return_arrays[2]) from _call_initialize_game_state_VT01

    python:
        if easy_mode:
            # increased business stats
            mc.business.funds = 500000
            mc.business.funds_yesterday = 10000
            mc.business.supply_count = 1000
            mc.business.supply_goal = 10000
            mc.business.effectiveness_cap = 110
            mc.business.marketability = 100
            mc.business.max_employee_count = 12
            # increased player stats
            mc.energy = 500
            mc.max_energy = 500
            mc.free_clarity += 10500
            mc.clarity_multiplier = 3.0     # gain clarity 3 times faster
            # default unlock policies
            purchase_policy(mandatory_paid_serum_testing_policy, ignore_cost = True)
            purchase_policy(serum_size_1_policy, ignore_cost = True)
            purchase_policy(recruitment_batch_one_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_one_policy, ignore_cost = True)
            purchase_policy(recruitment_skill_improvement_policy, ignore_cost = True)
            purchase_policy(business_size_1_policy, ignore_cost = True)
            purchase_policy(theoretical_research, ignore_cost = True)
            purchase_policy(max_attention_increase_1_policy, ignore_cost = True)

        #KiNA Mode
        if kina_mode:
            mc.max_stats = 10
            mc.max_work_skills = 10
            mc.max_sex_skills = 10
            mc.max_energy_cap = 300
            mc.business.supply_goal = 1000
            purchase_policy(theoretical_research, ignore_cost = True)

        #Cherry Mode
        if cherry_mode:
            # increased business stats
            mc.business.funds = 500000
            mc.business.funds_yesterday = 10000
            mc.business.supply_count = 1000
            mc.business.supply_goal = 10000
            mc.business.effectiveness_cap = 110
            mc.business.marketability = 100
            mc.business.max_employee_count = 12
            # increased player stats
            mc.charisma +=4
            mc.int +=4
            mc.focus +=4
            mc.hr_skill +=4
            mc.market_skill +=4
            mc.research_skill +=4
            mc.production_skill +=4
            mc.supply_skill +=4
            mc.sex_skills["Foreplay"] +=4
            mc.sex_skills["Oral"] +=4
            mc.sex_skills["Anal"] +=4
            mc.sex_skills["Vaginal"] +=4
            mc.max_stats = 15
            mc.max_work_skills = 15
            mc.max_sex_skills = 15
            mc.max_energy_cap = 600
            mc.business.supply_goal += 1000
            mc.energy = 500
            mc.max_energy = 500
            mc.free_clarity += 10500
            mc.clarity_multiplier = 3.0     # gain clarity 3 times faster
            # default unlock policies

            #========= Clothing Policies=============================
            purchase_policy(strict_uniform_policy, ignore_cost = True)
            purchase_policy(relaxed_uniform_policy, ignore_cost = True)
            purchase_policy(casual_uniform_policy, ignore_cost = True)
            purchase_policy(reduced_coverage_uniform_policy, ignore_cost = True)
            purchase_policy(minimal_coverage_uniform_policy, ignore_cost = True)
            purchase_policy(corporate_enforced_nudity_policy, ignore_cost = True)
            purchase_policy(maximal_arousal_uniform_policy, ignore_cost = True)
            #mandatory_vibe_policy,
            #mandatory_bullet_policy,
            #mandatory_plug_policy,
            purchase_policy(male_focused_marketing_policy, ignore_cost = True)
            #creative_colored_uniform_policy,
            #personal_bottoms_uniform_policy,
            purchase_policy(casual_friday_uniform_policy, ignore_cost = True)
            #creative_skimpy_uniform_policy,
            purchase_policy(dress_code_policy, ignore_cost = True)
            #easier_access_policy,
            purchase_policy(commando_uniform_policy, ignore_cost = True)

            #========= Organization Policies=============================
            purchase_policy(business_size_1_policy, ignore_cost = True)
            purchase_policy(business_size_2_policy, ignore_cost = True)
            purchase_policy(business_size_3_policy, ignore_cost = True)
            #business_size_4_policy,
            purchase_policy(business_contract_increase_1_policy, ignore_cost = True)
            purchase_policy(business_contract_offer_increase_1_policy, ignore_cost = True)
            purchase_policy(business_contract_increase_2_policy, ignore_cost = True)
            purchase_policy(business_contract_offer_increase_2_policy, ignore_cost = True)
            purchase_policy(public_advertising_license_policy, ignore_cost = True)
            #office_punishment,
            #corporal_punishment,
            #strict_enforcement,
            #draconian_enforcement,
            #bureaucratic_nightmare,
            purchase_policy(theoretical_research, ignore_cost = True)
            purchase_policy(research_journal_subscription, ignore_cost = True)
            purchase_policy(practical_experimentation, ignore_cost = True)
            #office_conduct_guidelines,
            #mandatory_staff_reading,
            #superliminal_office_messaging,
            #max_attention_increase_1_policy,
            #attention_bleed_increase_1_policy,
            #attention_floor_increase_1_policy,

            #======== Recruitment Policies===================================
            purchase_policy(recruitment_batch_one_policy, ignore_cost = True)
            purchase_policy(recruitment_batch_two_policy, ignore_cost = True)
            #recruitment_batch_three_policy,
            purchase_policy(recruitment_knowledge_one_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_two_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_three_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_four_policy, ignore_cost = True)
            purchase_policy(recruitment_skill_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_skill_minimums_policy, ignore_cost = True)
            purchase_policy(recruitment_stat_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_stat_minimums_policy, ignore_cost = True)
            purchase_policy(recruitment_suggest_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_obedience_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_slut_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_sex_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_sex_minimums_policy, ignore_cost = True)
            #recruitment_small_tits_policy,
            #recruitment_tiny_tits_policy,
            #recruitment_big_tits_policy,
            #recruitment_huge_tits_policy,
            #recruitment_short_policy,
            #recruitment_tall_policy,
            #recruitment_single_policy,
            #recruitment_married_policy,
            purchase_policy(recruitment_teen_policy, ignore_cost = True)
            #recruitment_old_policy,
            #recruitment_mothers_policy,
            #recruitment_childless_policy,

            #======= Serum/Production Policies==========================
            purchase_policy(mandatory_paid_serum_testing_policy, ignore_cost = True)
            purchase_policy(mandatory_unpaid_serum_testing_policy, ignore_cost = True)
            #daily_serum_dosage_policy,
            #weekend_serum_dosage_policy,
            purchase_policy(serum_size_1_policy, ignore_cost = True)
            purchase_policy(serum_size_2_policy, ignore_cost = True)
            purchase_policy(serum_size_3_policy, ignore_cost = True)
            purchase_policy(serum_production_1_policy, ignore_cost = True)
            purchase_policy(serum_production_2_policy, ignore_cost = True)
            purchase_policy(serum_production_3_policy, ignore_cost = True)
            purchase_policy(production_line_addition_1_policy, ignore_cost = True)
            purchase_policy(production_line_addition_2_policy, ignore_cost = True)
            purchase_policy(breast_milking_space_policy, ignore_cost = True)
            purchase_policy(auto_pumping_stations_policy, ignore_cost = True)
            purchase_policy(high_suction_pumping_machinery_policy, ignore_cost = True)

        renpy.hide("Loading", layer = "solo")


    $ renpy.block_rollback()
    menu:
        "Play introduction and tutorial":
            call tutorial_start from _call_tutorial_start_VT01

        "Skip introduction and tutorial":
            $ mc.business.event_triggers_dict["Tutorial_Section"] = False
    jump normal_start
# Counter VT01
# Tweaked start
define config.name = _("Lab Rats 2 Reformulate - Cherries Edition")
define config.window_icon = "VTimages/mod_icon.png"
define VT_Game_Version = "VTMod4.0.12"

init python:
    config.version += VT_Game_Version
    
    # Define your lists
    VTvaginalknowlist = [
        "Want to be inside her pussy?",
        "Would you like to have vaginal sex with her?",
        "Want to penetrate her vagina?",
        "Her warm pussy around your cock?",
        "Want to make love to her with your cock in her pussy?",
        "Take care of her pussy needs with your body?",
        "Wonder how good her pussy feels?",
        "Feel her tight vagina around your cock?",
        "Want to thrust into her pussy?",
        "Get intimate with her vagina?",
        "Want to fill her pussy up?",
        "Have her ride your cock with her vagina?",
        "Want to be deep inside her vagina?",
        "Feel her vaginal wetness on your cock?",
        "Want to make her cum with your cock in her pussy?",
        "Take control of her vagina?",
        "Want to be one with her through vaginal sex?",
        "Feel her vaginal muscles squeeze your cock?",
        "Want to pound into her pussy?",
        "Have her take your cock in her vagina?",
        "Want to ravage her pussy?"]
    VTvaginalvirginlist = [
        "Her body is untouched and innocent.",
        "She's never had a man inside her.",
        "Her vagina is pure and unclaimed.",
        "That body has never known pleasure.",
        "She's a virgin, waiting to be explored.",
        "Her vagina is a treasure, untouched and unspoiled.",
        "She's never been with a man before.",
        "Her body is a blank canvas, waiting for you.",
        "Those curves are ripe for the taking.",
        "Her innocence is waiting to be claimed."]
    VTvaginalclaimlist = [
        "This pussy is yours now.",
        "You own this vagina.",
        "This vagina belongs to you.",
        "Taken possession of my body.",
        "I'm yours to take, to fill.",
        "My vagina is your territory.",
        "You've marked this vagina as yours.",
        "This vagina is your property.",
        "You claimed this kitty!"]
    VTvaginalclaimfirstlist = [
        "Someone else had her before you, now make her yours.",
        "She's not a virgin, but claim her body as your own.",
        "Others have been inside her, but take possession now.",
        "She's been with others, but make her vagina yours alone.",
        "Someone else got there first, but claim her as your territory.",
        "Her body has been explored before, but take control now.",
        "She's been with others, but make her your property.",
        "Someone else had the first time, but make the last one count.",
        "Her vagina has a past, but claim it for your future.",
        "Others have had her, but make her yours now."]
    VToralknowlist = [
        "Want those lips on your cock?",
        "Would you like to have oral sex?",
        "Want her to blow you?",
        "Her tongue on the underside of your cock?",
        "Want her to suck you off?",
        "Take care of you with her mouth?",
        "Wonder how good she is playing the skin flute?",
        "Feel her warm breath on your cock?",
        "Want her to deepthroat you?",
        "Get a blowjob from her?",
        "Have her swallow your cum?",
        "Want her to lick your balls?",
        "Feel her tongue on your shaft?",
        "Want her to give you a handjob with her mouth?",
        "Get head from her?",
        "Want her to suck your cock dry?",
        "Feel her lips wrapped around your cock?",
        "Want her to take care of your hard-on?",
        "Have her give you a sloppy blowjob?",
        "Want her to make you cum with her mouth?"]
    VToralvirginlist = [
        "Her lips look sweet and inexperienced.",
        "Those lips have never been kissed.",
        "Her mouth is untouched and innocent.",
        "She's never had a man's lips on hers.",
        "Her lips are pure and unclaimed.",
        "That mouth has never known pleasure.",
        "Her lips are a blank canvas, waiting for you.",
        "She's a kissing virgin, waiting to be explored.",
        "Those lips are ripe for the taking.",
        "Her mouth is a treasure, untouched and unspoiled."]
    VToralclaimlist = [
        "This mouth is yours now.",
        "You own this mouth.",
        "This mouth belongs to you.",
        "Taken possession of my mouth.",
        "I'm yours to kiss, to taste.",
        "My mouth is your territory.",
        "You've marked this mouth as yours.",
        "This mouth is your property.",
        "You Claimed this Pie Hole!"]
    VToralclaimfirstlist = [
        "Someone else tasted her lips first, now make them yours.",
        "She's been kissed before, but claim her mouth as your own.",
        "Others have had her lips, but take possession now.",
        "She's not new to kissing, but make her lips yours alone.",
        "Someone else got there first, but claim her mouth as your territory.",
        "Her lips have been kissed before, but take control now.",
        "She's been with others, but make her mouth your property.",
        "Someone else had the first kiss, but make the last one count.",
        "Her lips have a past, but claim them for your future.",
        "Others have tasted her, but make her yours now."]
    VTanalknowlist = [
        "Want to be inside her from behind?",
        "Would you like to have anal sex with her?",
        "Want to penetrate her anus?",
        "Want to explore her backside?",
        "Her ass around your cock?",
        "Want to make love to her anally?",
        "Take care of her needs with your body from behind?",
        "Wonder how good she is at anal?",
        "Feel her tight anus around your cock?",
        "Want to thrust into her from behind?",
        "Get intimate with her ass?",
        "Want to fill her anus up?",
        "Have her take it from behind?",
        "Want to be deep inside her ass?",
        "Feel her anal muscles squeeze your cock?",
        "Want to pound into her from behind?",
        "Take control of her ass?",
        "Want to ravage her anus?",
        "Have her submit to anal sex?",
        "Want to own her ass?",
        "Feel her ass cheeks on your thighs?",
        "Want to make her cum from anal sex?"]
    VTanalfirstlist = [
        "Her ass is untouched and innocent.",
        "She's never had a man inside her from behind.",
        "Her anus is pure and unclaimed.",
        "That body has never known anal pleasure.",
        "She's an anal virgin, waiting to be explored.",
        "Her anus is a treasure, untouched and unspoiled.",
        "She's never been with a man in that way before.",
        "Her body is a blank canvas, waiting for you to explore.",
        "Those curves are ripe for the taking from behind.",
        "Her innocence is waiting to be claimed in a new way."]
    VTanalclaimlist = [
        "This booty is yours now.",
        "You own this anus.",
        "This anus belongs to you.",
        "Taken possession of her booty.",
        "She's yours to take, to claim from behind.",
        "Her anus is your territory.",
        "You've marked this anus as yours.",
        "This anus is your property.",
        "You claimed this booty!"]
    VTanalclaimfirstlist = [
        "Someone else had her before you, now make her yours.",
        "She's not an anal virgin, but claim her body as your own.",
        "Others have been inside her from behind, but take possession now.",
        "She's been with others in that way, but make her anus yours alone.",
        "Someone else got there first, but claim her booty as your territory.",
        "Her body has been explored before, but take control now in a new way.",
        "She's been with others, but make her booty your property.",
        "Someone else had the first time, but make this one matter.",
        "Her anus has a past, but claim it for your future.",
        "Make it... UR, ANUS... badda.. bum.. kisss.."]
    condom_words = [
        "bare", "naked", "exposed", "uncovered", "unsheathed", "raw", "unprotected", "condom-free", "bareback", "unwrapped", "unshielded", "unbridled", "unrestrained", "wild", "free"]
    condom_on_words = [
        "sheathed", "covered", "protected", "wrapped", "condom-clad", "rubber-wrapped", "shielded", "armored", "guarded", "safe", "secured", "suited up", "strapped up", "geared up", "locked and loaded", "protected and served"]
    pussy_words = [
        "pussy", "cunt", "vulva", "muff", "box", "kitty", "snatch", "slit", "sex", "center", "folds", "secret paradise", "hidden pleasure", "erotic zone", "sensitive flesh", "intimate playground", "luscious lips", "velvet softness", "vagina", "twat", "love canal", "honeypot", "sweet surrender", "tender temptation", "feminine fire", "passionate portal", "sensual sanctuary"]
    anal_words = [
        "anus", "ass", "asshole", "bum", "butt", "backdoor", "rear", "rectum", "anal cavity", "anal orifice", "rosebud", "pucker", "tight hole", "small entrance", "secret passage", "hidden treasure", "hot ass", "tight anus", "wet dark hole", "eager pucker", "hungry hole", "inviting backdoor", "tempting rear", "seductive slit", "erotic entrance", "passionate portal", "sensual sphincter", "luscious loophole", "fiery fissure", "blazing backdoor", "burning bum", "bowels"]
    mouth_words = [
        "mouth", "lips", "kissers", "orifice", "oral cavity", "luscious lips", "sinful smile", "hot mouth", "wet lips", "inviting orifice", "erotic entrance", "sensual slit", "passionate portal", "juicy lips", " succulent mouth",  "fiery lips", "blazing mouth", "tasty lips", "sweet mouth", "voluptuous lips", "sultry mouth", "erotic lips", "intimate orifice", "sensual mouth", "passionate lips", "ardent mouth", "hungry lips", "eager mouth", "lustful lips", "desirous mouth"]
    cock_words = [
        "penis", "cock", "dick", "prick", "shaft", "rod", "stick", "member", "organ", "phallus", "manhood", "erection", "hard-on", "boner", "passion stick", "throbbing dick", "pulsating prick", "rigid shaft", "steely rod", "hot stick", "swollen member", "erotic engine", "sensual sword", "fiery phallus", "blazing rod", "burning cock", "ardent erection", "lustful member", "passionate penis", "seductive shaft", "tantalizing tool"]
    # Initialize indices
    VTvaginalknow_index = 0
    VTvaginalvirgin_index = 0
    VTvaginalclaim_index = 0
    VTvaginalclaimfirst_index = 0
    VToralknow_index = 0
    VToralvirgin_index = 0
    VToralclaim_index = 0
    VToralclaimfirst_index = 0
    VTanalknow_index = 0
    VTanalfirst_index = 0
    VTanalclaim_index = 0
    VTanalclaimfirst_index = 0
    condom_words_index = 0
    condom_on_words_index = 0
    pussy_words_index = 0
    anal_words_index = 0
    mouth_words_index = 0
    cock_words_index = 0
    # Function to get the next random item from a list
    def VT_get_next_random_item(index, list_name):
        item = list_name[index]
        index = (index + 1) % len(list_name)  # Wrap around to the start of the list
        return item, index

    # Function to shuffle lists and update text variables
    def VT_shuffle_and_update():
        global VTvaginalknowlist
        global VTvaginalvirginlist
        global VTvaginalclaimlist
        global VTvaginalclaimfirstlist
        global VToralknowlist
        global VToralvirginlist
        global VToralclaimlist
        global VToralclaimfirstlist
        global VTanalknowlist
        global VTanalfirstlist
        global VTanalclaimlist
        global VTanalclaimfirstlist
        global condom_words
        global condom_on_words
        global pussy_words
        global anal_words
        global mouth_words
        global cock_words

        renpy.random.shuffle(VTvaginalknowlist)
        renpy.random.shuffle(VTvaginalvirginlist)
        renpy.random.shuffle(VTvaginalclaimlist)
        renpy.random.shuffle(VTvaginalclaimfirstlist)
        renpy.random.shuffle(VToralknowlist)
        renpy.random.shuffle(VToralvirginlist)
        renpy.random.shuffle(VToralclaimlist)
        renpy.random.shuffle(VToralclaimfirstlist)
        renpy.random.shuffle(VTanalknowlist)
        renpy.random.shuffle(VTanalfirstlist)
        renpy.random.shuffle(VTanalclaimlist)
        renpy.random.shuffle(VTanalclaimfirstlist)
        renpy.random.shuffle(condom_words)
        renpy.random.shuffle(condom_on_words)
        renpy.random.shuffle(pussy_words)
        renpy.random.shuffle(anal_words)
        renpy.random.shuffle(mouth_words)
        renpy.random.shuffle(cock_words)

        # Update text variables
        global VTvaginalknow_index
        global VTvaginalvirgin_index
        global VTvaginalclaim_index
        global VTvaginalclaimfirst_index
        global VToralknow_index
        global VToralvirgin_index
        global VToralclaim_index
        global VToralclaimfirst_index
        global VTanalknow_index
        global VTanalfirst_index
        global VTanalclaim_index
        global VTanalclaimfirst_index
        global condom_words_index
        global condom_on_words_index
        global pussy_words_index
        global anal_words_index
        global mouth_words_index
        global cock_words_index

        VTvaginalknowtext, VTvaginalknow_index = VT_get_next_random_item(VTvaginalknow_index, VTvaginalknowlist)
        VTvaginalvirgintext, VTvaginalvirgin_index = VT_get_next_random_item(VTvaginalvirgin_index, VTvaginalvirginlist)
        VTvaginalclaimtext, VTvaginalclaim_index = VT_get_next_random_item(VTvaginalclaim_index, VTvaginalclaimlist)
        VTvaginalclaimfirsttext, VTvaginalclaimfirst_index = VT_get_next_random_item(VTvaginalclaimfirst_index, VTvaginalclaimfirstlist)
        VToralknowtext, VToralknow_index = VT_get_next_random_item(VToralknow_index, VToralknowlist)
        VToralvirgintext, VToralvirgin_index = VT_get_next_random_item(VToralvirgin_index, VToralvirginlist)
        VToralclaimtext, VToralclaim_index = VT_get_next_random_item(VToralclaim_index, VToralclaimlist)
        VToralclaimfirsttext, VToralclaimfirst_index = VT_get_next_random_item(VToralclaimfirst_index, VToralclaimfirstlist)
        VTanalknowtext, VTanalknow_index = VT_get_next_random_item(VTanalknow_index, VTanalknowlist)
        VTanalfirsttext, VTanalfirst_index = VT_get_next_random_item(VTanalfirst_index, VTanalfirstlist)
        VTanalclaimtext, VTanalclaim_index = VT_get_next_random_item(VTanalclaim_index, VTanalclaimlist)
        VTanalclaimfirsttext, VTanalclaimfirst_index = VT_get_next_random_item(VTanalclaimfirst_index, VTanalclaimfirstlist)
        random_condom_word, condom_words_index = VT_get_next_random_item(condom_words_index, condom_words)
        random_condom_word, condom_on_words_index = VT_get_next_random_item(condom_on_words_index, condom_on_words)
        random_pussy_word, pussy_words_index = VT_get_next_random_item(pussy_words_index, pussy_words)
        random_anal_word, anal_words_index = VT_get_next_random_item(anal_words_index, anal_words)
        random_mouth_word, mouth_words_index = VT_get_next_random_item(mouth_words_index, mouth_words)
        random_cock_word, cock_words_index = VT_get_next_random_item(cock_words_index, cock_words)

    # Call the function after it is defined
    VT_shuffle_and_update()

init -1 python:
    gui.main_menu_background = Image(get_file_handle("VTimages/background_images/LR2_Title.png"))
    gui.game_menu_background = Image(get_file_handle("VTimages/background_images/LR2_Title.png"))

    def Moresomes_enabled():
        try:
            return renpy.has_label("bedroom_orgy_label")
        except NameError:
            return False

    def RealPorn_enabled():
        try:
            return renpy.has_label("describe_girl_climax_RP")
        except NameError:
            return False

    def KiNA_enabled():
        try:
            return KiNA_MOD is not None
        except NameError:
            return False

    def vt_enabled():
        try:
            return VT_MOD
        except NameError:
            return False

    def Kaden_enabled():
        try:
            return kaden_mod is not None
        except NameError:
            return False

    def ZenPak_enabled():
        try:
            return noncest_version
        except NameError:
            return False 

    def kina_update_game_speed(speed):
        global GAME_SPEED, TIER_1_TIME_DELAY, TIER_2_TIME_DELAY, TIER_3_TIME_DELAY

        GAME_SPEED = speed
        if speed == 0:
            #TIER_0_TIME_DELAY = -1
            TIER_1_TIME_DELAY = 1
            TIER_2_TIME_DELAY = 3
            TIER_3_TIME_DELAY = 5
        elif speed == 1:
            #TIER_0_TIME_DELAY = 1
            TIER_1_TIME_DELAY = 3
            TIER_2_TIME_DELAY = 7
            TIER_3_TIME_DELAY = 10
        elif speed == 2:
            #TIER_0_TIME_DELAY = 1
            TIER_1_TIME_DELAY = 5
            TIER_2_TIME_DELAY = 11
            TIER_3_TIME_DELAY = 15
        elif speed ==3:
            #TIER_0_TIME_DELAY = 2
            TIER_1_TIME_DELAY = 7
            TIER_2_TIME_DELAY = 15
            TIER_3_TIME_DELAY = 20
        else:
            GAME_SPEED = 3
            #TIER_0_TIME_DELAY = -1
            TIER_1_TIME_DELAY = 1
            TIER_2_TIME_DELAY = 3
            TIER_3_TIME_DELAY = 5

        return



init 15 python:
    config.label_overrides["start"] = "VT_start"

label VT_start():
    scene bg paper_menu_background with fade
    "Lab Rats 2 contains adult content. If you are not over 18 or your country's equivalent age you should not view this content."
    menu:
        "I am over 18":
            "Excellent, let's continue then."

        "I am not over 18":
            $renpy.full_restart()

    "[config.version] represents an early iteration of Lab Rats 2. Expect to run into limited content, unexplained features, and unbalanced game mechanics."

    $ modsinstalled = []

    if vt_enabled():
        $ modsinstalled.append("VT Mod")
    if KiNA_enabled():
        $ modsinstalled.append("KiNA Mod")
    if Kaden_enabled():
        $ modsinstalled.append("Kaden Mod")
    if ZenPak_enabled():
        $ modsinstalled.append("ZenPak Mod")
    if RealPorn_enabled():
        $ modsinstalled.append("RealPorn Mod")
    if Moresomes_enabled():
        $ modsinstalled.append("Moresomes Mod")

    if modsinstalled == []:
        "No mods are installed."
    else:
        $ mod_message = "🍒The following mods are installed: \n " + ", ".join(modsinstalled)
        "[mod_message]"

    "Lab Rats 2 contains content related to impregnation and pregnancy. These settings may be changed in the menu at any time."

    menu:
        "No pregnancy content\n{size=16}Girls never become pregnant. Most pregnancy content hidden.{/size}":
            $ persistent.pregnancy_pref = 0

        "Predictable pregnancy content\n{size=16}Birth control is 100%% effective. Girls always default to taking birth control.{/size}":
            $ persistent.pregnancy_pref = 1

        "Semi-Realistic pregnancy content\n{size=16}Birth control is not 100%% effective. Girls may not be taking birth control.{/size}":
            $ persistent.pregnancy_pref = 2

        "🍒Realistic🍒 pregnancy content\n{size=16}Realistic cycles. Girls know their fertile times. Pulling out not 100%% effective. Girls don't want to get pregnant.{/size}":
            $ persistent.pregnancy_pref = 3

    "How quickly would you like stories from the game to play out? This will affect spacing between story events."
    menu:
        "Quick":
            $ kina_update_game_speed(0)
        "Standard":
            $ kina_update_game_speed(1)
        "Epic":
            $ kina_update_game_speed(2)
        "Marathon":
            $ kina_update_game_speed(3)
        "KiNA Mode (Quick but Reduced Interaction)":
            $ kina_update_game_speed(4)

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
        "🍒Easy Cherries🍒":
            "Easy Cherries! Easy Mode + Higher Stats, everything set to just have fun."
            $ cherry_mode = True

    "Finally, the game uses random generated characters, the mod offers you the ability to control the random generation."
    "We will now open that screen for you, so you can set it to your preferences."

    call screen generic_preference_ui()
    call screen VTMOD_setup_ui()

    $ starting_hires = False
    "Do you want to start the game employing just the head researcher? Or would you like to hire someone for each department?"
    menu:
        "Just Head Researcher":
            pass
        "Hire for Each Department":
            $ starting_hires = True

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
            mc.business.funds = 10000
            mc.business.funds_yesterday = 10000
            mc.business.supply_count = 1000
            mc.business.supply_goal = 1000
            mc.business.base_effectiveness_cap  = 110
            mc.business.marketability = 100
            # increased player stats
            mc.max_energy = 120
            mc.free_clarity += 500
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

        if starting_hires:
            market_hire = create_random_person()
            hr_hire = create_random_person()
            prod_hire = create_random_person()
            supply_hire = create_random_person()

            market_hire.market_skill = 4
            market_hire.charisma = 4
            market_hire.focus = 1
            market_hire.int = 1
            market_hire.hr_skill = 1
            market_hire.research_skill = 1
            market_hire.production_skill = 1
            market_hire.supply_skill = 1
            market_hire.set_opinion("marketing work", 2, False)
            market_hire.generate_home().add_person(market_hire)

            hr_hire.market_skill = 1
            hr_hire.charisma = 4
            hr_hire.focus = 1
            hr_hire.int = 1
            hr_hire.hr_skill = 4
            hr_hire.research_skill = 1
            hr_hire.production_skill = 1
            hr_hire.supply_skill = 1
            hr_hire.set_opinion("hr work", 2, False)
            hr_hire.generate_home().add_person(hr_hire)

            prod_hire.market_skill = 1
            prod_hire.charisma = 1
            prod_hire.focus = 4
            prod_hire.int = 1
            prod_hire.hr_skill = 1
            prod_hire.research_skill = 1
            prod_hire.production_skill = 4
            prod_hire.supply_skill = 1
            prod_hire.set_opinion("production work", 2, False)
            prod_hire.generate_home().add_person(prod_hire)

            supply_hire.market_skill = 1
            supply_hire.charisma = 1
            supply_hire.focus = 4
            supply_hire.int = 1
            supply_hire.hr_skill = 1
            supply_hire.research_skill = 1
            supply_hire.production_skill = 1
            supply_hire.supply_skill = 4
            supply_hire.set_opinion("supply work", 2, False)
            supply_hire.generate_home().add_person(supply_hire)

            mc.business.add_employee_marketing(market_hire)
            mc.business.add_employee_hr(hr_hire)
            mc.business.add_employee_production(prod_hire)
            mc.business.add_employee_supply(supply_hire)

        #KiNA Mode
        if kina_mode:
            mc.max_stats = 10
            mc.max_work_skills = 10
            mc.max_sex_skills = 10
            mc.max_energy_cap = 300
            mc.business.supply_count = 500
            mc.business.supply_goal = 1000
            purchase_policy(theoretical_research, ignore_cost = True)

        #Cherry Mode
        if cherry_mode:
            # increased business stats
            mc.business.funds = 500000
            mc.business.funds_yesterday = 10000
            mc.business.supply_count = 1000
            mc.business.supply_goal = 10000
            mc.business.base_effectiveness_cap  = 110
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
            mc.max_stats = 20
            mc.max_work_skills = 20
            mc.max_sex_skills = 20
            mc.max_energy_cap = 1000
            mc.business.supply_goal += 1000
            mc.energy = 500
            mc.max_energy = 600
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
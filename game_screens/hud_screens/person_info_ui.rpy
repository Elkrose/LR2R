# Override default person_info_ui screen by VREN to show extra information about character

init 900 python in vt_store:
    DEBUG = True

init -2 python:
    @renpy.pure
    def person_info_ui_format_hearts(value):
        heart_value = builtins.abs(value)
        if (heart_value / 4) > 10:
            return get_hearts(heart_value / 4, color = "gold")
        return get_hearts(heart_value)

    def person_info_ui_get_formatted_tooltip(person):
        tooltip = []
        for situation in person.situational_sluttiness:
            ss = person.situational_sluttiness[situation]
            tooltip.append(f"{get_coloured_arrow(ss[0])} {person_info_ui_format_hearts(ss[0])} - {ss[1]}\n")
        return "".join(tooltip)

    def person_info_ui_get_formatted_obedience_tooltip(person):
        tooltip = []
        for situation in person.situational_obedience:
            so = person.situational_obedience[situation]
            tooltip.append(f"{get_coloured_arrow(so[0])} {('+' if so[0] > 0 else '')}{so[0]} Obedience - {so[1]}\n")
        return "".join(tooltip)

    def person_info_ui_get_serum_info_tooltip(person):
        tooltips = []
        for serum in person.serum_effects:
            tooltips.append(f"{serum.name}: {serum.total_duration - serum.duration_counter} Turns Left\n")
        return "\n".join(tooltips)

    def person_info_ui_get_special_role_information(person):
        info_list = []
        fetish_roles = [anal_fetish_role, cum_fetish_role, breeding_fetish_role, exhibition_fetish_role, vaginal_fetish_role]
        for role in [x for x in person.special_role if not x.hidden and x not in fetish_roles]:
            info_list.append(role.role_name)

        active_fetishes = []
        if anal_fetish_role in person.special_role and person.known_opinion("anal sex"):
            active_fetishes.append("Anal")
        if cum_fetish_role in person.special_role and (person.known_opinion("anal creampies") or person.known_opinion("creampies") or person.known_opinion("being covered in cum")):
            active_fetishes.append("Cum")
        if breeding_fetish_role in person.special_role and person.known_opinion("creampies") and person.known_opinion("vaginal sex"):
            active_fetishes.append("Breeding")
        if exhibition_fetish_role in person.special_role and person.known_opinion("public sex"):
            active_fetishes.append("Exhibition")
        if vaginal_fetish_role in person.special_role and person.known_opinion("vaginal sex"):
            active_fetishes.append("Vaginal")

        return (sorted(info_list), active_fetishes)

    def person_info_ui_get_job_title(person):
        title = "Unknown"
        if person.primary_job.job_known:
            title = person.primary_job.job_title
        extra_jobs = []
        if person.side_job and person.side_job.job_known:
            extra_jobs.append(person.side_job.job_title)
        if person.secondary_job and person.secondary_job.job_known:
            extra_jobs.append(person.secondary_job.job_title)
        if extra_jobs:
            return f"{title} {{size=14}}[{', '.join(extra_jobs)}]{{/size}}"
        return title

    def person_info_ui_get_label_tag(person, label_name = "Love", tag_name = "Love"):
        if person.active_serum_with_hidden_tag(tag_name):
            if tag_name == "Love":
                return f"{{color=#b14343}}{label_name}{{/color}}"
            if tag_name == "Obedience":
                return f"{{color=#bf94e4}}{label_name}{{/color}}"
            if tag_name == "Slut":
                return f"{{color=#d0d010}}{label_name}{{/color}}"
            if tag_name == "Energy":
                return f"{{color=#43B197}}{label_name}{{/color}}"
            return f"{{color=#d0d010}}{label_name}{{/color}}"
        return label_name

screen person_info_ui(person): #Used to display stats for a person while you're talking to them.
    tag master_tooltip
    layer "solo" #By making this layer active it is cleared whenever we draw a person or clear them off the screen.
    zorder 200

    default home_hub_name = person.home_hub.formal_name
    default height_info = height_to_string(person.height)
    default weight_info = get_person_weight_string(person)

    $ vt_store.sexualized = 'position_choice' in globals() and hasattr(position_choice, 'skill_tag')

    python:
        love_label = person_info_ui_get_label_tag(person, "Love", "Love")
        obedience_label = person_info_ui_get_label_tag(person, "Obedience", "Obedience")
        slut_label = person_info_ui_get_label_tag(person, "Sluttiness", "Slut")
        suggest_label = person_info_ui_get_label_tag(person, "Suggestibility", "Suggest")
        energy_label = person_info_ui_get_label_tag(person, "Energy", "Energy")
        job_title = person_info_ui_get_job_title(person)
        arousal_info = get_arousal_with_token_string(person.arousal, person.max_arousal)
        energy_info = get_energy_string(person.energy, person.max_energy)
        happiness_info = str(builtins.int(person.happiness))
        love_info = get_love_hearts(person.love, 5)
        sluttiness_info = get_heart_image_list(person.sluttiness, person.effective_sluttiness())
        obedience_info = f"{person.obedience} {{image=triskelion_token_small}} {get_obedience_string(person.obedience)}"
        (role_list, fetish_list) = person_info_ui_get_special_role_information(person)
        fetish_info = ", ".join(fetish_list)

    frame:
        background Transform("topboxVT", alpha=persistent.hud_alpha)
        xsize 1100
        ysize 200
        yalign 0.0
        xalign 0.5
        xanchor 0.5
        padding (5, 5)
        hbox:
            xanchor 0.5
            xalign 0.5
            yalign 0.1
            spacing 40
            vbox:
                xmaximum 340
                xminimum 340

                hbox:
                    text format_titles(person) style "menu_text_style" size 30
                    use favourite_toggle_button(person)

                text "Job: [job_title]" style "menu_text_style" xoffset 20

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    xsize 260
                    ysize 100
                    vbox:
                        xmaximum 250
                        if len(fetish_list) > 0:
                            text "- Fetishes: [fetish_info]" style "menu_text_style" size 12 xoffset 20

                        for role in role_list:
                            text "- [role]" style "menu_text_style" size 12 xoffset 20

            vbox:
                yoffset 5
                xmaximum 280
                xminimum 280

                textbutton "Arousal: [arousal_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip f"When a girl is brought to 100% arousal she will start to climax. Climaxing will make a girl happier and may put them into a Trance if their suggestibility is higher than 0.\nCurrently: {get_arousal_number_string(person.arousal, person.max_arousal)}"
                    action NullAction()

                textbutton "[energy_label]: [energy_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip f"Energy is spent while having sex, with more energy spent on positions that give the man more pleasure. Some energy comes back each turn, and a lot of energy comes back overnight.\nCurrently {get_energy_number_string(person.energy, person.max_energy)}"
                    action NullAction()

                textbutton "Happiness: [happiness_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "The happier a girl the more tolerant she will be of low pay and unpleasant interactions. High or low happiness will return to it's default value over time."
                    action NullAction()

                textbutton "[love_label]: [love_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip f"Girls who love you will be more willing to have sex when you're in private (as long as they aren't family) and be more devoted to you. Girls who hate you will have a lower effective sluttiness regardless of the situation.\nWhen a girl is not part of your harem, she will slowly lose love until it reaches 80, having sex once every five days will stop the love bleed.\nLove: {get_attention_number_string(person.love, 100)}"
                    action NullAction()

                hbox:
                    textbutton "[obedience_label]: [obedience_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip f"Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, low obedience girls are likely to refuse altogether.\nActive modifiers will be shown under {{image=question_mark_small}}.\nDominant girls will bleed 1 obedience a day and any other girl that is not a slave will bleed one obedience per day to 200."
                        action NullAction()

                    if bool(person.situational_obedience):
                        textbutton "{image=question_mark_small}":
                            style "transparent_style"
                            tooltip person_info_ui_get_formatted_obedience_tooltip(person)
                            action NullAction()

                hbox:
                    textbutton "[slut_label]: [sluttiness_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip f"The higher a girls sluttiness the more slutty actions she will consider acceptable and normal. Temporary sluttiness ({{image=red_heart_token_small}}) is added to her sluttiness based on arousal, active modifiers will be shown under {{image=question_mark_small}}.\nSluttiness: {get_attention_number_string(person.effective_sluttiness(), 100)}"
                        action NullAction()

                    if bool(person.situational_sluttiness):
                        textbutton "{image=question_mark_small}":
                            style "transparent_style"
                            tooltip person_info_ui_get_formatted_tooltip(person)
                            action NullAction()

            vbox:
                yoffset 5
                xmaximum 200
                xminimum 200

                textbutton f"{suggest_label}: {min(100,person.suggestibility)}%":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "How likely a girl is to slip into a trance when she cums. While in a trance she will be highly suggestible, and you will be able to directly influence her stats, skills, and opinions."
                    action NullAction()

                textbutton "Age: [person.age]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "The age of the girl."
                    action NullAction()

                textbutton "Height: [height_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    if persistent.use_imperial_system:
                        tooltip "The length of the girl in feet and inches."
                    else:
                        tooltip "The length of the girl in centimetres."
                    action NullAction()

                textbutton "Cup size: [person.tits]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "The size of the breasts."
                    action NullAction()

                textbutton "Weight: [weight_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "The weight of the girl in {weight_system}.\nDetermines the body type."
                    action NullAction()

                textbutton f"Novelty: {person.novelty:.0f}%":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Higher novelty score gives more clarity during orgasms, whe she makes you cum novelty decreases, breaking taboos increases novelty."
                    action NullAction()

        imagebutton:
            pos (50, 5)
            idle "gui/extra_images/information.png"
            action Show("person_info_detailed", None, person)
            tooltip f"Detailed Information for {person.fname}"

        if person.has_story:
            imagebutton:
                pos (10, 5)
                idle "labbook"
                focus_mask True
                action [
                    Show("story_progress", None, person)
                ]
                tooltip f"Story Progress for {person.fname}"

        if person.mc_knows_address or person.home == harem_mansion:
            imagebutton:
                pos (1020, 5)
                idle "home_marker"
                tooltip f"She lives in {home_hub_name}."
                action NullAction()

        if person.can_clone:
            imagebutton:
                pos (1060, 5)
                idle "dna_sequence"
                tooltip "This person can be cloned."
                action NullAction()

        if person.is_free_use:
            imagebutton:
                pos (1020, 50)
                if person.has_role(employee_freeuse_role):
                    idle "doggy_style_marker"
                    tooltip "She is the company free-use slut and can be used anytime."
                else:
                    idle "stocking_marker"
                    tooltip "She is a free-use slut, who loves sex."
                action NullAction()

        if person.serum_tolerance == 0:
            imagebutton:
                pos (55, 50)
                idle "serum_vial3"
                tooltip "Warning: this person has no tolerance for serums\n" + person_info_ui_get_serum_info_tooltip(person)
                action NullAction()
        elif person.serum_effects:
            imagebutton:
                pos (55, 50)
                idle ("serum_vial3" if person.active_serum_count > person.serum_tolerance
                else "serum_vial2" if person.active_serum_count == person.serum_tolerance
                else "serum_vial")
                tooltip person_info_ui_get_serum_info_tooltip(person)
                action NullAction()

        if person.knows_pregnant:
            imagebutton:
                pos(10, 50)
                idle "feeding_bottle"
                action NullAction()

        if person.bc_status_known and person.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception"):
            imagebutton:
                pos(10, 50)
                idle "beezee"
                action NullAction()
                tooltip f"{{image=beezee_token_small}} She is ovulating and has a higher chance of getting pregnant, based on birth control and desire to get pregnant."

    ##### VT Starts from Here on
        $ random_condom_word = ""
        if mc.condom == False:
            $ random_condom_word = VT_get_next_random_item(condom_words_index, condom_words)[0]
        else:
            $ random_condom_word = VT_get_next_random_item(condom_on_words_index, condom_on_words)[0]
        $ random_pussy_word = VT_get_next_random_item(pussy_words_index, pussy_words)[0]
        $ random_anal_word = VT_get_next_random_item(anal_words_index, anal_words)[0]
        $ random_mouth_word = VT_get_next_random_item(mouth_words_index, mouth_words)[0]
        $ random_cock_word = VT_get_next_random_item(cock_words_index, cock_words)[0]
        $ dayslastsex = 0
        $ daysince = ""
        $ VTbuzz = ""

        if person.has_event_day("last_insemination"):
            $ days_since_insemination = person.days_since_event("last_insemination")
            if days_since_insemination < 4 and days_since_insemination > 1:
                $ dayslastsex = 4 - days_since_insemination
                $ daysince = f"\nYour sperm in me for {dayslastsex} more day{'s' if dayslastsex > 1 else ''}!\n{'Such warm butterflies!' if dayslastsex > 1 else 'My womb feels empty!'}"

        # if person.has_event_day("last_insemination") and person.days_since_event("last_insemination") < 4:
            # if person.days_since_event("last_insemination") > 1:
                # $ dayslastsex = 4 - person.days_since_event("last_insemination") 
                # if dayslastsex == 1:
                    # $ daysince = "\nMy womb feels empty!"
                # else:
                    # $ daysince = "\nYour sperm in me for "+str(dayslastsex)+" more days!\n Such warm butterflies!"
        $VTorifice_current = "None"
    #### VT HUD UI ####
        if getattr(persistent, "HUDVT")==1:
    #### Relationship Status
            if getattr(persistent, "relationship")==1:
                $ VTrelationshipst = "norelations"
                $ VTrelationshiptt = f"{{image=dontknow_token_small}} Has no romantic relations with you."
                $ VTrelationshipStatusTT = f"\n\n Total in Polycule: "+str(mc.stats.polycules)+f"\n{{image=harem_token_small}} Poly: "+ str(mc.stats.polycule_girlfriends) +f" {{image=parapoly_token_small}} Parapoly: "+ str(mc.stats.polycule_paramours) +f" {{image=familypoly_small}} Polyfamilia: "+ str(mc.stats.polycule_familia) +f"\n\n Total Girlfriends: "+str(mc.stats.girlfriends)+f"\n{{image=gf_token_small}} Girlfriends: "+ str(mc.stats.girlfriends_sansfamilia) + f" {{image=paramour_token_small}} Paramours: "+ str(mc.stats.paramours) + f" {{image=familylove_small}} Familia: "+ str(mc.stats.familia) +f"\n\nTotal Slaves: "+str(mc.stats.slaves)+f"\n{{image=slave_small}} Slaves: "+ str(mc.stats.slaves_norel)+f" {{image=gfslave_small}} Girlfriends: "+ str(mc.stats.slaves_girlfriends)+f" {{image=paraslave_small}} Paramours: "+ str(mc.stats.slaves_paramour)+f" {{image=familiaslave_small}} Familia: "+ str(mc.stats.slaves_familia)+f" {{image=gffamiliaslave_small}} Girlfriend: "+ str(mc.stats.slaves_gffamilia)+f" {{image=polyfamiliaslave_small}} Polycule: "+ str(mc.stats.slaves_polyfamilia)

                if person.has_relation_with_mc:
                    if person.is_slave:
                        if person.has_role(harem_role):
                            if person.has_role(affair_role):
                                $ VTrelationshipst = "parapolyslave"
                                $ VTrelationshiptt = f"{{image=parapolyslave_small}} She is your slave, part of your polycule, and your paramour."
                            else:
                                if person.is_family:
                                    $ VTrelationshipst = "polyfamiliaslave"
                                    $ VTrelationshiptt = f"{{image=polyfamiliaslave_small}} She is "+person.relation_possessive_title+",\n slave, and part of your polycule."
                                else:
                                    $ VTrelationshipst = "polyslave"
                                    $ VTrelationshiptt = f"{{image=polyslave_small}} She is your slave and part of your polycule."
                        else:
                            if person.has_role(affair_role):
                                $ VTrelationshipst = "paraslave"
                                $ VTrelationshiptt = f"{{image=paraslave_small}} She is your slave and paramour."
                            else:
                                if person.is_family:
                                    $ VTrelationshipst = "gffamiliaslave"
                                    $ VTrelationshiptt = f"{{image=gffamiliaslave_small}} She is "+person.relation_possessive_title+",\nand your slave."
                                else:
                                    $ VTrelationshipst = "gfslave"
                                    $ VTrelationshiptt = f"{{image=gfslave_small}} She is your girlfriend and your slave."
                    else:
                        if person.has_role(harem_role):
                            if person.has_role(affair_role):
                                $ VTrelationshipst = "parapoly"
                                $ VTrelationshiptt = f"{{image=parapoly_token_small}} She is part of your polycule, and your paramour."
                            else:
                                if person.is_family:
                                    $ VTrelationshipst = "familypoly"
                                    $ VTrelationshiptt = f"{{image=familypoly_small}} She is "+person.relation_possessive_title+",\nand part of your polycule."
                                else:
                                    $ VTrelationshipst = "polyamorous"
                                    $ VTrelationshiptt = f"{{image=harem_token_small}} She is part of your polycule."
                        else:
                            if person.has_role(affair_role):
                                $ VTrelationshipst = "paramour"
                                $ VTrelationshiptt = f"{{image=paramour_token_small}} She is your paramour."
                            else:
                                if person.is_family:
                                    $ VTrelationshipst = "familylove"
                                    $ VTrelationshiptt = f"{{image=familylove_small}} She is "+person.relation_possessive_title+",\nand your girlfriend."
                                else:
                                    $ VTrelationshipst = "girlfriend"
                                    $ VTrelationshiptt = f"{{image=gf_token_small}} She is your girlfriend."
                    imagebutton:
                        pos(249, 166)
                        idle VTrelationshipst
                        action NullAction()
                        tooltip VTrelationshiptt+VTrelationshipStatusTT
                else:
                    if person.is_family:
                        if person.is_slave:
                            $ VTrelationshipst = "familiaslave"
                            $ VTrelationshiptt = f"{{image=familiaslave_small}} She is "+person.relation_possessive_title+", and your slave."
                        else:
                            $ VTrelationshipst = "familycircle"
                            $ VTrelationshiptt = f"{{image=familycircle_small}} She is "+person.relation_possessive_title+"."
                    else:
                        if person.is_slave:
                            $ VTrelationshipst = "slave"
                            $ VTrelationshiptt = f"{{image=slave_small}} She is your slave."
                        else:
                            $ VTrelationshipst = "norelations"
                            $ VTrelationshiptt = f"{{image=dontknow_token_small}} Has no romantic relations with you."
                if person.love >=80 and not person.has_role(harem_role):
                    if person.is_girlfriend or person.has_role(affair_role):
                        $ VTrelationshiptt += f"\n{{image=red_heart_token_small}} She is ready to be part of your polycule!"
                    else:
                        $ VTrelationshiptt += f"\n{{image=progress_token_small}} Need to make her your girlfriend first!"
                elif person.love < 80 and person.love >= 60 and not person.has_role(harem_role) and (person.has_role(affair_role) or person.is_girlfriend):
                    if person.love <=80 and (person.has_role(affair_role) or person.is_girlfriend):
                        $ VTrelationshiptt += f"\n{{image=progress_token_small}} {80 - person.love} more {{image=red_heart_token_small}} to add her to your polycule!"
                    else:
                        $ VTrelationshiptt += f"\n{{image=question_mark_small}} Want her to be your girlfriend?"
                        if not person.relationship == "Single":
                            if person.opinion.cheating_on_men < 2:
                                $ VTrelationshiptt += f"\n{{image=progress_token_small}} Needs to like cheating."
                        else:
                            $ VTrelationshiptt += f"\n{{image=red_heart_token_small}} Ask her to be your girlfriend!"
                elif person.love <= 60  and not (person.is_affair or person.is_girlfriend):
                        $ VTrelationshiptt += f"\n{{image=question_mark_small}} Want her to be your girlfriend?"
                        if person.love == 60:
                            $ VTrelationshiptt += f"\n{{image=red_heart_token_small}} Ask her to be your girlfriend!"
                        else:
                            $ VTrelationshiptt += f"\n{{image=progress_token_small}} {60 - person.love} more to make her your girlfriend!"
                if not person.relationship == "Single" and not person.has_role(harem_role):
                    if person.opinion.cheating_on_men < 2:
                        $ VTrelationshiptt += f"\n{{image=progress_token_small}} Needs to like cheating."
                if person.opinion.polyamory < 2 and not person.has_role(harem_role):
                    $ VTrelationshiptt += f"\n{{image=progress_token_small}} Needs to like polyamory."
                if person.opinion.threesomes < 2 and not person.has_role(harem_role):
                    $ VTrelationshiptt += f"\n{{image=progress_token_small}} Needs to like threesomes."
                
                imagebutton:
                    pos(249, 166)
                    idle VTrelationshipst
                    action NullAction()
                    tooltip VTrelationshiptt+VTrelationshipStatusTT
    ### Age 
            if getattr(persistent, "passionage")==1:
                $ VTagest = "knowpeach"
                $ VTagett = "Talk to her to get a glimpse of her age."
                if person.age<=19:
                    $ VTagest = "whitelotus"
                    $ VTagett = f"{{image=whitelotus_small}} The White Lotus: Young, pure and growth."
                    if person.hymen <= 1 and person.vaginal_virgin <=1:
                        $ VTagett += f"\n{{image=virgin_token_small}} She looks so young, innocent and inexperienced."
                    else:
                        $ VTagett += f"\n{{image=vtcherries_small}} She looks like a young vixen."
                if person.age >19 and person.age <=29:
                    $ VTagest = "pinklotus"
                    $ VTagett = f"{{image=pinklotus_small}} The Pink Lotus: Feminine energy and passion."
                    if person.hymen <= 1 and person.vaginal_virgin <=1:
                        $ VTagett += f"\n{{image=virgin_token_small}} She looks sexually inexperienced."
                    else:
                        $ VTagett += f"\n{{image=vtcherries_small}} She is in her prime sexual peak."
                if person.age >29 and person.age <=35:
                    $ VTagest = "redlotus"
                    $ VTagett = f"{{image=redlotus_small}} The Red Lotus: Passion, inspiration and emotions."
                    if person.hymen <= 1 and person.vaginal_virgin <=1:
                        $ VTagett += f"\n{{image=virgin_token_small}} She looks sexually inexperienced."
                    else:
                        $ VTagett += f"\n{{image=vtcherries_small}} She is in her prime sexual peak."
                if person.age >35:
                    $ VTagest = "bluelotus"
                    $ VTagett = f"{{image=bluelotus_small}} The Blue Lotus: Wisedom and maturity."
                    if person.hymen <= 1 and person.vaginal_virgin <=1:
                        $ VTagett += f"\n{{image=virgin_token_small}} She looks sexually inexperienced."
                    else:
                        $ VTagett += f"\n{{image=vtcherries_small}} She is ready to rumble and tumble."
                if person.age>=31 and person.sluttiness>30:
                    $ VTagest = "cougar"
                    $ VTagett += f"\n{{image=vtcherries_small}} She is on the prowl.... Beware!"
                if person.has_cum_fetish and (person.has_breeding_fetish or person.has_anal_fetish) and person.has_exhibition_fetish and person.opinion.polyamory>1:
                    $ VTagest = "goldlotus"
                    $ VTagett += f"{{image=creamcherry_small}} The Golden Lotus: Total Sexual Enlightenment. \nThe Poke'Her'Man"
                imagebutton:
                    pos(286, 166)
                    idle VTagest
                    action NullAction()
                    tooltip VTagett
    ###### Threesome Flag - note polyamorous added
            if getattr(persistent, "knowthreesome")==1:
                $ VTpolyat = "talking"
                $ VTpolyst = "knowthreesome"
                $ VTpolytt =  f"{{image=knowthreesome_small}} Does she like threesomes?"

                if person.sexy_opinions.get("threesomes") is not None:
                    if person.sexy_opinions.get("threesomes")[1]:
                        if person.opinion.threesomes >= 2:
                            if person.opinion.polyamory >= 2 and mc.stats.polycules >= 2 and person.has_role(harem_role):
                                $ VTpolyst = "threesometriad"
                                $ VTpolytt = f"{{image=creamcherry_small}} More the merrier! The mess we will make!"
                            else:
                                $ VTpolyst = "opentriad"
                                if mc.stats.polycules >=1 and (person.has_role(affair_role) or person.is_girlfriend) and not person.has_role(harem_role):
                                    $ VTpolytt = f"{{image=progress_token_small}} Add her to the polycule!"
                                elif (person.has_role(affair_role) or person.is_girlfriend) and mc.stats.girlfriends >=2 and mc.stats.polycules==0:
                                    $ VTpolytt = f"{{image=progress_token_small}} Start a polycule!"
                                elif (person.has_role(affair_role) or person.is_girlfriend) and mc.stats.polycules == 0:
                                    $ VTpolytt = f"{{image=progress_token_small}} Get another girlfriend to create a polycule!"
                                else:
                                    if mc.stats.polycules ==1:
                                        $ VTpolytt = f"{{image=progress_token_small}} Polycule Started, go find another girlfriend!"
                                    else:
                                        $ VTpolytt = f"{{image=progress_token_small}} Open her mind up to more!"
                                if person.love >=80 and not person.has_role(harem_role):
                                    if person.is_girlfriend or person.has_role(affair_role):
                                        $ VTpolytt += f"\n{{image=red_heart_token_small}} She is ready to be part of your polycule!"
                                    else:
                                        $ VTpolytt += f"\n{{image=progress_token_small}} Need to make her your girlfriend first!"
                                elif person.love < 80 and person.love >= 60 and not person.has_role(harem_role) and not (person.has_role(affair_role) or person.is_girlfriend):
                                    if person.love <80 and (person.has_role(affair_role) or person.is_girlfriend):
                                        $ VTpolytt += f"\n{{image=progress_token_small}} {80 - person.love} more to add her to your polycule!"
                                    else:
                                        $ VTpolytt += f"\n{{image=question_mark_small}} Want her to be your girlfriend?"
                                        if not person.relationship == "Single":
                                            if person.opinion.cheating_on_men < 2:
                                                if person.opinion.cheating_on_men == 1:
                                                    $ VTpolytt += f"\n{{image=progress_token_small}} Needs to love cheating more!"
                                                else:
                                                    $ VTpolytt += f"\n{{image=progress_token_small}} Needs to like cheating."
                                        else:
                                            $ VTpolytt += f"\n{{image=red_heart_token_small}} Ask her to be your girlfriend!"
                                elif person.love < 60  and not (person.is_affair or person.is_girlfriend):
                                        $ VTpolytt += f"\n{{image=progress_token_small}} {60 - person.love} more to make her your girlfriend!"
                            if person.sexy_opinions.get("polyamory") is not None:
                                if person.sexy_opinions.get("polyamory")[1]:
                                    if person.opinion.polyamory < 2 or person.opinion.polyamory is None:
                                        if person.opinion.polyamory == 1:
                                            $ VTpolytt += f"\n{{image=red_heart_token_small}} Needs to love polyamorous more!"
                                        else:
                                            $ VTpolytt += f"\n{{image=question_mark_small}} Needs to like polyamorous relationships."
                                else:
                                    $ VTpolytt = f"{{image=knowthreesome_small}} Does she like polyamory?"
                            else:
                                $ VTpolytt = f"{{image=knowthreesome_small}} Does she like polyamory?"
                        else:
                            $ VTpolyst = "opentriad"
                            if person.opinion.threesomes > 0:
                                $ VTpolytt = f"{{image=progress_token_small}} Open her mind up to the possibility of more!"
                                $ VTpolytt += f"\n{{image=red_heart_token_small}} Make her love threesomes!"
                            elif person.opinion.threesomes == 0:
                                $ VTpolytt = f"{{image=question_mark_small}} She's indifferent to threesomes, so make her like it..."
                            else:
                                if person.opinion.threesomes == -2:
                                    $ VTpolytt = f"{{image=dislike_small}} She hates threesomes!"
                                elif person.opinion.threesomes == -1:
                                    $ VTpolytt = f"{{image=dislike_small}} She dislikes threesomes!"
                    else:
                        $ VTpolyst = "knowthreesome"
                        $ VTpolytt = f"{{image=knowthreesome_small}} Does she like threesomes?"

                #the interactive icons during sex stuff
                if 'position_choice' in globals():
                    if hasattr(position_choice, 'skill_tag'):
                        $ VTpolyat = "sexualized"

                if VTpolyat=="sexualized":
                    imagebutton:
                        pos(323, 166)
                        idle VTpolyst
                        action NullAction()
                        tooltip VTpolytt

                if VTpolyat=="talking":
                    imagebutton:
                        pos(323, 166)
                        idle VTpolyst
                        action NullAction()
                        tooltip VTpolytt
    ### Personalities 
            if getattr(persistent, "personalities")==1:
                $ VTpersonalityst = "knowpeach"
                $ VTpersonalitytt = f"{{image=question_mark_small}} What is her personality?"
                $ VTpersonality = "relaxed"
                if person.type in ["story", "unique"]:
                    $ VTpersonality = person.personality.default_prefix
                else:
                    $ VTpersonality = person.personality.personality_type_prefix
                if person.has_relation_with_mc or perk_system.has_ability_perk("Social Sage")  or person.event_triggers_dict["chatted"] > 10:
                    if VTpersonality == "bimbo":
                        $VTpersonalityst = "bimbo"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears bubbly and enthusiastic, with a bright smile plastered on her face. She studies you up and down, her eyes widening with excitement as she takes in your appearance. Her tone is sugary sweet and overly friendly, with a hint of airheadedness. Her brain is with NASA, in space."
                    elif VTpersonality == "cougar":
                        $VTpersonalityst = "cougar"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears sultry and seductive, with a confident and flirtatious smile. She studies you with a piercing gaze, her eyes seeming to sparkle with a knowing glint. Her tone is low and husky, with a hint of a purr, as if she is savoring every word."
                    elif VTpersonality == "alpha":
                        $VTpersonalityst = "alpha"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears confident and assertive, with a strong and commanding presence. She studies you with a direct and piercing gaze, her eyes seeming to bore into your very soul. Her tone is firm and authoritative, with a hint of a growl, as if she is daring you to challenge her."
                    elif VTpersonality == "relaxed":
                        $VTpersonalityst = "relaxed"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears calm and serene, with a warm and gentle smile on her face. She studies you with a soft and peaceful gaze, her eyes crinkling at the corners as she smiles. Her tone is low and soothing, with a hint of a drawl, as if she is savoring every word."
                    elif VTpersonality == "introvert":
                        $VTpersonalityst = "introvert"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears quiet and introspective, with a subtle hint of nervousness in her demeanor. She studies you with a gentle gaze, her eyes soft and thoughtful. Her tone is soft and measured, with a hint of hesitation and reserve."
                    elif VTpersonality == "reserved":
                        $VTpersonalityst = "reserved"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears calm and composed, with a subtle hint of shyness in her demeanor. She studies you with a gentle gaze, her eyes soft and introspective. Her tone is quiet and measured, with a hint of reserve and caution."
                    elif VTpersonality == "wild":
                        $VTpersonalityst = "wild"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears excited and energetic, with a huge smile on her face. She studies you with a sparkling gaze, her eyes shining with a love of fun and adventure. Her tone is loud and boisterous, with a hint of infectious enthusiasm."
                    elif VTpersonality == "wilder":
                        $VTpersonalityst = "wild"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She's a frenzied firecracker, face alight with a maniacal grin. Her eyes blaze with reckless abandon, sparkling with a love of mayhem. Her tone is a deafening scream of unbridled chaos and infectious enthusiasm."
                    elif VTpersonality == "dandere":
                        $VTpersonalityst = "dandere"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears distracted and preoccupied, with a far-off look in her eyes. She studies you with a slightly vacant expression, as if they were gazing right through you. Her tone is flat and monotone, with a hint of disinterest and detachment."
                    elif VTpersonality == "goudere":
                        $VTpersonalityst = "goudere"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears to be smiling and enthusiastic, with a radiant glow in her eyes. She studies you with a warm and inviting expression, her face lighting up with excitement. Her tone is bright and cheerful, with a hint of playfulness and mischief."
                    elif VTpersonality == "kuudere":
                        $VTpersonalityst = "kuudere"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears quiet and reserved, with a subtle hint of sadness in her eyes. She studies you with a gentle, almost imperceptible smile, her expression soft and melancholic. Her tone is low and soothing, with a hint of wistfulness and longing."
                    elif VTpersonality == "tsundere":
                        $VTpersonalityst = "tsundere"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears irritated and annoyed, with a scowl on her face. She studies you with a mixture of disdain and disinterest, her eyes flashing with a hint of anger. Her tone is sharp and curt, with a hint of sarcasm and mockery."
                    elif VTpersonality == "yandere":
                        $VTpersonalityst = "yandere"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears sweet and innocent, with a gentle smile on her face. She studies you with big, shining eyes, her gaze filled with adoration and devotion. Her tone is soft and melodious, with a hint of shyness and vulnerability."
                    elif VTpersonality == "alluring":
                        $VTpersonalityst = "pinklips"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears sophisticated and elegant, with a confident and poised demeanor. She studies you up and down, her eyes sparkling with interest and curiosity, her gaze lingering on your best features. Her tone is smooth and sultry, with a hint of playfulness and flirtation."
                    elif VTpersonality == "gothic":
                        $VTpersonalityst = "gothic"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears dark and introspective, with a hint of mystery and intrigue. She studies you up and down, her eyes narrowing slightly as she takes in your appearance, her gaze lingering on any perceived flaws or imperfections. Her tone is low and melancholic, with a hint of sarcasm and dry wit."
                    elif VTpersonality == "bimboed":
                        $VTpersonalityst = "bimbo"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears bubbly and enthusiastic, with a bright smile plastered on her face. She studies you up and down, her eyes widening with excitement as she takes in your appearance. Her tone is sugary sweet and overly friendly, with a hint of airheadedness. Her brain is with NASA, in space."
                    elif VTpersonality == "tomboy":
                        $VTpersonalityst = "tomboy"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears relaxed and casual, with a hint of a smirk on her face. She studies you with a slightly raised eyebrow, her expression a mix of curiosity and amusement. Her tone is laid-back and friendly, with a hint of teasing and playfulness."
                    elif VTpersonality == "foodie":
                        $VTpersonalityst = "foodie"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She appears to be savoring the moment, her eyes lingering on you like a rich, decadent sauce on a perfectly cooked dish. She raises an eyebrow, and a hint of a smile plays on her lips, as if she's anticipating the first bite of a long-awaited meal."
                    elif VTpersonality == "cosplay":
                        $VTpersonalityst = "cosplay"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} Her eyes sparkle with excitement as she strikes a pose, her confidence and charisma radiating from every angle."
                    elif VTpersonality == "slutty":
                        $VTpersonalityst = "openmouth"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She turns to face you with a sly smile spreading across her face. Her eyes sparkle with a hint of mischief, and her body language screams \"I'm available and ready to play\"."
                    elif VTpersonality == "pornstar":
                        $VTpersonalityst = "matureteen"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She saunters into view, her hips swaying seductively as she moves. Her eyes sparkle with a naughty glint, and her full lips curve into a sultry smile. She looks you up and down, her gaze lingering on your crotch before meeting your eyes with a flirtatious wink."
                    elif VTpersonality == "breeder":
                        $VTpersonalityst = "breeder"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} She walks into view with a confident stride, her hips swaying gently as she moves. Her eyes shine with a warm, nurturing light, and her full lips curve into a soft, inviting smile. She looks you up and down with a discerning gaze, her eyes lingering on your face before meeting your eyes with a gentle, encouraging smile."
                    else:
                        $VTpersonalityst = "vtcherries"
                        $VTpersonalitytt = f"{{image=vtcherries_small}} Her personality is unique."
                else:
                    $ VTpersonalityst = "knowpeach"
                    $ VTpersonalitytt = f"{{image=question_mark_small}} What is her personality?"
                imagebutton:
                    pos(360, 166)
                    idle VTpersonalityst
                    action NullAction()
                    tooltip VTpersonalitytt
    ###### Birth Control Status
            if getattr(persistent, "knowbirthcontrol")==1:
                $ VTbcat = "talking"
                $ VTbcst = "knowbirthcontrol"
                $ VTbctt = f"{{image=knowbc_token_small}} Is she on birth control?"
                $ VTpro = ""
                if person.bc_status_known:
                    if person._birth_control and person.on_birth_control:
                        $ VTbcst = "birthcontrol"
                        $ VTbctt = f"{{image=bc_image_small}} She is on birth control."
                        $ VTpro = " protected"
                    else:
                        $ VTbcst = "nobirthcontrol"
                        $ VTbctt = f"{{image=nobc_image_small}} She is not on birth control."
                        $ VTpro = " defenseless"
                        if person.is_infertile:
                            $ VTpro = " infertile"
                        #needed an exception for Erica... core issue (Needs better way of preventing story chars from getting knocked up before story done)
                        if not person._birth_control and person.on_birth_control and person.name=="Erica":
                            $ VTbcst = "birthcontrol"
                            $ VTbctt = f"{{image=bc_image_small}} She is on birth control."
                            $ VTpro = " protected"
                else:
                    $ VTbcst = "knowbirthcontrol"
                    $ VTbctt = f"{{image=knowbc_token_small}} Is she on birth control?"

                $ VTbreedfertile = ""
                if person.bc_status_known and person.is_highly_fertile and not person.on_birth_control and perk_system.has_ability_perk("Ovulation Cycle Perception") and persistent.pregnancy_pref > 0:
                    $ VTbreedfertile = " highly fertile"
                    $ VTbuzz = "beezee_token_small"
                #the interactive icons during sex stuff
                if 'position_choice' in globals():
                    $ VTbcat = "sexualized"
                #PREGNANCY HAXX
                if person.knows_pregnant:
                        $ VTbcst = "pregnant"
                        $ VTbctt = f"{{image=vtcherries_small}} She is pregnant."
                        $ VTpro = ""
                        $ VTbreedfertile = " pregnant"
                if VTbcat=="sexualized":
                    imagebutton:
                        pos(397, 166)
                        idle VTbcst
                        action NullAction()
                        tooltip VTbctt
                    if person.bc_status_known and not person.on_birth_control and person.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception") and persistent.pregnancy_pref > 0:
                        $ VTbctt += f"\n{{image=beezee_token_small}} She is highly fertile."
                        imagebutton:
                            pos(397, 166)
                            idle "beezee"
                            action NullAction()
                            tooltip VTbctt

                if VTbcat=="talking":
                    imagebutton:
                        pos(397, 166)
                        idle VTbcst
                        action NullAction()
                        tooltip VTbctt
                    if person.bc_status_known and not person.on_birth_control and person.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception") and persistent.pregnancy_pref > 0:
                        $ VTbctt += f"\n{{image=beezee_token_small}} She is highly fertile."
                        imagebutton:
                            pos(397, 166)
                            idle "beezee"
                            action NullAction()
                            tooltip VTbctt

                if person.vaginal_cum >0:
                    $ VTbcst = "bc_cum"
                    if person.vaginal_cum ==1:
                        $ VTbctt += f"\n{{image=creamcherry_small}} Your cum is swimming in her"+VTbreedfertile+VTpro+" womb."
                    else:
                        $ VTbctt += f"\n{{image=creamcherry_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."
                    imagebutton:
                        pos(397, 166)
                        idle VTbcst
                        action NullAction()
                        tooltip VTbctt
    ####### Wants Condom
            if getattr(persistent, "knowcondom")==1:
                $ VTcondomat = "talking"
                $ VTcondommc = "condom"
                $ VTcondomst = "knowcondom"
                $ VTcondomtt = f"{{image=knowcondom_token_small}} Does she like bareback sex?"
                if person.sexy_opinions.get("bareback sex")==None:
                    $ VTcondomst = "knowcondom"
                    $ VTcondomtt = f"{{image=knowcondom_token_small}} Does she like bareback sex?"
                else:
                    if person.sexy_opinions.get("bareback sex")[1]==True:
                        if person.opinion.bareback_sex >= 2 and person.wants_creampie and (person.has_cum_fetish or person.has_anal_fetish or person.has_breeding_fetish) and not person.wants_condom():
                            $ VTcondomst = "vtcherries"
                            $ VTcondomtt = f"{{image=creamcherry_small}} She loves it raw!"
                        else:
                            if person.opinion.bareback_sex >= 2 and not person.wants_condom():
                                $ VTcondomst = "nocondom"
                                $ VTcondomtt = f"{{image=progress_token_small}} She seems to love raw sex! "
                                if person.has_cum_fetish==False:
                                    $ VTcondomtt += f"\n{{image=triskelion_token_small}} Needs the Cum Fetish Unlocked."
                            else:
                                if person.opinion.bareback_sex >0:
                                    $ VTcondomst = "wearcondom"
                                    $ VTcondomtt = f"{{image=progress_token_small}} Open her mind up to enjoying raw more!"
                                    $ VTcondomtt += f"\n{{image=red_heart_token_small}} Make her love raw sex more!"
                                else:
                                    if person.opinion.bareback_sex == 0:
                                        $ VTcondomst = "wearcondom"
                                        $ VTcondomtt = f"{{image=progress_token_small}} She's indifferent to raw sex, so make her like it..."
                                    else:
                                        $ VTcondomst = "nocondom"
                                        $ VTcondomtt = f"{{image=progress_token_small}} She's indifferent to raw sex, so make her like it..."
                                        if person.opinion.bareback_sex == -2:
                                            $ VTcondomtt = f"{{image=dislike_small}} She hates raw sex!"
                                        if person.opinion.bareback_sex == -1:
                                            $ VTcondomtt = f"{{image=dislike_small}} She dislikes raw sex!"
                    else:
                        $ VTcondomst = "knowcondom"
                        $ VTcondomtt = f"{{image=knowcondom_token_small}} Does she like bareback sex?"
                #the interactive icons during sex stuff
                if 'position_choice' in globals():
                    if hasattr(position_choice, 'skill_tag'):
                        $ VTcondomat = "sexualized"
                        if mc.condom == False:
                            $ VTcondomst = "vtcherries"
                            $ VTcondommc = "condomoff"
                            $ VTcondomtt = f"{{image=vtcherries_small}} Your {random_cock_word} is {random_condom_word}."
                            if person.days_since_event("last_insemination")<1 and person.vaginal_cum >0:
                                $ VTcondomst = "creamcherry"
                                $ VTcondomtt += f"\n{{image=vtcherries_small}} You recently came inside her {random_pussy_word}."
                        else:
                            $ VTcondomst = "wearcondom"
                            $ VTcondomtt = f"{{image=wearcondom_token_small}} You are {random_condom_word}."

                if VTcondomat=="sexualized":
                    #TODO add creamcherries when they cum during raw
                    if VTcondommc == "condomoff":
                        $ VTcondomst = "vtcherries"
                        $ VTcondomtt = f"{{image=vtcherries_small}} Your {random_cock_word} is {random_condom_word}."
                        if person.days_since_event("last_insemination")<1 and person.vaginal_cum >0:
                            $ VTcondomst = "creamcherry"
                            $ VTcondomtt += f"\n{{image=vtcherries_small}} You recently came inside her {random_pussy_word}."
                    imagebutton:
                        pos(434, 166)
                        idle VTcondomst
                        action NullAction()
                        tooltip VTcondomtt

                if VTcondomat=="talking":
                    if VTcondommc == "condomoff":
                        $ VTcondomst = "vtcherries"
                        $ VTcondomtt = f"{{image=vtcherries_small}} Your {random_cock_word} is {random_condom_word}."
                        if person.days_since_event("last_insemination")<1 and person.vaginal_cum >0:
                            $ VTcondomst = "creamcherry"
                            $ VTcondomtt += f"\n{{image=vtcherries_small}} You recently came inside her {random_pussy_word}."
                    imagebutton:
                        pos(434, 166)
                        idle VTcondomst
                        action NullAction()
                        tooltip VTcondomtt                    
                    if person.sexy_opinions.get("bareback sex")!=None:
                        if person.opinion.bareback_sex <0 and person.sexy_opinions.get("bareback sex")[1]==True:
                            $ VTcondomtt += f"\n{{image=dislike_small}} She does not like bareback sex."
                            imagebutton:
                                pos(434, 166)
                                idle "dislike"
                                action NullAction()
                                tooltip VTcondomtt
    #the sex stuffs
    #### Tranced
            if getattr(persistent, "ahegaotrance")==1:
                if person.has_exact_role(very_heavy_trance_role):
                    imagebutton:
                        pos(486, 166)
                        idle "ahegaotrance"
                        action NullAction()
                        tooltip f"{{image=ahegaotrance_token_small}} In a very deep trance!\n {{image=creamcherry_small}} Best time to train her!"
                else:
                    if person.has_exact_role(heavy_trance_role):
                        imagebutton:
                            pos(486, 166)
                            idle "heavytrance"
                            action NullAction()
                            tooltip f"{{image=heavytrance_token_small}} In a deep trance!\n {{image=triskelion_token_small}} Good time to train her!"
                    else:
                        if person.has_exact_role(trance_role):
                            imagebutton:
                                pos(486, 166)
                                idle "starttrance"
                                action NullAction()
                                tooltip f"{{image=starttrance_token_small}} In a trance!\n {{image=triskelion_token_small}} She is open to suggestions!"
                if person.event_triggers_dict.get("trance_training_available", True) == False:
                    imagebutton:
                        pos(486, 166)
                        idle "donetrain"
                        action NullAction()
                        tooltip f"{{image=donetrain_token_small}} Already Trained her!"

    #hymen is 0 = sealed, 1=recently torn bleeding, 2=normal - serum to regenerate vaginal and hymen
    #0=virgin, 1=just the tip, 2=full penetration, 3-10 is degree of tightness
    #### Oral Virgin Flag
            if getattr(persistent, "knowlips")==1:
                $ VToralknowtext = VT_get_next_random_item(VToralknow_index, VToralknowlist)[0]
                $ VToralvirgintext = VT_get_next_random_item(VToralvirgin_index, VToralvirginlist)[0]
                $ VToralclaimtext = VT_get_next_random_item(VToralclaim_index, VToralclaimlist)[0]
                $ VToralclaimfirsttext = VT_get_next_random_item(VToralclaimfirst_index, VToralclaimfirstlist)[0]
                $ VTOVF = int(person.oral_virgin)
                $ VToralat = "talking"
                $ VToralst = "knowlips"
                $ VToraltt = f"{{image=question_mark_small}} {VToralknowtext}"
                # Determine Oral Claim Status
                if perk_system.has_ability_perk("Lip Lock Intuition") or (person.has_broken_taboo("sucking_cock")):
                    if VTOVF == 0:
                        $ VToralst = "virgin_oral"
                        $ VToraltt = f"{{image=virgin_oral_small}} {VToralvirgintext}"
                    elif person.oral_first == mc.name:
                        $ VToralst = "claimedmouth"
                        $ VToraltt = f"{{image=handprint_token_small}} {VToralclaimtext}"
                    elif person.oral_first is not None and person.oral_virgin > 0:
                        $ VToralst = "oralclaimed"
                        $ VToraltt = f"{{image=oralclaimed_small}} {VToralclaimfirsttext}"
                #the interactive icons during sex stuff
                if ('position_choice' in globals() and hasattr(position_choice, 'skill_tag')) :
                    if position_choice.skill_tag == 'Oral':
                        $ VToralat = "sexualized"
                        if position_choice.name in ["Blowjob", "Deepthroat", "Skull Fuck","Cunnilingus", "Cowgirl Cunnilingus", "Kneeling oral","Sixty-Nine", "Cum Fetish Blowjob", "Ophelia Blowjob", "Standing Oral", "Standing Cunnilingus", "Cowgirl Blowjob"]:
                            $ VTorifice_current = "Oral"
                            if position_choice.name in ["Blowjob", "Cum Fetish Blowjob", "Ophelia Blowjob", "Standing Oral", "Deepthroat", "Skull Fuck", "Sixty-Nine", "Cowgirl Blowjob"]:
                                $ VToralst = "openmouth"  
                                if position_choice.name == "Blowjob":
                                    $ VToraltt = f"{{image=openmouth_small}} Her {random_mouth_word} wraps around your {random_condom_word} {random_cock_word}, sucking gently."
                                elif position_choice.name == "Cowgirl Blowjob":
                                    $ VToraltt = f"{{image=openmouth_small}} She sucks your {random_condom_word} {random_cock_word} wantonly, you groan from the stimulation...."
                                elif position_choice.name == "Cum Fetish Blowjob":
                                    $ VToraltt = f"{{image=openmouth_small}} She is sucking your {random_condom_word} {random_cock_word} like a vacuum, eager for your cum."
                                elif position_choice.name == "Ophelia Blowjob":
                                    $ VToraltt = f"{{image=openmouth_small}} Her {random_mouth_word} working your {random_condom_word} {random_cock_word} so amazingly, you feel yourself getting harder."
                                elif position_choice.name == "Standing Oral":
                                    $ VToraltt = f"{{image=openmouth_small}} She worships your {random_condom_word} {random_cock_word} with her warm wet tongue, making you feel like a king."
                                elif position_choice.name == "Deepthroat":
                                    $ VToraltt = f"{{image=openmouth_small}} You deeply fuck her throat with your {random_condom_word} {random_cock_word}, feeling her gag reflex."
                                elif position_choice.name == "Skull Fuck":
                                    $ VToraltt = f"{{image=openmouth_small}} You grab her head and skull fuck her with your {random_condom_word} {random_cock_word}, feeling her struggle to breathe."
                                elif position_choice.name == "Sixty-Nine":
                                    $ VToraltt = f"{{image=openmouth_small}} She moans on your {random_condom_word} {random_cock_word} as you lick her {random_pussy_word}, the pleasure is mutual."
                            elif position_choice.name in ["Cunnilingus", "Cowgirl Cunnilingus", "Kneeling oral", "Standing Cunnilingus"]:
                                $ VToralst = "bitelip"
                                if position_choice.name == "Cunnilingus":
                                    $ VToraltt = f"{{image=bitelip_small}} She moans as you lick her juicy {random_pussy_word}, her legs trembling with pleasure."
                                elif position_choice.name == "Standing Cunnilingus":
                                    $ VToraltt = f"{{image=bitelip_small}} She moans as you lick her juicy {random_pussy_word}, her hands grasping your hair."
                                elif position_choice.name == "Cowgirl Cunnilingus":
                                    $ VToraltt = f"{{image=bitelip_small}} She moans as you lick her juicy {random_pussy_word}, her hips grinding against your face."
                                elif position_choice.name == "Kneeling oral":
                                    $ VToraltt = f"{{image=bitelip_small}} She moans as she watches you lick her juicy {random_pussy_word}, her eyes filled with desire."
                    elif position_choice.skill_tag == 'Foreplay':   
                        $ VTorifice_current = "Oral Foreplay"
                        if position_choice.name == 'Kissing':
                            $ VToralat = "sexualized"
                            $ VToralst = "pinklips"
                            $ VToraltt = f"{{image=openmouth_small}} In the throes of kissing you."                        

                    if VToralat=="sexualized" and VTorifice_current in ["Oral","Oral Foreplay"] and not position_choice.name in ["Cunnilingus", "Cowgirl Cunnilingus", "Kneeling oral", "Kissing", "Standing Cunnilingus"]:
                        if person.oral_virgin == 0:
                                $ person.oral_virgin = 1
                                $ person.oral_first = mc.name

                if ('current_node' in globals() and hasattr(current_node, 'position')):
                    if current_node.position.skill_tag == "Oral":
                        $ VToralat = "sexualized"
                        if current_node.position.name in ["Blowjob", "Deepthroat", "Skull Fuck", "Kneeling oral","Sixty-Nine", "Cum Fetish Blowjob", "Ophelia Blowjob", "Standing Oral", "Cowgirl Blowjob"]:
                            $ VToralst = "openmouth" 
                            if current_node.position.name == "Blowjob":
                                $ VToraltt = f"{{image=openmouth_small}} Her {random_mouth_word} wrap around your {random_condom_word} {random_cock_word}, sucking gently."
                            elif current_node.position.name == "Deepthroat":
                                    $ VToraltt = f"{{image=openmouth_small}} You deeply fuck her throat with your {random_condom_word} {random_cock_word}, feeling her gag reflex."
                            elif current_node.position.name == "Skull Fuck":
                                $ VToraltt = f"{{image=openmouth_small}} You grab her head and skull fuck her with your {random_condom_word} {random_cock_word}, feeling her struggle to breathe."
                    if VToralat=="sexualized" and VTorifice_current in ["Oral","Oral Foreplay"] and not current_node.position.name in ["Cunnilingus", "Cowgirl Cunnilingus", "Kneeling oral", "Kissing", "Standing Cunnilingus"]:
                        if person.oral_virgin == 0:
                            $ person.oral_virgin = 1
                            $ person.oral_first = mc.name

                if 'climax_type' in globals():
                    if climax_type == "mouth":
                        if mc.condom == False:
                            $ VToralst = "ahegaomouth"
                            $ VToraltt = f"{{image=ahegaomouth_small}} You unleash a torrent of cum into her mouth, filling it to the brim."
                        else:
                            $ VToralst = "openmouth"
                            $ VToraltt = f"{{image=openmouth_small}} You erupt into the condom as her tongue wraps around you, teasing out every last drop."
                    if climax_type == "throat":
                        if mc.condom == False:
                            $ VToralst = "ahegaomouth"
                            $ VToraltt = f"{{image=ahegaomouth_small}} You flood her belly with your cum, feeling her throat constrict around you."
                        else:
                            $ VToralst = "openmouth"
                            $ VToraltt = f"{{image=openmouth_small}} You fill the condom to bursting as her throat squeezes you, milking you dry."
                    if climax_type == "face":
                        $ VToralst = "ahegaomouth"
                        $ VToraltt = f"{{image=openmouth_small}} You shoot your load all over her face, covering her in a sticky mask of cum."
                    if climax_type =="body":
                        $ VToralst = "bitelip"
                        $ VToraltt = f"{{image=openmouth_small}} You blow your load all over her body, decorating her skin with streaks of cum."                      

                if VToralat=="sexualized":
                    imagebutton:
                        pos(523, 166)
                        idle VToralst
                        action NullAction()
                        tooltip VToraltt

                if VToralat == "talking" :
                    # Determine Arousal Status and Cum Status
                    if person.arousal_perc >= 59:
                        if person.oral_cum == 0:
                            $ VToralst = "ahegaoface"
                            if person.oral_virgin == 0:
                                $ VToraltt += f"\n{{image=virgin_oral_small}} Her innocent eyes sparkle with desire, her hungry pussy aching for attention.\n{{image=bitelip_small}} She bites her lip coyly, trying to contain her excitement."
                            else:
                                if person.oral_first == mc.name:
                                    $ VToraltt += f"\n{{image=handprint_token_small}} She locks eyes with you, her gaze burning with passion, and bites her lip sexily."
                                else:
                                    $ VToraltt += f"\n{{image=oralclaimed_small}} She pants and breathes heavily, her chest heaving with desire, and bites her lip."
                            # if person.energy <20 and person.had_sex_today:
                                # $ VToraltt += f"\n{{image=bitelip_small}} She seems lost in her bliss, her eyes glazing over as she pants with pleasure."
                        else:
                            $ VToralst = "handass"
                            if person.oral_cum==1:
                                $ VToralst = "ahegaoface"
                                $ VToraltt += f"\nShe seems lost in her bliss and panting. \n{{image=ahegaomouth_small}}She has a warm dose of your protein in her belly."
                            else:
                                if person.oral_cum>3:
                                    $ VToralst = "ahegaoface"
                                    if person.oral_cum > 6:
                                        $ VToraltt += f"\n*Her eyes glaze over as she smiles contently* \n{{image=ahegaomouth_small}} She has "+ str(person.oral_cum) +" doses of your cum \n swimming in her stomach, a noticeable bulge forming."
                                    else:
                                        $ VToraltt += f"\n*Her eyes glaze over as she smiles contently* \n{{image=ahegaomouth_small}} She has "+ str(person.oral_cum) +" doses of your cum. \n Her belly is warm with your protein, a gentle bulge forming."
                                else:
                                    $ VToralst = "ahegaoface"
                                    $ VToraltt += f"\n*Her eyes glaze over as she smiles contently*\n{{image=ahegaomouth_small}} Her belly is warm with "+ str(person.oral_cum) +" doses of your cum \n swimming in her belly."
                        if person.energy < 20 and person.had_sex_today:
                            $ VToraltt += f"\n{{image=bitelip_small}} She seems lost in her bliss, her eyes glazing over as she pants with pleasure."
                    else:
                        if person.oral_cum > 0:
                            if person.oral_cum == 1:
                                $ VToralst = "bitelip"
                                $ VToraltt += f"\nShe looks at you with lust in her innocent hungry eyes, her gaze burning with desire. \n{{image=ahegaomouth_small}} Her belly is warm with a dose of your protein."
                            else:
                                if person.oral_cum>3:
                                    $ VToralst = "ahegaomouth"
                                    $ VToraltt += f"\n{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in the slight bulge of her belly, a noticeable glow forming."
                                else:
                                    $ VToralst = "bitelip"
                                    $ VToraltt += f"\n{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \nswimming in her belly, a gentle warmth forming."
                        else:
                            if perk_system.has_ability_perk("Lip Lock Intuition")  or (person.has_broken_taboo("sucking_cock")):
                                if person.oral_virgin == 0 and not person.had_sex_today:
                                    $ VToraltt += f"\n{{image=virgin_oral_small}} She looks at you with lust in her innocent hungry eyes, her gaze sparkling with curiosity."
                                elif person.oral_first == mc.name and not person.had_sex_today:
                                    $ VToraltt += f"\n{{image=handprint_token_small}} She starts to drool and undress you with her eyes, her gaze burning with desire."
                                elif not person.had_sex_today:
                                    $ VToraltt += f"\n{{image=bitelip_small}} She looks at you with curiosity, her eyes sparkling with interest."
                                if person.energy < 20 and person.had_sex_today:
                                    $ VToraltt += f"\n{{image=bitelip_small}} She seems lost in her bliss, her eyes glazing over as she pants with pleasure."

                    imagebutton:
                        pos(523, 166)
                        idle VToralst
                        action NullAction()
                        tooltip VToraltt
    # ### Vaginal Virgin Flag
            if getattr(persistent, "knowvaginal")==1:
                $ VTvaginalknowtext  = VT_get_next_random_item(VTvaginalknow_index, VTvaginalknowlist)[0]
                $ VTvaginalvirgintext = VT_get_next_random_item(VTvaginalvirgin_index, VTvaginalvirginlist)[0]
                $ VTvaginalclaimtext = VT_get_next_random_item(VTvaginalclaim_index, VTvaginalclaimlist)[0]
                $ VTvaginalclaimfirsttext = VT_get_next_random_item(VTvaginalclaimfirst_index, VTvaginalclaimfirstlist)[0]
                $ VTVVF = int(person.vaginal_virgin)
                $ VTvaginalat = "talking"
                $  VTvaginalst = "knowpeach"
                $  VTvaginaltt = f"{{image=question_mark_small}} {VTvaginalknowtext}"
                # Determine Vaginal Claim Status
                if perk_system.has_ability_perk("Rose Petal Insight") or (person.has_broken_taboo("vaginal_sex")):
                    if VTVVF == 0:
                        $  VTvaginalst = "virgin_vaginal"
                        $  VTvaginaltt = f"{{image=virgin_vaginal_small}} {VTvaginalvirgintext}"
                    elif person.vaginal_first == mc.name:
                        $  VTvaginalst = "claimedvag"
                        $  VTvaginaltt = f"{{image=handprint_token_small}} {VTvaginalclaimtext}"
                    elif person.vaginal_first is not None and person.vaginal_virgin > 0:
                        $  VTvaginalst = "vaginalclaimed"
                        $  VTvaginaltt = f"{{image=vaginalclaimed_small}} {VTvaginalclaimfirsttext}"
                #the interactive icons during sex stuff
                if 'position_choice' in globals() and hasattr(position_choice, 'skill_tag'):
                    if position_choice.skill_tag == 'Pussy':
                        $ VTvaginalat = "sexualized"
                        if position_choice.name in ["Against Wall", "Cowgirl", "Doggy","Facing Wall", "Missionary", "Piledriver","Piledriver DP", "Prone Bone", "Reverse Cowgirl", "Spooning Sex", "Standing Doggy"]:
                            $ VTorifice_current = "Pussy"
                            if position_choice.name in ["Against Wall", "Cowgirl", "Doggy","Facing Wall", "Missionary", "Piledriver","Piledriver DP", "Prone Bone", "Reverse Cowgirl", "Spooning Sex", "Standing Doggy"]:
                                $ VTvaginalst = "spreadvag"
                                if position_choice.name == "Against Wall":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} You slam your {random_condom_word} {random_cock_word} into her {random_pussy_word}, feeling her warm juices gush around you as she screams in ecstasy."
                                elif position_choice.name == "Cowgirl":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} She rides your {random_condom_word} {random_cock_word} with reckless abandon, her hips bucking wildly as she milks you for every last drop."
                                elif position_choice.name == "Doggy":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} You pound your {random_condom_word} {random_cock_word} into her from behind, her moans echoing through the air as she begs for more."
                                elif position_choice.name == "Facing Wall":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} You pin her against the wall, your {random_condom_word} {random_cock_word} buried deep within her {random_pussy_word} as you ravage her with kisses."
                                elif position_choice.name == "Missionary":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} You gaze into her eyes as you make love, your bodies entwined in a passionate dance of desire."
                                elif position_choice.name == "Piledriver":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} You drive your {random_condom_word} {random_cock_word} into her with savage intensity, her cries of pleasure music to your ears as you claim her {random_pussy_word} as your own."
                                elif position_choice.name == "Piledriver DP":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} You thrust your {random_condom_word} {random_cock_word} into her {random_pussy_word} while a dildo fills her ass, a symphony of pleasure and pain as she's stretched to the limit and screams with delight."
                                elif position_choice.name == "Prone Bone":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} You lie on top of her, your bodies pressed together, your {random_condom_word} {random_cock_word} thrusting into her {random_pussy_word} deeply."
                                elif position_choice.name == "Reverse Cowgirl":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} She rides you with wild abandon,  as she takes control and rides your {random_condom_word} {random_cock_word} like a cowgirl on a bronco."
                                elif position_choice.name == "Spooning Sex":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} You hold her close, your bodies curled together like spoons as you make love with a tender passion that sets your souls on fire."
                                elif position_choice.name == "Standing Doggy":
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} You take her from behind, your bodies standing upright as you lose yourselves in the moment and surrender to the primal urge that drives you."

                if 'climax_type' in globals():
                    if climax_type == "pussy":
                        if mc.condom == False:
                            if person.hymen ==1:
                                $ VTvaginalst = "vaghymen"
                                $ VTvaginaltt = f"{{image=handprint_token_small}}  You unleash a torrent of your virile cum into her freshly deflowered {VTbreedfertile}{VTpro} {random_pussy_word} , claiming her innocence as your own! \n Her virginity is forever lost in a sea of your seed! "
                            else:
                                $ VTvaginalst = "openvag"
                                $ VTvaginaltt = f"{{image=openvag_small}} You erupt into her {VTbreedfertile}{VTpro} womb, flooding her with a tidal wave of cum that threatens to overflow her very being!"
                                if person.vaginal_cum >=3:
                                    $ VTvaginalst = "ahegaovag"
                        else:
                            if person.hymen ==1:
                                $ VTvaginalst = "spreadvag"
                                $ VTvaginaltt = f"{{image=handprint_token_small}} You fill the condom in her freshly fucked virgin {random_pussy_word} to the brim with your scorching hot cum, the latex straining to contain the sheer force of your ejaculation!"
                            else:
                                $ VTvaginalst = "spreadvag"
                                $ VTvaginaltt = f"{{image=spreadvag_small}} You drive deep and unleash a fury of cum into the condom, the sound of your seed splashing against the latex a symphony of pleasure!"
                    if climax_type =="body":
                        $ VTvaginalst = "spreadvag"
                        if mc.condom == False:
                            $ VTvaginaltt = f"{{image=spreadvag_small}} You explode in a frenzy of cum, covering her body in a sticky film of your seed as you mark her as your own!"
                        else:
                            $ VTvaginaltt = f"{{image=spreadvag_small}} You fill the condom to bursting as you pull out of her, the latex straining to contain the sheer force of your ejaculation!"

                if VTvaginalat == "sexualized" and VTorifice_current == "Pussy":
                    if person.vaginal_virgin == 0:
                        $ person.vaginal_virgin = 1
                        $ person.vaginal_first = mc.name
                    imagebutton:
                        pos(560, 166)
                        idle VTvaginalst
                        action NullAction()
                        tooltip VTvaginaltt

                    $ VTvaginalcum = "bc_cum"
                    if person.hymen > 1 and person.vaginal_cum > 1:
                        $ VTvaginaltt += f"\n{{image=creamcherry_small}} {person.vaginal_cum} doses of your cum \n swimming in her{VTbreedfertile}{VTpro} womb.{daysince}"
                    elif person.hymen < 2 and person.vaginal_cum > 0:
                        $ VTvaginalcum = "vaghymen"

                    if person.vaginal_cum > 0:
                            imagebutton:
                                pos(560, 166)
                                idle VTvaginalcum
                                action NullAction()
                                tooltip VTvaginaltt

                if VTvaginalat == "talking" :
                    # Determine Arousal Status and Cum Status
                    if person.arousal_perc >= 59:
                        if person.vaginal_cum == 0:
                            $ VTvaginalst = "spreadvag"
                            if person.hymen == 0:
                                $ VTvaginaltt += f"\n{{image=virgin_vaginal_small}} She's aching to be fucked, her {random_pussy_word} throbbing with anticipation."
                            elif person.anal_first == mc.name:
                                $ VTvaginaltt += f"\n{{image=spreadvag_small}} Her fresh {random_pussy_word} is dripping with desire, begging to be claimed by your {random_cock_word}.\n*The scent of her arousal is intoxicating*"
                            else:
                                $ VTvaginaltt += f"\n{{image=spreadvag_small}} Her {random_pussy_word} is drenched in her own juices, ready to be devoured by your hungry {random_cock_word}.\n*The smell of her arousal is driving you wild*"
                        else:
                            if person.vaginal_cum == 1:
                                if person.hymen <= 1:
                                    $ VTvaginalst = "vaghymen"
                                    $ VTvaginaltt += f"\n{{image=handprint_token_small}} You've branded her fresh{VTbreedfertile}{VTpro} womb with your scorching hot seed, claiming her innocence as your own."
                                else:
                                    $ VTvaginalst = "openvag"
                                    $ VTvaginaltt += f"\n{{image=beezee_token_small}} You've flooded her {VTbreedfertile}{VTpro} womb with your cum, marking her as your own personal playground."
                            else:
                                if person.vaginal_cum>3:
                                    if person.hymen <= 1:
                                        $ VTvaginalst = "vaghymen"
                                        $ VTvaginaltt += f"\n{{image=handprint_token_small}}  Her fresh {random_pussy_word} is overflowing with the {person.vaginal_cum} doses of your cum, her{VTbreedfertile}{VTpro} womb struggling to contain the sheer volume of your seed.{daysince}"
                                    else:
                                        $ VTvaginalst = "ahegaopeach"
                                        $ VTvaginaltt += f"\n{{image=beezee_token_small}} Her {random_pussy_word} is a cum-soaked paradise, the {person.vaginal_cum} doses of your seed swimming in her{VTbreedfertile}{VTpro} womb and oozing out in a sticky, sweet mess.{daysince}"
                                else:
                                    if person.hymen <= 1:
                                        $ VTvaginalst = "vaghymen"
                                        $ VTvaginaltt += f"\n{{image=handprint_token_small}} You've claimed her fresh{VTbreedfertile}{VTpro} womb with your seed, marking her as your own personal property."
                                    else:
                                        $ VTvaginalst = "ahegaovag"
                                        $ VTvaginaltt += f"\n{{image=beezee_token_small}} You've dosed her {VTbreedfertile}{VTpro} womb with {person.vaginal_cum} loads of your cum, turning her into a walking, talking cum-dumpster."
                        if person.energy < 20 and person.had_sex_today:
                            $ VTvaginaltt += f"\n{{image=ahegaovag_small}} She's lost in a haze of post-coital bliss, her body still trembling from the aftershocks of your lovemaking."
                    else:
                        if person.vaginal_cum == 0:
                            if perk_system.has_ability_perk("Rose Petal Insight") or (person.has_broken_taboo("vaginal_sex")):
                                #$ VTvaginalst = "spreadvag"
                                if person.hymen == 0:
                                    $ VTvaginalst = "virgin_vaginal"
                                    $ VTvaginaltt += f"\n{{image=virgin_vaginal_small}} Her {random_pussy_word} is aching to be claimed, her tender flesh quivering with anticipation."
                                elif person.vaginal_first == mc.name:
                                    $ VTvaginaltt += f"\n{{image=handprint_token_small}} Her fresh, moist {random_pussy_word} is spread wide open for you, inviting you to take her."
                                else:
                                    $ VTvaginaltt += f"\n{{image=vaginalclaimed_small}} Her {random_pussy_word} is a siren's call, beckoning you to come and claim her as your own."
                        else:
                            if person.vaginal_cum == 1:
                                if person.hymen <= 1:
                                    $ VTvaginalst = "vaghymen"
                                    $ VTvaginaltt += f"\n{{image=handprint_token_small}} You've branded her fresh{VTbreedfertile}{VTpro} womb with your scorching hot seed, claiming her innocence as your own."
                                else:
                                    $ VTvaginalst = "openvag"
                                    $ VTvaginaltt += f"\n{{image=beezee_token_small}} You've flooded her {VTbreedfertile}{VTpro} womb with your cum, marking her as your own personal playground."
                            else:
                                if person.vaginal_cum>3:
                                    if person.hymen <= 1:
                                        $ VTvaginalst = "vaghymen"
                                        $ VTvaginaltt += f"\n{{image=handprint_token_small}} Her fresh {random_pussy_word} is overflowing with the {person.vaginal_cum} doses of your cum, her{VTbreedfertile}{VTpro} womb struggling to contain the sheer volume of your seed.{daysince}"
                                    else:
                                        $ VTvaginalst = "ahegaopeach"
                                        $ VTvaginaltt += f"\n{{image=beezee_token_small}} Her {random_pussy_word} is a cum-soaked paradise, the {person.vaginal_cum} doses of your seed swimming in her{VTbreedfertile}{VTpro} womb and oozing out in a sticky, sweet mess.{daysince}"
                                else:
                                    if person.hymen <= 1:
                                        $ VTvaginalst = "vaghymen"
                                        $ VTvaginaltt += f"\n{{image=handprint_token_small}} You've claimed her fresh{VTbreedfertile}{VTpro} womb with your seed, marking her as your own personal property."
                                    else:
                                        $ VTvaginalst = "ahegaovag"
                                        $ VTvaginaltt += f"\n{{image=beezee_token_small}} You've dosed her {VTbreedfertile}{VTpro} womb with {person.vaginal_cum} loads of your cum, turning her into a walking, talking cum-dumpster."
                        if person.energy < 20 and person.had_sex_today:
                            $ VTvaginaltt += f"\n{{image=ahegaovag_small}} She's lost in a haze of post-coital bliss, her body still trembling from the aftershocks of your lovemaking."

                    imagebutton:
                        pos(560, 166)
                        idle VTvaginalst
                        action NullAction()
                        tooltip VTvaginaltt
                    $ VTvaginalcum = "bc_cum"
                    if person.hymen < 2 and person.vaginal_cum > 0:
                        $  VTvaginalcum = "vaghymen"
                    if person.vaginal_cum > 0:
                        imagebutton:
                            pos(560, 166)
                            idle VTvaginalcum
                            action NullAction()
                            tooltip VTvaginaltt
    ### Anal Virgin Flag
            if getattr(persistent, "knowanal")==1:
                $ VTanalknowtext = VT_get_next_random_item(VTanalknow_index, VTanalknowlist)[0]
                $ VTanalvirgintext = VT_get_next_random_item(VTanalfirst_index, VTanalfirstlist)[0]
                $ VTanalclaimtext = VT_get_next_random_item(VTanalclaim_index, VTanalclaimlist)[0]
                $ VTanalclaimfirsttext = VT_get_next_random_item(VTanalclaimfirst_index, VTanalclaimfirstlist)[0]
                $ VTAVF = int(person.anal_virgin)
                $ VTanalat = "talking"
                $ VTanalst = "knowpeach"
                $ VTanaltt = f"{{image=question_mark_small}} {VTanalknowtext}"
                # Determine Anal Claim Status
                if perk_system.has_ability_perk("Midnight Mirage") or (person.has_broken_taboo("anal_sex")):
                        if VTAVF== 0:
                            $  VTanalst = "virgin_anal"
                            $  VTanaltt = f"{{image=virgin_anal_small}} {VTanalvirgintext}"
                        elif person.anal_first == mc.name:
                            $  VTanalst = "claimedass"
                            $  VTanaltt = f"{{image=handprint_token_small}} {VTanalclaimtext}"
                        elif person.anal_first is not None and person.anal_virgin > 0:
                            $  VTanalst = "analclaimed"
                            $  VTanaltt = f"{{image=analclaimed_small}} {VTanalclaimfirsttext}"
                #the interactive icons during sex stuff
                if 'position_choice' in globals()and hasattr(position_choice, 'skill_tag'):
                    if position_choice.skill_tag == 'Anal':
                        $ VTanalat = "sexualized"
                        if position_choice.name in ["Anal Cowgirl", "Anal Doggy", "Anal On Lap", "Anal Piledriver", "Anal Standing", "Anal Swing", "Doggy Anal", "Doggy Anal Dildo DP", "Prone Anal", "Standing Anal"]:
                            $VTorifice_current = "Anal"
                            $ VTanalst = "yesanal"
                            if position_choice.name == "Anal Doggy":
                                $ VTanaltt = f"{{image=yesanal_small}} She screams in ecstasy as you pound her {random_anal_word} with reckless abandon, her body trembling with each thrust...."
                            elif position_choice.name == "Anal Cowgirl":
                                $ VTanaltt = f"{{image=yesanal_small}} She rides your {random_condom_word} {random_cock_word} in her {random_anal_word} with wild abandon, her hips bucking wildly as she milks you for every last drop...."
                            elif position_choice.name == "Anal On Lap":
                                $ VTanaltt = f"{{image=yesanal_small}} She grinds her {random_anal_word} against your {random_condom_word} {random_cock_word}, her body pressed against yours as you devour each other with kisses...."
                            elif position_choice.name == "Anal Piledriver":
                                $ VTanaltt = f"{{image=yesanal_small}} You drill your {random_condom_word} {random_cock_word} deep into her {random_anal_word}, her cries of pleasure music to your ears as you claim her as your own...."
                            elif position_choice.name == "Anal Standing":
                                $ VTanaltt = f"{{image=yesanal_small}} You thrust your {random_condom_word} {random_cock_word} deep up her {random_anal_word}, her body trembling with each thrust as you take her from behind...."
                            elif position_choice.name == "Anal Swing":
                                $ VTanaltt = f"{{image=yesanal_small}} You fuck her {random_anal_word} while rocking the swing, the motion sending waves of pleasure through her body...."
                            elif position_choice.name == "Standing Anal":
                                $ VTanaltt = f"{{image=yesanal_small}} You thrust your {random_condom_word} {random_cock_word} deep up her {random_anal_word}, her body trembling with each thrust as you take her from behind...."
                            elif position_choice.name == "Doggy Anal":
                                $ VTanaltt = f"{{image=yesanal_small}} You fuck her like a bitch in heat, her body responding to your every thrust as you take her from behind...."
                            elif position_choice.name == "Doggy Anal Dildo DP":
                                $ VTanaltt = f"{{image=yesanal_small}} You fuck her {random_anal_word} as you thrust the dildo into her pussy, her body overwhelmed by the sheer pleasure of it all...."
                            elif position_choice.name == "Prone Anal":
                                $ VTanaltt = f"{{image=yesanal_small}} Pinning her down, you thrust into her {random_anal_word} with savage intensity, her body trembling with each thrust...."
                            $ VTanalcondom = "bare"
                            if mc.condom == True:
                                $ VTanalcondom = "wrapped"
                            $ VTanaltt += f"\n{{image=yesanal_small}} You fuck her {random_anal_word} with your "+VTanalcondom+" cock."

                if 'climax_type' in globals():
                    if climax_type == "anal":
                            if mc.condom == False:
                                if person.anal_virgin ==0:
                                    $ VTanalst = "handass"
                                    $ VTanaltt = f"{{image=handprint_token_small}} You unleash a torrent of cum into her virgin asshole, claiming her innocence as your own! \n Her tight {random_anal_word} is flooded with your seed, her juices mixing with your cum in a sweet, sticky mess!"
                                else:
                                    if person.anal_cum >=3:
                                        $ VTanalst = "ahegaopeach"
                                    else:
                                        $ VTanalst = "handass"
                                    $ VTanaltt = f"{{image=handass_small}} You erupt into her {random_anal_word}, flooding her bowels with a tidal wave of cum that threatens to overflow her very being!"
                            else:
                                $ VTanalst = "yesanal"
                                $ VTanaltt = f"{{image=yesanal_small}} You fill the condom with your scorching hot seed, feeling her pulse around you as she milks you for every last drop!"
                    if climax_type =="body":
                        $ VTanalst = "yesanal"
                        if mc.condom == False:
                            $ VTanaltt = f"{{image=bareback_small}} You explode in a frenzy of cum, covering her body in a sticky film of your seed as you mark her as your own."
                        else:
                            $ VTanaltt = f"{{image=spreadvag_small}} You fill the condom to bursting as you pull out of her, the latex straining to contain the sheer force of your ejaculation."

                if VTanalat=="sexualized" and VTorifice_current == "Anal":
                    if person.anal_virgin == 0:
                            $ person.anal_virgin = 1
                            $ person.anal_first = mc.name
                    imagebutton:
                        pos(597, 166)
                        idle VTanalst
                        action NullAction()
                        tooltip VTanaltt

                if VTanalat=="talking" :
                    # Determine Arousal Status and Cum Status                   
                    if person.arousal_perc >= 59:
                        if person.anal_cum == 0:
                            $ VTanalst = "yesanal"
                            if person.anal_virgin == 0:
                                $ VTanaltt += f"\n{{image=virgin_anal_small}} Her {random_anal_word} is a ripe, juicy peach, begging to be devoured by your hungry {random_condom_word} {random_cock_word}!"
                            else:
                                if person.anal_first == mc.name:
                                    $ VTanaltt += f"\n{{image=handprint_token_small}} Her {random_anal_word} sways hypnotically, beckoning you to come and take her again!"
                                else:
                                    $ VTanaltt += f"\n{{image=analclaimed_small}} Her {random_anal_word} is a gaping, hungry hole, begging to be filled by your {random_condom_word} {random_cock_word}.\nCome and take her, she's all yours!"
                            if person.energy < 20 and person.had_sex_today:
                                $ VTanaltt += f"\n{{image=ahegaoanal_small}} She's lost in a haze of post-coital bliss, her body still trembling from the aftershocks of your lovemaking."
                        else:
                            $ VTanalst = "handass"
                            if person.anal_cum==1:
                                $ VTanaltt += f"\n{{image=handass_small}} She's still reeling from the dose of your protein in her {random_anal_word}, her body craving more of your cum."
                            else:
                                if person.anal_cum>3:
                                    $ VTanalst = "ahegaopeach"
                                    $ VTanaltt += f"\n{{image=ahegaoanal_small}} Her eyes are hungry for more cum, her belly bulging with the {person.anal_cum} doses of your seed swimming in her {random_anal_word}."
                                else:
                                    $ VTanaltt += f"\n{{image=ahegaoanal_small}} She's addicted to your cum, her body craving the next fix of your seed.\nShe has {person.anal_cum} doses of your cum swimming in her {random_anal_word}."
                        if person.energy < 20 and person.had_sex_today:
                            $ VTanaltt += f"\n{{image=ahegaoanal_small}} She's lost in a haze of post-coital bliss, her body still trembling from the aftershocks of your lovemaking."
                    else:
                        if person.anal_cum > 0:
                            if person.anal_cum == 1:
                                $ VTanalst = "handass"
                                $ VTanaltt += f"\n{{image=handass_small}} She looks at you with lust in her eyes, her body still feeling the effects of your cum in her {random_anal_word}."
                            else:
                                if person.anal_cum>3:
                                    $ VTanalst = "ahegaopeach"
                                    $ VTanaltt += f"\n{{image=ahegaoanal_small}} Her belly is bulging with the {person.anal_cum} doses of your cum swimming in her {random_anal_word}."
                                else:
                                    $ VTanaltt += f"\n{{image=ahegaoanal_small}} She has {person.anal_cum} doses of your cum swimming in her {random_anal_word}, her body craving more of your seed."
                        else:
                            if perk_system.has_ability_perk("Midnight Mirage") or (person.has_broken_taboo("anal_sex")):
                                if person.anal_virgin == 0 and not person.had_sex_today:
                                    $ VTanaltt += f"\n{{image=virgin_anal_small}} She looks at you with lust in her innocent, hungry eyes, her body begging to be deflowered."
                                elif person.anal_first == mc.name and not person.had_sex_today:
                                    $ VTanaltt += f"\n{{image=handprint_token_small}} She's drooling at the thought of your {random_condom_word} {random_cock_word}, her eyes undressing you with desire."
                                elif not person.had_sex_today:
                                    $ VTanaltt += f"\n{{image=handass_small}} She's curious about your {random_condom_word} {random_cock_word}, her body wondering what it would be like to be fucked by you."
                                if person.energy < 20 and person.had_sex_today:
                                    $ VTanaltt += f"\n{{image=ahegaoanal_small}} She's lost in a haze of post-coital bliss, her body still trembling from the aftershocks of your lovemaking."
                    imagebutton:
                        pos(597, 166)
                        idle VTanalst
                        action NullAction()
                        tooltip VTanaltt
    #### Had sex today
            if getattr(persistent, "hadsextoday")==1:
                if person.had_sex_today:
                    imagebutton:
                        pos(634, 166)
                        idle "hadsextoday"
                        action NullAction()
                        tooltip f"{{image=hadsextoday_small}} You had fun with her today."  
    ### Thermometer - Arousal
            if getattr(persistent, "tempnormal")==1:
                $ arousal_levels = [
                    (100, "tempbroke", f"{{image=creamcherry_small}} Her brain melted! Way to go!"),
                    (90, "temp90", f"{{image=vtcherries_small}} She is on the verge of cumming!"),
                    (80, "temp80", f"{{image=vtcherries_small}} She is extremely horny."),
                    (70, "temp70", f"{{image=vtcherries_small}} She is really aroused."),
                    (0, "tempnormal", f"{{image=vtcherries_small}} She seems okay, really.")
                ]
                $ VTtempst, VTtemptt = next(((tempst, temptt) for threshold, tempst, temptt in arousal_levels if person.arousal > threshold), ("tempblank", f"{{image=vtcherries_small}} She is completely sedated."))

                imagebutton:
                    pos(681, 166)
                    idle VTtempst
                    action NullAction()
                    tooltip VTtemptt
    ######## Exhibitionist Fetish
            if getattr(persistent, "knowbody")==1:
                $ VTexhibitfetishat = "talking"
                $ VTexhibitfetishst = "knowbody"
                $ VTexhibitfetishtt = f"{{image=question_mark_small}} Does she like public sex?"
                #The Requirements to Unlock
                if person.sexy_opinions.get("public sex")==None:
                    $ VTexhibitfetishst = "knowbody"
                    $ VTexhibitfetishtt = f"{{image=question_mark_small}} Does she like public sex?"
                else:
                    if person.sexy_opinions.get("public sex")[1]==True:
                        if person.has_exhibition_fetish:
                            if person.days_since_event("LastExhibitionFetish") > 10:
                                $ VTexhibitfetishst = "vtcherries"
                                $ VTexhibitfetishtt = f"{{image=progress_token_small}} Ugh my skin is itchy I need a pearl necklace soon!"
                            else:
                                $ VTexhibitfetishst = "creamcherry"
                                $ VTexhibitfetishtt = "*fetish 'a'salted complete*"
                                $ VTexhibitfetishtt = f"{{image=creamcherry_small}} MMmmMm my skin feels good."
                            $ VTexhibitfetishtt += f"\n{{image=creamcherry_small}} Will trigger in another "+str(person.event_triggers_dict.get("LastExhibitionFetish", 0)  - day)+" days!"
                        else:
                            #List of everything one needs to make Exhibition happen
                            if (
                                person.sex_record.get("Public Sex", 0) >= 20
                                and person.has_broken_taboo("sucking_cock")
                                and person.has_broken_taboo("vaginal_sex")
                                and person.has_broken_taboo("anal_sex")
                                and person.has_broken_taboo("bare_tits")
                                and person.has_broken_taboo("bare_pussy")
                                and person.sluttiness >= 60
                                and person.oral_sex_skill >= 4
                                and person.vaginal_sex_skill >= 4
                                and person.anal_sex_skill >= 4
                                and person.opinion.public_sex >= 2
                                and person.opinion.not_wearing_anything >= 2
                                and person.opinion.not_wearing_underwear >= 2
                                and person.opinion.showing_her_ass >= 2
                                and person.opinion.showing_her_tits >= 2
                                and person.opinion.skimpy_outfits >= 2
                                and person.opinion.skimpy_uniforms >= 2
                                and person.opinion.masturbating >= 2
                            ):
                                $ VTexhibitfetishst = "vtcherries"
                                if person.event_triggers_dict.get("exhibition_fetish_locked", 0) > day and person.event_triggers_dict.get("VT_exhibition_fetish_start", False) is True:
                                    $ VTexhibitfetishtt = f"{{image=creamcherry_small}} Exhibition Fetish Intro will unlock in "+str(person.event_triggers_dict.get("exhibition_fetish_locked", 0)  - day)+" days!"
                                else:
                                    $ VTexhibitfetishtt = f"{{image=creamcherry_small}} She meets the requirements! \n It will unlock the following day."
                            else:
                                $ VTexhibitfetishtt = f"{{image=question_mark_small}} Unlock the Exhibition Fetish?"
                                #the amount of sex related to fetish
                                if person.sex_record.get("Public Sex", 0) < 20:
                                    $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Have sex with her in public places {20 - person.sex_record.get('Public Sex', 0)} more times!"
                                #the taboos related to fetish
                                if not person.has_broken_taboo("sucking_cock"):
                                    $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Get her to suck your cock!"
                                elif not person.has_broken_taboo("vaginal_sex"):
                                    $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Have vaginal sex with her!"
                                elif not person.has_broken_taboo("anal_sex"):
                                    $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Have anal sex with her!"
                                elif not person.has_broken_taboo("bare_tits"):
                                    $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Get her to show you her tits!"
                                elif not person.has_broken_taboo("bare_pussy"):
                                    $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Get her to show you her pussy!"
                                #the sluttiness required
                                if person.sluttiness < 60:
                                    $ VTexhibitfetishtt += f"\n{{image=gold_heart_token_small}} Corrupt her innocence by {60 - person.sluttiness} points!"
                                #the skills required
                                if person.oral_sex_skill < 4:
                                    $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Boost her Oral Skills ({4 - person.oral_sex_skill} to go)!"
                                if person.vaginal_sex_skill < 4:
                                    $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Unlock her Vaginal Secrets ({4 - person.vaginal_sex_skill} to go)!"
                                if person.anal_sex_skill < 4:
                                    $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Master her Anal Delights ({4 - person.anal_sex_skill} to go)!"
                                # Opinions
                                if not person.known_opinion("public sex"):
                                    $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Ask about public sex."
                                elif person.opinion.public_sex < 2:
                                    $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Get her to love public sex."

                                elif not person.known_opinion("not wearing underwear"):
                                    $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Ask about going commando."
                                elif person.opinion.not_wearing_underwear < 2:
                                    $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Get her to love going without underwear."

                                elif not person.known_opinion("not wearing anything"):
                                    $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Ask about nudity."
                                elif person.opinion.not_wearing_anything < 2:
                                    $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Get her to love being naked."

                                elif not person.known_opinion("showing her ass"):
                                    $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Ask about showing her ass."
                                elif person.opinion.showing_her_ass < 2:
                                    $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Get her to love showing off her ass."

                                elif not person.known_opinion("showing her tits"):
                                    $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Ask about flashing her tits."
                                elif person.opinion.showing_her_tits < 2:
                                    $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Get her to love showing off her tits."

                                elif not person.known_opinion("skimpy outfits"):
                                    $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Ask about sexy outfits."
                                elif person.opinion.skimpy_outfits < 2:
                                    $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Get her to love wearing sexy outfits."

                                elif not person.known_opinion("skimpy uniforms"):
                                    $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Ask about sexy uniforms."
                                elif person.opinion.skimpy_uniforms < 2:
                                    $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Get her to love wearing sexy uniforms."

                #the interactive icons during sex stuff
                if 'position_choice' in globals():
                    if hasattr(position_choice, 'skill_tag'):
                        $ VTexhibitfetishat = "sexualized"
                else:
                    $ VTexhibitfetishat="talking"

                #Determine Clothing Status                    
                if (person.tits_visible and person.vagina_visible) or (person.tits_available and person.vagina_available and person.vagina_visible and perk_system.has_ability_perk("Bald Eagle Perception") and perk_system.has_ability_perk("Strap Sense")):
                    $ VTexhibitfetishst = "nudebody"
                    $ VTexhibitfetishtt += f"\n{{image=vtcherries_small}} You're treated to a breathtaking view of her luscious tits and juicy {random_pussy_word}."
                    if person.arousal_perc >= 59:
                        $ VTexhibitfetishtt += f"\n{{image=vtcherries_small}} Her nipples are rock-hard and her {random_pussy_word} is dripping with desire, begging to be devoured by your hungry {random_cock_word}."
                    if person.vaginal_cum >0:
                        if person.vaginal_cum >3:
                            $ VTexhibitfetishtt += f"\n{{image=openvag_small}} Your cum is oozing out of her {random_pussy_word}, a sticky reminder of the intense pleasure you shared."
                        else:
                            $ VTexhibitfetishtt += f"\n{{image=openvag_small}} Your cum is starting to drip from her {random_pussy_word}, a tantalizing sight that fills you with satisfaction and pleasure."
                else:
                    if person.vagina_visible or (person.vagina_available and perk_system.has_ability_perk("Bald Eagle Perception")):
                        $ VTexhibitfetishst = "bodybra"
                        if person.vaginal_cum >0:
                            if person.vaginal_cum >3:
                                $ VTexhibitfetishtt += f"\n{{image=openvag_small}} Your cum is oozing out of her {random_pussy_word}, a sticky reminder of the intense pleasure you shared."
                            else:
                                $ VTexhibitfetishtt += f"\n{{image=openvag_small}} Your cum is starting to drip from her {random_pussy_word}, a tantalizing sight that fills you with satisfaction and pleasure."
                        else:
                            if person.arousal_perc >= 59:
                                $ VTexhibitfetishtt += f"\n{{image=spreadvag_small}} Her {random_pussy_word} is a sopping wet, juicy paradise, begging to be explored by your eager fingers or {random_cock_word}."
                            else:
                                $ VTexhibitfetishtt += f"\n{{image=spreadvag_small}} You catch a glimpse of her {random_pussy_word}, a tantalizing tease of the pleasure that's to come."
                    elif person.tits_visible or (person.tits_available and perk_system.has_ability_perk("Strap Sense")) :
                        $ VTexhibitfetishst = "bodypanties"
                        $ VTexhibitfetishtt += f"\n{{image=vtcherries_small}} You're treated to a breathtaking view of her luscious tits, her nipples begging to be sucked and licked."
                        if person.arousal_perc >= 59:
                            $ VTexhibitfetishtt += f"\n{{image=vtcherries_small}} Her nipples are rock-hard, a clear sign that she's ready to be taken to the next level of pleasure."
                    else:
                        if perk_system.has_ability_perk("Bald Eagle Perception") or perk_system.has_ability_perk("Strap Sense"):
                            $ VTexhibitfetishst = "bodyconcealed"
                            $ VTexhibitfetishtt += f"\n{{image=knowbody_small}} She's hiding her treasures beneath a layer of clothing, but you can sense the heat emanating from her body."
                        else:
                            $ VTexhibitfetishst = "knowbody"
                            $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} She's a mystery waiting to be unraveled, her body hidden beneath a layer of clothing that's just begging to be stripped away."

                if VTexhibitfetishat=="sexualized":
                    imagebutton:
                        pos(718, 166)
                        idle VTexhibitfetishst
                        action NullAction()
                        tooltip VTexhibitfetishtt

                if VTexhibitfetishat=="talking":
                    imagebutton:
                        pos(718, 166)
                        idle VTexhibitfetishst
                        action NullAction()
                        tooltip VTexhibitfetishtt

    ###### Cum Fetish
            if getattr(persistent, "knowcumfetish")==1:
                $ VTcumfetishat = "talking"
                $ VTcumfetishst = "knowlips"
                $ VTcumfetishtt = f"{{image=question_mark_small}} Does she like giving blow jobs?"
                if person.sexy_opinions.get("giving blowjobs")==None:
                    $ VTcumfetishst = "knowlips"
                    $ VTcumfetishtt = f"{{image=question_mark_small}} Does she like giving blow jobs?"
                else:
                    if person.sexy_opinions.get("giving blowjobs")[1]==True:
                        if person.has_cum_fetish:
                            if person.days_since_event("LastCumFetish") > 10:
                                $ VTcumfetishst = "vtcherries"
                                $ VTcumfetishtt = f"{{image=progress_token_small}} MMmmMm going to need your yummy\nlollipop in my mouth in soon!"
                            else:
                                $ VTcumfetishst = "creamcherry"
                                $ VTcumfetishtt = "*fetish 'salty' lipbalm complete!*"
                                $ VTcumfetishtt += f"\n{{image=creamcherry_small}} MMmmMm still taste you in my mouth..."
                        
                            $ VTcumfetishtt += f"\n{{image=creamcherry_small}} Will trigger in another "+str(person.event_triggers_dict.get("LastCumFetish", 0)  - day)+" days!"
                        else:
                            #List of everything one needs to make Cum Fetish happen
                            if (
                                person.cum_exposure_count >=20
                                and person.has_broken_taboo("sucking_cock")
                                and person.has_broken_taboo("condomless_sex")
                                and person.has_broken_taboo("anal_sex")
                                and person.has_broken_taboo("vaginal_sex")
                                and person.has_broken_taboo("bare_tits")
                                and person.has_broken_taboo("bare_pussy")
                                and person.sluttiness >= 60
                                and person.oral_sex_skill >= 4
                                and person.opinion.giving_blowjobs >= 2
                                and person.opinion.being_covered_in_cum >= 2
                                and person.opinion.cum_facials >= 2
                                and person.opinion.drinking_cum >= 2
                                and person.opinion.showing_her_tits >= 2
                                and person.opinion.creampies >= 2
                                and person.opinion.anal_creampies >= 2
                                and person.opinion.bareback_sex >= 2
                                and person.opinion.giving_handjobs >= 2 ):
                                $ VTcumfetishst = "bitelip"
                                if person.event_triggers_dict.get("cum_fetish_locked", 0) > day and person.event_triggers_dict.get("VT_cum_fetish_start", False) is True:
                                    $ VTcumfetishtt = f"{{image=creamcherry_small}} Cum Fetish Intro will unlock in "+str(person.event_triggers_dict.get("cum_fetish_locked", 0)  - day)+" days!"
                                else:
                                    $ VTcumfetishtt = f"{{image=creamcherry_small}} She meets the requirements! \n It will unlock the following day."
                            else:
                                $ VTcumfetishtt = f"{{image=question_mark_small}} Unlock the Cum Fetish?"
                                #the amount of sex related to fetish
                                if person.cum_exposure_count < 20:
                                    $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Feed her, spray her, or fill her\n with your cum {20 - person.cum_exposure_count} more times!"
                                #the taboos related to fetish
                                if not person.has_broken_taboo("sucking_cock"):
                                    $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Get her to suck your cock!"
                                elif not person.has_broken_taboo("condomless_sex"):
                                    $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Lose the condom!"
                                elif not person.has_broken_taboo("vaginal_sex"):
                                    $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Have vaginal sex with her!"
                                elif not person.has_broken_taboo("anal_sex"):
                                    $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Have anal sex with her!"
                                elif not person.has_broken_taboo("bare_tits"):
                                    $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Get her to show you her tits!"
                                elif not person.has_broken_taboo("bare_pussy"):
                                    $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Get her to show you her pussy!"
                                #the sluttiness required
                                if person.sluttiness < 60:
                                    $ VTcumfetishtt += f"\n{{image=gold_heart_token_small}} Corrupt her innocence by {60 - person.sluttiness} points!"
                                #the skills required
                                if person.oral_sex_skill < 4:
                                    $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Boost her Oral Skills ({4 - person.oral_sex_skill} to go)!"
                                #the opinions required
                                if not person.known_opinion("giving blowjobs"):
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Ask about giving blowjobs."
                                elif person.opinion.giving_blowjobs < 2:
                                    $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Get her to love blowjobs."

                                elif not person.known_opinion("being covered in cum"):
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Ask about being covered in cum."
                                elif person.opinion.being_covered_in_cum < 2:
                                    $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Get her to love being covered in cum."

                                elif not person.known_opinion("cum facials"):
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Ask about cum facials."
                                elif person.opinion.cum_facials < 2:
                                    $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Get her to love cum facials."

                                elif not person.known_opinion("drinking cum"):
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Ask about drinking cum."
                                elif person.opinion.drinking_cum < 2:
                                    $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Get her to love drinking cum."

                                elif not person.known_opinion("showing her tits"):
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Ask about flashing her tits."
                                elif person.opinion.showing_her_tits < 2:
                                    $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Get her to love showing off her tits."

                                elif not person.known_opinion("creampies"):
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Ask about vaginal creampies."
                                elif person.opinion.creampies < 2:
                                    $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Get her to love vaginal creampies."

                                elif not person.known_opinion("anal creampies"):
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Ask about anal creampies."
                                elif person.opinion.anal_creampies < 2:
                                    $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Get her to love anal creampies."

                                elif not person.known_opinion("giving handjobs"):
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Ask about handjobs."
                                elif person.opinion.giving_handjobs < 2:
                                    $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Get her to love handjobs."

                                elif not person.known_opinion("bareback sex"):
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Ask about bareback sex."
                                elif person.opinion.bareback_sex < 2:
                                    $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Get her to love bareback sex."

                #the interactive icons during sex stuff
                if 'position_choice' in globals():
                    $ VTcumfetishat = "sexualized"
                    if person.oral_cum ==1:
                        $ VTcumfetishst = "bitelip"
                    if person.oral_cum >1:
                        $ VTcumfetishst = "ahegaomouth"
                else:
                    $ VTcumfetishat = "talking"

                if VTcumfetishat=="sexualized":
                    if person.oral_cum >0:
                        if person.oral_cum == 1:
                            $ VTcumfetishtt += f"\n{{image=ahegaomouth_small}} Your cum is digesting in her stomach."
                        else:
                            $ VTcumfetishtt += f"\n{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in her stomach."
                    imagebutton:
                        pos(755, 166)
                        idle VTcumfetishst
                        action NullAction()
                        tooltip VTcumfetishtt

                if VTcumfetishat=="talking":
                    if person.oral_cum >0:
                        if person.oral_cum == 1:
                            $ VTcumfetishtt += f"\n{{image=ahegaomouth_small}}She has a dose of your protein in her belly."
                        else:
                            $ VTcumfetishtt += f"\n{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in her belly."
                    imagebutton:
                        pos(755, 166)
                        idle VTcumfetishst
                        action NullAction()
                        tooltip VTcumfetishtt
                    if person.oral_cum >1:
                        imagebutton:
                            pos(755, 166)
                            idle "bc_cum"
                            action NullAction()
                            tooltip VTcumfetishtt
    ###### Vaginal Fetish
            if getattr(persistent, "knowvaginalfetish")==1:
                $ VTvaginalfetishat = "talking"
                $ VTvaginalfetishst = "knowpeach"
                $ VTvaginalfetishtt =  f"{{image=question_mark_small}} Her thoughts on vaginal sex?"
                #The Requirements to Unlock
                if person.sexy_opinions.get("vaginal sex")==None:
                    $ VTvaginalfetishst = "knowpeach"
                    $ VTvaginalfetishtt = f"{{image=question_mark_small}} Her thoughts on vaginal sex?"
                else:
                    if person.sexy_opinions.get("vaginal sex")[1]==True:
                        if person.has_vaginal_fetish or vaginal_fetish_role in person.special_role:
                            if person.days_since_event("LastVaginalFetish") > 10:
                                if person.vaginal_cum == 0:
                                    $ VTvaginalfetishst = "vtcherries"
                                    $ VTvaginalfetishtt = f"{{image=progress_token_small}} My {random_pussy_word} is aching for your {random_cock_word}... I need to feel you inside me."
                                else:
                                    $ VTvaginalfetishst = "creamcherry"
                                    $ VTvaginalfetishtt = f"{{image=triskelion_token_small}} The memory of your {random_cock_word} is still etched in my {random_pussy_word}... I can almost feel your presence."
                            else:
                                if person.vaginal_cum > 0:
                                    $ VTvaginalfetishst = "creamcherry"
                                    $ VTvaginalfetishtt = "*fetish 'puss'salted complete*"
                                    $ VTvaginalfetishtt += f"\n{{image=creamcherry_small}} My {random_pussy_word} is still throbbing from your {random_cock_word}... the sensation lingers, a delicious echo."
                                else:
                                    $ VTvaginalfetishst = "vtcherries"
                                    $ VTvaginalfetishtt = f"{{image=creamcherry_small}} I crave the feeling of your {random_cock_word} sliding into my {random_pussy_word}, stretching me, filling me..."
                            $ VTvaginalfetishtt += f"\n{{image=creamcherry_small}} Will trigger in another "+str(person.event_triggers_dict.get("LastVaginalFetish", 0)  - day)+" days!"
                        else:
                            #List of everything one needs to make Vaginal  Fetish happen
                            if (
                                (person.vaginal_sex_count >= 10 or person.vaginal_creampie_count >= 10)
                                and person.vaginal_sex_skill >= 4
                                and person.is_willing(missionary)
                                and person.has_broken_taboo("vaginal_sex")
                                and person.sluttiness >= 60
                                and (person.opinion.vaginal_sex >= 2 or person.opinion.creampies >= 2)
                                and person.opinion.bareback_sex >= 2
                                and person.opinion.showing_her_ass >= 2
                                and person.opinion.missionary_style >= 2
                            ):
                                $ VTvaginalfetishst = "vtcherries"
                                if person.event_triggers_dict.get("vaginal_fetish_locked", 0) > day and person.event_triggers_dict.get("VT_vaginal_fetish_start", False) is True:
                                    $ VTvaginalfetishtt = f"{{image=creamcherry_small}} Vaginal Fetish Intro will unlock in "+str(person.event_triggers_dict.get("vaginal_fetish_locked", 0)  - day)+" days!"
                                else:
                                    $ VTvaginalfetishtt = f"{{image=creamcherry_small}} She meets the requirements! \nIt will unlock the following day."
                            else:
                                $ VTvaginalfetishtt = f"{{image=question_mark_small}} Unlock the Vaginal Fetish?"
                                #the amount of sex related to fetish
                                if person.vaginal_sex_count < 10 and person.vaginal_creampie_count < 10:
                                    $ VTvaginalfetishtt += f"\n{{image=progress_token_small}} Make love to your Vaginal Queen!"
                                    $ VTvaginalfetishtt += f"\n{{image=triskelion_token_small}} Have vaginal sex with her "+str(10 - person.vaginal_sex_count)+" more times!"
                                    $ VTvaginalfetishtt += f"\n OR "
                                    $ VTvaginalfetishtt += f"\n{{image=triskelion_token_small}} Fill her {random_pussy_word} full of cum "+str(10 - person.vaginal_creampie_count)+" more times!"
                                #the skills required
                                if person.vaginal_sex_skill < 4:
                                    $ VTvaginalfetishtt += f"\n{{image=triskelion_token_small}} Boost her Vaginal Sex Skills ({4 - person.vaginal_sex_skill} to go)!"
                                #sex position related to fetish
                                if not person.is_willing(missionary):
                                    $ VTvaginalfetishtt += f"\n{{image=progress_token_small}} She needs to be willing to do missionary position."
                                #the taboos related to fetish
                                if not person.has_broken_taboo("vaginal_sex"):
                                    $ VTvaginalfetishtt += f"\n{{image=triskelion_token_small}} Have vaginal sex with her!"
                                #the sluttiness required
                                if person.sluttiness < 60:
                                    $ VTvaginalfetishtt += f"\n{{image=gold_heart_token_small}} Corrupt her innocence by {60 - person.sluttiness} /60 points!"
                                #the opinions required
                                if person.opinion.vaginal_sex < 2  or person.opinion.creampies < 2:
                                    $ VTvaginalfetishtt += f"\n Make her opinion loves Vaginal Sex or Creampies"
                                    if not person.known_opinion("vaginal sex"):
                                        $ VTvaginalfetishtt += f"\n{{image=question_mark_small}} Ask about Vaginal Sex."
                                    elif person.opinion.vaginal_sex < 2:
                                        $ VTvaginalfetishtt += f"\n{{image=red_heart_token_small}} Get her to love vaginal sex."
                                    if not person.known_opinion("creampies"):
                                        $ VTvaginalfetishtt += f"\n{{image=question_mark_small}} Ask about Vaginal Creampies."
                                    elif person.opinion.creampies < 2:
                                        $ VTvaginalfetishtt += f"\n{{image=red_heart_token_small}} Get her to love vaginal creampies."

                                elif not person.known_opinion("bareback sex"):
                                    $ VTvaginalfetishtt += f"\n{{image=red_heart_token_small}} Ask about Bareback Sex."
                                elif person.opinion.bareback_sex < 2:
                                    $ VTvaginalfetishtt += f"\n{{image=red_heart_token_small}} Get her to love bareback sex."

                                elif not person.known_opinion("showing her ass"):
                                    $ VTvaginalfetishtt += f"\n{{image=question_mark_small}} Ask about showing her ass."
                                elif person.opinion.showing_her_ass < 2:
                                    $ VTvaginalfetishtt += f"\n{{image=red_heart_token_small}} Get her to love showing her ass."

                                elif not person.known_opinion("missionary style sex"):
                                    $ VTvaginalfetishtt += f"\n{{image=question_mark_small}} Ask about Missionary Style Sex."
                                elif person.opinion.missionary_style < 2:
                                    $ VTvaginalfetishtt += f"\n{{image=red_heart_token_small}} Get her to love Missionary Style Sex."

                #the interactive icons during sex stuff
                if 'position_choice' in globals():
                    $ VTvaginalfetishat = "sexualized"
                else:
                    $ VTvaginalfetishat = "talking"
                if VTvaginalfetishat=="sexualized":
                    if person.vaginal_cum >0:
                        if person.vaginal_cum == 1:
                            $ VTvaginalfetishst = "openvag"
                            $ VTvaginalfetishtt += f"\n{{image=beezee_token_small}} Your cum is swimming in her"+VTbreedfertile+VTpro+" womb."
                        else:
                            $ VTvaginalfetishst = "ahegaovag"
                            $ VTvaginalfetishtt += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."
                    imagebutton:
                        pos(792, 166)
                        idle VTvaginalfetishst
                        action NullAction()
                        tooltip VTvaginalfetishtt

                if VTvaginalfetishat=="talking":
                    if person.vaginal_cum >0:
                        if person.vaginal_cum == 1:
                            $ VTvaginalfetishtt += f"\n{{image=beezee_token_small}} Your cum is swimming in her"+VTbreedfertile+VTpro+" womb."
                        else:
                            $ VTvaginalfetishtt += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n is swimming in her"+VTbreedfertile+VTpro+" womb."
                    imagebutton:
                        pos(792, 166)
                        idle VTvaginalfetishst
                        action NullAction()
                        tooltip VTvaginalfetishtt
    ###### Anal Fetish
            if getattr(persistent, "knowanalfetish")==1:
                $ VTanalfetishat = "talking"
                $ VTanalfetishst = "knowpeach"
                $ VTanalfetishtt = f"{{image=question_mark_small}} Her thoughts on anal sex?"
                #The Requirements to Unlock
                if person.sexy_opinions.get("anal sex")==None:
                    $ VTanalfetishst = "knowpeach"
                    $ VTanalfetishtt = f"{{image=question_mark_small}} Her thoughts on anal sex?"
                else:
                    if person.sexy_opinions.get("anal sex")[1]==True:
                        if person.has_anal_fetish:
                            $ VTanalfetishst = "vtcherries"
                            $ VTanalfetishtt = f"\n{{image=triskelion_token_small}} mmmm stick your cock in my ass!"
                            if person.days_since_event("LastAnalFetish") > 10:
                                if person.anal_cum == 0:
                                    $ VTanalfetishst = "vtcherries"
                                    $ VTanalfetishtt = f"{{image=progress_token_small}} MMmmMm going to need your yummy\ncock in my ass soon!"
                                else:
                                    $ VTanalfetishst = "creamcherry"
                                    $ VTanalfetishtt = f"{{image=triskelion_token_small}} MMmmMm still feel your juice in my ass!"
                            else:
                                $ VTanalfetishst = "creamcherry"
                                $ VTanalfetishtt = "*fetish 'ass'salted complete*"
                                $ VTanalfetishtt += f"\n{{image=creamcherry_small}} MMmmMm my ass still molded to your cock."
                            $ VTanalfetishtt += f"\n{{image=creamcherry_small}} Will trigger in another "+str(person.event_triggers_dict.get("LastAnalFetish", 0)  - day)+" days!"
                        else:
                            #List of everything one needs to make Anal  Fetish happen
                            if (
                                (person.anal_sex_count >= 10 or person.anal_creampie_count >= 10)
                                and person.anal_sex_skill >= 4
                                and person.is_willing(doggy_anal)
                                and person.has_broken_taboo("anal_sex")
                                and person.sluttiness >= 60
                                and (person.opinion.anal_sex >= 2 or person.opinion.anal_creampies >= 2)
                                and person.opinion.doggy_style >= 2
                                and person.opinion.showing_her_ass >= 2
                            ):
                                $ VTanalfetishst = "vtcherries"
                                if person.event_triggers_dict.get("anal_fetish_locked", 0) > day and person.event_triggers_dict.get("VT_anal_fetish_start", False) is True:
                                    $ VTanalfetishtt = f"{{image=creamcherry_small}} Anal Fetish Intro will unlock in "+str(person.event_triggers_dict.get("anal_fetish_locked", 0)  - day)+" days!"
                                else:
                                    $ VTanalfetishtt = f"{{image=creamcherry_small}} She meets the requirements! \n It will unlock the following day."
                            else:
                                $ VTanalfetishtt = f"{{image=question_mark_small}} Unlock the Anal Fetish?"
                                #the amount of sex related to fetish
                                if person.anal_sex_count < 10 or person.anal_creampie_count < 10:
                                    $ VTanalfetishtt += f"\n{{image=progress_token_small}} Sodomize your Anal Queen!"
                                    $ VTanalfetishtt += f"\n{{image=triskelion_token_small}} Have anal sex with her "+str(10 - person.anal_sex_count)+" more times!"
                                    $ VTanalfetishtt += f"\n OR "
                                    $ VTanalfetishtt += f"\n{{image=triskelion_token_small}} Fill her bowels full of cum "+str(10 - person.anal_creampie_count)+" more times!"
                                #the skills required
                                if person.anal_sex_skill < 4:
                                    $ VTanalfetishtt += f"\n{{image=triskelion_token_small}} Boost her Anal Sex Skills ({4 - person.anal_sex_skill} to go)!"
                                #sex position related to fetish
                                if not person.is_willing(doggy_anal):
                                    $ VTanalfetishtt += f"\n{{image=progress_token_small}} She needs to be willing to do doggy style position."
                                #the taboos related to fetish
                                if not person.has_broken_taboo("anal_sex"):
                                    $ VTanalfetishtt += f"\n{{image=triskelion_token_small}} Have anal sex with her!"
                                #the sluttiness required
                                if person.sluttiness < 60:
                                    $ VTanalfetishtt += f"\n{{image=gold_heart_token_small}} Corrupt her innocence by {60 - person.sluttiness} points!"
                                #the opinions required
                                if person.opinion.anal_sex < 2  or person.opinion.anal_creampies < 2:
                                    if not person.known_opinion("anal sex"):
                                        $ VTanalfetishtt += f"\n{{image=question_mark_small}} Ask about Anal Sex."
                                    elif person.opinion.anal_sex < 2:
                                        $ VTanalfetishtt += f"\n{{image=red_heart_token_small}} Get her to love anal sex."
                                    if not person.known_opinion("anal creampies"):
                                        $ VTanalfetishtt += f"\n{{image=question_mark_small}} Ask about Anal Creampies."
                                    elif person.opinion.anal_creampies < 2:
                                        $ VTanalfetishtt += f"\n{{image=red_heart_token_small}} Get her to love anal creampies."

                                elif not person.known_opinion("showing her ass"):
                                    $ VTanalfetishtt += f"\n{{image=question_mark_small}} Ask about showing her ass."
                                elif person.opinion.showing_her_ass < 2:
                                    $ VTanalfetishtt += f"\n{{image=red_heart_token_small}} Get her to love showing her ass."

                                elif not person.known_opinion("doggystyle"):
                                    $ VTanalfetishtt += f"\n{{image=question_mark_small}} Ask about Doggy Style Sex."
                                elif person.opinion.doggy_style < 2:
                                    $ VTanalfetishtt += f"\n{{image=red_heart_token_small}} Get her to love doggy style sex."
                #the interactive icons during sex stuff
                if 'position_choice' in globals():
                    $ VTanalfetishat = "sexualized"
                else:
                    $ VTanalfetishat = "talking"
                if VTanalfetishat=="sexualized":
                    if person.anal_cum ==1:
                        $ VTanalfetishst = "handass"
                        $ VTanalfetishtt += f"\n{{image=ahegaoanal_small}} Your cum is lubricating her bowels."
                    if person.anal_cum >1:
                        $ VTanalfetishtt += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n swimming in her bowels."
                    if person.anal_cum >3:
                        $ VTanalfetishst = "ahegaopeach"
                    imagebutton:
                        pos(829, 166)
                        idle VTanalfetishst
                        action NullAction()
                        tooltip VTanalfetishtt

                if VTanalfetishat=="talking":
                    if person.anal_cum ==1:
                        $ VTanalfetishtt += f"\n{{image=ahegaoanal_small}} Your cum is lubricating in her bowels."
                    if person.anal_cum >1:
                        $ VTanalfetishtt += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n swimming in her bowels."
                    imagebutton:
                        pos(829, 166)
                        idle VTanalfetishst
                        action NullAction()
                        tooltip VTanalfetishtt
    ###### Breeding Fetish
            if getattr(persistent, "knowbreedingfetish")==1 and persistent.pregnancy_pref > 0:
                $ VTbreedfetishat = "talking"
                $ VTbreedfetishst = "knowpeach"
                $ VTbreedfetishtt =  f"{{image=question_mark_small}} Her thoughts on vaginal sex?"
                #The Requirements to Unlock
                if person.sexy_opinions.get("vaginal sex")==None:
                    $ VTbreedfetishst = "knowpeach"
                    $ VTbreedfetishtt = f"{{image=question_mark_small}} Her thoughts on vaginal sex?"
                else:
                    if person.sexy_opinions.get("vaginal sex")[1]==True:
                        if person.has_breeding_fetish or breeding_fetish_role in person.special_role:
                            if person.days_since_event("LastBreedingFetish") > 10 and not person.is_pregnant:
                                if person.vaginal_cum == 0:
                                    $ VTbreedfetishst = "vtcherries"
                                    $ VTbreedfetishtt = f"{{image=progress_token_small}} My womb is craving your seed... fill me to the brim!"
                                else:
                                    $ VTbreedfetishst = "creamcherry"
                                    $ VTbreedfetishtt = f"{{image=triskelion_token_small}} Your cum is warming my belly... I can feel it trying to take root."
                            else:
                                if person.is_pregnant:
                                    $ VTbreedfetishst = "creamcherry"
                                    $ VTbreedfetishtt = "*fetish 'full'filled*"
                                    $ VTbreedfetishtt = f"{{image=creamcherry_small}} Blissful and bred... my womb is at peace."
                                else:
                                    if person.vaginal_cum > 0:
                                        $ VTbreedfetishst = "creamcherry"
                                        $ VTbreedfetishtt = "*fetish 'full'filled*"
                                        $ VTbreedfetishtt = f"{{image=creamcherry_small}} More, please... I'm not yet sated."
                                    else:
                                        $ VTbreedfetishst = "vtcherries"
                                        $ VTbreedfetishtt = f"{{image=creamcherry_small}} Claim me, breed me, fill me to overflowing!"
                                $ VTbreedfetishtt += f"\n{{image=creamcherry_small}} Will trigger in another "+str(person.event_triggers_dict.get("LastBreedingFetish", 0)  - day)+" days!"
                        else:
                            #List of everything one needs to make Breeding  Fetish happen
                            if (person.vaginal_creampie_count >= 10
                                and person.vaginal_sex_skill >= 4
                                and person.is_willing(missionary)
                                and person.has_broken_taboo("condomless_sex")
                                and person.has_broken_taboo("vaginal_sex")
                                and person.sluttiness >= 60
                                and person.opinion.vaginal_sex >= 2 
                                and person.opinion.creampies >= 2
                                and person.opinion.bareback_sex >= 2
                                and person.opinion.showing_her_ass >= 2
                                and person.opinion.missionary_style >= 2
                            ):
                                $ VTbreedfetishst = "vtcherries"
                                if person.event_triggers_dict.get("breeding_fetish_locked", 0) > day and person.event_triggers_dict.get("VT_breeding_fetish_start", False) is True:
                                    $ VTbreedfetishtt = f"{{image=creamcherry_small}} Breeding Fetish Intro will unlock in "+str(person.event_triggers_dict.get("breeding_fetish_locked", 0)  - day)+" days!"
                                else:
                                    $ VTbreedfetishtt = f"{{image=creamcherry_small}} She meets the requirements! \n It will unlock the following day."
                            else:
                                $ VTbreedfetishtt = f"{{image=question_mark_small}} Unlock the Breeding Fetish?"
                                #the amount of sex related to fetish
                                if person.vaginal_creampie_count<10:
                                    $ VTbreedfetishtt += f"\n{{image=triskelion_token_small}} Fill her baby room full of cum "+ str(10 - person.vaginal_creampie_count)+" more times!"
                                #the skills required
                                if person.vaginal_sex_skill < 4:
                                    $ VTbreedfetishtt += f"\n{{image=triskelion_token_small}} Boost her Vaginal Sex Skills ({4 - person.vaginal_sex_skill} to go)!"
                                #sex position related to fetish
                                if not person.is_willing(missionary):
                                    $ VTbreedfetishtt += f"\n{{image=progress_token_small}} She needs to be willing to do missionary position."
                                #the taboos related to fetish
                                if not person.has_broken_taboo("condomless_sex"):
                                    $ VTbreedfetishtt += f"\n{{image=triskelion_token_small}} Have condomless sex with her!"
                                if not person.has_broken_taboo("vaginal_sex"):
                                    $ VTbreedfetishtt += f"\n{{image=triskelion_token_small}} Have vaginal sex with her!"
                                #the sluttiness required
                                if person.sluttiness < 60:
                                    $ VTbreedfetishtt += f"\n{{image=gold_heart_token_small}} Corrupt her innocence by {60 - person.sluttiness} points!"
                                #the opinions required

                                if not person.known_opinion("vaginal sex"):
                                    $ VTbreedfetishtt += f"\n{{image=question_mark_small}} Ask about Vaginal Sex."
                                elif person.opinion.vaginal_sex < 2:
                                    $ VTbreedfetishtt += f"\n{{image=red_heart_token_small}} Get her to love vaginal sex."

                                elif not person.known_opinion("creampies"):
                                    $ VTbreedfetishtt += f"\n{{image=question_mark_small}} Ask about Vaginal Creampies."
                                elif person.opinion.creampies < 2:
                                    $ VTbreedfetishtt += f"\n{{image=red_heart_token_small}} Get her to love vaginal creampies."

                                elif not person.known_opinion("bareback sex"):
                                    $ VTbreedfetishtt += f"\n{{image=question_mark_small}} Ask about bareback sex."
                                elif person.opinion.showing_her_ass < 2:
                                    $ VTbreedfetishtt += f"\n{{image=red_heart_token_small}} Get her to love bareback sex."

                                elif not person.known_opinion("showing her ass"):
                                    $ VTbreedfetishtt += f"\n{{image=question_mark_small}} Ask about showing her ass."
                                elif person.opinion.showing_her_ass < 2:
                                    $ VTbreedfetishtt += f"\n{{image=red_heart_token_small}} Get her to love showing her ass."

                                elif not person.known_opinion("missionary style sex"):
                                    $ VTbreedfetishtt += f"\n{{image=question_mark_small}} Ask about Missionary Style Sex."
                                elif person.opinion.missionary_style < 2:
                                    $ VTbreedfetishtt += f"\n{{image=red_heart_token_small}} Get her to love Missionary Style Sex."
                #the interactive icons during sex stuff
                if 'position_choice' in globals():
                    if hasattr(position_choice, 'skill_tag'):
                        $ VTbreedfetishat = "sexualized"

                if VTbreedfetishat=="sexualized":
                    if person.vaginal_cum >0:
                        if person.vaginal_cum == 1:
                            if person.hymen <=1:
                                $ VTbreedfetishst = "vaghymen"
                                $ VTbreedfetishtt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."
                            else:
                                $ VTbreedfetishtt += f"\n{{image=beezee_token_small}} Your seed is in her"+VTbreedfertile+VTpro+" womb."
                        else:
                            if person.hymen <=1:
                                $ VTbreedfetishst = "vaghymen"
                                $ VTbreedfetishtt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} Marked her fresh"+VTbreedfertile+VTpro+" womb with "+str(person.vaginal_cum)+ " doses of your seed."
                            else:
                                if person.vaginal_cum <3:
                                    $ VTbreedfetishst = "openvag"
                                else:
                                    $ VTbreedfetishst = "ahegaovag"
                                $ VTbreedfetishtt += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."+daysince
                    imagebutton:
                        pos(866, 166)
                        idle VTbreedfetishst
                        action NullAction()
                        tooltip VTbreedfetishtt

                if VTbreedfetishat=="talking":
                    if person.vaginal_cum >0:
                        if person.vaginal_cum == 1:
                            if person.hymen <=1:
                                $ VTbreedfetishtt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} Marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."
                            else:
                                $ VTbreedfetishtt += f"\n{{image=beezee_token_small}} Your seed is in her"+VTbreedfertile+VTpro+" womb."
                        else:
                            if person.hymen <=1:
                                $ VTbreedfetishtt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} Marked her fresh"+VTbreedfertile+VTpro+" womb with "+str(person.vaginal_cum)+ " doses of your seed."
                            else:
                                $ VTbreedfetishtt += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."+daysince
                    imagebutton:
                        pos(866, 166)
                        idle VTbreedfetishst
                        action NullAction()
                        tooltip VTbreedfetishtt

                    # if person.hymen >1 and person.vaginal_cum >1:
                        # imagebutton:
                            # pos(866, 166)
                            # idle "bc_cum"
                            # action NullAction()
                            # tooltip VTbreedfetishtt

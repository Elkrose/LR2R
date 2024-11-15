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
        fetish_roles = [anal_fetish_role, cum_fetish_role, breeding_fetish_role, exhibition_fetish_role]
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
#### Virgin UI ####
        $ dayslastsex = 0
        $ daysince = ""
        if person.has_event_day("last_insemination") and person.days_since_event("last_insemination") < 4:
            if person.days_since_event("last_insemination") > 1:
                $ dayslastsex = 4 - person.days_since_event("last_insemination") 
                if dayslastsex == 1:
                    $ daysince = "\nMy womb feels empty!"
                else:
                    $ daysince = "\nYour sperm in me for "+str(dayslastsex)+" more days!\n Such warm butterflies!"
#### Relationship Status
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
            imagebutton:
                pos(249, 166)
                idle VTrelationshipst
                action NullAction()
                tooltip VTrelationshiptt+VTrelationshipStatusTT
### Age 
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
            $ VTagest = "redlotus"
            $ VTagett = f"{{image=redlotus_small}} The Red Lotus: Passion, inspiration and emotions."
            if person.hymen <= 1 and person.vaginal_virgin <=1:
                $ VTagett += f"\n{{image=virgin_token_small}} She looks sexually inexperienced."
            else:
                $ VTagett += f"\n{{image=vtcherries_small}} She is in her prime fertile peak."
        if person.age >29 and person.age <=35:
            $ VTagest = "pinklotus"
            $ VTagett = f"{{image=pinklotus_small}} The Pink Lotus: Feminine energy and passion."
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
            $ VTagett = f"{{image=creamcherry_small}} The Golden Lotus: Total Sexual Enlightenment."
        imagebutton:
            pos(286, 166)
            idle VTagest
            action NullAction()
            tooltip VTagett

###### Threesome Flag - note polyamorous added
        $ VTpolyat = "talking"
        $ VTpolyst = "knowthreesome"
        $ VTpolytt = f"{{image=knowthreesome_small}} Does she like threesomes?"
        if person.sexy_opinions.get("threesomes")==None:
            $ VTpolyst = "knowthreesome"
            $ VTpolytt = f"{{image=knowthreesome_small}} Does she like threesomes?"
        else:
            if person.sexy_opinions.get("threesomes")[1]==True:
                if person.opinion.threesomes >=2 and person.opinion.polyamory >=2 and mc.stats.polycules>=2:
                    $ VTpolyst = "threesometriad"
                    $ VTpolytt = f"{{image=creamcherry_small}} More the merrier! The mess we will make!"
                else:
                    if person.opinion.threesomes >=2:
                        $ VTpolyst = "threesometriad"
                        $ VTpolytt = f"{{image=progress_token_small}} Open her mind up to more!"
                        if person.has_role(harem_role)==False:
                            if person.love <80:
                                $ VTpolytt += f"\n{{image=progress_token_small}} "+ str(80 - person.love) +" more to add her to your polycule!"
                            else:
                                $ VTpolytt += f"\n{{image=red_heart_token_small}} She is ready to be part of your polycule!"
                        if person.opinion.polyamory <2:
                            if person.opinion.polyamory ==1:
                                $ VTpolytt += f"\n{{image=red_heart_token_small}} Needs to love polyamorous more!"
                            else:
                                if person.sexy_opinions.get("polyamory")==None:
                                    $ VTpolytt += f"\n{{image=question_mark_small}} Needs to like polyamorous relationships."
                    else:
                        if person.opinion.threesomes >0:
                            $ VTpolyst = "opentriad"
                            $ VTpolytt = f"{{image=progress_token_small}} Open her mind up to the possibility of more!"
                            $ VTpolytt += f"\n{{image=red_heart_token_small}} Make her love threesomes!"
                        else:
                            if person.opinion.threesomes == 0:
                                $ VTpolyst = "opentriad"
                                $ VTpolytt = f"{{image=question_mark_small}} She's indifferent to threesomes, so make her like it..."
                            else:
                                $ VTpolyst = "opentriad"
                                if person.opinion.threesomes == -2:
                                    $ VTpolytt = f"{{image=dislike_small}} She hates threesomes!"
                                if person.opinion.threesomes == -1:
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
        if person.sexy_opinions.get("threesomes", (0, False))[1]:
            if person.sexy_opinions.get("threesomes")[1]==True:
                if person.opinion.threesomes <0 or person.opinion.polyamory <0:
                    imagebutton:
                        pos(323, 166)
                        idle "dislike"
                        action NullAction()
                        tooltip VTpolytt
### Personalities 
        $ VTpersonalityst = "knowpeach"
        $ VTpersonalitytt = f"{{image=question_mark_small}} What is her personality?"
        if person.personality.default_prefix == "bimbo":
            $VTpersonalityst = "bimbo"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears bubbly and enthusiastic, with a bright smile plastered on her face. She studies you up and down, her eyes widening with excitement as she takes in your appearance. Her tone is sugary sweet and overly friendly, with a hint of airheadedness. Her brain is with NASA, in space."
        elif person.personality.default_prefix == "cougar":
            $VTpersonalityst = "cougar"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears sultry and seductive, with a confident and flirtatious smile. She studies you with a piercing gaze, her eyes seeming to sparkle with a knowing glint. Her tone is low and husky, with a hint of a purr, as if she is savoring every word."
        elif person.personality.default_prefix == "alpha":
            $VTpersonalityst = "alpha"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears confident and assertive, with a strong and commanding presence. She studies you with a direct and piercing gaze, her eyes seeming to bore into your very soul. Her tone is firm and authoritative, with a hint of a growl, as if she is daring you to challenge her."
        elif person.personality.default_prefix == "relaxed":
            $VTpersonalityst = "relaxed"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears calm and serene, with a warm and gentle smile on her face. She studies you with a soft and peaceful gaze, her eyes crinkling at the corners as she smiles. Her tone is low and soothing, with a hint of a drawl, as if she is savoring every word."
        elif person.personality.default_prefix == "introvert":
            $VTpersonalityst = "introvert"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears quiet and introspective, with a subtle hint of nervousness in her demeanor. She studies you with a gentle gaze, her eyes soft and thoughtful. Her tone is soft and measured, with a hint of hesitation and reserve."
        elif person.personality.default_prefix == "reserved":
            $VTpersonalityst = "reserved"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears calm and composed, with a subtle hint of shyness in her demeanor. She studies you with a gentle gaze, her eyes soft and introspective. Her tone is quiet and measured, with a hint of reserve and caution."
        elif person.personality.default_prefix == "wild":
            $VTpersonalityst = "wild"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears excited and energetic, with a huge smile on her face. She studies you with a sparkling gaze, her eyes shining with a love of fun and adventure. Her tone is loud and boisterous, with a hint of infectious enthusiasm."
        elif person.personality.default_prefix == "dandere":
            $VTpersonalityst = "dandere"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears distracted and preoccupied, with a far-off look in her eyes. She studies you with a slightly vacant expression, as if they were gazing right through you. Her tone is flat and monotone, with a hint of disinterest and detachment."
        elif person.personality.default_prefix == "goudere":
            $VTpersonalityst = "goudere"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears to be smiling and enthusiastic, with a radiant glow in her eyes. She studies you with a warm and inviting expression, her face lighting up with excitement. Her tone is bright and cheerful, with a hint of playfulness and mischief."
        elif person.personality.default_prefix == "kuudere":
            $VTpersonalityst = "kuudere"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears quiet and reserved, with a subtle hint of sadness in her eyes. She studies you with a gentle, almost imperceptible smile, her expression soft and melancholic. Her tone is low and soothing, with a hint of wistfulness and longing."
        elif person.personality.default_prefix == "tsundere":
            $VTpersonalityst = "tsundere"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears irritated and annoyed, with a scowl on her face. She studies you with a mixture of disdain and disinterest, her eyes flashing with a hint of anger. Her tone is sharp and curt, with a hint of sarcasm and mockery."
        elif person.personality.default_prefix == "yandere":
            $VTpersonalityst = "yandere"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears sweet and innocent, with a gentle smile on her face. She studies you with big, shining eyes, her gaze filled with adoration and devotion. Her tone is soft and melodious, with a hint of shyness and vulnerability."
        elif person.personality.default_prefix == "alluring":
            $VTpersonalityst = "pinklips2"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears sophisticated and elegant, with a confident and poised demeanor. She studies you up and down, her eyes sparkling with interest and curiosity, her gaze lingering on your best features. Her tone is smooth and sultry, with a hint of playfulness and flirtation."
        elif person.personality.default_prefix == "gothic":
            $VTpersonalityst = "gothic"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears dark and introspective, with a hint of mystery and intrigue. She studies you up and down, her eyes narrowing slightly as she takes in your appearance, her gaze lingering on any perceived flaws or imperfections. Her tone is low and melancholic, with a hint of sarcasm and dry wit."
        elif person.personality.default_prefix == "bimboed":
            $VTpersonalityst = "bimbo"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears bubbly and enthusiastic, with a bright smile plastered on her face. She studies you up and down, her eyes widening with excitement as she takes in your appearance. Her tone is sugary sweet and overly friendly, with a hint of airheadedness. Her brain is with NASA, in space."
        elif person.personality.default_prefix == "tomboy":
            $VTpersonalityst = "tomboy"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears relaxed and casual, with a hint of a smirk on her face. She studies you with a slightly raised eyebrow, her expression a mix of curiosity and amusement. Her tone is laid-back and friendly, with a hint of teasing and playfulness."
        elif person.personality.default_prefix == "foodie":
            $VTpersonalityst = "foodie"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She appears to be savoring the moment, her eyes lingering on you like a rich, decadent sauce on a perfectly cooked dish. She raises an eyebrow, and a hint of a smile plays on her lips, as if she's anticipating the first bite of a long-awaited meal."
        elif person.personality.default_prefix == "cosplay":
            $VTpersonalityst = "cosplay"
            $VTpersonalitytt = f"{{image=vtcherries_small}} Her eyes sparkle with excitement as she strikes a pose, her confidence and charisma radiating from every angle."
        elif person.personality.default_prefix == "slutty":
            $VTpersonalityst = "pinklips"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She turns to face you with a sly smile spreading across her face. Her eyes sparkle with a hint of mischief, and her body language screams \"I'm available and ready to play\"."
        elif person.personality.default_prefix == "pornstar":
            $VTpersonalityst = "matureteen"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She saunters into view, her hips swaying seductively as she moves. Her eyes sparkle with a naughty glint, and her full lips curve into a sultry smile. She looks you up and down, her gaze lingering on your crotch before meeting your eyes with a flirtatious wink."
        elif person.personality.default_prefix == "breeder":
            $VTpersonalityst = "breeder"
            $VTpersonalitytt = f"{{image=vtcherries_small}} She walks into view with a confident stride, her hips swaying gently as she moves. Her eyes shine with a warm, nurturing light, and her full lips curve into a soft, inviting smile. She looks you up and down with a discerning gaze, her eyes lingering on your face before meeting your eyes with a gentle, encouraging smile."
        else:
            $VTpersonalityst = "vtcherries"
            $VTpersonalitytt = f"{{image=vtcherries_small}} Her personality is unique."

        imagebutton:
            pos(360, 166)
            idle VTpersonalityst
            action NullAction()
            tooltip VTpersonalitytt
###### Birth Control Status
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
                        
                        if not (person.has_cum_fetish or person.has_anal_fetish or person.has_breeding_fetish):
                            if person.has_anal_fetish==False:
                                $ VTcondomtt += f"\n{{image=ahegaoanal_small}} Needs the Anal Fetish Unlocked." 
                            if person.has_breeding_fetish==False:
                                $ VTcondomtt += f"\n{{image=ahegaovag_small}} Needs the Breeding Fetish Unlocked."
                            if person.has_cum_fetish==False:
                                $ VTcondomtt += f"\n{{image=ahegaomouth_small}} Needs the Cum Fetish Unlocked."
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
                    $ VTcondomtt = f"{{image=vtcherries_small}} You are natural."
                    if person.days_since_event("last_insemination")<1 and person.vaginal_cum >0:
                        $ VTcondomst = "creamcherry"
                        $ VTcondomtt += f"\n{{image=vtcherries_small}} You recently came inside her pussy."
                else:
                    $ VTcondomst = "wearcondom"
                    $ VTcondomtt = f"{{image=wearcondom_token_small}} You are wearing a condom."

        if VTcondomat=="sexualized":
            #TODO add creamcherries when they cum during raw
            if VTcondommc == "condomoff":
                $ VTcondomst = "vtcherries"
                $ VTcondomtt = f"{{image=vtcherries_small}} You are natural."
                if person.days_since_event("last_insemination")<1 and person.vaginal_cum >0:
                    $ VTcondomst = "creamcherry"
                    $ VTcondomtt += f"\n{{image=vtcherries_small}} You recently came inside her pussy."
            imagebutton:
                pos(434, 166)
                idle VTcondomst
                action NullAction()
                tooltip VTcondomtt

        if VTcondomat=="talking":
            if VTcondommc == "condomoff":
                $ VTcondomst = "vtcherries"
                $ VTcondomtt = f"{{image=vtcherries_small}} You are natural."
                if person.days_since_event("last_insemination")<1 and person.vaginal_cum >0:
                    $ VTcondomst = "creamcherry"
                    $ VTcondomtt += f"\n{{image=vtcherries_small}} You recently came inside her pussy."
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
        if person.has_exact_role(very_heavy_trance_role):
            imagebutton:
                pos(486, 166)
                idle "ahegaotrance"
                action NullAction()
                tooltip f"{{image=ahegaotrance_token_small}} In a very deep trance!\n Good time to train her!"
        else:
            if person.has_exact_role(heavy_trance_role):
                imagebutton:
                    pos(486, 166)
                    idle "heavytrance"
                    action NullAction()
                    tooltip f"{{image=heavytrance_token_small}} In a deep trance!\n Good time to train her!"
            else:
                if person.has_exact_role(trance_role):
                    imagebutton:
                        pos(486, 166)
                        idle "starttrance"
                        action NullAction()
                        tooltip f"{{image=starttrance_token_small}} In a trance! She is open to suggestions!"
        if person.event_triggers_dict.get("trance_training_available", True) == False:
            imagebutton:
                pos(486, 166)
                idle "donetrain"
                action NullAction()
                tooltip f"{{image=donetrain_token_small}} Already Trained her!"

#hymen is 0 = sealed, 1=recently torn bleeding, 2=normal - serum to regenerate vaginal and hymen
#0=virgin, 1=just the tip, 2=full penetration, 3-10 is degree of tightness
### Oral Virgin Flag
        $ VToralat = "talking"
        $ VToralst = ""
        $ VToraltt = ""
        #the interactive icons during sex stuff
        if 'position_choice' in globals():
            if hasattr(position_choice, 'skill_tag'):
                if position_choice.skill_tag == 'Oral':
                    if position_choice.name == 'Blowjob':
                        $ VToralat = "sexualized"
                        $ VToralst = "openmouth"
                        $ VToraltt = f"{{image=openmouth_small}} She sucks your cock."
                    if position_choice.name == "Deepthroat":
                        $ VToralat = "sexualized"
                        $ VToralst = "openmouth"
                        $ VToraltt = f"{{image=openmouth_small}} You deeply fuck her throat with your cock."
                    if position_choice.name == "Skull Fuck":
                        $ VToralat = "sexualized"
                        $ VToralst = "openmouth"
                        $ VToraltt = f"{{image=openmouth_small}} You grab her head and skull fuck her with your cock."
                    if 'climax_type' in globals():
                        if climax_type == "mouth" or climax_type == "throat":
                            $ VToralat = "sexualized"
                            if mc.condom == False:
                                $ VToralst = "ahegaomouth"
                                $ VToraltt = f"{{image=ahegaomouth_small}} You flood her mouth full of your cum."
                            else:
                                $ VToralst = "openmouth"
                                $ VToraltt = "You fill the condom as her tongue wraps around you."
                        if climax_type == "throat":
                            $ VToralat = "sexualized"
                            if mc.condom == False:
                                $ VToralst = "ahegaomouth"
                                $ VToraltt = "You flood her belly with your cum."
                            else:
                                $ VToralst = "openmouth"
                                $ VToraltt = "You fill the condom as her throat squeezes you."
                        if climax_type == "face":
                            $ VToralat = "sexualized"
                            $ VToralst = "ahegaomouth"
                            $ VToraltt = "You shoot your load all over her face."
                        if climax_type =="body":
                            $ VToralat = "sexualized"
                            $ VToralst = "bitelip"
                            $ VToraltt = "You blow your load all over her body."
                            #TODO need to trigger the others accordingly
                            $ VTanalst = "yesanal"
                            $ VTanaltt = "You blow your load all over her body."
                elif position_choice.skill_tag == 'Foreplay':   
                    if position_choice.name == 'Kissing':
                        $ VToralat = "sexualized"
                        $ VToralst = "pinklips"
                        $ VToraltt = "In the throes of kissing you."
                else:
                    $ VToralat = "sexualized"
                    if person.oral_cum >0:
                        if person.oral_cum == 1:
                            if person.arousal_perc >= 59:
                                $ VToralst = "ahegaoface"
                                $ VToraltt = f"She seems lost in her bliss and panting. \n{{image=ahegaomouth_small}}She has a dose of your protein in her belly."
                            else:
                                $ VToralst = "bitelip"
                                $ VToraltt = f"She looks at you with lust \n in her innocent hungry eyes. \n{{image=ahegaomouth_small}}She has a dose of your protein in her belly."
                        else:
                            if person.oral_cum >3:
                                if person.arousal_perc >= 59:
                                    $ VToralst = "ahegaoface"
                                    $ VToraltt = f"*Hunger in her eyes wants more cum*\n{{image=ahegaomouth_small}} She has "+ str(person.oral_cum) +" doses of your cum \n swimming in her stomach, causing a bit of a bulge."
                                else:
                                    $ VToralst = "ahegaomouth"
                                    $ VToraltt = f"{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in the slight bulge of her belly."
                            else:
                                if person.arousal_perc >= 59:
                                    $ VToralst = "ahegaoface"
                                    $ VToraltt = f"*She hungrily gazes at you for more cum.*\n{{image=ahegaomouth_small}} She has "+ str(person.oral_cum) +" doses of your cum \n swimming in her belly."
                                else:
                                    $ VToralst = "bitelip"
                                    $ VToraltt = f"{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \nswimming in her belly."
                    else:
                        $ VToralst = "bitelip"
                        if person.oral_virgin == 0:
                            $ VToraltt = f"{{image=virgin_token_small}} She plays with her innocent hungry fresh pussy.\nShe bites her lip coyly."
                        else:
                            if person.oral_first == mc.name:
                                $ VToraltt = f"{{image=handprint_token_small}} She locks eyes with you and bite her lip sexily."
                            else:
                                $ VToraltt = f"{{image=bitelip_small}} She pants and breathes heavily and bites her lip."
                        if person.energy <20 and person.had_sex_today:
                            $ VToraltt += f"{{image=bitelip_small}} She seems lost in her bliss and panting."

        if VToralat=="sexualized":
            imagebutton:
                pos(523, 166)
                idle VToralst
                action NullAction()
                tooltip VToraltt

        if VToralat=="talking":
            if person.arousal_perc >= 59:
                if person.oral_cum ==0:
                    $ VToralst = "ahegaoface"
                    if person.oral_virgin == 0:
                        $ VToraltt = f"{{image=virgin_token_small}} She looks at you with lust \n in her innocent hungry eyes."
                    else:
                        if person.oral_first == mc.name:
                            $ VToraltt = f"{{image=handprint_token_small}} She starts to drool \n and undress you with her eyes."
                        else:
                            $ VToraltt = f"{{image=bitelip_small}} She looks at you with savage lust in her eyes."
                    if person.energy <20 and person.had_sex_today:
                        $ VToraltt = f"{{image=bitelip_small}} She seems lost in her bliss and panting."
                if person.oral_cum >0:
                    $ VToralst = "ahegaoface"
                    if person.energy <20 and person.had_sex_today:
                        $ VToraltt = f"{{image=bitelip_small}} She seems lost in her bliss and panting."
                    else:
                        $ VToraltt = f"{{image=bitelip_small}} She hungrily gazes at you for more cum."
                    if person.oral_cum == 1:
                        $ VToraltt += f"\n{{image=ahegaomouth_small}} She has a dose of your protein in her belly."
                    else:
                        $ VToraltt += f"\n{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in her belly."
            else:
                if person.oral_virgin == 0: #morevisual with virgin
                    $ VToralst = "truevirgin"
                    $ VToraltt = f"{{image=virgin_token_small}} Her lips look sweet and inexperienced."
                if person.oral_first == mc.name:
                    $ VToralst = "claimedmouth"
                    $ VToraltt = f"{{image=handprint_token_small}} You Claimed this Pie Hole!"
                else:
                    if person.oral_first !=None and person.oral_virgin>0:
                        $ VToralst = "knowlips"
                        $ VToraltt = f"{{image=taboo_break}} Someone else had her lips before you... CLAIM IT!"
                if person.oral_cum >0:
                    $ VToralst = "bitelip"
                    if person.oral_cum == 1:
                        $ VToraltt += f"\n{{image=ahegaomouth_small}} She has a dose of your protein in her belly."
                    else:
                        $ VToraltt += f"\n{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in her belly."
            imagebutton:
                pos(523, 166)
                idle VToralst
                action NullAction()
                tooltip VToraltt

### Vaginal Virgin Flag
        $ VTvaginalat = "talking"
        $ VTvaginalst = ""
        $ VTvaginaltt = ""
        #the interactive icons during sex stuff
        if 'position_choice' in globals():
            if hasattr(position_choice, 'skill_tag'):
                if position_choice.skill_tag == 'Vaginal':
                    if 'climax_type' in globals():
                        if climax_type == "pussy":
                            if mc.condom == False:
                                if person.hymen ==1:
                                    $ VTvaginalat = "sexualized"
                                    $ VTvaginalst = "vaghymen"
                                    $ VTvaginaltt = f"{{image=handprint_token_small}} You mark her fresh"+VTbreedfertile+VTpro+" womb with your virile seed! \n Her virinity mixes with your cum!"
                                else:
                                    $ VTvaginalat = "sexualized"
                                    $ VTvaginalst = "openvag"
                                    $ VTvaginaltt = f"{{image=openvag_small}} You flood her"+VTbreedfertile+VTpro+" womb with your seed!"
                                    if person.vaginal_cum >=1:
                                        $ VTvaginalst = "ahegaovag"
                            else:
                                if person.hymen ==1:
                                    $ VTvaginalat = "sexualized"
                                    $ VTvaginalst = "spreadvag"
                                    $ VTvaginaltt = f"{{image=handprint_token_small}} You fill the condom in her freshly fucked pussy with your cum!"
                                else:
                                    $ VTvaginalat = "sexualized"
                                    $ VTvaginalst = "spreadvag"
                                    $ VTvaginaltt = f"{{image=spreadvag_small}} You push deep and fill the condom with your seed!"
                        if climax_type =="body":
                            $ VTvaginalat = "sexualized"
                            $ VTvaginalst = "spreadvag"
                            $ VTvaginaltt = f"{{image=spreadvag_small}} You blow your load all over her body."
                    else:
                        $ VTvaginalat = "sexualized"
                        $ VTvaginalst = "spreadvag"
                        $ VTvaginalcondom = " bare "
                        if mc.condom == True:
                           $ VTvaginalcondom = " wrapped "
                        $ VTvaginaltt = f"{{image=spreadvag_small}} You fuck her juicy"+VTbreedfertile+VTpro+" pussy with your"+VTvaginalcondom+"cock."
                else:
                    $ VTvaginalat ="sexualized"
                    if person.vaginal_cum >0:
                        if person.vaginal_cum == 1:
                            if person.hymen <=1:
                                if person.hymen == 0:
                                    $ VTvaginalst = "vaghymen"
                                    $ VTvaginaltt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} Marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."                            
                                else:
                                    $ VTvaginalst = "vaghymen"
                                    $ VTvaginaltt += f"{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."
                            else:
                                $ VTvaginalst = "openvag"
                                $ VTvaginaltt = f"{{image=beezee_token_small}} Your seed in her"+VTbreedfertile+VTpro+" womb."
                        else:
                            if person.hymen <=1:
                                if person.vaginal_cum >3:
                                    $ VTvaginalst = "ahegaovag"
                                    $ VTvaginaltt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} Her freshly fucked"+VTbreedfertile+VTpro+" womb \ncan barely contain your "+str(person.vaginal_cum)+ " doses of your seed. \n It is already oozing out."
                                else:
                                    $ VTvaginalst = "vaghymen"
                                    $ VTvaginaltt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb \n with "+str(person.vaginal_cum)+ " doses of your seed."
                            else:
                                if person.vaginal_cum >3:
                                    $ VTvaginalst = "ahegaovag"
                                    $ VTvaginaltt = f"{{image=beezee_token_small}} Her pussy can barely contain \nthe "+ str(person.vaginal_cum) +" doses of your cum swimming in \nher"+VTbreedfertile+VTpro+" womb and is already oozing out."+daysince
                                else:
                                    $ VTvaginalst = "openvag"
                                    $ VTvaginaltt = f"{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."+daysince
                        if person.arousal_perc >= 59:
                            $ VTvaginaltt += f"\n{{image=spreadvag_small}} *You can really smell her arousal*"
                    else:
                        $ VTvaginalst = "spreadvag"
                        if person.vaginal_virgin == 0:
                            $ VTvaginaltt = f"{{image=virgin_token_small}} She plays with her fresh innocent hungry pussy."
                        else:
                            if person.vaginal_first == mc.name:
                                $ VTvaginaltt = f"{{image=handprint_token_small}} She locks eyes with you and licks her lips \n and plays with her pussy."
                            else:
                                $ VTvaginaltt = f"{{image=spreadvag_small}} She pants heavily as she plays with her pussy."
                        if person.energy <20 and person.had_sex_today:
                            $ VTvaginaltt = f"{{image=spreadvag_small}} She seems lost in her bliss and panting."

        if VTvaginalat=="sexualized":
            imagebutton:
                pos(560, 166)
                idle VTvaginalst
                action NullAction()
                tooltip VTvaginaltt
            $ VTvaginalcum = "bc_cum"
            if person.hymen >1 and person.vaginal_cum >1:
                $ VTvaginalcum = "bc_cum"
                $ VTvaginaltt += f"\n{{image=creamcherry_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."+daysince
            else:
                if person.hymen <2 and person.vaginal_cum>0:
                    $ VTvaginalcum = "vaghymen"
            if person.vaginal_cum>0:
                imagebutton:
                    pos(560, 166)
                    idle VTvaginalcum
                    action NullAction()
                    tooltip VTvaginaltt
        if VTvaginalat=="talking":
            if person.hymen == 0 and person.vaginal_virgin <=1: #morevisual with virgin
                $ VTvaginalst = "truevirgin"
                $ VTvaginaltt = f"{{image=virgin_token_small}} She looks so innocent and inexperienced."
            if person.vaginal_first == mc.name:
                $ VTvaginalst = "claimedvag"
                $ VTvaginaltt = f"{{image=handprint_token_small}} You Claimed this Pussy!"
            else:
                if person.vaginal_first !=None and person.hymen==2:
                    $ VTvaginalst = "knowpeach"
                    $ VTvaginaltt = f"{{image=taboo_break}} Someone else had this pussy before you... OWN IT!"
            if person.arousal_perc >= 59 and person.vaginal_cum<=0:
                $ VTvaginalst = "spreadvag"
                if person.vaginal_virgin <= 1:
                    $ VTvaginaltt += f"\n{{image=virgin_token_small}} Her fresh pussy is dripping for you.\n*You can really smell her arousal*"
                    if person.hymen ==0:
                        $ VTvaginaltt += f"\n{{image=virgin_token_small}} She is more than ready to be fucked."
                else:
                    if person.vaginal_first == mc.name:
                        $ VTvaginaltt += f"\n{{image=handprint_token_small}} Her pussy is dripping for you.\n*You can really smell her arousal*\nCome take me!"
                    else:
                        $ VTvaginaltt += f"\n{{image=vagclosed_small}} Her pussy is dripping down her leg.\n*She is really aroused*"
            else:
                if person.vaginal_cum >0:
                    if person.vaginal_cum == 1:
                        if person.hymen <=1:
                            if person.hymen == 0:
                                $ VTvaginalst = "vaghymen"
                                $ VTvaginaltt = f"{{image=handprint_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."                            
                            else:
                                $ VTvaginalst = "vaghymen"
                                $ VTvaginaltt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."
                        else:
                            $ VTvaginalst = "openvag"
                            $ VTvaginaltt += f"\n{{image=beezee_token_small}} Your seed in her"+VTbreedfertile+VTpro+" womb."
                    else:
                        if person.hymen <=1:
                            if person.vaginal_cum >3:
                                $ VTvaginalst = "ahegaovag"
                                $ VTvaginaltt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} Her freshly fucked"+VTbreedfertile+VTpro+" womb can barely contain your "+str(person.vaginal_cum)+ " doses of your seed.\nIt is already oozing out."
                            else:
                                $ VTvaginalst = "vaghymen"
                                $ VTvaginaltt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with "+str(person.vaginal_cum)+ " doses of your seed."
                        else:
                            if person.vaginal_cum >3:
                                $ VTvaginalst = "ahegaovag"
                                $ VTvaginaltt += f"\n{{image=beezee_token_small}} Her pussy can barely contain\n the "+ str(person.vaginal_cum) +" doses of your cum \n swimming \nin her"+VTbreedfertile+VTpro+" womb and is already oozing out."+daysince
                            else:
                                $ VTvaginalst = "openvag"
                                $ VTvaginaltt += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."+daysince
                    if person.arousal_perc >= 59:
                        $ VTvaginaltt += f"\n{{image=vagclosed_small}} *You can really smell her arousal*"
            imagebutton:
                pos(560, 166)
                idle VTvaginalst
                action NullAction()
                tooltip VTvaginaltt
            $ VTvaginalcum = "bc_cum"
            if person.hymen >1 and person.vaginal_cum >1:
                $ VTvaginalcum = "bc_cum"
            else:
                if person.hymen <2 and person.vaginal_cum>0:
                    $ VTvaginalcum = "vaghymen"
            if person.vaginal_cum>0:
                imagebutton:
                    pos(560, 166)
                    idle VTvaginalcum
                    action NullAction()
                    tooltip VTvaginaltt

### Anal Virgin Flag
        $ VTanalat = "talking"
        $ VTanalst = ""
        $ VTanaltt = ""
        #the interactive icons during sex stuff
        if 'position_choice' in globals():
            if hasattr(position_choice, 'skill_tag'):
                if position_choice.skill_tag == 'Anal':
                    if 'climax_type' in globals():
                        if climax_type == "anal":
                                if mc.condom == False:
                                    $ VTanalst = "handass"
                                    $ VTanaltt = f"{{image=handass_small}} You flood her bowels with your seed!"
                                    if person.anal_cum >=1:
                                        $ VTanalst = "ahegaopeach"
                                else:
                                    $ VTanalst = "yesanal"
                                    $ VTanaltt = f"{{image=yesanal_small}} You fill the condom with your seed, as she pulses around you!"
                        if climax_type =="body":
                            $ VTanalst = "yesanal"
                            $ VTanaltt = f"{{image=yesanal_small}} You blow your load all over her body."
                    else:
                        $ VTanalst = "yesanal"
                        $ VTanaltt = f"{{image=yesanal_small}} You fuck her ass with your cock."
                else:
                    $ VTanalat = "sexualized"
                    if person.anal_cum >0:
                        if person.anal_cum == 1:
                            if person.arousal_perc >= 59:
                                $ VTanalst = "handass"
                                $ VTanaltt = f"{{image=handass_small}} She seems lost in her bliss and panting. \n{{image=handass_small}}She has a dose of your protein in her bowels."
                            else:
                                $ VTanalst = "handass"
                                $ VTanaltt = f"{{image=handass_small}} She looks at you with lust \n in her innocent hungry eyes. \n{{image=ahegaoanal_small}}She has a dose of your protein in her bowels."
                        else:
                            if person.anal_cum >3:
                                if person.arousal_perc >= 59:
                                    $ VTanalst = "ahegaopeach"
                                    $ VTanaltt = f"{{image=ahegaoanal_small}} *Hunger in her eyes wants more cum*\n{{image=ahegaoanal_small}} She has "+ str(person.anal_cum) +" doses of your cum \n swimming in her bowels, causing her belly a bit of a bulge."
                                else:
                                    $ VTanalst = "ahegaopeach"
                                    $ VTanaltt = f"{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n swimming in the slight bulge of her belly."
                            else:
                                if person.arousal_perc >= 59:
                                    $ VTanalst = "ahegaopeach"
                                    $ VTanaltt = f"{{image=ahegaoanal_small}} *She hungrily gazes at you for more cum.*\n{{image=ahegaoanal_small}} She has "+ str(person.anal_cum) +" doses of your cum \n swimming in her belly."
                                else:
                                    $ VTanalst = "handass"
                                    $ VTanaltt = f"{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n swimming in her belly."
                    else:
                        $ VTanalst = "yespeach"
                        if person.anal_virgin == 0:
                            $ VTanaltt = f"{{image=virgin_token_small}} Her ass sways so ripely, ready for the taking!"
                        else:
                            if person.anal_first == mc.name:
                                $ VTanaltt = f"{{image=handprint_token_small}} Her ass sways, hypnotizing you..\nThen she slaps it!"
                            else:
                                $ VTanaltt = f"{{image=yesanal_small}} Her ass sways and she spreads her ass for you.\nCome take me!"
                                if person.anal_virgin >=4:
                                    $ VTanaltt = f"{{image=yesanal_small}} Her ass sways and she spreads her gaping asshole for you.\nCome take me!"
                        if person.energy <20 and person.had_sex_today:
                            $ VTanaltt += f"{{image=handass_small}} She seems lost in her bliss and panting."
        if VTanalat=="sexualized":
            imagebutton:
                pos(597, 166)
                idle VTanalst
                action NullAction()
                tooltip VTanaltt

        if VTanalat=="talking":
            if person.anal_virgin == 0:
                $ VTanalst = "truevirgin"
                $ VTanaltt = f"{{image=virgin_token_small}} Her ass sways so ripely, ready for the taking"
            if person.arousal_perc >= 59:
                if person.anal_cum ==0:
                    $ VTanalst = "yespeach"
                    if person.anal_virgin == 0:
                        $ VTanaltt = f"{{image=virgin_token_small}} Her ass sways so ripely, ready for the taking!"
                    else:
                        if person.anal_first == mc.name:
                            $ VTanaltt = f"{{image=handprint_token_small}} Her ass sways, hypnotizing you while \nshe rubs it!"
                        else:
                            $ VTanaltt = f"{{image=yesanal_small}} Her ass sways and she spreads her ass for you.\nCome take me!"
                            if person.anal_virgin >=4:
                                $ VTanaltt = f"{{image=yesanal_small}} Her ass sways and she spreads her gaping asshole for you.\nCome take me!"
                if person.anal_cum >0:
                    if person.anal_cum == 1:
                        $ VTanalst = "handass"
                        $ VTanaltt += f"\n{{image=ahegaoanal_small}} You painted her bowels with your cum."
                    else:
                        $ VTanalst = "ahegaopeach"
                        $ VTanaltt += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n coating her bowels."
            else:
                if person.anal_first == mc.name:
                    $ VTanalst = "claimedass"
                    $ VTanaltt = f"{{image=handprint_token_small}} You Claimed this Ass!"
                else:
                    if person.anal_first !=None and person.anal_virgin>0:
                        $ VTanalst = "knowpeach"
                        $ VTanaltt = f"{{image=taboo_break}} Someone else had her ass before you... RECLAIM IT!"
                if person.anal_cum >0:
                    $ VTanalst = "bitelip"
                    if person.anal_cum == 1:
                        $ VTanalst = "handass"
                        $ VTanaltt += f"\n{{image=ahegaoanal_small}} You have painted her bowels with your cum."
                    else:
                        $ VTanalst = "ahegaopeach"
                        $ VTanaltt += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n coating her bowels."
            imagebutton:
                pos(597, 166)
                idle VTanalst
                action NullAction()
                tooltip VTanaltt

#### Had sex today
        if person.had_sex_today:
            imagebutton:
                pos(634, 166)
                idle "hadsextoday"
                action NullAction()
                tooltip f"{{image=hadsextoday_small}} You had fun with her today."  

### Thermometer - Arousal
        $ VTtempst = "tempblank"
        $ VTtemptt = f"{{image=vtcherries_small}} She is completely sedated."

        if person.arousal > 100:
            $ VTtempst = "tempbroke"
            $ VTtemptt = f"{{image=creamcherry_small}} Her brain melted! Way to go!"
        elif person.arousal > 90:
            $ VTtempst = "temp90"
            $ VTtemptt = f"{{image=vtcherries_small}} She is on the verge of cumming!"
        elif person.arousal > 80:
            $ VTtempst = "temp80"
            $ VTtemptt = f"{{image=vtcherries_small}} She is extremely horny."
        elif person.arousal > 70:
            $ VTtempst = "temp70"
            $ VTtemptt = f"{{image=vtcherries_small}} She is really aroused."
        else:
            $ VTtempst = "tempnormal"
            $ VTtemptt = f"{{image=vtcherries_small}} She seems okay, really."

        imagebutton:
            pos(681, 166)
            idle VTtempst
            action NullAction()
            tooltip VTtemptt

######## Exhibitionist Fetish
        $ VTexhibitfetishat = "talking"
        $ VTexhibitfetishst = "knowbody"
        $ VTexhibitfetishtt = f"{{image=question_mark_small}} Does she like public sex?"
        if person.sexy_opinions.get("public sex")==None:
            $ VTexhibitfetishst = "knowbody"
            $ VTexhibitfetishtt = f"{{image=question_mark_small}} Does she like public sex?"
        else:
            if person.sexy_opinions.get("public sex")[1]==True:
                if person.has_exhibition_fetish:
                    $ VTexhibitfetishst = "vtcherries"
                    $ VTexhibitfetishtt = f"{{image=vtcherries_small}} My body deserves to be seen!"
                    if person.event_triggers_dict.get("exhibition_fetish_locked",0)<day:
                        $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Ugh my skin is itchy I need\nmy skin free soon!"
                    else:
                        $ VTexhibitfetishtt += f"\n{{image=creamcherry_small}} MMmmMm my skin feels good."
                else:
                    if person.opinion.public_sex >=2 and person.opinion.not_wearing_underwear >= 2 and person.opinion.not_wearing_anything >= 2  and person.known_opinion("not wearing underwear") and person.known_opinion("not wearing anything") and person.opinion.showing_her_ass >= 2 and person.opinion.showing_her_tits >= 2  and person.known_opinion("showing her ass") and person.known_opinion("showing her tits") and person.opinion.skimpy_outfits >= 2 and person.opinion.skimpy_uniforms >= 2 and person.known_opinion("skimpy outfits") and person.known_opinion("skimpy uniforms"):
                        $ VTexhibitfetishst = "nudebody"
                        $ VTexhibitfetishtt = f"{{image=progress_token_small}} My skin needs to breathe and be free!"
                        if person.has_taboo("sucking_cock"):
                            $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Have her suck your cock."
                        if person.has_taboo("vaginal_sex"):
                            $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}} Have sex with her."
                        if person.known_opinion("being covered in cum"):
                            if person.opinion.being_covered_in_cum <2:
                                $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Needs to love being covered in cum!"
                        else:
                            $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Need her opinion on being covered in cum."
                        if person.cum_exposure_count < 19:
                            $ VTexhibitfetishtt += f"\n{{image=triskelion_token_small}}  Feed her, spray her, or fill her\n with your cum "+ str(19 - person.cum_exposure_count)+" more times!"
                        else:
                            if person.event_triggers_dict.get("exhibition_fetish_locked",0)<day:
                                $ VTexhibitfetishtt += f"\n{{image=creamcherry_small}} Natural Exhibition Fetish Event will trigger soon!"
                    else:
                        if person.opinion.not_wearing_underwear >= 2 and person.opinion.not_wearing_anything >= 2  and person.known_opinion("not wearing underwear") and person.known_opinion("not wearing anything") and person.opinion.skimpy_outfits >= 2 and person.opinion.skimpy_uniforms >= 2 and person.known_opinion("skimpy outfits") and person.known_opinion("skimpy uniforms") and person.opinion.public_sex>=2 and person.known_opinion("public sex"):
                            $ VTexhibitfetishst = "nudebody"
                            $ VTexhibitfetishtt = f"{{image=progress_token_small}} Needs to be more comfortable showing skin!"
                            if person.known_opinion("showing her ass")==False:
                                $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Need her opinion on showing her ass."
                            else:
                                if person.opinion.showing_her_ass <2:
                                    $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Needs to be more comfortable showing her ass."
                            if person.known_opinion("showing her tits")==False:
                                $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Need her opinion on showing her tits."
                            else:
                                if person.opinion.showing_her_tits <2:
                                    $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Needs to be more comfortable showing her tits."
                        else:
                            if person.opinion.skimpy_outfits >= 2 and person.opinion.skimpy_uniforms >= 2 and person.known_opinion("skimpy outfits") and person.known_opinion("skimpy uniforms") and person.opinion.public_sex>=1 and person.known_opinion("public sex"):
                                $ VTexhibitfetishst = "underwear"
                                $ VTexhibitfetishtt = f"{{image=progress_token_small}} Train her to be more comfortable not wearing underwear.. How about nothing at all?!"
                                if person.opinion.public_sex <2:
                                    $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Needs to be more comfortable having public sex."
                                if person.known_opinion("not wearing underwear")==False:
                                    $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Need her opinion on not wearing underwear."
                                else:
                                    if person.opinion.not_wearing_underwear <2:
                                        $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Needs to be more comfortable wearing no underwear."
                                if person.known_opinion("not wearing anything")==False:
                                    $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Need her opinion on not wearing anything."
                                else:
                                    if person.opinion.not_wearing_anything <2:
                                        $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Needs to be more comfortable not wearing anything."
                            else:
                                if person.opinion.public_sex >0 and person.known_opinion("public sex"):
                                    $ VTexhibitfetishst = "bodyconcealed"
                                    $ VTexhibitfetishtt = f"{{image=progress_token_small}} Turn her into a beautiful exhibitionist!"
                                    if person.known_opinion("skimpy outfits")==False:
                                        $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Need her opinion on skimpy outfits."
                                    else:
                                        if person.opinion.skimpy_outfits <2:
                                            $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Needs to love skimpy outfits."
                                    if person.known_opinion("skimpy uniforms")==False:
                                        $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Need her opinion on skimpy uniforms."
                                    else:
                                        if person.opinion.skimpy_uniforms <2:
                                            $ VTexhibitfetishtt += f"\n{{image=red_heart_token_small}} Needs to love skimpy uniforms."
                                    if person.known_opinion("public sex")==False:
                                        $ VTexhibitfetishtt += f"\n{{image=question_mark_small}} Need to know if she likes public sex."
                                else:
                                    if person.opinion.public_sex == 0 and person.known_opinion("public sex"):
                                        $ VTexhibitfetishst = "bodyconcealed"
                                        $ VTexhibitfetishtt = f"{{image=progress_token_small}} She's indifferent to public sex, so make her like it..."
                                    else:
                                        $ VTexhibitfetishst = "bodyconcealed"
                                        $ VTexhibitfetishtt = f"{{image=question_mark_small}} Does she like public sex?"
                                        if person.opinion.public_sex <= -2:
                                            $ VTexhibitfetishtt = f"{{image=dislike_small}} She hates public sex!"
                                        else:
                                            $ VTexhibitfetishtt = f"{{image=dislike_small}} She dislikes public sex!"
            else:
                $ VTexhibitfetishst = "knowbody"
                $ VTexhibitfetishtt = f"{{image=question_mark_small}} Does she like public sex?"
        #the interactive icons during sex stuff
        if 'position_choice' in globals():
            if hasattr(position_choice, 'skill_tag'):
                $ VTexhibitfetishat = "sexualized"
                if person.vagina_available or person.tits_available:
                    $ VTexhibitfetishst = "bodyskimpy"
                    $ VTexhibitfetishtt = f"{{image=progress_token_small}} She is fully clothed."
                    if person.vagina_available and person.tits_available:
                        $ VTexhibitfetishst = "nudebody"
                        $ VTexhibitfetishtt = f"{{image=vtcherries_small}} You can see her tits and pussy."
                        if person.arousal_perc >= 59:
                            $ VTexhibitfetishtt += f"\n{{image=vtcherries_small}} You can see her aroused nipples and wet hot juicy pussy."
                        if person.vaginal_cum >0:
                            if person.vaginal_cum >3:
                                $ VTexhibitfetishtt += f"\n{{image=openvag_small}} You can see your cum oozing from her pussy."
                            else:
                                $ VTexhibitfetishtt += f"\n{{image=openvag_small}} You can see your cum starting to drip from her pussy."
                    else:
                        $ VTexhibitfetishtt = f"{{image=vtcherries_small}} She is partly clothed."
                        if person.tits_available:
                            $ VTexhibitfetishst = "bodypanties"
                            $ VTexhibitfetishtt += f"\n{{image=vtcherries_small}} You can see her tits."
                        if person.vagina_available:
                            $ VTexhibitfetishst = "bodybra"
                            if person.arousal_perc >= 59:
                                $ VTexhibitfetishtt += f"\n{{image=spreadvag_small}} You can see her wet hot juicy pussy."
                            else:
                                $ VTexhibitfetishtt += f"\n{{image=spreadvag_small}} You can see her pussy."
                            if person.vaginal_cum >0:
                                if person.vaginal_cum >3:
                                    $ VTexhibitfetishtt += f"\n{{image=openvag_small}} You can see your cum oozing from her pussy."
                                else:
                                    $ VTexhibitfetishtt += f"\n{{image=openvag_small}} You can see your cum starting to drip from her pussy."
                else:
                    $ VTexhibitfetishst = "bodyskimpy"
                    $ VTexhibitfetishtt += f"{{image=progress_token_small}} She is fully clothed."

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

        if person.sexy_opinions.get("public sex", (0, False))[1]:
            if person.opinion.public_sex < 0 and person.sexy_opinions.get("public sex")[1]==True and VTexhibitfetishat=="talking":
                imagebutton:
                    pos(718, 166)
                    idle "dislike"
                    action NullAction()
                    tooltip VTexhibitfetishtt

###### Cum Fetish
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
                        $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} MMmmMm going to need your yummy\nlollipop in my mouth in soon!"
                    else:
                        $ VTcumfetishst = "creamcherry"
                        $ VTcumfetishtt = "*fetish 'a'salted complete*"
                        $ VTcumfetishtt += f"\n{{image=creamcherry_small}} MMmmMm still taste you in my mouth..."
                else:
                    if person.oral_sex_skill >= 4 and person.opinion.giving_blowjobs >= 2 and (person.opinion.drinking_cum >= 2 or person.opinion.cum_facials >= 2) and person.opinion.being_covered_in_cum>=2 and not person.has_taboo("sucking_cock") and not person.has_taboo("condomless_sex"):
                        $ VTcumfetishst = "openmouth"
                        $ VTcumfetishtt = f"{{image=progress_token_small}} Likes your cum! EVERYWHERE!"
                        if person.cum_exposure_count>=19:
                             $ VTcumfetishtt += f"\n{{image=creamcherry_small}} Natural Oral fetish event will trigger soon!"
                        else:
                            $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Feed her, spray her, or fill her\n with your cum "+ str(19 - person.cum_exposure_count)+" more times!"
                    else:
                        if person.opinion.giving_blowjobs >= 2 and ((person.opinion.drinking_cum >= 2 and person.known_opinion("drinking cum")) or (person.opinion.cum_facials >= 2 and person.known_opinion("cum facials"))) and person.opinion.being_covered_in_cum>=2:
                            $ VTcumfetishst = "bitelip"
                            $ VTcumfetishtt = f"{{image=progress_token_small}} Train her oral skills to vacuum and polish you like a pro!"
                            if person.oral_sex_skill<4:
                                $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Train her oral skills "+ str(4 - person.oral_sex_skill)+" more times!\nIncrease her Hoover Power!"
                            if person.has_taboo("sucking_cock"):
                                $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Have her suck your cock!"
                            if person.has_taboo("condomless_sex"):
                                $ VTcumfetishtt += f"\n{{image=triskelion_token_small}} Have sex without a condom with her!"
                        else:
                            if person.opinion.giving_blowjobs >= 1:
                                $ VTcumfetishst = "pinklips"
                                $ VTcumfetishtt = f"{{image=progress_token_small}} Make her become your cum Queen!"
                                if person.known_opinion("drinking cum")==False:
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Needs her opinion on drinking cum."
                                else:
                                    if person.opinion.drinking_cum < 2:
                                        $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Need her to love drinking cum."
                                if person.known_opinion("cum facials")==False:
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Needs her opinion on cum facials."
                                else:
                                    if person.opinion.cum_facials < 2:
                                        $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Need her to love cum facials."
                                if person.known_opinion("being covered in cum")==False:
                                    $ VTcumfetishtt += f"\n{{image=question_mark_small}} Needs her opinion on being covered in cum."
                                else:
                                    if person.opinion.being_covered_in_cum < 2:
                                        $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Need her to love being covered in cum."
                                if person.opinion.giving_blowjobs < 2:
                                    $ VTcumfetishtt += f"\n{{image=red_heart_token_small}} Need her to love giving blowjobs."
                            else:
                                if person.opinion.giving_blowjobs == 0:
                                    $ VTcumfetishst = "openmouth"
                                    $ VTcumfetishtt = f"{{image=progress_token_small}} She's indifferent to oral, so make her like it..."
                                else:
                                    $ VTcumfetishst = "openmouth"
                                    if person.opinion.giving_blowjobs == -2:
                                        $ VTcumfetishtt = f"{{image=dislike_small}} She hates oral!"
                                    if person.opinion.giving_blowjobs == -1:
                                        $ VTcumfetishtt = f"{{image=dislike_small}} She dislikes oral!"
            else:
                $ VTcumfetishst = "knowlips"
                $ VTcumfetishtt = f"{{image=question_mark_small}} Does she like giving blow jobs?"

        #the interactive icons during sex stuff
        if 'position_choice' in globals():
            $ VTcumfetishat = "sexualized"
            if person.oral_cum ==1:
                $ VTcumfetishst = "bitelip"
            if person.oral_cum >1:
                $ VTcumfetishst = "ahegaomouth"

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

        if person.sexy_opinions.get("giving blowjobs", (0, False))[1]:
            if person.opinion.giving_blowjobs < 0 and person.sexy_opinions.get("giving blowjobs")[1]==True:
                imagebutton:
                    pos(755, 166)
                    idle "dislike"
                    action NullAction()
                    tooltip VTcumfetishtt
###### Anal Fetish
        $ VTanalfetishat = "talking"
        $ VTanalfetishst = "knowpeach"
        $ VTanalfetishtt = "Her thoughts on anal sex?"
        if person.sexy_opinions.get("anal sex")==None:
            $ VTanalfetishst = "knowpeach"
            $ VTanalfetishtt = f"{{image=question_mark_small}} Her thoughts on anal sex?"
        else:
            if person.sexy_opinions.get("anal sex")[1]==True:
                if person.has_anal_fetish:
                    $ VTanalfetishst = "vtcherries"
                    $ VTanalfetishtt = f"\n{{image=triskelion_token_small}} mmmm stick your cock in my ass!"
                    if person.days_since_event("LastAnalFetish") > 10:
                        $ VTanalfetishtt = f"{{image=triskelion_token_small}} MMmmMm going to need your yummy\ncock in my ass soon!"
                    else:
                        $ VTanalfetishst = "creamcherry"
                        $ VTanalfetishtt = "*fetish 'ass'salted complete*"
                        $ VTanalfetishtt += f"\n{{image=creamcherry_small}} MMmmMm my ass still molded to your cock."
                else:
                    if person.anal_sex_skill >= 5 and (person.opinion.anal_sex >= 2  or person.opinion.anal_creampies >= 2):
                        $ VTanalfetishst = "handass"
                        $ VTanalfetishtt = f"{{image=progress_token_small}} Sodomize your Anal Queen!"
                        if person.anal_sex_count>=10 or person.anal_creampie_count>=10:
                            $ VTanalfetishtt += f"\n{{image=creamcherry_small}} Wait for the anal fetish event to trigger!"
                        else:
                            if person.anal_sex_count<10 and person.opinion.anal_sex >=2:
                                $ VTanalfetishtt += f"\n{{image=triskelion_token_small}} Have anal sex with her "+str(10 - person.anal_sex_count)+" more times!"
                            if person.anal_creampie_count<10 and person.opinion.anal_creampies >=2:
                                $ VTanalfetishtt += f"\n{{image=triskelion_token_small}} Fill her bowels full of cum "+str(10 - person.anal_creampie_count)+" more times!"
                    else:
                        if (person.opinion.anal_creampies >= 1 and person.known_opinion("anal creampies")) or person.opinion.anal_sex >= 1:
                            $ VTanalfetishst = "yesanal"
                            $ VTanalfetishtt = f"{{image=progress_token_small}} Train her into your Anal Queen!"
                            if person.anal_sex_skill <5:
                                $ VTanalfetishtt += f"\n{{image=triskelion_token_small}} Train her anal sex skill "+ str(5 - person.anal_sex_skill)+" more times!"
                            
                            if person.known_opinion("anal creampies")==False:
                                $ VTanalfetishtt += f"\n{{image=question_mark_small}} Need her opinion on anal creampies."
                            else:
                                if person.opinion.anal_creampies <2:
                                    $ VTanalfetishtt += f"\n{{image=red_heart_token_small}} Need her to love anal creampies."
                            
                            if person.opinion.anal_sex <2:
                                $ VTanalfetishtt += f"\n{{image=red_heart_token_small}} Need her to love anal sex."
                        else:
                            if person.opinion.anal_sex == 0:
                                $ VTanalfetishst = "bodyconcealed"
                                $ VTanalfetishtt = f"{{image=progress_token_small}} She's indifferent to public sex, so make her like it..."
                            else:
                                $ VTanalfetishst = "yespeach"
                                $ VTanalfetishtt = f"{{image=progress_token_small}} Train your Anal Queen!"
                                if person.opinion.anal_sex == -2:
                                    $ VTanalfetishtt += f"\n{{image=dislike_small}} She hates anal!"
                                if person.opinion.anal_sex == -1:
                                    $ VTanalfetishtt += f"\n{{image=dislike_small}} She dislikes anal!"
            else:
                $ VTanalfetishst = "knowpeach"
                $ VTanalfetishtt = f"{{image=question_mark_small}} Her thoughts on anal sex?"

        #the interactive icons during sex stuff
        if 'position_choice' in globals():
            # if hasattr(position_choice, 'skill_tag'):
            $ VTanalfetishat = "sexualized"

        if VTcumfetishat=="sexualized":
            if person.anal_cum ==1:
                $ VTanalfetishst = "handass"
                $ VTanalfetishtt += f"\n{{image=ahegaoanal_small}} Your cum is lubricating her bowels."
            if person.anal_cum >1:
                $ VTanalfetishtt += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n swimming in her bowels."
            if person.anal_cum >3:
                $ VTanalfetishst = "ahegaopeach"
            imagebutton:
                pos(792, 166)
                idle VTanalfetishst
                action NullAction()
                tooltip VTanalfetishtt

        if VTanalfetishat=="talking":
            if person.anal_cum ==1:
                $ VTanalfetishtt += f"\n{{image=ahegaoanal_small}} Your cum is lubricating in her bowels."
            if person.anal_cum >1:
                $ VTanalfetishtt += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n swimming in her bowels."
            imagebutton:
                pos(792, 166)
                idle VTanalfetishst
                action NullAction()
                tooltip VTanalfetishtt

        if person.sexy_opinions.get("anal sex", (0, False))[1]:
            if person.opinion.anal_sex < 0 and person.sexy_opinions.get("anal sex")[1]==True:
                imagebutton:
                    pos(792, 166)
                    idle "dislike"
                    action NullAction()
                    tooltip VTanalfetishtt
###### Breeding Fetish
        $ VTbreedfetishat = "talking"
        $ VTbreedfetishst = "knowpeach"
        $ VTbreedfetishtt = f"{{image=question_mark_small}} Her thoughts on vaginal sex?"
        if person.sexy_opinions.get("vaginal sex")==None:
            $ VTbreedfetishst = "knowpeach"
            $ VTbreedfetishtt = f"{{image=question_mark_small}} Her thoughts on vaginal sex?"
        else:
            if person.sexy_opinions.get("vaginal sex")[1]==True:
                if person.has_breeding_fetish:
                    
                    if person.days_since_event("LastBreedingFetish") > 10 and not person.is_pregnant and person.vaginal_cum == 0:
                        $ VTbreedfetishtt = f"{{image=triskelion_token_small}} MMmmMm going to need another \nyummy creampie filling soon!"
                    else:
                        if person.is_pregnant or person.vaginal_cum > 0:
                            $ VTbreedfetishst = "creamcherry"
                            $ VTbreedfetishtt = "*fetish 'full'filled*"
                            $ VTbreedfetishtt += f"\n{{image=creamcherry_small}} MMmmMmmm my womb is happy."
                        else:
                            $ VTbreedfetishst = "vtcherries"
                            $ VTbreedfetishtt = "Breed me! Fill my baby room full of your cum!"
                else:
                    if person.vaginal_sex_skill >= 5 and person.opinion.vaginal_sex >= 2  and person.opinion.creampies >= 2 and person.known_opinion("creampies"):
                        $ VTbreedfetishst = "openvag"
                        $ VTbreedfetishtt = f"{{image=progress_token_small}} She loves your cum in her womb!"
                        if person.vaginal_creampie_count<10:
                            $ VTbreedfetishtt += f"\n{{image=triskelion_token_small}} Fill her full of cum "+ str(10 - person.vaginal_creampie_count)+" more times!"
                        else:
                            if person.is_pregnant:
                                $ VTbreedfetishtt += f"\n{{image=creamcherry_small}} She is already pregnant!"
                            else:
                                $ VTbreedfetishtt += f"\n{{image=creamcherry_small}} Natural breeding fetish event will trigger soon!"
                        if person.has_taboo("condomless_sex"):
                            $ VTbreedfetishtt += f"\n{{image=triskelion_token_small}} Break her condomless sex taboo!"
                        if person.has_taboo("vaginal_sex"):
                            $ VTbreedfetishtt += f"\n{{image=triskelion_token_small}} Have vaginal sex with her to break taboo!"
                    else:
                        if person.opinion.vaginal_sex >= 2 and person.vaginal_sex_skill >=2  and (person.opinion.creampies >= 2 and person.known_opinion("creampies")):
                            $ VTbreedfetishst = "spreadvag"
                            $ VTbreedfetishtt = f"{{image=progress_token_small}} Train her vaginal sex skills!"
                            if person.vaginal_sex_skill <5:
                                $ VTbreedfetishtt += f"\n{{image=triskelion_token_small}} Train her vaginal sex skill "+ str(5 - person.vaginal_sex_skill)+" more"
                                if (2 - person.vaginal_sex_skill) == 1:
                                    $ VTbreedfetishtt += " time!"
                                else:
                                    $ VTbreedfetishtt += " times!"
                            if person.opinion.creampies <2:
                                $ VTbreedfetishtt += f"\n{{image=red_heart_token_small}} Need her to love vaginal creampies."
                        else:
                            $ VTbreedfetishst = "vagclosed"
                            $ VTbreedfetishtt = f"{{image=progress_token_small}} Train her into your Breeding Stock!"
                            if (person.opinion.creampies >= 1 and person.known_opinion("creampies")) or person.opinion.vaginal_sex >= 1:
                                if person.vaginal_sex_skill <2:
                                    $ VTbreedfetishtt += f"\n{{image=triskelion_token_small}} Train her vaginal sex skill "+ str(2 - person.vaginal_sex_skill)+" more"
                                    if (2 - person.vaginal_sex_skill) == 1:
                                        $ VTbreedfetishtt += " time!"
                                    else:
                                        $ VTbreedfetishtt += " times!"
                                if person.known_opinion("creampies")==False:
                                    $ VTbreedfetishtt += f"\n{{image=question_mark_small}} Need her opinion on vaginal creampies."
                                else:
                                    if person.opinion.creampies < 2:
                                        $ VTbreedfetishtt += f"\n{{image=red_heart_token_small}} Need her to love vaginal creampies."
                                if person.known_opinion("vaginal sex")==False:
                                    $ VTbreedfetishtt += f"\n{{image=question_mark_small}} Need her opinion on vaginal sex."
                                else:
                                    if person.opinion.vaginal_sex < 2:
                                        $ VTbreedfetishtt += f"\n{{image=red_heart_token_small}} Need her to love vaginal sex."
                            else:
                                if person.opinion.vaginal_sex == 0:
                                    $ VTbreedfetishst = "vagclosed"
                                    $ VTbreedfetishtt += f"\n{{image=progress_token_small}} She's indifferent to vaginal sex, so make her like it..."
                                else:
                                    $ VTbreedfetishst = "vagclosed"
                                    if person.opinion.vaginal_sex == -2:
                                        $ VTbreedfetishtt += f"\n{{image=dislike_small}} She hates vaginal sex!"
                                    else:
                                        if person.opinion.vaginal_sex == -1:
                                            $ VTbreedfetishtt += f"\n{{image=dislike_small}} She dislikes vaginal sex!"
            else:
                $ VTbreedfetishst = "knowpeach"
                $ VTbreedfetishtt = f"{{image=question_mark_small}} Her thoughts on vaginal sex?"

        #the interactive icons during sex stuff
        if 'position_choice' in globals():
            if hasattr(position_choice, 'skill_tag'):
                $ VTbreedfetishat = "sexualized"

        if VTbreedfetishat=="sexualized":
            if person.vaginal_cum >0:
                if person.vaginal_cum == 1:
                    if person.hymen <=1:
                        $ VTbreedfetishst = "vaghymen"
                        $ VTbreedfetishtt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."
                    else:
                        $ VTbreedfetishtt = f"{{image=beezee_token_small}} Your seed is in her"+VTbreedfertile+VTpro+" womb."
                else:
                    if person.hymen <=1:
                        $ VTbreedfetishst = "vaghymen"
                        $ VTbreedfetishtt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} Marked her fresh"+VTbreedfertile+VTpro+" womb with "+str(person.vaginal_cum)+ " doses of your seed."
                    else:
                        if person.vaginal_cum <3:
                            $ VTbreedfetishst = "openvag"
                        else:
                            $ VTbreedfetishst = "ahegaovag"
                        $ VTbreedfetishtt = f"{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."+daysince
            imagebutton:
                pos(829, 166)
                idle VTbreedfetishst
                action NullAction()
                tooltip VTbreedfetishtt

        if VTbreedfetishat=="talking":
            if person.vaginal_cum >0:
                if person.vaginal_cum == 1:
                    if person.hymen <=1:
                        $ VTbreedfetishst = "vaghymen"
                        $ VTbreedfetishtt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} Marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."
                    else:
                        $ VTbreedfetishtt += f"\n{{image=beezee_token_small}} Your seed is in her"+VTbreedfertile+VTpro+" womb."
                else:
                    if person.hymen <=1:
                        $ VTbreedfetishst = "vaghymen"
                        $ VTbreedfetishtt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} Marked her fresh"+VTbreedfertile+VTpro+" womb with "+str(person.vaginal_cum)+ " doses of your seed."
                    else:
                        $ VTbreedfetishtt += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."+daysince
            imagebutton:
                pos(829, 166)
                idle VTbreedfetishst
                action NullAction()
                tooltip VTbreedfetishtt

            if person.hymen >1 and person.vaginal_cum >1:
                imagebutton:
                    pos(829, 166)
                    idle "bc_cum"
                    action NullAction()
                    tooltip VTbreedfetishtt

        if person.sexy_opinions.get("vaginal sex", (0, False))[1]:
            if person.opinion.vaginal_sex < 0 and person.sexy_opinions.get("vaginal sex")[1]==True and VTbreedfetishat=="talking":
                imagebutton:
                    pos(829, 166)
                    idle "dislike"
                    action NullAction()
                    tooltip VTbreedfetishtt

##### Wants Creampies
        $ VTcreampieat = "talking"
        $ VTcreampieck = ""
        $ VTcreamcount = 0
        if person.wants_creampie and (person.has_anal_fetish or person.has_breeding_fetish) and (person.opinion.anal_creampies >= 2 and person.known_opinion("anal creampies")) and (person.opinion.creampies >= 2 and person.known_opinion("creampies")):
            $ VTcreampiett = f"{{image=creamcherry_small}} She loves her creampies!"
            if person.has_breeding_fetish and (person.days_since_event("LastBreedingFetish") < 10 or person.is_pregnant):
                $ VTcreamcount +=1
                $ VTcreampiett += f"\n{{image=creamcherry_small}} MMmmMmmm my womb is happy."
            else:
                if person.has_breeding_fetish:
                    $ VTcreampiett += f"\n{{image=progress_token_small}} Needs cum in my pussy!"
                else:
                    $ VTcreampiett += f"\n{{image=progress_token_small}} Needs Breeding Fetish Unlocked."
            if person.has_anal_fetish and person.days_since_event("LastAnalFetish") < 10:
                $ VTcreampiett += f"\n{{image=creamcherry_small}} MMmmMm my ass still molded to your cock."
                $ VTcreamcount +=1
            else:
                if person.has_anal_fetish:
                    $ VTcreampiett += f"\n{{image=progress_token_small}} Needs cum in my ass!"
                else:
                    $ VTcreampiett += f"\n{{image=progress_token_small}} Needs Anal Fetish Unlocked."
            if VTcreamcount >0:
                $ VTcreampiest = "creamcherry"
            else:
                $ VTcreampiest = "vtcherries"
                $ VTcreampiett  += f"\n{{image=triskelion_token_small}} She needs her cream!"
        else:
            if (person.opinion.anal_creampies >= 1 and person.known_opinion("anal creampies")) or (person.opinion.creampies >= 1 and person.known_opinion("creampies")):
                $ VTcreampiest = "openpeach"
                $ VTcreampiett = f"{{image=progress_token_small}} Keep giving her the cream fillings!"
                if person.known_opinion("anal creampies")==False or person.opinion.anal_creampies < 2:
                    $ VTcreampiett += f"\n{{image=red_heart_token_small}} Make her love anal creampies!"
                if person.known_opinion("creampies")==False or person.opinion.creampies < 2:
                    $ VTcreampiett += f"\n{{image=red_heart_token_small}} Make her love vaginal creampies!"
                if not person.has_anal_fetish:
                    $ VTcreampiett += f"\n{{image=ahegaoanal_small}} Needs the Anal Fetish Unlocked." 
                if not person.has_breeding_fetish and persistent.pregnancy_pref > 0:
                    $ VTcreampiett += f"\n{{image=ahegaovag_small}} Needs the Breeding Fetish Unlocked."
            else:
                if person.known_opinion("anal creampies") or person.known_opinion("creampies"):
                    if (person.known_opinion("anal creampies") and person.opinion.anal_creampies < 1) or (person.known_opinion("creampies") and person.opinion.creampies <1):
                        $ VTcreampiest = "yespeach"
                        $ VTcreampiett = f"{{image=progress_token_small}} Doesn't seem to like creampies?"
                        if person.known_opinion("anal creampies")==False or person.opinion.anal_creampies < 2:
                            $ VTcreampiett += f"\n{{image=question_mark_small}} Make her like anal creampies!"
                        if person.known_opinion("creampies")==False or person.opinion.creampies < 2:
                            $ VTcreampiett += f"\n{{image=question_mark_small}} Make her like vaginal creampies!"
                    if (person.known_opinion("anal creampies") and person.opinion.anal_creampies < 1) or (person.known_opinion("creampies") and person.opinion.creampies <1):
                        $ VTcreampiest = "yespeach"
                        $ VTcreampiett = f"{{image=progress_token_small}} Make her like creampies!"
                        if (person.known_opinion("anal creampies") and person.opinion.anal_creampies < 1):
                            if person.opinion.anal_creampies ==-2:
                                $ VTcreampiett += f"\n{{image=dislike_small}} She hates anal creampies!"
                            else:
                                if person.opinion.anal_creampies == 0:
                                     $ VTcreampiett += f"\n{{image=knowpeach_small}} She is indifferent to anal creampies!"
                                else:
                                     $ VTcreampiett += f"\n{{image=dislike_small}} She doesn't like anal creampies!"
                        if (person.known_opinion("creampies") and person.opinion.creampies <1):
                            if person.opinion.creampies ==-2:
                                $ VTcreampiett += f"\n{{image=dislike_small}} She hates vaginal creampies!"
                            else:
                                if person.opinion.creampies == 0:
                                     $ VTcreampiett += f"\n{{image=knowpeach_small}} She is indifferent to vaginal creampies!"
                                else:
                                     $ VTcreampiett += f"\n{{image=dislike_small}} She doesn't like vaginal creampies!"
                else:
                    $ VTcreampiest = "knowpeach"
                    $ VTcreampiett = f"{{image=question_mark_small}} Does she like creampies?"

        #the interactive icons during sex stuff
        if 'position_choice' in globals():
            if hasattr(position_choice, 'skill_tag'):
                $ VTcreampieat = "sexualized"

        if VTcreampieat=="sexualized":
            if person.vaginal_cum >0:
                if person.vaginal_cum == 1:
                    $ VTcreampiest = "openvag"
                    $ VTcreampiett += f"\n{{image=beezee_token_small}} Your cum is swimming in her"+VTbreedfertile+VTpro+" womb."
                else:
                    $ VTcreampiest = "ahegaovag"
                    $ VTcreampiett += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."
            if person.anal_cum >0:
                if person.anal_cum == 1:
                    $ VTcreampiest = "handass"
                    $ VTcreampiett += f"\n{{image=ahegaoanal_small}} Your cum is swimming in her bowels."
                else:
                    $ VTcreampiest = "ahegaopeach"
                    $ VTcreampiett += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n is swimming in her bowels."
            imagebutton:
                pos(866, 166)
                idle VTcreampiest
                action NullAction()
                tooltip VTcreampiett                    

        if VTcreampieat=="talking":
            if person.vaginal_cum >0:
                if person.vaginal_cum == 1:
                    $ VTcreampiett += f"\n{{image=beezee_token_small}} Your cum is swimming in her"+VTbreedfertile+VTpro+" womb."
                else:
                    $ VTcreampiett += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n is swimming in her"+VTbreedfertile+VTpro+" womb."
            if person.anal_cum >0:
                if person.anal_cum == 1:
                    $ VTcreampiett += f"\n{{image=ahegaoanal_small}} Your cum is swimming in her bowels."
                else:
                    $ VTcreampiett += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n is swimming in her bowels."
            imagebutton:
                pos(866, 166)
                idle VTcreampiest
                action NullAction()
                tooltip VTcreampiett
            if person.anal_cum >1 or person.vaginal_cum >1:
                imagebutton:
                    pos(866, 166)
                    idle "bc_cum"
                    action NullAction()
                    tooltip VTcreampiett
        if (person.known_opinion("anal creampies") and person.opinion.anal_creampies < 0) or (person.known_opinion("creampies") and person.opinion.creampies <0):
            imagebutton:
                pos(866, 166)
                idle "dislike"
                action NullAction()
                tooltip VTcreampiett

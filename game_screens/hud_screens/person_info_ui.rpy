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
        if anal_fetish_role in person.special_role:
            active_fetishes.append("Anal")
        if cum_fetish_role in person.special_role:
            active_fetishes.append("Cum")
        if breeding_fetish_role in person.special_role:
            active_fetishes.append("Breeding")
        if exhibition_fetish_role in person.special_role:
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

screen person_info_ui(person): #Used to display stats for a person while you're talking to them.
    tag master_tooltip
    layer "solo" #By making this layer active it is cleared whenever we draw a person or clear them off the screen.
    zorder 200

    default home_hub_name = person.home_hub.formal_name
    default job_title = person_info_ui_get_job_title(person)
    default height_info = height_to_string(person.height)
    default weight_info = get_person_weight_string(person)

    $ vt_store.sexualized = 'position_choice' in globals() and hasattr(position_choice, 'skill_tag')

    python:
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
                        if len(fetish_list) > 0:
                            text "- Fetishes: [fetish_info]" style "menu_text_style" size 12 xoffset 60

                        for role in role_list:
                            text "- [role]" style "menu_text_style" size 12 xoffset 60

            vbox:
                yoffset 5
                xmaximum 280
                xminimum 280

                textbutton "Arousal: [arousal_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip f"When a girl is brought to 100% arousal she will start to climax. Climaxing will make a girl happier and may put them into a Trance if their suggestibility is higher than 0.\nCurrently: {get_arousal_number_string(person.arousal, person.max_arousal)}"
                    action NullAction()
                    sensitive True

                textbutton "Energy: [energy_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip f"Energy is spent while having sex, with more energy spent on positions that give the man more pleasure. Some energy comes back each turn, and a lot of energy comes back overnight.\nCurrently {get_energy_number_string(person.energy, person.max_energy)}"
                    action NullAction()
                    sensitive True

                textbutton "Happiness: [happiness_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "The happier a girl the more tolerant she will be of low pay and unpleasant interactions. High or low happiness will return to it's default value over time."
                    action NullAction()
                    sensitive True

                textbutton "Love: [love_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip f"Girls who love you will be more willing to have sex when you're in private (as long as they aren't family) and be more devoted to you. Girls who hate you will have a lower effective sluttiness regardless of the situation.\nWhen a girl is not part of your harem, she will slowly loose love until it reaches 80, having sex once every five days will stop the love bleed.\nLove: {get_attention_number_string(person.love, 100)}"
                    action NullAction()
                    sensitive True

                hbox:
                    textbutton "Obedience: [obedience_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip f"Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, low obedience girls are likely to refuse altogether.\nActive modifiers will be shown under {{image=question_mark_small}}.\nDominant girls will bleed 1 obedience a day and any other girl that is not a slave will bleed one obedience per day to 200."
                        action NullAction()
                        sensitive True

                    if bool(person.situational_obedience):
                        textbutton "{image=question_mark_small}":
                            style "transparent_style"
                            tooltip person_info_ui_get_formatted_obedience_tooltip(person)
                            action NullAction()
                            sensitive True

                hbox:
                    textbutton "Sluttiness: [sluttiness_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip f"The higher a girls sluttiness the more slutty actions she will consider acceptable and normal. Temporary sluttiness ({{image=red_heart_token_small}}) is added to her sluttiness based on arousal, active modifiers will be shown under {{image=question_mark_small}}.\nSluttiness: {get_attention_number_string(person.effective_sluttiness(), 100)}"
                        action NullAction()
                        sensitive True

                    if bool(person.situational_sluttiness):
                        textbutton "{image=question_mark_small}":
                            style "transparent_style"
                            tooltip person_info_ui_get_formatted_tooltip(person)
                            action NullAction()
                            sensitive True

            vbox:
                yoffset 5
                xmaximum 200
                xminimum 200

                textbutton "Suggestibility: [person.suggestibility]%":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "How likely a girl is to slip into a trance when she cums. While in a trance she will be highly suggestible, and you will be able to directly influence her stats, skills, and opinions."
                    action NullAction()
                    sensitive True

                textbutton "Age: [person.age]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "The age of the girl."
                    action NullAction()
                    sensitive True

                textbutton "Height: [height_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    if persistent.use_imperial_system:
                        tooltip "The length of the girl in feet and inches."
                    else:
                        tooltip "The length of the girl in centimetres."
                    action NullAction()
                    sensitive True

                textbutton "Cup size: [person.tits]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "The size of the breasts."
                    action NullAction()
                    sensitive True

                textbutton "Weight: [weight_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    if persistent.use_imperial_system:
                        tooltip "The weight of the girl in pounds.\nDetermines the body type."
                    else:
                        tooltip "The weight of the girl in kilograms\nDetermines the body type."
                    action NullAction()
                    sensitive True

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

        if person.mc_knows_address:
            imagebutton:
                pos (1020, 5)
                idle "home_marker"
                tooltip f"She lives in {home_hub_name}."
                action NullAction()
                sensitive True

        if person.can_clone:
            imagebutton:
                pos (1060, 5)
                idle "dna_sequence"
                tooltip "This person can be cloned."
                action NullAction()
                sensitive True

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
                sensitive True

        if person.serum_tolerance == 0:
            imagebutton:
                pos (55, 50)
                idle "serum_vial3"
                tooltip "Warning: this person has no tolerance for serums\n" + person_info_ui_get_serum_info_tooltip(person)
                action NullAction()
                sensitive True
        elif person.serum_effects:
            imagebutton:
                pos (55, 50)
                idle ("serum_vial3" if len(person.serum_effects) > person.serum_tolerance
                else "serum_vial2" if len(person.serum_effects) == person.serum_tolerance
                else "serum_vial")
                tooltip person_info_ui_get_serum_info_tooltip(person)
                action NullAction()
                sensitive True

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
                tooltip "She is ovulating and has a higher chance of getting pregnant, based on birth control and desire to get pregnant."

        # imagebutton:
                # pos(240, 200)
                # idle "vtcherries"
                # action NullAction()

#### Relationship Status
        $ vt_store.relationship_icon = "norelations"
        $ vt_store.relationship_tooltip = "Has no romantic relations with you."
        if person.has_relation_with_mc:
            if person.has_role(harem_role):
                if person.has_role(affair_role):
                    $ vt_store.relationship_icon = "parapoly"
                    $ vt_store.relationship_tooltip = "She is part of your polycule, and your paramour."
                else:
                    $ vt_store.relationship_icon = "polyamorous"
                    $ vt_store.relationship_tooltip = "She is part of your polycule."
            else:
                if person.has_role(affair_role):
                    $ vt_store.relationship_icon = "paramour"
                    $ vt_store.relationship_tooltip = "She is your paramour."
                else:
                    $ vt_store.relationship_icon = "girlfriend"
                    $ vt_store.relationship_tooltip = "She is your girlfriend."

            # append global MC relationship numbers
            $ vt_store.relationship_tooltip += f"\nGirlfriends: "+ str(mc.stats.girlfriends) +" \nParamours: "+ str(mc.stats.paramours) +"\nSlaves: "+ str(mc.stats.slaves)

        imagebutton:
            pos(285, 166)
            idle vt_store.relationship_icon
            action NullAction()
            tooltip vt_store.relationship_tooltip

### Teen
        if person.age < Person.get_age_floor() + 1:
            $ vt_store.teen_tooltip = "She looks so innocent and inexperienced."
            if person.hymen <= 1 and person.vaginal_virgin <= 1:
                $ vt_store.teen_tooltip = f"{{image=virgin_token_small}} She looks so young, innocent and inexperienced."
            else:
                $ vt_store.teen_tooltip = f"{{image=yespeach_small}} She looks like a young vixen."

            imagebutton:
                pos(322, 166)
                idle "matureteen"
                action NullAction()
                tooltip vt_store.teen_tooltip

###### Birth Control Status
        # set defaults
        $ vt_store.birth_control_status_icon = "knowbirthcontrol"
        $ vt_store.birth_control_tooltip = "Is she on birth control?"
        $ vt_store.fertility_tag = ""
        $ vt_store.known_fertile = False

        if person.bc_status_known:
            if person._birth_control:
                $ vt_store.birth_control_status_icon = "birthcontrol"
                $ vt_store.birth_control_tooltip = "She is on birth control."
                $ vt_store.fertility_tag = " protected"
            elif person.is_infertile:
                $ vt_store.birth_control_status_icon = "birthcontrol"
                $ vt_store.birth_control_tooltip = "She is infertile."
                $ vt_store.fertility_tag = " infertile"
            else:
                $ vt_store.birth_control_status_icon = "nobirthcontrol"
                $ vt_store.birth_control_tooltip = "She is not on birth control."
                $ vt_store.fertility_tag = " defenseless"

                # person is not on birth control, and is not infertile
                if person.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception"):
                    $ vt_store.fertility_tag = " highly fertile" + vt_store.fertility_tag
                    $ vt_store.birth_control_tooltip += "\nShe is highly fertile."
                    $ vt_store.known_fertile = True

        # after above, check if pregnant, and override anything set above
        if person.knows_pregnant:
                $ vt_store.birth_control_status_icon = "pregnant"
                $ vt_store.birth_control_tooltip = "She is pregnant."
                $ vt_store.fertility_tag = " pregnant"

        # display base icon
        imagebutton:
            pos(359, 166)
            idle vt_store.birth_control_status_icon
            action NullAction()
            tooltip vt_store.birth_control_tooltip

        # display beezee overlay if known fertile
        if vt_store.known_fertile:
            imagebutton:
                pos(359, 166)
                idle "beezee"
                action NullAction()
                tooltip vt_store.birth_control_tooltip

        # display cum overlay if vagina holding cum
        if person.vaginal_cum > 0:
            if person.vaginal_cum == 1:
                $ vt_store.birth_control_tooltip += f"\n{{image=beezee_token_small}} Your cum swimming in her" + vt_store.fertility_tag + " womb."
            elif person.vaginal_cum > 1:
                $ vt_store.birth_control_tooltip += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her" + vt_store.fertility_tag + " womb."

            imagebutton:
                pos(359, 166)
                idle "bc_cum"
                action NullAction()
                tooltip vt_store.birth_control_tooltip

####### Wants Condom
        # set placeholders
        $ vt_store.condom_status_icon = ""
        $ vt_store.condom_status_tooltip = ""

        # validate that the opinion exists and is known
        if "bareback sex" in person.get_known_opinion_list(include_sexy=True, include_normal=False):
            if person.opinion.bareback_sex >= 2 and person.wants_creampie and person.has_cum_fetish and person.has_anal_fetish and person.has_breeding_fetish and not person.wants_condom():
                # she loves it
                $ vt_store.condom_status_icon = "ahegaocondom"
                $ vt_store.condom_status_tooltip = "She loves it raw!"

            elif person.opinion.bareback_sex >= 0:
                # she doesn't dislike it
                $ vt_store.condom_status_icon = "wearcondom"
                if person.opinion.bareback_sex == 2 and not person.wants_condom():
                    $ vt_store.condom_status_tooltip = f"{{image=progress_token_small}} She seems to love raw sex! "
                    if not person.has_anal_fetish:
                        $ vt_store.condom_status_tooltip += f"\n{{image=ahegaoanal_small}} Needs the Anal Fetish Unlocked."
                    if not person.has_breeding_fetish:
                        $ vt_store.condom_status_tooltip += f"\n{{image=ahegaovag_small}} Needs the Breeding Fetish Unlocked."
                    if not person.has_cum_fetish:
                        $ vt_store.condom_status_tooltip += f"\n{{image=ahegaomouth_small}} Needs the Cum Fetish Unlocked."

                elif person.opinion.bareback_sex == 1:
                    $ vt_store.condom_status_tooltip = f"{{image=progress_token_small}} Open her mind up to enjoying raw more!"
                    $ vt_store.condom_status_tooltip += f"\n{{image=red_heart_token_small}} Make her love raw sex more!"
                elif person.opinion.bareback_sex == 0:
                    $ vt_store.condom_status_tooltip = f"{{image=progress_token_small}} She's indifferent to raw sex, so make her like it..."

            else:
                # she does not like it
                # display the nocondom icon with a "not" overlay
                $ vt_store.condom_status_icon = "nocondom"
                if person.opinion.bareback_sex == -1:
                    $ vt_store.condom_status_tooltip = f"She dislikes raw sex!"
                elif person.opinion.bareback_sex == -2:
                    $ vt_store.condom_status_tooltip = f"She hates raw sex!"
        else:
            # opinion not known
            $ vt_store.condom_status_icon = "knowcondom"
            $ vt_store.condom_status_tooltip = f"{{image=question_mark_small}} Does she like bareback sex?"

        # override during sex
        if vt_store.sexualized:
            # during sex
            $ vt_store.condom_status_icon = "wearcondom"
            if mc.condom:
                $ vt_store.condom_status_tooltip = "You are wearing a condom"
            else:
                $ vt_store.condom_status_tooltip = "You are natural."

            # show condom icon
            imagebutton:
                pos(396, 166)
                idle vt_store.condom_status_icon
                action NullAction()
                tooltip vt_store.condom_status_tooltip

            # overlay "not" icon if not wearing condom
            if not mc.condom:
                imagebutton:
                    pos(396, 166)
                    idle "dislike"
                    action NullAction()
                    tooltip vt_store.condom_status_tooltip

        else:
            # in conversation
            # show the base status
            imagebutton:
                pos(396, 166)
                idle vt_store.condom_status_icon
                action NullAction()
                tooltip vt_store.condom_status_tooltip

            # if the opinion is known and negative
            if person.known_opinion("bareback sex") < 0:
                # show the "dislike" overlay
                imagebutton:
                    pos(396, 166)
                    idle "dislike"
                    action NullAction()
                    tooltip vt_store.condom_status_tooltip

###### Threesome Flag - note polyamorous added
        $ vt_store.poly_status_icon = ""
        $ vt_store.poly_tooltip = ""

        # validate the opinion exists and is known
        if "threesomes" in person.get_known_opinion_list(include_sexy=True, include_normal=False):
            if person.opinion.threesomes >= 2 and person.has_cum_fetish and person.has_anal_fetish and person.known_opinion("polyamory") >=2:
                # she really loves it
                $ vt_store.poly_status_icon = "ahegaothreesomes"
                $ vt_store.poly_tooltip = "More the merrier! The mess we will make!"
            elif person.opinion.threesomes >= 2:
                # she loves it
                $ vt_store.poly_status_icon = "threesometriad"
                $ vt_store.poly_tooltip = f"{{image=progress_token_small}} Open her mind up to more!"
                if not person.has_role(harem_role):
                    if person.love < 80:
                        $ vt_store.poly_tooltip += f"\n{{image=red_heart_token_small}} "+ str(80 - person.love) +" more to add her to your polycule!"
                    else:
                        $ vt_store.poly_tooltip += "\nShe is ready to be part of your polycule!"
                if person.known_opinion("polyamory") < 2:
                    if person.known_opinion("polyamory") == 1:
                        # polyamory opinion is known, but not high enough
                        $ vt_store.poly_tooltip += f"\n{{image=red_heart_token_small}} Needs to love polyamorous more!"
                    else:
                        # polyamory opinion might not be known, or is zero/negative
                        $ vt_store.poly_tooltip += f"\n{{image=question_mark_small}} Needs to like polyamorous relationships."
                if not person.has_anal_fetish:
                    $ vt_store.poly_tooltip += f"\n{{image=ahegaoanal_small}} Needs the Anal Fetish Unlocked."
                if not person.has_cum_fetish:
                    $ vt_store.poly_tooltip += f"\n{{image=ahegaomouth_small}} Needs the Cum Fetish Unlocked."
            else:
                # she doesn't love it
                $ vt_store.poly_status_icon = "opentriad"
                if person.opinion.threesomes == 1:
                    # she likes it
                    $ vt_store.poly_tooltip = f"{{image=progress_token_small}} Open her mind up to the possibility of more!"
                    $ vt_store.poly_tooltip += f"\n{{image=red_heart_token_small}} Make her love threesomes!"
                elif person.opinion.threesomes == 0:
                    # she doesn't care
                    $ vt_store.poly_tooltip = "She's indifferent to threesomes, so make her like it..."
                elif person.opinion.threesomes == -1:
                    # she dislikes it
                    $ vt_store.poly_tooltip = f"She dislikes threesomes!"
                elif person.opinion.threesomes == -2:
                    # she hates it
                    $ vt_store.poly_tooltip = f"She hates threesomes!"
        else:
            # opinion not known
            $ vt_store.poly_status_icon = "knowthreesome"
            $ vt_store.poly_tooltip = f"{{image=question_mark_small}} Does she like threesomes?"

        # possible interactive icons during sex stuff
        if vt_store.sexualized:
            pass

        # show the base icon
        imagebutton:
            pos(433, 166)
            idle vt_store.poly_status_icon
            action NullAction()
            tooltip vt_store.poly_tooltip

        # potentially overlay dislike icon
        if person.known_opinion("threesomes") < 0 or person.known_opinion("polyamory") < 0:
            imagebutton:
                pos(433, 166)
                idle "dislike"
                action NullAction()
                tooltip vt_store.poly_tooltip

##### Wants Creampies
        $ vt_store.creampie_status_icon = ""
        $ vt_store.creampie_tooltip = ""

        if person.wants_creampie and person.known_opinion("creampies") >= 2 and person.known_opinion("anal_creampies") >= 2 and (person.has_anal_fetish and person.has_breeding_fetish):
            # she really loves both
            $ vt_store.creampie_status_icon = "ahegaopeach"
            $ vt_store.creampie_tooltip = "She wants to be filled!"

        elif builtins.max(person.known_opinion("anal creampies"), person.known_opinion("creampies")) >= 1:
            # she likes at least one
            $ vt_store.creampie_status_icon = "openpeach"
            $ vt_store.creampie_tooltip = f"{{image=progress_token_small}} Keep giving her the cream fillings!"
            if person.known_opinion("anal creampies") < 2:
                # anal creampie opinion needs raised or discovered
                $ vt_store.creampie_tooltip += f"\n{{image=red_heart_token_small}} Make her love anal creampies!"
            if person.known_opinion("creampies") < 2:
                # creampie opinion needs raised or discovered
                $ vt_store.creampie_tooltip += f"\n{{image=red_heart_token_small}} Make her love vaginal creampies!"
            if not person.has_anal_fetish:
                $ vt_store.creampie_tooltip += f"\n{{image=ahegaoanal_small}} Needs the Anal Fetish Unlocked."
            if not person.has_breeding_fetish:
                $ vt_store.creampie_tooltip += f"\n{{image=ahegaovag_small}} Needs the Breeding Fetish Unlocked."

        elif builtins.min(person.known_opinion("anal creampies"), person.known_opinion("creampies")) <= 0 and builtins.any(builtins.set(person.get_known_opinion_list(include_sexy=True, include_normal=False)).union(builtins.set(("anal creampies", "creampies")))):
            # she does not have a positive opinion of either (else would take previous branch)
            # but she does have a known opinion
            $ vt_store.creampie_tooltip = f"{{image=progress_token_small}} Doesn't seem to like creampies?"

            if builtins.all(person.known_opinion(vt_opinion) == 0 for vt_opinion in ("anal creampies", "creampies")):
                # she is indifferent to both
                $ vt_store.creampie_status_icon = "nocream"

            elif -2 < builtins.min(person.known_opinion("anal creampies"), person.known_opinion("creampies")) < 0:
                # she dislikes at least one, but she doesn't hate either of them
                $ vt_store.creampie_status_icon = "yespeach"
                if person.known_opinion("anal creampies") < 2:
                    # anal creampie opinion needs raised or discovered
                    $ vt_store.creampie_tooltip += f"\n{{image=question_mark_small}} Make her like anal creampies!"
                if person.known_opinion("creampies") < 2:
                    # creampie opinion needs raised or discovered
                    $ vt_store.creampie_tooltip += f"\n{{image=question_mark_small}} Make her like vaginal creampies!"

            # she hates at least one of them
            elif builtins.min(person.known_opinion("anal creampies"), person.known_opinion("creampies")) <= -2:
                $ vt_store.creampie_status_icon = "yespeach"
                if person.known_opinion("anal creampies") < -1 and person.known_opinion("creampies") < -1:
                    # she hates both
                    $ vt_store.creampie_tooltip = f"{{image=progress_token_small}} She hates creampies!"
                elif person.known_opinion("anal creampies") < -1:
                    $ vt_store.creampie_tooltip = f"She hates anal creampies!"
                elif person.known_opinion("creampies") < -1:
                    $ vt_store.creampie_tooltip = f"She hates vaginal creampies!"

        else:
            $ vt_store.creampie_status_icon = "knowpeach"
            $ vt_store.creampie_tooltip = f"{{image=question_mark_small}} Does she likes creampies?"

        # modify icon (if during sex) and tooltip based on cum content
        if builtins.max(person.anal_cum, person.vaginal_cum) > 1:
            if person.vaginal_cum >= person.anal_cum:
                if vt_store.sexualized:
                    $ vt_store.creampie_status_icon = "ahegaovag"
                $ vt_store.creampie_tooltip += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her" + vt_store.fertility_tag + " womb."
            else:
                if vt_store.sexualized:
                    $ vt_store.creampie_status_icon = "ahegaopeach"
                $ vt_store.creampie_tooltip += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum \n swimming in her bowels."
        elif builtins.max(person.anal_cum, person.vaginal_cum) > 0:
            if person.vaginal_cum >= person.anal_cum:
                if vt_store.sexualized:
                    $ vt_store.creampie_status_icon = "openvag"
                $ vt_store.creampie_tooltip += f"\n{{image=beezee_token_small}} Your cum swimming in her" + vt_store.fertility_tag + " womb."
            else:
                if vt_store.sexualized:
                    $ vt_store.creampie_status_icon = "handass"
                $ vt_store.creampie_tooltip += f"\n{{image=ahegaoanal_small}} Your cum swimming in her bowels."

        # show the status and tooltip
        imagebutton:
            pos(470, 166)
            idle vt_store.creampie_status_icon
            action NullAction()
            tooltip vt_store.creampie_tooltip

        # if talking and they have lots of cum in them, show the overlay
        if not vt_store.sexualized and (person.anal_cum > 1 or person.vaginal_cum > 1):
            imagebutton:
                pos(470, 166)
                idle "bc_cum"
                action NullAction()
                tooltip vt_store.creampie_tooltip

        # if they don't like creampies, show the dislike overlay
        if person.known_opinion("anal creampies") < 0 or person.known_opinion("creampies") < 0:
            imagebutton:
                pos(470, 166)
                idle "dislike"
                action NullAction()
                tooltip vt_store.creampie_tooltip
###### Cum Fetish
        $ vt_store.cum_fetish_status_icon = ""
        $ vt_store.cum_fetish_tooltip = ""

        # validate opinion exists and is known
        if "giving blowjobs" in person.get_known_opinion_list(include_sexy=True, include_normal=False):
            if person.has_cum_fetish:
                # she loves it
                $ vt_store.cum_fetish_status_icon = "ahegaomouth"
                if person.days_since_event("LastCumFetish") > 10:
                    $ vt_store.cum_fetish_tooltip = "MMmmMm going to need your yummy\nlollipop in my mouth in soon!"
                else:
                    $ vt_store.cum_fetish_tooltip = "MMmmMm still taste you in my mouth..."

            elif person.oral_sex_skill >= 5 and person.opinion.giving_blowjobs >= 2 and (person.known_opinion("drinking cum") >= 2 or person.known_opinion("cum facials") >= 2) and person.known_opinion("being covered in cum") >= 2:
                # she likes it and is quite good at it
                $ vt_store.cum_fetish_status_icon = "openmouth"
                $ vt_store.cum_fetish_tooltip = f"{{image=progress_token_small}} Likes your cum! EVERYWHERE!"
                if person.cum_exposure_count < 19:
                    $ vt_store.cum_fetish_tooltip += f"\n{{image=triskelion_token_small}} Feed her, spray her, or fill her\n with your cum "+ str(19 - person.cum_exposure_count)+" more times!"
                else:
                    $ vt_store.cum_fetish_tooltip += f"\n{{image=progress_token_small}} Wait for the cum fetish event to trigger!"

            elif person.opinion.giving_blowjobs >= 2 and (person.known_opinion("drinking cum") >= 2 or person.known_opinion("cum facials") >= 2) and person.known_opinion("being covered in cum") >= 2:
                # she likes it a lot, but she could be better
                $ vt_store.cum_fetish_status_icon = "openmouth"
                $ vt_store.cum_fetish_tooltip = f"{{image=progress_token_small}} Train her oral skills to vacuum and polish you like a pro!"
                $ vt_store.cum_fetish_tooltip += f"\n{{image=triskelion_token_small}} Increase her oral skill "+ str(5 - person.oral_sex_skill)+" more times!\nIncrease her Hoover Power!"

            elif person.opinion.giving_blowjobs >= 1:
                # she likes it
                $ vt_store.cum_fetish_status_icon = "bitelip"
                $ vt_store.cum_fetish_tooltip = f"{{image=progress_token_small}} Make her become your Cum Queen!"

                for opinion in ("drinking cum", "cum facials", "being covered in cum", "giving blowjobs"):
                    if opinion not in person.get_known_opinion_list(include_sexy=True, include_normal=False):
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=question_mark_small}} Need her opinion on " + opinion + "."
                    elif person.known_opinion(opinion) < 2:
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=red_heart_token_small}} Need her to love " + opinion + "."

            elif person.opinion.giving_blowjobs == 0:
                $ vt_store.cum_fetish_status_icon = "pinklips"
                $ vt_store.cum_fetish_tooltip = f"{{image=progress_token_small}} She's indifferent to oral, so make her like it..."

            else:
                $ vt_store.cum_fetish_status_icon = "openmouth"
                if person.opinion.giving_blowjobs == -1:
                    $ vt_store.cum_fetish_tooltip = f"She dislikes oral!"
                elif person.opinion.giving_blowjobs == -2:
                    $ vt_store.cum_fetish_tooltip = f"She hates oral!"
        else:
            # opinion unknown
            $ vt_store.cum_fetish_status_icon = "knowlips"
            $ vt_store.cum_fetish_tooltip = f"{{image=question_mark_small}} Does she like giving blow jobs?"


        if person.oral_cum == 1:
            if vt_store.sexualized:
                $ vt_store.cum_fetish_status_icon = "bitelip"
                $ vt_store.cum_fetish_tooltip += f"\n{{image=ahegaomouth_small}} Your cum digesting in her stomach."
            else:
                $ vt_store.cum_fetish_tooltip += f"\n{{image=ahegaomouth_small}} She has a dose of your protein in her belly."

        elif person.oral_cum > 1:
            if vt_store.sexualized:
                $ vt_store.cum_fetish_status_icon = "ahegaomouth"
                $ vt_store.cum_fetish_tooltip += f"\n{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in her stomach."
            else:
                $ vt_store.cum_fetish_tooltip += f"\n{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in her belly."

        imagebutton:
            pos(507, 166)
            idle vt_store.cum_fetish_status_icon
            action NullAction()
            tooltip vt_store.cum_fetish_tooltip

        if not vt_store.sexualized and person.oral_cum > 1:
            imagebutton:
                pos(507, 166)
                idle "bc_cum"
                action NullAction()
                tooltip vt_store.cum_fetish_tooltip

        if person.known_opinion("giving blowjobs") < 0:
            imagebutton:
                pos(507, 166)
                idle "dislike"
                action NullAction()
                tooltip vt_store.cum_fetish_tooltip

###### Anal Fetish
        $ vt_store.anal_fetish_status_icon = ""
        $ vt_store.anal_fetish_tooltip = ""

        if "anal sex" in person.get_known_opinion_list(include_sexy=True, include_normal=False):
            if person.has_anal_fetish:
                # she loves it
                $ vt_store.anal_fetish_status_icon = "ahegaopeach"
                if person.days_since_event("LastAnalFetish") > 10:
                    $ vt_store.anal_fetish_tooltip = "MMmmMm going to need your yummy\ncock in my ass in soon!"
                else:
                    $ vt_store.anal_fetish_tooltip = "MMmmMm my ass still molded to your cock."

            elif person.anal_sex_skill >= 5 and (person.opinion.anal_sex >= 2  or person.known_opinion("anal creampies") >= 2):
                # she likes it, and is quite good at it
                $ vt_store.anal_fetish_status_icon = "handass"
                $ vt_store.anal_fetish_tooltip = f"{{image=progress_token_small}} Sodomize your Anal Queen!"
                if person.anal_sex_count >= 19 or person.anal_creampie_count >= 19:
                    $ vt_store.anal_fetish_tooltip += f"\n{{image=progress_token_small}} Wait for the anal fetish event to trigger!"
                elif person.anal_sex_count < 19 and person.opinion.anal_sex >= 2:
                    $ vt_store.anal_fetish_tooltip += f"\n{{image=triskelion_token_small}} Have anal sex with her "+str(19 - person.anal_sex_count)+" more times!"
                elif person.anal_creampie_count < 19 and person.opinion.anal_creampies >=2:
                    $ vt_store.anal_fetish_tooltip += f"\n{{image=triskelion_token_small}} Fill her bowels full of cum "+str(19 - person.anal_creampie_count)+" more times!"

            elif person.opinion.anal_sex >= 1 or person.known_opinion("anal creampies") >= 1:
                # she likes it, but could be better
                $ vt_store.anal_fetish_status_icon = "yesanal"
                $ vt_store.anal_fetish_tooltip = f"{{image=progress_token_small}} Train her into your Anal Queen!"
                $ vt_store.anal_fetish_tooltip += f"\n{{image=triskelion_token_small}} Increase her anal sex skill "+ str(5 - person.anal_sex_skill)+" more times!"

                for opinion in ("anal creampies", "anal sex"):
                    if opinion not in person.get_known_opinion_list(include_sexy=True, include_normal=False):
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=question_mark_small}} Need her opinion on " + opinion + "."
                    elif person.known_opinion(opinion) < 2:
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=red_heart_token_small}} Need her to love " + opinion + "."

            elif person.opinion.anal_sex == 0:
                $ vt_store.anal_fetish_status_icon = "nocream"
                $ vt_store.anal_fetish_tooltip = f"{{image=progress_token_small}} She's indifferent to anal sex, so make her like it..."
            else:
                $ vt_store.anal_fetish_status_icon = "yespeach"
                $ vt_store.anal_fetish_tooltip = f"{{image=progress_token_small}} Train your Anal Queen!"
                if person.opinion.anal_sex == -1:
                    $ vt_store.anal_fetish_tooltip = f"She dislikes anal!"
                elif person.opinion.anal_sex == -2:
                    $ vt_store.anal_fetish_tooltip = f"She hates anal!"
        else:
            $ vt_store.anal_fetish_status_icon = "knowpeach"
            $ vt_store.anal_fetish_tooltip = f"{{image=question_mark_small}} Her thoughts on anal sex?"

        if person.anal_cum == 1:
            if vt_store.sexualized and person.anal_cum <= 3:
                $ vt_store.anal_fetish_status_icon = "handass"
            $ vt_store.anal_fetish_tooltip += f"\n{{image=ahegaoanal_small}} Your cum is lubricating her bowels."
        elif person.anal_cum > 1:
            $ vt_store.anal_fetish_tooltip += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum\nswimming in her bowels."
        if person.anal_cum > 3 and vt_store.sexualized:
                $ vt_store.anal_fetish_status_icon = "ahegaopeach"

        imagebutton:
            pos(544, 166)
            idle vt_store.anal_fetish_status_icon
            action NullAction()
            tooltip vt_store.anal_fetish_tooltip

        if person.known_opinion("anal sex") < 0:
            imagebutton:
                pos(544, 166)
                idle "dislike"
                action NullAction()
                tooltip vt_store.anal_fetish_tooltip

###### Breeding Fetish
        $ vt_store.breed_fetish_status_icon = ""
        $ vt_store.breed_fetish_tooltip = ""
        $ dayslastsex = 0
        $ daysince = ""

        if person.has_event_day("last_insemination") and 1 < person.days_since_event("last_insemination") < 4:
            $ dayslastsex = 4 - person.days_since_event("last_insemination")
            if dayslastsex == 1:
                $ daysince = "\nMy womb feels empty!"
            else:
                $ daysince = "\nYour sperm in me for "+str(dayslastsex)+" more days!\n Such warm butterflies!"

        # validate opinion exists and known
        if "vaginal sex" in person.get_known_opinion_list(include_sexy=True, include_normal=False):
            if person.has_breeding_fetish:
                # she has the fetish
                $ vt_store.breed_fetish_status_icon = "ahegaovag"
                $ vt_store.breed_fetish_tooltip = "Breed me! I need your cum!"
                if person.days_since_event("LastBreedingFetish") > 10:
                    $ vt_store.breed_fetish_tooltip = "MMmmMm going to need another \nyummy creampie filling soon!"
                else:
                    $ vt_store.breed_fetish_tooltip = "MMmmMmmm my womb is happy."

            elif person.vaginal_sex_skill >= 5 and person.opinion.vaginal_sex >= 2  and person.known_opinion("creampies") >= 2:
                # she loves it and is pretty good at it
                $ vt_store.breed_fetish_status_icon = "openvag"
                $ vt_store.breed_fetish_tooltip = f"{{image=progress_token_small}} She loves your cum in her womb!"
                if person.vaginal_creampie_count < 19:
                    $ vt_store.breed_fetish_tooltip += f"\n{{image=triskelion_token_small}} Fill her full of cum "+ str(19 - person.vaginal_creampie_count)+" more times!"
                else:
                    $ vt_store.breed_fetish_tooltip += f"\n{{image=progress_token_small}} Wait for the breeding fetish event to trigger!"

            elif person.opinion.vaginal_sex >= 2  and person.known_opinion("creampies") >= 2:
                # she loves it, but she could be better
                $ vt_store.breed_fetish_status_icon = "spreadvag"
                $ vt_store.breed_fetish_tooltip = f"{{image=progress_token_small}} Train her vaginal sex skills!"
                $ vt_store.breed_fetish_tooltip += f"\n{{image=triskelion_token_small}} Increase her vaginal sex skill "+ str(5 - person.vaginal_sex_skill)+" more times!"

            elif (person.opinion.creampies >= 1 and person.known_opinion("creampies")) or person.opinion.vaginal_sex >= 1:
                # she likes it
                $ vt_store.breed_fetish_status_icon = "vagclosed"
                $ vt_store.breed_fetish_tooltip = f"{{image=progress_token_small}} Train her into your Breeding Stock!"

                for opinion in ("creampies", "vaginal sex"):
                    if opinion not in person.get_known_opinion_list(include_sexy=True, include_normal=False):
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=question_mark_small}} Need her opinion on " + opinion + "."
                    elif person.known_opinion(opinion) < 2:
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=red_heart_token_small}} Need her to love " + opinion + "."

            elif person.opinion.vaginal_sex <= 0:
                # her opinion is not positive
                $ vt_store.breed_fetish_status_icon = "vagclosed"
                if person.opinion.vaginal_sex == 0:
                    $ vt_store.breed_fetish_tooltip = f"{{image=progress_token_small}} She's indifferent to vaginal sex, so make her like it..."
                elif person.opinion.vaginal_sex == -1:
                    $ vt_store.breed_fetish_tooltip = f"She dislikes vaginal sex!"
                elif person.opinion.vaginal_sex <= -2:
                    $ vt_store.breed_fetish_tooltip = f"She hates vaginal sex!"
        else:
            # opinion not known
            $ vt_store.breed_fetish_status_icon = "knowpeach"
            $ vt_store.breed_fetish_tooltip = f"{{image=question_mark_small}} Her thoughts on vaginal sex?"

        if person.vaginal_cum > 0:
            # set the icon
            if person.hymen <= 1:
                $ vt_store.breed_fetish_status_icon = "vaghymen"
            elif vt_store.sexualized and person.vaginal_cum < 3:
                $ vt_store.breed_fetish_status_icon = "openvag"
            elif vt_store.sexualized:
                $ vt_store.breed_fetish_status_icon = "ahegaovag"

            # modify the tooltip
            if person.hymen <= 1 and person.vaginal_cum == 1:
                $ vt_store.breed_fetish_tooltip = f"{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh" + vt_store.fertility_tag + " womb with your seed."
            elif person.vaginal_cum == 1: # and hymen == 2
                $ vt_store.breed_fetish_tooltip = f"{{image=beezee_token_small}} Your seed is in her" + vt_store.fertility_tag + " womb."
            elif person.hymen <= 1 and person.vaginal_cum > 1:
                $ vt_store.breed_fetish_tooltip = f"{{image=handprint_token_small}}{{image=beezee_token_small}} Marked her fresh" + vt_store.fertility_tag + " womb with "+str(person.vaginal_cum)+ " doses of your seed."
            else: # vaginal_cum > 0 and hymen == 2
                $ vt_store.breed_fetish_tooltip = f"{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her" + vt_store.fertility_tag + " womb."+daysince

        imagebutton:
            pos(581, 166)
            idle vt_store.breed_fetish_status_icon
            action NullAction()
            tooltip vt_store.breed_fetish_tooltip

        # show cum overlay when talking
        if not vt_store.sexualized and person.hymen > 1 and person.vaginal_cum > 1:
            imagebutton:
                pos(581, 166)
                idle "bc_cum"
                action NullAction()
                tooltip vt_store.breed_fetish_tooltip

        # show dislike overlay
        if person.known_opinion("vaginal sex") < 0:
            imagebutton:
                pos(581, 166)
                idle "dislike"
                action NullAction()
                tooltip vt_store.breed_fetish_tooltip

######## Exhibitionist Fetish
        $ vt_store.exhibitionist_fetish_status_icon = ""
        $ vt_store.exhibitionist_fetish_tooltip = ""

        if "public sex" in person.get_known_opinion_list(include_sexy=True, include_normal=False):
            if person.has_exhibition_fetish:
                # she has the fetish
                $ vt_store.exhibitionist_fetish_status_icon = "ahegaoex"
                $ vt_store.exhibitionist_fetish_tooltip = "My body deserves to be seen!"
                if person.event_triggers_dict.get("anal_fetish_locked",0) >= day:
                    $ vt_store.exhibitionist_fetish_tooltip = "Ugh my skin is itchy I need\nmy skin free soon!"
                else:
                    $ vt_store.exhibitionist_fetish_tooltip = "MMmmMm my skin feels good."

            elif builtins.all(person.known_opinion(vt_opinion) >= 2 for vt_opinion in ("public sex", "not wearing underwear", "not wearing anything", "showing her ass", "showing her tits", "skimpy outfits", "skimpy uniforms")):
                $ vt_store.exhibitionist_fetish_status_icon = "nudebody"
                $ vt_store.exhibitionist_fetish_tooltip = f"{{image=progress_token_small}} My skin needs to breathe and be free!"
                if person.event_triggers_dict.get("anal_fetish_locked",0) >= day:
                    $ vt_store.exhibitionist_fetish_tooltip += f"\n{{image=question_mark_small}} Exhibition Fetish Event (not yet written)"

            elif builtins.all(person.known_opinion(vt_opinion) >= 2 for vt_opinion in ("public sex", "not wearing underwear", "not wearing anything", "skimpy outfits", "skimpy uniforms")):
                $ vt_store.exhibitionist_fetish_status_icon = "nudebody"
                $ vt_store.exhibitionist_fetish_tooltip = f"{{image=progress_token_small}} Needs to be more comfortable showing skin!"

                for opinion in ("showing her ass", "showing her tits"):
                    if opinion not in person.get_known_opinion_list(include_sexy=True, include_normal=False):
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=question_mark_small}} Need her opinion on " + opinion + "."
                    elif person.known_opinion(opinion) < 2:
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=red_heart_token_small}} Need her to be more comfortable " + opinion + "."

            elif person.opinion.public_sex >= 1 and builtins.all(person.known_opinion(vt_opinion) >= 2 for vt_opinion in ("showing her ass", "showing her tits", "skimpy outfits", "skimpy uniforms")):
                $ vt_store.exhibitionist_fetish_status_icon = "underwear"
                $ vt_store.exhibitionist_fetish_tooltip = f"{{image=progress_token_small}} Train her to be more comfortable not wearing underwear.. How about nothing at all?!"

                for opinion in ("public sex", "not wearing underwear", "not wearing anything"):
                    if opinion not in person.get_known_opinion_list(include_sexy=True, include_normal=False):
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=question_mark_small}} Need her opinion on " + opinion + "."
                    elif person.known_opinion(opinion) < 2:
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=red_heart_token_small}} Need her to love " + opinion + "."

            elif person.opinion.public_sex > 0:
                $ vt_store.exhibitionist_fetish_status_icon = "bodyconcealed"
                $ vt_store.exhibitionist_fetish_tooltip = f"{{image=progress_token_small}} Turn her into a beautiful exhibitionist!"

                for opinion in ("public sex", "skimpy outfits", "skimpy outfits"):
                    if opinion not in person.get_known_opinion_list(include_sexy=True, include_normal=False):
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=question_mark_small}} Need her opinion on " + opinion + "."
                    elif person.known_opinion(opinion) < 2:
                        $ vt_store.cum_fetish_tooltip += f"\n{{image=red_heart_token_small}} Need her to love " + opinion + "."

            elif person.opinion.public_sex <= 0:
                $ vt_store.exhibitionist_fetish_status_icon = "bodyconcealed"

                if person.opinion.public_sex == 0:
                    $ vt_store.exhibitionist_fetish_tooltip = f"{{image=progress_token_small}} She's indifferent to public sex, so make her like it..."
                elif person.opinion.public_sex == -1:
                    $ vt_store.exhibitionist_fetish_tooltip = f"She dislikes public sex!"
                elif person.opinion.public_sex <= -2:
                    $ vt_store.exhibitionist_fetish_tooltip = f"She hates public sex!"

        else:
            $ vt_store.exhibitionist_fetish_status_icon = "knowbody"
            $ vt_store.exhibitionist_fetish_tooltip = f"{{image=question_mark_small}} Does she like public sex?"

        if vt_store.sexualized:
            if not person.vagina_available and not person.tits_available:
                $ vt_store.exhibitionist_fetish_status_icon = "bodyskimpy"
                $ vt_store.exhibitionist_fetish_tooltip += "\nShe is fully clothed."

            elif person.vagina_available and person.tits_available:
                $ vt_store.exhibitionist_fetish_status_icon = "nudebody"
                if person.arousal_perc <= 59:
                    $ vt_store.exhibitionist_fetish_tooltip += "\nYou can see her tits and pussy."
                elif person.arousal_perc >= 60 and person.vaginal_cum == 0:
                    $ vt_store.exhibitionist_fetish_tooltip += "\nYou can see her tits and wet hot juicy pussy."
                elif 1 < person.vaginal_cum <= 3:
                    $ vt_store.exhibitionist_fetish_tooltip += "\nYou can see your cum starting to drip from her pussy."
                elif person.vaginal_cum > 3:
                    $ vt_store.exhibitionist_fetish_tooltip += "\nYou can see your cum oozing from her pussy."

            elif person.tits_available:
                $ vt_store.exhibitionist_fetish_status_icon = "bodypanties"
                $ vt_store.exhibitionist_fetish_tooltip += "\nYou can see her tits."

            elif person.vagina_available:
                $ vt_store.exhibitionist_fetish_status_icon = "bodybra"
                if person.arousal_perc <= 59:
                    $ vt_store.exhibitionist_fetish_tooltip += "\nYou can see her pussy."
                elif person.arousal_perc >= 60 and person.vaginal_cum == 0:
                    $ vt_store.exhibitionist_fetish_tooltip += "\nYou can see her wet hot juicy pussy."
                elif 1 < person.vaginal_cum <= 3:
                    $ vt_store.exhibitionist_fetish_tooltip += "\nYou can see your cum starting to drip from her pussy."
                elif person.vaginal_cum > 3:
                    $ vt_store.exhibitionist_fetish_tooltip += "\nYou can see your cum oozing from her pussy."

        imagebutton:
            pos(618, 166)
            idle vt_store.exhibitionist_fetish_status_icon
            action NullAction()
            tooltip vt_store.exhibitionist_fetish_tooltip

        if person.known_opinion("public sex") < 0 and not vt_store.sexualized:
                imagebutton:
                    pos(618, 166)
                    idle "dislike"
                    action NullAction()
                    tooltip vt_store.exhibitionist_fetish_tooltip
#hymen is 0 = sealed, 1=recently torn bleeding, 2=normal - serum to regenerate vaginal and hymen
#0=virgin, 1=just the tip, 2=full penetration, 3-10 is degree of tightness
### Oral Virgin Flag
        $ vt_store.oral_status_icon = ""
        $ vt_store.oral_tooltip = ""

        if person.oral_virgin == 0: #morevisual with virgin
            $ vt_store.oral_status_icon = "truevirgin"
            $ vt_store.oral_tooltip = f"{{image=virgin_token_small}} She looks at you with lust\nin her innocent hungry eyes."

        #the interactive icons during sex stuff
        elif vt_store.sexualized:
            if position_choice.skill_tag == 'Oral' and not 'climax_type' in globals():

                $ vt_store.oral_status_icon = "openmouth"
                if position_choice.name == 'Blowjob':
                    $ vt_store.oral_tooltip = "She sucks your cock."
                elif position_choice.name == "Deepthroat":
                    $ vt_store.oral_status_icon = "openmouth"
                    $ vt_store.oral_tooltip = "You deeply fuck her throat with your cock."
                elif position_choice.name == "Skull Fuck":
                    $ vt_store.oral_status_icon = "openmouth"
                    $ vt_store.oral_tooltip = "You grab her head and skull fuck her with your cock."

            elif position_choice.skill_tag == 'Oral' and 'climax_type' in globals():
                $ vt_store.oral_status_icon = "ahegaomouth"
                if climax_type == "mouth":
                    if mc.condom:
                        $ vt_store.oral_tooltip = "You fill the condom as her tongue wraps around you."
                    else:
                        $ vt_store.oral_tooltip = "You flood her mouth full of your cum."

                elif climax_type == "throat":
                    if mc.condom:
                        $ vt_store.oral_tooltip = "You fill the condom as her throat squeezes you."
                    else:
                        $ vt_store.oral_tooltip = "You flood her belly with your cum."

                elif climax_type == "face":
                    $ vt_store.oral_tooltip = "You shoot your load all over her face."

                elif climax_type =="body":
                    # $ vt_store.oral_status_icon = "ahegaobody" # or "openmouth"?
                    $ vt_store.oral_tooltip = "You blow your load all over her body."

            elif position_choice.skill_tag == 'Foreplay':
                if position_choice.name == 'Kissing':
                    $ vt_store.oral_status_icon = "pinklips"
                    $ vt_store.oral_tooltip = "In the throes of kissing you."

            elif person.oral_cum == 1:
                if person.arousal_perc >= 60:
                    $ vt_store.oral_status_icon = "ahegaoface"
                    $ vt_store.oral_tooltip = "She seems lost in her bliss and panting. \n{{image=ahegaomouth_small}}She has a dose of your protein in her belly."
                else:
                    $ vt_store.oral_status_icon = "bitelip"
                    $ vt_store.oral_tooltip = "She looks at you with lust \n in her innocent hungry eyes. \n{{image=ahegaomouth_small}}She has a dose of your protein in her belly."

            elif 1 < person.oral_cum <= 3:
                if person.arousal_perc >= 60:
                    $ vt_store.oral_status_icon = "ahegaoface"
                    $ vt_store.oral_tooltip = f"*She hungrily gazes at you for more cum.*\n{{image=ahegaomouth_small}} She has "+ str(person.oral_cum) +" doses of your cum \n swimming in her belly."
                else:
                    $ vt_store.oral_status_icon = "bitelip"
                    $ vt_store.oral_tooltip = f"{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \nswimming in her belly."

            elif person.oral_cum > 3:
                if person.arousal_perc >= 60:
                    $ vt_store.oral_status_icon = "ahegaoface"
                    $ vt_store.oral_tooltip = f"*Hunger in her eyes wants more cum*\n{{image=ahegaomouth_small}} She has "+ str(person.oral_cum) +" doses of your cum \n swimming in her stomach, causing a bit of a bulge."
                else:
                    $ vt_store.oral_status_icon = "ahegaomouth"
                    $ vt_store.oral_tooltip = f"{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in the slight bulge of her belly."

            else:
                $ vt_store.oral_status_icon = "bitelip"
                if person.oral_virgin == 0:
                    $ vt_store.oral_tooltip = f"{{image=virgin_token_small}} She plays with her innocent hungry fresh pussy.\nShe bites her lip coyly."
                elif person.oral_first == mc.name:
                    $ vt_store.oral_tooltip = f"{{image=handprint_token_small}} She locks eyes with you and bite her lip sexily."
                else:
                    $ vt_store.oral_tooltip = "She pants and breathes heavily and bites her lip."

                if person.energy < 20 and person.had_sex_today:
                    $ vt_store.oral_tooltip += "She seems lost in her bliss and panting."


        elif not vt_store.sexualized:
            # talking
            if person.arousal_perc >= 60:
                if person.oral_cum == 0:
                    $ vt_store.oral_status_icon = "bitelip"
                    if person.oral_virgin == 0:
                        $ vt_store.oral_tooltip = f"{{image=virgin_token_small}} She looks at you with lust \n in her innocent hungry eyes."
                    elif person.oral_first == mc.name:
                        $ vt_store.oral_tooltip = f"{{image=handprint_token_small}} She starts to drool \n and undress you with her eyes."
                    else:
                        $ vt_store.oral_tooltip = "She looks at you with savage lust in her eyes."

                    if person.energy <20 and person.had_sex_today:
                        $ vt_store.oral_tooltip = "She seems lost in her bliss and panting."

                elif person.oral_cum > 0:
                    $ vt_store.oral_status_icon = "ahegaoface"
                    if person.energy < 20 and person.had_sex_today:
                        $ vt_store.oral_tooltip = "She seems lost in her bliss and panting."
                    else:
                        $ vt_store.oral_tooltip = "She hungrily gazes as you for more cum."

                    if person.oral_cum == 1:
                        $ vt_store.oral_tooltip += f"\n{{image=ahegaomouth_small}} She has a dose of your protein in her belly."
                    else:
                        $ vt_store.oral_tooltip += f"\n{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in her belly."

            elif person.arousal_perc < 60:
                if person.oral_first == mc.name:
                    $ vt_store.oral_status_icon = "claimedmouth"
                    $ vt_store.oral_tooltip = f"{{image=handprint_token_small}} You Claimed this Pie Hole!"
                elif person.oral_first is not None and person.oral_virgin > 0:
                    $ vt_store.oral_status_icon = "knowlips"
                    $ vt_store.oral_tooltip = f"{{image=taboo_break}} Someone else had her lips before you... CLAIM IT!"

                if person.oral_cum > 0:
                    $ vt_store.oral_status_icon = "bitelip"
                    if person.oral_cum == 1:
                        $ vt_store.oral_tooltip += f"\n{{image=ahegaomouth_small}} She has a dose of your protein in her belly."
                    else:
                        $ vt_store.oral_tooltip += f"\n{{image=ahegaomouth_small}} "+ str(person.oral_cum) +" doses of your cum \n swimming in her belly."

            # display talking status
            imagebutton:
                pos(678, 166)
                idle vt_store.oral_status_icon
                action NullAction()
                tooltip vt_store.oral_tooltip

### Anal Virgin Flag
        $ vt_store.anal_status_icon = ""
        $ vt_store.anal_tooltip = ""

        if person.anal_virgin == 0:
            $ vt_store.anal_status_icon = "truevirgin"
            $ vt_store.anal_tooltip = f"{{image=virgin_token_small}} Her ass sways so ripely, ready for the taking"

        #the interactive icons during sex stuff
        elif vt_store.sexualized:
            if position_choice.skill_tag == 'Anal' and 'climax_type' in globals():
                if climax_type == "anal":
                        if mc.condom:
                            $ vt_store.anal_status_icon = "yesanal"
                            $ vt_store.anal_tooltip = "You fill the condom with your seed, as she pulses around you!"
                        else:
                            $ vt_store.anal_tooltip = "You flood her bowels with your seed!"
                            if person.anal_cum == 0:
                                $ vt_store.anal_status_icon = "handass"
                            elif person.anal_cum >= 1:
                                $ vt_store.anal_status_icon = "ahegaopeach"

                if climax_type =="body":
                    $ vt_store.anal_status_icon = "yesanal"
                    $ vt_store.anal_tooltip = "You blow your load all over her body."

            elif position_choice.skill_tag == 'Anal':
                $ vt_store.anal_status_icon = "yesanal"
                $ vt_store.anal_tooltip = "You fuck her ass with your cock."

            elif person.anal_cum == 1:
                if person.arousal_perc >= 60:
                    $ vt_store.anal_status_icon = "handass"
                    $ vt_store.anal_tooltip = f"She seems lost in her bliss and panting.\n{{image=ahegaoanal_small}} She has a dose of your protein in her bowels."
                else:
                    $ vt_store.anal_status_icon = "handass"
                    $ vt_store.anal_tooltip = f"She looks at you with lust\nin her innocent hungry eyes.\n{{image=ahegaoanal_small}} She has a dose of your protein in her bowels."

            elif 1 < person.anal_cum <= 3:
                if person.arousal_perc >= 60:
                    $ vt_store.anal_status_icon = "ahegaopeach"
                    $ vt_store.anal_tooltip = f"*She hungrily gazes at you for more cum.*\n{{image=ahegaomouth_small}} She has "+ str(person.anal_cum) +" doses of your cum\nswimming in her belly."
                else:
                    $ vt_store.anal_status_icon = "handass"
                    $ vt_store.anal_tooltip = f"{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum\nswimming in her belly."

            elif person.anal_cum > 3:
                if person.arousal_perc >= 60:
                    $ vt_store.anal_status_icon = "ahegaopeach"
                    $ vt_store.anal_tooltip = f"*Hunger in her eyes wants more cum*\n{{image=ahegaoanal_small}} She has "+ str(person.anal_cum) +" doses of your cum\nswimming in her bowels, causing her belly a bit of a bulge."
                else:
                    $ vt_store.anal_status_icon = "ahegaomouth"
                    $ vt_store.anal_tooltip = f"{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum\nswimming in the slight bulge of her belly."

            else: # having sex, no specific anal related details
                $ vt_store.anal_status_icon = "yespeach"
                if person.anal_virgin == 0:
                    $ vt_store.anal_tooltip = f"{{image=virgin_token_small}} Her ass sways so ripely, ready for the taking!"
                elif person.anal_first == mc.name:
                    $ vt_store.anal_tooltip = f"\n{{image=handprint_token_small}} Her ass sways, hypnotizing you..\nThen she slaps it!"
                elif person.anal_virgin < 4:
                    $ vt_store.anal_tooltip = "Her ass sways and she spreads her ass for you.\nCome take me!"
                elif person.anal_virgin >= 4:
                    $ vt_store.anal_tooltip = "Her ass sways and she spreads her gaping asshole for you.\nCome take me!"

                if person.energy < 20 and person.had_sex_today:
                    $ vt_store.anal_tooltip += "She seems lost in her bliss and panting."


        elif not vt_store.sexualized:
            # talking
            if person.arousal_perc >= 60:
                if person.anal_cum == 0:
                    $ vt_store.anal_status_icon = "yespeach"
                    if person.anal_virgin == 0:
                        $ vt_store.anal_tooltip = f"\n{{image=virgin_token_small}} Her ass sways so ripely, ready for the taking!"
                    elif person.anal_first == mc.name:
                        $ vt_store.anal_tooltip = f"{{image=handprint_token_small}} Her ass sways, hypnotizing you while\nshe rubs it!"
                    elif person.anal_virgin < 4:
                        $ vt_store.anal_tooltip = "Her ass sways and she spreads her ass for you.\nCome take me!"
                    elif person.anal_virgin >=4:
                        $ vt_store.anal_tooltip = "Her ass sways and she spreads her gaping asshole for you.\nCome take me!"

                elif person.anal_cum == 1:
                    $ vt_store.anal_status_icon = "handass"
                    $ vt_store.anal_tooltip = f"{{image=ahegaoanal_small}} You painted her bowels with your cum."
                elif person.anal_cum > 1:
                    $ vt_store.anal_status_icon = "ahegaopeach"
                    $ vt_store.anal_tooltip = f"{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum\ncoating her bowels."

            elif person.arousal_perc < 60:
                if person.anal_first == mc.name:
                    $ vt_store.anal_status_icon = "claimedass"
                    $ vt_store.anal_tooltip = f"{{image=handprint_token_small}} You Claimed this Ass!"
                elif person.anal_first is not None and person.anal_virgin > 0:
                    $ vt_store.anal_status_icon = "knowpeach"
                    $ vt_store.anal_tooltip = f"{{image=taboo_break}} Someone else had her ass before you... RECLAIM IT!"
                elif person.anal_cum == 1:
                    $ vt_store.anal_status_icon = "handass"
                    $ vt_store.anal_tooltip += f"\n{{image=ahegaoanal_small}} You have painted her bowels with your cum."
                elif person.anal_cum > 1:
                    $ vt_store.anal_status_icon = "ahegaopeach"
                    $ vt_store.anal_tooltip += f"\n{{image=ahegaoanal_small}} "+ str(person.anal_cum) +" doses of your cum\ncoating her bowels."

        imagebutton:
            pos(715, 166)
            idle vt_store.anal_status_icon
            action NullAction()
            tooltip vt_store.anal_tooltip

### Vaginal Virgin Flag
        $ VTvaginalst = ""
        $ VTvaginaltt = ""

        if person.hymen == 0 and person.vaginal_virgin <= 1: #morevisual with virgin
            $ VTvaginalst = "truevirgin"
            $ VTvaginaltt = f"{{image=virgin_token_small}} She looks so innocent and inexperienced."

        #the interactive icons during sex stuff
        elif vt_store.sexualized:
            if position_choice.skill_tag == 'Vaginal' and 'climax_type' in globals():
                if climax_type == "pussy":
                    if not mc.condom:
                        if person.hymen == 1:
                            $ VTvaginalst = "vaghymen"
                            $ VTvaginaltt = f"{{image=handprint_token_small}} You mark her fresh" + vt_store.fertility_tag + " womb with your virile seed! \n Her virinity mixes with your cum!"
                        else:
                            $ VTvaginalst = "openvag"
                            $ VTvaginaltt = "You flood her" + vt_store.fertility_tag + " womb with your seed!"
                            if person.vaginal_cum >= 1:
                                $ VTvaginalst = "ahegaovag"

                    elif mc.condom:
                        if person.hymen == 1:
                            $ VTvaginalst = "spreadvag"
                            $ VTvaginaltt = f"{{image=handprint_token_small}} You fill the condom in her freshly fucked pussy with your cum!"
                        else:
                            $ VTvaginalst = "spreadvag"
                            $ VTvaginaltt = "You push deep and fill the condom with your seed!"

                elif climax_type == "body":
                    $ VTvaginalst = "spreadvag"
                    $ VTvaginaltt = "You blow your load all over her body."

            elif position_choice.skill_tag == 'Vaginal':
                $ VTvaginalst = "spreadvag"
                $ VTvaginaltt = "You fuck her juicy" + vt_store.fertility_tag + " pussy with your cock."

            elif person.vaginal_cum > 0:
                if person.vaginal_cum == 1:
                    if person.hymen == 0:
                        $ VTvaginalst = "vaghymen"
                        $ VTvaginaltt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} Marked her fresh" + vt_store.fertility_tag + " womb with your seed."
                    elif person.hymen == 1:
                        $ VTvaginalst = "vaghymen"
                        $ VTvaginaltt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh" + vt_store.fertility_tag + " womb with your seed."
                    elif person.hymen == 2:
                        $ VTvaginalst = "openvag"
                        $ VTvaginaltt = f"{{image=beezee_token_small}} Your seed in her" + vt_store.fertility_tag + " womb."
                elif person.vaginal_cum > 1:
                    if person.hymen <= 1:
                        if person.vaginal_cum > 3:
                            $ VTvaginalst = "ahegaovag"
                            $ VTvaginaltt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} Her freshly fucked" + vt_store.fertility_tag + " womb\ncan barely contain your "+str(person.vaginal_cum)+ " doses of your seed.\nIt is already oozing out."
                        elif person.vaginal_cum <= 3:
                            $ VTvaginalst = "vaghymen"
                            $ VTvaginaltt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh" + vt_store.fertility_tag + " womb\nwith "+str(person.vaginal_cum)+ " doses of your seed."
                    elif person.hymen == 2:
                        if person.vaginal_cum > 3:
                            $ VTvaginalst = "ahegaovag"
                            $ VTvaginaltt = f"{{image=beezee_token_small}} Her pussy can barely contain \nthe "+ str(person.vaginal_cum) +" doses of your cum swimming in\nher" + vt_store.fertility_tag + " womb and is already oozing out."+daysince
                        elif person.vaginal_cum <= 3:
                            $ VTvaginalst = "openvag"
                            $ VTvaginaltt = f"{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum\nswimming in her" + vt_store.fertility_tag + " womb."+daysince

                if person.arousal_perc >= 60:
                    $ VTvaginaltt += f"\n*You can really smell her arousal*"
            else:
                $ VTvaginalst = "spreadvag"
                if person.vaginal_virgin == 0:
                    $ VTvaginaltt = f"{{image=virgin_token_small}} She plays with her fresh innocent hungry pussy."
                elif person.vaginal_first == mc.name:
                    $ VTvaginaltt = f"{{image=handprint_token_small}} She locks eyes with you and licks her lips\nand plays with her pussy."
                else:
                    $ VTvaginaltt = "She pants heavily as she plays with her pussy."

                if person.energy <20 and person.had_sex_today:
                    $ VTvaginaltt = "She seems lost in her bliss and panting."


        elif not vt_store.sexualized:
            if person.vaginal_first == mc.name:
                $ VTvaginalst = "claimedvag"
                $ VTvaginaltt = f"{{image=handprint_token_small}} You claimed this pussy!"
            elif person.vaginal_first is not None and person.hymen == 2:
                $ VTvaginalst = "knowpeach"
                $ VTvaginaltt = f"{{image=taboo_break}} Someone else had this pussy before you... OWN IT!"

            if person.arousal_perc >= 59 and person.vaginal_cum <= 0:
                $ VTvaginalst = "spreadvag"
                if person.vaginal_virgin <= 1:
                    $ VTvaginaltt += f"\n{{image=virgin_token_small}} Her fresh pussy is dripping for you.\n*You can really smell her arousal*"
                    if person.hymen == 0:
                        $ VTvaginaltt += f"\n{{image=virgin_token_small}} She is more than ready to be fucked."
                elif person.vaginal_virgin > 2:
                    if person.vaginal_first == mc.name:
                        $ VTvaginaltt += f"\n{{image=handprint_token_small}} Her pussy is dripping for you.\n*You can really smell her arousal*\nCome take me!"
                    elif person.vaginal_first != mc.name:
                        $ VTvaginaltt += "\nHer pussy is dripping down her leg.\n*She is really aroused*"

            elif person.vaginal_cum > 0:
                if person.vaginal_cum == 1:
                    if person.hymen == 0:
                        $ VTvaginalst = "vaghymen"
                        $ VTvaginaltt = f"{{image=handprint_token_small}} You marked her fresh" + vt_store.fertility_tag + " womb with your seed."
                    elif person.hymen == 1:
                        $ VTvaginalst = "vaghymen"
                        $ VTvaginaltt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh" + vt_store.fertility_tag + " womb with your seed."
                    elif person.hymen == 2:
                        $ VTvaginalst = "openvag"
                        $ VTvaginaltt += f"\n{{image=beezee_token_small}} Your seed in her" + vt_store.fertility_tag + " womb."
                else:
                    if person.hymen <= 1:
                        if person.vaginal_cum > 3:
                            $ VTvaginalst = "ahegaovag"
                            $ VTvaginaltt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} Her freshly fucked" + vt_store.fertility_tag + " womb can barely contain your "+str(person.vaginal_cum)+ " doses of your seed.\nIt is already oozing out."
                        elif person.vaginal_cum <= 3:
                            $ VTvaginalst = "vaghymen"
                            $ VTvaginaltt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh" + vt_store.fertility_tag + " womb with "+str(person.vaginal_cum)+ " doses of your seed."

                    elif person.hymen == 2:
                        if person.vaginal_cum > 3:
                            $ VTvaginalst = "ahegaovag"
                            $ VTvaginaltt += f"\n{{image=beezee_token_small}} Her pussy can barely contain\n the "+ str(person.vaginal_cum) +" doses of your cum \n swimming \nin her" + vt_store.fertility_tag + " womb and is already oozing out."+daysince
                        elif person.vaginal_cum <= 3:
                            $ VTvaginalst = "openvag"
                            $ VTvaginaltt += f"\n{{image=beezee_token_small}} "+ str(person.vaginal_cum) +" doses of your cum \n swimming in her" + vt_store.fertility_tag + " womb."+daysince

                if person.arousal_perc >= 59:
                    $ VTvaginaltt += f"\n*You can really smell her arousal*"

        imagebutton:
            pos(752, 166)
            idle VTvaginalst
            action NullAction()
            tooltip VTvaginaltt

        if not vt_store.sexualized and person.hymen > 1 and person.vaginal_cum > 3:
            imagebutton:
                pos(752, 166)
                idle "bc_cum"
                action NullAction()
                tooltip VTvaginaltt
#### Had sex today
        if person.had_sex_today:
            imagebutton:
                pos(789, 166)
                idle "hadsextoday"
                action NullAction()
                tooltip "You had fun with her today."
#### Tranced
        $ vt_store.trance_status_icon = ""
        $ vt_store.trance_tooltip = ""
        if not person.is_in_trance:
            $ vt_store.trance_status_icon = "notrance"
            $ vt_store.trance_tooltip = "Not in a trance! Make her climax!"
        elif person.is_in_trance and not person.trance_training_available:
            $ vt_store.trance_status_icon = "donetrain"
            $ vt_store.trance_tooltip = "Already Trained her!"
        elif person.has_exact_role(very_heavy_trance_role):
            $ vt_store.trance_status_icon = "ahegaotrance"
            $ vt_store.trance_tooltip = "In a very deep trance! Good time to train her!"
        elif person.has_exact_role(heavy_trance_role):
            $ vt_store.trance_status_icon = "heavytrance"
            $ vt_store.trance_tooltip = "In a deep trance! Good time to train her!"
        elif person.has_exact_role(trance_role):
            $ vt_store.trance_status_icon = "starttrance"
            $ vt_store.trance_tooltip = "In a trance! She is open to suggestions!"

        imagebutton:
            pos(826, 166)
            idle vt_store.trance_status_icon
            action NullAction()
            tooltip vt_store.trance_tooltip

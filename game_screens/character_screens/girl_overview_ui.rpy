screen person_info_detailed(person):
    add paper_background_image
    modal True
    zorder 100

    default hr_base = human_resource_potential_stat(person)
    default market_base = marketing_potential_stat(person)
    default research_base = research_potential_stat(person)
    default prod_base = production_potential_stat(person)
    default supply_base = supply_potential_stat(person)
    default master_opinion_dict = dict(person.opinions, **person.sexy_opinions)
    default relationship_list = sorted(town_relationships.get_relationship_type_list(person, visible = True), key = lambda x: x[0].name)
    default visible_roles = ", ".join([x.role_name for x in person.special_role if not x.hidden])
    default person_portrait = person.build_person_portrait()
    default person_job_info = person_info_ui_get_job_title(person)
    default base_salary = sum(x.base_salary for x in person.jobs if x.is_paid)
    default fertility_info = f"{person.effective_fertility:.1f}%"
    default baby_desire_string = get_baby_desire_format(person)
    default fertility_peak_day = str(person.ideal_fertile_day + 1)
    default known_days = str(day - person.event_triggers_dict.get("birth_control_known_day", 0))
    default last_vaginal_day = person.sex_record.get("Last Vaginal Day", 0)
    default last_oral_day = person.sex_record.get("Last Oral Day", 0)
    default last_anal_day = person.sex_record.get("Last Anal Day", 0)
    default last_exhibition_day = person.sex_record.get("Last Exhibition Day", 0)
    default public_sex = person.sex_record.get("Public Sex", 0)
    default obedience_info = get_obedience_string(person.obedience)
    default personality_info = person.personality.base_personality_prefix.capitalize()
    default height_info = height_to_string(person.height)
    if persistent.pregnancy_pref == 0:
        default fertility_tooltip = ""
    elif persistent.pregnancy_pref == 1:
        default fertility_tooltip = "The fertility percentage is a fixed value for the character."
    elif persistent.pregnancy_pref == 2:
        default fertility_tooltip = "The fertility percentage is calculated based on curve that increases around her peak day."
    else:
        default fertility_tooltip  = "The fertility percentage is 1% when not in the 5 day ovulation window, when in the window the fertility increases, she can get pregnant from one insemination for several days."

    if isinstance(person.hair_colour, list) and isinstance(person.hair_colour[0], basestring):
        default hair_info = person.hair_colour[0].title()
    else:
        default hair_info = ""
    if isinstance(person.eyes, list) and isinstance(person.eyes[0], basestring):
        default eyes_info = person.eyes[0].title()
    else:
        default eyes_info = ""

    vbox:
        spacing 25
        xalign 0.5
        xanchor 0.5
        yalign 0.2
        frame:
            xsize 1750
            ysize 120
            padding (0, 10)
            align (.5, .5)
            background "#1a45a1aa"
            hbox:
                spacing 30
                imagebutton:
                    offset (0, -20)
                    idle person_portrait at zoom(.65)
                    xysize (465, 120)
                fixed:
                    xsize (720 if persistent.pregnancy_pref > 0 else 1270)
                    vbox:
                        hbox:
                            text format_titles(person) style "menu_text_style" size 30 xalign 0.5 yalign 0.5 yanchor 0.5 color person.char.who_args["color"] font person.char.what_args["font"]
                            use favourite_toggle_button(person)
                        text "Job: [person_job_info]" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5
                        if visible_roles:
                            text "Special Roles: [visible_roles]" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

                if isinstance(person, Person) and persistent.pregnancy_pref > 0:
                    vbox:
                        xsize 320
                        if person.knows_pregnant:
                            text "Pregnant: Yes" style "menu_text_style"
                            if day < person.pregnancy_show_day:
                                text f"- Visible Day: {person.pregnancy_show_day}" style "menu_text_style"
                            elif day < person.pregnancy_due_day:
                                text f"- Delivery Day: {person.pregnancy_due_day}" style "menu_text_style"
                        elif (person.is_clone and hasattr(person, 'clone_womb_revived')==False):
                            text "Fertility: Sterile" style "menu_text_style"
                        elif person.is_infertile:
                            text "Fertility: Infertile" style "menu_text_style"
                        elif person.fertility_percent < 0:
                            text "Fertility: Intrauterine Device" style "menu_text_style"
                        else:
                            if persistent.pregnancy_pref > 0:
                                hbox:
                                    text "Fertility: [fertility_info]" style "menu_text_style"
                                    textbutton "{image=question_mark_small}":
                                        style "transparent_style"
                                        tooltip fertility_tooltip
                                        action NullAction()
                            if person.bc_status_known and person.on_birth_control:
                                text "BirthControl: [person.birthcontrol_efficiency:.0f]%" style "menu_text_style"
                            if persistent.pregnancy_pref >= 2:
                                text "Monthly Peak Day: [fertility_peak_day]" style "menu_text_style"
                            if person.bc_status_known and persistent.pregnancy_pref > 0:
                                text "Pregnancy chance: [person.pregnancy_chance:.2f]%" style "menu_text_style"

                    vbox:
                        xsize 320
                        if person.is_clone or person.fertility_percent <= -100:
                            pass
                        elif person.knows_pregnant:
                            text "Birth Control: No" style "menu_text_style"
                        elif not person.bc_status_known:
                            text "Birth Control: Unknown" style "menu_text_style"
                        else:
                            hbox:
                                text "Birth Control:" style "menu_text_style"
                                vbox:
                                    text ("Yes" if person.on_birth_control else "No") style "menu_text_style"
                                    text "Known [known_days] days ago" size 12 style "menu_text_style"
                            if persistent.pregnancy_pref >= 3:
                                text "Baby Desire: [baby_desire_string]" style "menu_text_style"

                        use serum_tolerance_indicator(person)

        hbox:
            xsize 1750
            spacing 30
            frame:
                background "#1a45a1aa"
                xysize (325, 264)
                vbox xfill True:
                    text "Status and Info" style "serum_text_style_header"
                    text "Happiness: [person.happiness]" style "menu_text_style"
                    text "Sluttiness: [person.sluttiness]%" style "menu_text_style"
                    text "Obedience: [person.obedience] {image=triskelion_token_small} [obedience_info]" style "menu_text_style"
                    text "Love: [person.love]" style "menu_text_style"
                    text "Personality: [personality_info]" style "menu_text_style"
                    if person.is_girlfriend:
                        text "Relationship: Girlfriend" style "menu_text_style"
                    else:
                        text "Relationship: [person.relationship]" style "menu_text_style"
                    if person.is_girlfriend:
                        text "Significant Other: [mc.name]" style "menu_text_style"
                    elif person.has_significant_other:
                        text "Significant Other: [person.SO_name]" style "menu_text_style"
                    if person.kids > 0:
                        text "Kids: [person.kids]" style "menu_text_style"
                    if person in mc.business.on_payroll:
                        text "Salary: $[person.salary:.2f]/day" style "menu_text_style"
                        if person.is_employee and person.has_event_day("last_promotion_day"):
                            text f"Last promotion: {get_formatted_date_only_string(person.get_event_day('last_promotion_day'))}" style "menu_text_style"

            frame:
                background "#1a45a1aa"
                xysize (325, 264)
                vbox xfill True:
                    text "Characteristics" style "serum_text_style_header"
                    text "Intelligence: [person.int]" style "menu_text_style"
                    text "Focus: [person.focus]" style "menu_text_style"
                    text "Charisma: [person.charisma]" style "menu_text_style"
                    text "Age: [person.age]" style "menu_text_style"
                    text "Cup size: [person.tits]" style "menu_text_style"
                    text "Height: [height_info]" style "menu_text_style"
                    text "Hair: [hair_info]" style "menu_text_style"
                    text "Eyes: [eyes_info]" style "menu_text_style"

            frame:
                background "#1a45a1aa"
                xysize (325, 264)
                vbox xfill True:
                    text "Work Skills" style "serum_text_style_header"
                    text "Human Resources: [person.hr_skill]" style "menu_text_style"
                    text "Marketing: [person.market_skill]" style "menu_text_style"
                    text "Research & Development: [person.research_skill]" style "menu_text_style"
                    text "Production: [person.production_skill]" style "menu_text_style"
                    text "Supply Procurement: [person.supply_skill]" style "menu_text_style"
                    text "Job Experience Level: [person.work_experience]" style "menu_text_style"
                    if person.current_job and (person.is_employee or person.is_intern):
                        textbutton f"Review Duties: {len(person.duties)}/{person.current_job.seniority_level}":
                            style "textbutton_style"
                            text_style "menu_text_style"
                            action Show("set_duties_screen", None, person, person.current_job, allow_changing_duties = False, show_available_duties = True, hide_on_exit = True)

            frame:
                background "#1a45a1aa"
                xysize (325, 264)
                vbox xfill True:
                    text "Sex Skills" style "serum_text_style_header"
                    text "Foreplay Skill: [person.foreplay_sex_skill]" style "menu_text_style"
                    text "Oral Skill: [person.oral_sex_skill]" style "menu_text_style"
                    text "Vaginal Skill: [person.vaginal_sex_skill]" style "menu_text_style"
                    text "Anal Skill: [person.anal_sex_skill]" style "menu_text_style"
                    text "Novelty: [person.novelty:.0f]%" style "menu_text_style"
                    #VTCODE HERE
                    if person.oral_first is None:
                        text "Oral: {image=virgin_token_small}" style "menu_text_style"
                    else:
                        text "Oral: {}".format(person.oral_first) style "menu_text_style"
                    if person.anal_first is None:
                        text "Anal: {image=virgin_token_small}" style "menu_text_style"
                    else:
                        text "Anal: {}".format(person.anal_first) style "menu_text_style"
                    if person.hymen <= 1 and person.vaginal_first is None:
                        text "Vaginal: {image=virgin_token_small}" style "menu_text_style"
                    else:
                        text "Vaginal: {}".format(person.vaginal_first) style "menu_text_style"
                    if person.hymen == 0 and person.vaginal_virgin <=1:
                        text "Hymen: Intact {image=virgin_token_small}" style "menu_text_style"
                    elif person.hymen == 1:
                        text "Hymen: Torn {image=virgin_token_small}" style "menu_text_style"
                    else:
                        text "Hymen: Remnant" style "menu_text_style"

            frame:
                background "#1a45a1aa"
                xysize (325, 264)
                vbox xfill True:
                    text "Sex Record" style "serum_text_style_header"
                    viewport:
                        scrollbars "vertical"
                        draggable False
                        mousewheel True
                        vbox:
                            for record, value in sorted(person.sex_record.items()):
                                if record == "Last Sex Day":
                                #VTCODE HERE
                                    text f"Last Sex: {last_sex_to_string(day, value)} " style "menu_text_style"
                                elif record == "Last Oral Day":
                                    text f"Oral Last: {last_sex_to_string(day, last_oral_day)} " style "menu_text_style"
                                elif record == "Last Anal Day":
                                    text f"Anal Last: {last_sex_to_string(day, last_anal_day)} [person.anal_cum]" style "menu_text_style"
                                elif record == "Last Vaginal Day":
                                    text f"Vaginal Last: {last_sex_to_string(day, last_vaginal_day)} [person.vaginal_cum]" style "menu_text_style"
                                elif record == "Last Exhibition Day":
                                    text f"Exhibition Last: {last_sex_to_string(day, last_exhibition_day)} {public_sex}" style "menu_text_style"
                                else:
                                    text "[record]: [value]" style "menu_text_style"

        hbox:
            xsize 1750
            spacing 30
            frame:
                background "#1a45a1aa"
                xysize (325, 400)
                vbox xfill True:
                    text "Loves" style "serum_text_style_header"
                    use opinion_list(master_opinion_dict, 2)

            frame:
                background "#1a45a1aa"
                xysize (325, 400)
                vbox xfill True:
                    text "Likes" style "serum_text_style_header"
                    use opinion_list(master_opinion_dict, 1)

            frame:
                background "#1a45a1aa"
                xysize (325, 400)
                vbox xfill True:
                    text "Dislikes" style "serum_text_style_header"
                    use opinion_list(master_opinion_dict, -1)

            frame:
                background "#1a45a1aa"
                xysize (325, 400)
                vbox xfill True:
                    text "Hates" style "serum_text_style_header"
                    use opinion_list(master_opinion_dict, -2)

            frame:
                background "#1a45a1aa"
                xysize (325, 400)
                vbox xfill True:
                    text "Other Relations" style "serum_text_style_header"
                    if len(relationship_list) > 10:
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                if hasattr(person, 'is_daughter_of_mc'):
                                    text "[mc.name] [mc.last_name] [[Father]" size 14 style "menu_text_style"
                                if person.is_family:
                                    if person is mom:
                                        text "[mc.name] [mc.last_name] [[Son]" size 14 style "menu_text_style"
                                    if person is lily:
                                        text "[mc.name] [mc.last_name] [[Brother]" size 14 style "menu_text_style"
                                    if person is aunt:
                                        text "[mc.name] [mc.last_name] [[Nephew]" size 14 style "menu_text_style"
                                    if person is cousin:
                                        text "[mc.name] [mc.last_name] [[Cousin]" size 14 style "menu_text_style"
                                for relationship in relationship_list:
                                    text "[relationship[0].name] [relationship[0].last_name] [[[relationship[1]]]" size 14 style "menu_text_style"
                    else:
                        if hasattr(person, 'is_daughter_of_mc'):
                            text "[mc.name] [mc.last_name] [[Father]" size 14 style "menu_text_style"
                        if person.is_family:
                            if person is mom:
                                text "[mc.name] [mc.last_name] [[Son]" size 14 style "menu_text_style"
                            if person is lily:
                                text "[mc.name] [mc.last_name] [[Brother]" size 14 style "menu_text_style"
                            if person is aunt:
                                text "[mc.name] [mc.last_name] [[Nephew]" size 14 style "menu_text_style"
                            if person is cousin:
                                text "[mc.name] [mc.last_name] [[Cousin]" size 14 style "menu_text_style"
                        for relationship in relationship_list:
                            text "[relationship[0].name] [relationship[0].last_name] [[[relationship[1]]]" size 14 style "menu_text_style"
        hbox:
            xsize 1750
            spacing 30
            frame:
                background "#1a45a1aa"
                xysize (325, 185)
                vbox xfill True:
                    text "Job Statistics" style "serum_text_style_header"
                    text "HR: [hr_base]% Company Efficiency" style "menu_text_style"
                    text "Marketing: [market_base] People" style "menu_text_style"
                    text "Research: [research_base] Research Points" style "menu_text_style"
                    text "Production: [prod_base] Production Points" style "menu_text_style"
                    text "Supply: [supply_base] Supply Units" style "menu_text_style"
                    if person in mc.business.on_payroll:
                        text "Desired Salary: $[base_salary:.2f]/day" style "menu_text_style"

            frame:
                background None
                anchor [0.5,1]
                align [0.5,0]
                xysize [1000,125]
                xoffset 10
                yoffset 30
                imagebutton:
                    align [0.0,0.5]
                    auto "gui/button/choice_%s_background.png"
                    focus_mask "gui/button/choice_idle_background.png"
                    action Hide("person_info_detailed")
                textbutton "Return" align [0.17,0.5] style "return_button_style"

                if person.has_story:
                    imagebutton:
                        align [1.0,0.5]
                        auto "gui/button/choice_%s_background.png"
                        focus_mask "gui/button/choice_idle_background.png"
                        action [
                            Show("story_progress", None, person)
                        ]
                    textbutton "Story Progress" align [0.87,0.5] style "return_button_style"
            frame:
                background "#1a45a1aa"
                xysize (325, 185)
                xoffset 30
                vbox xfill True:
                    text "Currently Affected By" style "serum_text_style_header"
                    viewport:
                        scrollbars "vertical"
                        draggable False
                        mousewheel True
                        vbox:
                            text "Suggestibility: [person.suggestibility:.0f]%" style "menu_text_style"
                            if not person.serum_effects:
                                text "No active serums" style "menu_text_style"
                            else:
                                for serum in person.serum_effects:
                                    text f"{serum.name}: {serum.duration - serum.duration_counter} Turns Left" style "menu_text_style"

    use default_tooltip("person_info_detailed")

screen opinion_list(opinion_dict, preference):
    if len([x for x in opinion_dict if opinion_dict[x][0] == preference]) > 10:
        viewport:
            scrollbars "vertical"
            draggable False
            mousewheel True
            vbox:
                use opinion_list_values(opinion_dict, preference)

    else:
        use opinion_list_values(opinion_dict, preference)

screen opinion_list_values(opinion_dict, preference):
    for opinion in sorted(opinion_dict):
        if opinion_dict[opinion][0] == preference:
            if opinion_dict[opinion][1]:
                text opinion.title() style "menu_text_style"
            else:
                text "???" style "menu_text_style"

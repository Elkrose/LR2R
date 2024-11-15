init -2 python:
    def interview_reveal_oral_virgin():
        reveal_oral_virgin = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_oral_virgin = reveal_oral_virgin or recruitment_policy.extra_data.get("reveal_oral_virgin",False)
        return reveal_oral_virgin

    def interview_reveal_vaginal_virgin():
        reveal_vaginal_virgin = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_vaginal_virgin = reveal_vaginal_virgin or recruitment_policy.extra_data.get("reveal_vaginal_virgin",False)
        return reveal_vaginal_virgin

    def interview_reveal_anal_virgin():
        reveal_anal_virgin = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_anal_virgin = reveal_anal_virgin or recruitment_policy.extra_data.get("reveal_anal_virgin",False)
        return reveal_anal_virgin

screen interview_ui(the_candidates, count):
    default requirements = mc.business.generate_candidate_requirements()
    default current_selection = 0
    default the_candidate = the_candidates[current_selection]
    vbox:
        yalign 0.2
        xalign 0.4
        xanchor 0.5
        spacing 30
        frame:
            background "#1a45a1aa"
            ysize 80
            xsize 1320
            xalign 0.5
            xanchor 0.5
            text "[the_candidate.name] [the_candidate.last_name]" style "menu_text_style" size 50 xanchor 0.5 xalign 0.5 color the_candidate.char.who_args["color"] font the_candidate.char.what_args["font"]
        hbox:
            xsize 1320
            spacing 30
            frame:
                background "#1a45a1aa"
                xsize 420
                ysize 550
                vbox:
                    text "Personal Information" style "menu_text_title_style" size 20 #Info about the person: age, height, happiness, obedience, etc.
                    if interview_reveal_age():
                        text "Age: [the_candidate.age]" style "menu_text_style" size 16
                    if interview_reveal_height():
                        text f"Height: {height_to_string(the_candidate.height)}" style "menu_text_style" size 16
                        text f"Weight: {get_person_weight_string(the_candidate)}" style "menu_text_style" size 16
                    if interview_reveal_happiness():
                        text "Happiness: [the_candidate.happiness]" style "menu_text_style" size 16
                    if interview_reveal_suggestibility():
                        text "Suggestibility: [the_candidate.suggestibility]" style "menu_text_style" size 16
                    if interview_reveal_sluttiness():
                        text "Sluttiness: [the_candidate.sluttiness]" style "menu_text_style" size 16
                    if interview_reveal_love():
                        text "Love: [the_candidate.love]" style "menu_text_style" size 16
                    if interview_reveal_obedience():
                        text f"Obedience: [the_candidate.obedience] - {get_obedience_string(the_candidate.obedience)}" style "menu_text_style" size 16
                    if interview_reveal_tits():
                        text "Cup Size: [the_candidate.tits]" style "menu_text_style" size 16
                        text f"Eye Colour: {the_candidate.eyes[0].title()}" style "menu_text_style" size 16
                    if interview_reveal_relationship():
                        if the_candidate.is_girlfriend:
                            text "Relationship: Girlfriend" style "menu_text_style" size 16
                        else:
                            text "Relationship: [the_candidate.relationship]" style "menu_text_style" size 16

                        if the_candidate.is_girlfriend:
                            text "Significant Other: [mc.name]" style "menu_text_style" size 16
                        elif the_candidate.has_significant_other:
                            text "Significant Other: [the_candidate.SO_name]" style "menu_text_style" size 16

                    if interview_reveal_kids():
                        text "Kids: [the_candidate.kids]" style "menu_text_style" size 16

                    $ salary = base_salary_calculation(the_candidate)
                    textbutton "Base Salary: $[salary:.2f]/day":
                        background None
                        padding (0, 0)
                        action NullAction()
                        text_style "menu_text_style"
                        text_size 16
                        tooltip "Salary depends on many factors, including the job a person will do, the base salary is a generic base-line for wages."

            frame:
                background "#1a45a1aa"
                xsize 420
                ysize 550
                vbox:
                    text "Stats and Skills" style "menu_text_title_style" size 20 #Info about the persons raw stats, work skills, and sex skills
                    text "Job Experience Level: [the_candidate.work_experience]" style "menu_text_style" size 16
                    text "Stats" style "menu_text_style" size 20
                    text "    Charisma: [the_candidate.charisma]" style "menu_text_style" size 16
                    text "    Intelligence: [the_candidate.int]" style "menu_text_style" size 16
                    text "    Focus: [the_candidate.focus]" style "menu_text_style" size 16
                    text "Work Skills" style "menu_text_style" size 20
                    text "    HR: [the_candidate.hr_skill]" style "menu_text_style" size 16
                    text "    Marketing: [the_candidate.market_skill]" style "menu_text_style" size 16
                    text "    Research: [the_candidate.research_skill]" style "menu_text_style" size 16
                    text "    Production: [the_candidate.production_skill]" style "menu_text_style" size 16
                    text "    Supply: [the_candidate.supply_skill]" style "menu_text_style" size 16
                    if interview_reveal_sex_skills():
                        text "Sex Skills" style "menu_text_style" size 20
                        text "    Foreplay Skill: [the_candidate.foreplay_sex_skill]" style "menu_text_style" size 16
                        text "    Oral Skill: [the_candidate.oral_sex_skill]" style "menu_text_style" size 16
                        text "    Vaginal Skill: [the_candidate.vaginal_sex_skill]" style "menu_text_style" size 16
                        text "    Anal Skill: [the_candidate.anal_sex_skill]" style "menu_text_style" size 16
                    #VTCODE HERE
                    if interview_reveal_anal_virgin() or interview_reveal_oral_virgin() or interview_reveal_vaginal_virgin():
                        text "Virginal Stats:" style "menu_text_style" size 20
                    if interview_reveal_oral_virgin():
                        if the_candidate.oral_first is None:
                            text "    Oral: {image=virgin_token_small}" style "menu_text_style" size 16
                        else:
                            text "    Oral: {}".format(the_candidate.oral_first) style "menu_text_style" size 16
                    if interview_reveal_anal_virgin():
                        if the_candidate.anal_first is None:
                            text "    Anal: {image=virgin_token_small}" style "menu_text_style" size 16
                        else:
                            text "    Anal: {}".format(the_candidate.anal_first) style "menu_text_style" size 16
                    if interview_reveal_vaginal_virgin():
                        if the_candidate.hymen <= 1 and the_candidate.vaginal_first is None:
                            text "    Vaginal: {image=virgin_token_small}" style "menu_text_style" size 16
                        else:
                            text "    Vaginal: {}".format(the_candidate.vaginal_first) style "menu_text_style" size 16
                        if the_candidate.hymen == 0 and the_candidate.vaginal_virgin <=1:
                            text "    Hymen: Intact {image=virgin_token_small}" style "menu_text_style" size 16
                        elif the_candidate.hymen == 1:
                            text "    Hymen: Torn {image=virgin_token_small}" style "menu_text_style" size 16
                        else:
                            text "    Hymen: Remnant" style "menu_text_style" size 16

            frame:
                $ master_opinion_dict = dict(the_candidate.opinions, **the_candidate.sexy_opinions)
                background "#1a45a1aa"
                xsize 420
                ysize 550
                vbox:
                    text "Opinions" style "menu_text_title_style" size 20 #Info about the persons loves, likes, dislikes, and hates
                    hbox:
                        spacing 5
                        vbox:
                            xsize 210
                            text "Loves" style "menu_text_style" size 22
                            for opinion in master_opinion_dict:
                                if master_opinion_dict[opinion][0] == 2:
                                    if master_opinion_dict[opinion][1]:
                                        text opinion.title() style "menu_text_style" size 16
                                    else:
                                        text "???" style "menu_text_style" size 16
                        vbox:
                            text "Likes" style "menu_text_style" size 22
                            for opinion in master_opinion_dict:
                                if master_opinion_dict[opinion][0] == 1:
                                    if master_opinion_dict[opinion][1]:
                                        text opinion.title() style "menu_text_style" size 16
                                    else:
                                        text "???" style "menu_text_style" size 16
                    hbox:
                        ysize 14
                    hbox:
                        spacing 5
                        vbox:
                            xsize 210
                            text "Dislikes" style "menu_text_style" size 20
                            for opinion in master_opinion_dict:
                                if master_opinion_dict[opinion][0] == -1:
                                    if master_opinion_dict[opinion][1]:
                                        text opinion.title() style "menu_text_style" size 16
                                    else:
                                        text "???" style "menu_text_style" size 16

                        vbox:
                            text "Hates" style "menu_text_style" size 20
                            for opinion in master_opinion_dict:
                                if master_opinion_dict[opinion][0] == -2:
                                    if master_opinion_dict[opinion][1]:
                                        text opinion.title() style "menu_text_style" size 16
                                    else:
                                        text "???" style "menu_text_style" size 16

        frame:
            background "#1a45a1aa"
            xsize 1320
            ysize 200
            hbox:
                vbox:
                    xsize 650
                    text "Expected Production" style "menu_text_title_style"
                    text f"    Human Resources: +{human_resource_potential_stat(the_candidate)}% Company efficiency per turn" style "menu_text_style" size 16
                    text f"    Marketing: +{marketing_potential_stat(the_candidate)} Market reach people per turn" style "menu_text_style" size 16
                    text f"    Research and Development: {research_potential_stat(the_candidate)} Research points per turn" style "menu_text_style" size 16
                    text f"    Production: {production_potential_stat(the_candidate)} Production points per turn" style "menu_text_style" size 16
                    text f"    Supply Procurement: {supply_potential_stat(the_candidate)} Units of supplies per turn" style "menu_text_style" size 16

                if count > 1:
                    vbox:
                        text "Recruitment Settings" style "menu_text_title_style"
                        text f"    Age Range: {requirements.get('age_floor', 18)} - {requirements.get('age_ceiling', 55)}" style "menu_text_style" size 16
                        if recruitment_single_policy.is_active or recruitment_married_policy.is_active:
                            text f"    Relation: {('Single' if recruitment_single_policy.is_active else 'Married')}" style "menu_text_style" size 16
                        if "tits" in requirements.keys():
                            text f"    Cup-size: {requirements.get('tits', 'AA')}" style "menu_text_style" size 16
                        if recruitment_mothers_policy.is_active or recruitment_childless_policy.is_active:
                            text f"    Children: {('Yes' if recruitment_mothers_policy.is_active else 'No')}" style "menu_text_style" size 16
                        if recruitment_short_policy.is_active or recruitment_tall_policy.is_active:
                            text f"    Height: {('Short' if recruitment_short_policy.is_active else 'Tall')}" style "menu_text_style" size 16
                        if recruitment_suggest_improvement_policy.is_active or recruitment_obedience_improvement_policy.is_active or recruitment_slut_improvement_policy.is_active:
                            text f"    Traits: {build_recruitment_traits_slug()}" style "menu_text_style" size 16

        frame:
            background "#1a45a1aa"
            xsize 1320
            ysize 100
            hbox:
                align (.5, .5)
                textbutton "Previous Candidate":
                    sensitive current_selection > 0
                    selected False
                    style "textbutton_style"
                    text_style "textbutton_text_style"
                    action [
                        SetScreenVariable("current_selection",current_selection-1),
                        SetScreenVariable("the_candidate",the_candidates[current_selection-1]),
                        Function(show_candidate,the_candidates[current_selection-1])
                    ]

                null width 320
                textbutton " Hire Nobody  ":
                    style "textbutton_style"
                    text_style "textbutton_text_style"
                    action [
                        Function(the_candidate.hide_person),
                        Return("None")
                    ]

                null width 20

                textbutton " Hire  ":
                    style "textbutton_style"
                    text_style "textbutton_text_style"
                    action [
                        Function(the_candidate.hide_person),
                        Return(the_candidate)
                    ]

                null width 320
                textbutton "Next Candidate":
                    sensitive current_selection < count-1
                    selected False
                    style "textbutton_style"
                    text_style "textbutton_text_style"
                    action [
                        SetScreenVariable("current_selection",current_selection+1),
                        SetScreenVariable("the_candidate",the_candidates[current_selection+1]),
                        Function(show_candidate,the_candidates[current_selection+1])
                    ]

    imagebutton:
        auto "/tutorial_images/restart_tutorial_%s.png"
        xysize (54, 54)
        anchor (1.0, 1.0)
        align (1.0, 1.0)
        action Function(mc.business.reset_tutorial,"hiring_tutorial")

    if mc.business.event_triggers_dict.get("hiring_tutorial", 0) > 0 and mc.business.event_triggers_dict.get("hiring_tutorial", 1) <= 5: #We use negative numbers to symbolize the tutorial not being enabled
        imagebutton:
            sensitive True
            xsize 1920
            ysize 1080
            idle f"/tutorial_images/hiring_tutorial_{mc.business.event_triggers_dict.get('hiring_tutorial', 1)}.png"
            hover f"/tutorial_images/hiring_tutorial_{mc.business.event_triggers_dict.get('hiring_tutorial', 1)}.png"
            action Function(mc.business.advance_tutorial,"hiring_tutorial")

    use default_tooltip("interview_ui")

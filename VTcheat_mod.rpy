#### Overriding the Corecheat

screen cheat_menu():
    zorder 120
    modal True

    # Screen management variables
    default main_screen_showing = True
    default naming_options = True # Extends the name_options viewport
    default time_control_showing = True

    default main_stats_options = True
    default work_skills_options = True
    default sex_stats_options = True
    default relation_options = True

    default appearance_options = True

    default salary_options = False

    default personality_options = False
    default face_options = False
    default eye_options = False
    default skin_options = False
    default body_options = False
    default tan_options = False
    default idle_options = False
    default breast_options = False
    default hair_style_options = False
    default hair_colour_options = False
    default pubes_options = False
    default pubes_color_options = False
    default font_color_options = False

    default divisions = get_cheat_menu_divisions()

    # Input management variables
    default name_select = False #Determines if the name button is currently taking an input or not

    if "the_person" in globals() and isinstance(the_person, Person):
        default editing_target = the_person # default open the_person cheat menu
        default last_editing_target = the_person.identifier # store identifier for company division highlighting
        default editable_characters = [mc, mc.business, the_person] # Add unique characters to this list if you want to customize them often
    else:
        default editable_characters = [mc, mc.business] # Add unique characters to this list if you want to customize them often
        default editing_target = mc.business
        default last_editing_target = None

    # Lists for common skill attributes.
    # The arrays are utilized in this order: key = "DisplayName", [0 = hasattr check], [1 = variable / key], [2 = amount to changed], [3 = sort order]
    # NOTE: Fields are duplicated in case things change later, less likely that the buttons will need to be re formated
    default main_stats = {
        "Charisma": ["charisma", "charisma", 1, 0, (0, 20)],
        "Focus": ["focus", "focus", 1 , 1, (0, 20)],
        "Intelligence": ["int", "int", 1, 2, (0, 20)],

        "Age": ["age", "age", 1, 3, (Person.get_age_floor(), 99)],
        "Height": ["height", "height", .005, 4, (.72, 1.25)],
        "Energy": ["energy", "energy", 10, 5, (60,  mc.max_energy)],
        "Max Energy": ["max_energy", "max_energy", 10, 6, (10,  mc.max_energy_cap)],
        "Serum Tolerance" : ["_serum_tolerance", "_serum_tolerance", 1, 8, (0, 5)],
        "Clarity": ["free_clarity", "free_clarity", 500, 9, (0, 100000)],
        "Lust": ["locked_clarity", "locked_clarity", 100, 10, (0, 1000)],
        "Clarity Multiplier": ["clarity_multiplier", "clarity_multiplier", .1, 11, (.2, 5)],

        "Funds": ["funds", "funds", 10000, 20, (0, 100000000)],
        "Supplies": ["supply_count", "supply_count", 10000, 21, (0, 100000)],
        "Base Efficiency": ["base_effectiveness_cap", "base_effectiveness_cap", 10, 23, (50, 300)],
        "Market Reach": ["market_reach", "market_reach", 1000,  24, (0, 100000000)]
        }
    default work_skills = {
        "Job Experience": ["work_experience", "work_experience", 1, 0, (1, 20)],
        "HR": ["hr_skill", "hr_skill", 1, 1, (0, 20)],
        "Marketing": ["market_skill", "market_skill", 1, 2, (0, 20)],
        "Researching": ["research_skill", "research_skill", 1, 3, (0, 20)],
        "Production": ["production_skill", "production_skill", 1, 4, (0, 20)],
        "Supplying": ["supply_skill", "supply_skill", 1, 5, (0, 20)],

        "Max Employees": ["max_employee_count", "max_employee_count", 5, 10, (5, 100)],
        "Serum Batch Size": ["batch_size", "batch_size", 1, 11, (1, 20)],
        "Research Tier": ["research_tier", "research_tier", 1, 12, (0, 4)],
        "Attention": ["attention", "attention", 10, 13, (0, 400)],
        "Max Attention": ["max_attention", "max_attention", 10, 13, (0, 400)],
        "Num of Contracts": ["max_offered_contracts", "max_offered_contracts", 1, 15, (1, 5)]
        }
    default relation_stats = {
        "Love": ["love", "love", 10, 0, (-100, 100)],
        "Suggestibility": ["suggestibility", "suggestibility", 10, 2, (0, 100)],
        "Obedience": ["obedience", "obedience", 10, 3, (0, 300)],
        "Happiness": ["happiness", "happiness", 10, 4, (0, 300)],
        "Arousal": ["arousal", "arousal", 10, 5, (0, 100)],
        "Sluttiness": ["_sluttiness", "_sluttiness", 5, 6, (0, 100)],
        "Novelty": ["novelty", "novelty", 5, 7, (0, 100)],
        "Kids": ["kids", "kids", 1, 8, (0, 20)]
        }
    default sex_stats = { # Sex Skills are stored in a dict
        "Foreplay": ["sex_skills", "Foreplay", 1, 0, (0, 20)],
        "Oral": ["sex_skills", "Oral", 1, 1, (0, 20)],
        "Vaginal": ["sex_skills", "Vaginal", 1, 2, (0, 20)],
        "Anal": ["sex_skills", "Anal", 1, 3, (0, 20)]
        }

    default job_options = {
        "Work Experience": ["seniority_level", "seniority_level", 1, 0, (1, 20)],
        "Salary": ["_base_salary", "_base_salary", 1, 0, (0, 1000)],
    }

    # Consider making it update the respective lists custom titles when it becomes possible
    default available_naming = {
        "Title": ["title"],
        "Player's Title": ["mc_title"],
        "Reference Title": ["possessive_title"],
        "First Name": ["name"],
        "Last Name": ["last_name"]
        }

    default business_naming = {
        "Name": ["name"],
    }

    default available_personalities = {}    # only allow personality switching for non-unique
    python:
        if available_personalities == {}:
            for x in list_of_personalities:
                available_personalities[x.personality_type_prefix] = x

    default available_faces = sorted(Person._list_of_faces, key = lambda x: int(x.split("_")[1]))
    default available_eyes = sorted(Person._list_of_eyes,  key = lambda x: x[0])
    default available_body_types = Person._list_of_body_types
    default available_breast_sizes = [x[0] for x in Person._list_of_tits]
    default available_hair_styles = sorted(hair_styles, key = lambda x: x.name)
    default available_hair_colours = sorted(Person._list_of_hairs, key = lambda x: x[0])
    default available_pubes_styles = sorted(pube_styles, key = lambda x: x.name)
    default available_idle_poses = ["stand2","stand3","stand4","stand5"]

    default available_skin = { #
        "White": ["skin", "white"],
        "Tan": ["skin", "tan"],
        "Black": ["skin", "black"]
    }

    default name_type = None
    # Lists for player exclusive attributes
    # Lists for person exclusive attributes
    # Lists for business exclusive attributes

    # Lists for other Objects attributes



    frame: # A main frame that all child elements position themselves after, covers the whole screen.
        background None
        yfill True
        xfill True
        if time_control_showing: # This section must have fail safes so creating individual buttons as before
            frame:
                xysize (390, 50)
                hbox:
                    # xfill True
                    # yfill True
                    grid 3 1:
                        xfill True
                        yfill True
                        textbutton f"D: {day_names[day%7]}":
                            xfill True
                            yfill True
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"

                            action [
                                SetVariable("day", day + 1)
                            ]
                            alternate [
                                SetVariable("day", day - 1)
                            ]

                        textbutton f"T: {time_names[time_of_day]}":
                            xfill True
                            yfill True
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"

                            action [
                                If(time_of_day == 4, true = SetVariable("time_of_day", time_of_day - 4), false = SetVariable("time_of_day", time_of_day + 1))
                            ]
                            alternate [
                                If(time_of_day == 0, true = SetVariable("time_of_day", time_of_day + 4), false = SetVariable("time_of_day", time_of_day - 1))
                            ]

                        textbutton "End Day":
                            xfill True

                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"

                            action [
                                SetVariable("time_of_day", 4), Call("advance_time", from_current=True)
                            ]

        if main_screen_showing:
            frame:
                yalign 0.5
                xysize (260,250)
                hbox:
                    vbox:
                        textbutton "Cheat Menu":
                            xfill True
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            action [
                                Hide("cheat_menu")
                            ]
                        viewport:
                            mousewheel True
                            draggable True
                            ysize 125
                            vbox:
                                for x in editable_characters:
                                    if hasattr(x, "name"):
                                        textbutton "[x.name]":
                                            xfill True

                                            if editing_target == x:
                                                background "#4f7ad6"
                                                hover_background "#4f7ad6"
                                            style "textbutton_no_padding_highlight"
                                            text_style "cheat_text_style"

                                            sensitive True

                                            hovered [
                                                NullAction()
                                            ]
                                            action [

                                                ToggleScreenVariable("editing_target", x, None)
                                            ]

                                            alternate [
                                                NullAction()
                                            ]


        if editing_target is not None:
            frame:
                xoffset 400
                yoffset 200
                xysize (1100, 300)
                grid 4 1:
                    xfill True
                    vbox:
                        textbutton "Main Stats":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True

                            action ToggleScreenVariable("main_stats_options")

                        if main_stats_options:
                            use cheat_stat_list(editing_target, main_stats)

                    vbox:
                            #Make this check if editing_target has any of the attributes in the list instead.
                        textbutton "Work Skills":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True

                            action ToggleScreenVariable("work_skills_options")
                        if work_skills_options:
                            use cheat_stat_list(editing_target, work_skills)

                    vbox:
                        textbutton "Sex Skills":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True

                            action ToggleScreenVariable("sex_stats_options")

                        if sex_stats_options:
                            use cheat_stat_list(editing_target, sex_stats)

                    vbox:

                        textbutton "Relations":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True

                            action ToggleScreenVariable("relation_options")

                        if relation_options:
                            use cheat_stat_list(editing_target, relation_stats)

            frame:
                xoffset 0
                yoffset 50
                xysize (390, 330)
                grid 1 1:
                    vbox:
                        textbutton "Name Options":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True

                            action ToggleScreenVariable("naming_options")

                        if naming_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    $ name_map = business_naming if isinstance(editing_target, Business) else available_naming
                                    for x in name_map:
                                        if hasattr(editing_target, str(name_map[x][0])):
                                            $ item_property = vars(editing_target)[name_map[x][0]]
                                            button:
                                                id "name_select"
                                                margin (2,2)
                                                xfill True

                                                background "#000080"

                                                if name_type == name_map[x][0]:
                                                    background "#4f7ad6"
                                                    hover_background "#4f7ad6"

                                                action [ToggleScreenVariable("name_select"), SetScreenVariable("name_type", name_map[x][0])]

                                                if name_select:
                                                    input default remove_display_tags(str(item_property)):
                                                        changed edit_name_func
                                                        style "cheat_text_style"
                                                        yalign 0.5
                                                        xalign 0.5
                                                        xfill True

                                                else:
                                                    text "[x]: [item_property]":
                                                        yalign 0.5
                                                        yfill True
                                                        style "cheat_text_style"

            if hasattr(editing_target, "jobs") and editing_target in mc.business.on_payroll:
                frame:
                    xoffset 950
                    yoffset 510
                    xysize (300, 400)
                    grid 1 3:
                        xfill True
                        for job in (x for x in editing_target.jobs if x.job_definition.is_paid):
                            vbox:
                                ysize 140
                                textbutton "[job.job_title]":
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"
                                    xfill True

                                use cheat_stat_list(job, job_options)


        if editing_target and isinstance(editing_target, Business):
            frame:
                xoffset 400
                yoffset 510
                xysize (515, 520)
                hbox:
                    vbox:
                        xsize 250
                        textbutton "Salary":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if salary_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("salary_options")]

                        for div in divisions:
                            textbutton "[div]":
                                style "textbutton_no_padding_highlight"
                                text_style "cheat_text_style"
                                xfill True
                                if divisions[div][1]:
                                    background "#4f7ad6"
                                    hover_background "#4f7ad6"
                                action [Function(cheat_collapse_menus), Function(toggle_division_visibility, div)]

                    vbox:
                        xsize 250
                        if salary_options:
                            for x in range(-4, 5):
                                textbutton f"Set to {(10 + x) * 10}%" :
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"
                                    action [
                                        Function(cheat_set_company_salaries, 1.0 + (x/10.0))
                                    ]
                        for div in divisions:
                            if divisions[div][1]:
                                for person in divisions[div][0]:
                                    textbutton "[person.name] [person.last_name]":
                                        xfill True
                                        style "textbutton_no_padding_highlight"
                                        text_style "cheat_text_style"
                                        if person.identifier == last_editing_target:
                                            background "#4f7ad6"
                                            hover_background "#4f7ad6"
                                        action [
                                            SetScreenVariable("last_editing_target", person.identifier),
                                            SetScreenVariable("editing_target", person),
                                            SetScreenVariable("editable_characters", [mc, mc.business, person]),
                                            Function(cheat_appearance)
                                        ]

        if editing_target and not isinstance(editing_target, Business) and not isinstance(editing_target, MainCharacter):
            frame:
                xoffset 400
                yoffset 510
                xysize (515, 520)
                hbox:
                    vbox:
                        xsize 250
                        textbutton "Face Type":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if face_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("face_options")]

                        textbutton "Skin Type":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if skin_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("skin_options")]

                        textbutton "Body Type":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if body_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("body_options")]

                        textbutton "Body Tan":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if tan_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("tan_options")]

                        textbutton "Idle Position":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if idle_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("idle_options")]

                        textbutton "Breast Size":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if breast_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("breast_options")]

                        textbutton "Eye Colour":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if eye_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("eye_options")]

                        textbutton "Hair Style":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if hair_style_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("hair_style_options")]

                        textbutton "Hair Colour":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if hair_colour_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("hair_colour_options")]

                        textbutton "Pubes Style":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if pubes_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("pubes_options")]

                        textbutton "Pubes Color":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if pubes_color_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("pubes_color_options")]

                        if hasattr(editing_target, "personality") and not editing_target.is_unique and editing_target.personality.personality_type_prefix in available_personalities:
                            textbutton "Personality":
                                style "textbutton_no_padding_highlight"
                                text_style "cheat_text_style"
                                xfill True
                                if personality_options:
                                    background "#4f7ad6"
                                    hover_background "#4f7ad6"
                                action [Function(cheat_collapse_menus), ToggleScreenVariable("personality_options")]

                        textbutton "Font Color":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if font_color_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("font_color_options")]

                    vbox:
                        xsize 250
                        if personality_options and hasattr(editing_target, "personality"):
                            viewport:
                                mousewheel True
                                scrollbars "vertical"
                                ysize 480

                                vbox:
                                    for x in sorted([x for x in available_personalities], key = lambda x: x.lower()):
                                        $ name = x.title()
                                        textbutton "[name]":
                                            xfill True
                                            style "textbutton_no_padding_highlight"
                                            text_style "cheat_text_style"

                                            if editing_target.personality.personality_type_prefix == x:
                                                sensitive False
                                                background "#4f7ad6"
                                                hover_background "#4f7ad6"

                                            action [
                                                Function(setattr, editing_target, "personality", available_personalities[x])
                                            ]

                        if face_options and hasattr(editing_target, "face_style"):
                            for x in available_faces:
                                $ name = x.replace("_", " ")
                                textbutton "[name]":
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.face_style == x:
                                        sensitive False
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        Function(setattr, editing_target, "face_style", x),
                                        Function(cheat_appearance)
                                    ]

                        if eye_options and hasattr(editing_target, "eyes"):
                            for x in available_eyes:
                                $ name = x[0].title()
                                textbutton "[name]":
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.eyes[0].lower() == x[0]:
                                        sensitive False
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        Function(setattr, editing_target, "eyes", x),
                                        Function(cheat_appearance)
                                    ]

                        if skin_options and hasattr(editing_target, "skin"):
                            for x in available_skin:
                                textbutton "[x]":
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.skin == available_skin[x][1]:
                                        sensitive False
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        Function(setattr, editing_target, available_skin[x][0], available_skin[x][1]),
                                        Function(cheat_appearance)
                                    ]

                        if body_options and hasattr(editing_target, "body_type"):
                            for x in available_body_types:
                                $ name = x.replace("_", " ").title()
                                textbutton "[name]":
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.body_type == x:
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        Function(setattr, editing_target, "body_type", x),
                                        Function(cheat_appearance)
                                    ]

                        if tan_options and hasattr(editing_target, "tan"):
                            for name in tan_images_dict:
                                textbutton "[name]":
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.tan == name:
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        Function(setattr, editing_target, "tan", name),
                                        Function(cheat_appearance)
                                    ]

                        if idle_options and hasattr(editing_target, "idle_pose"):
                            for x in available_idle_poses:
                                $ name = x.replace("_", " ").title()
                                textbutton "[name]":
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.idle_pose == x:
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        Function(setattr, editing_target, "idle_pose", x),
                                        Function(cheat_appearance)
                                    ]

                        if breast_options and hasattr(editing_target, "tits"):
                            for x in available_breast_sizes:
                                textbutton "[x]":
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.tits == x:
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        Function(setattr, editing_target, "tits", x),
                                        Function(cheat_appearance)
                                    ]

                        if hair_style_options and hasattr(editing_target, "hair_style" and "hair_colour"):
                            for x in available_hair_styles:
                                textbutton "[x.name]":
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if x.is_similar(editing_target.hair_style):
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        SetField(editing_target,"hair_style", x.get_copy()),
                                        SetField(editing_target, "hair_style.colour", editing_target.hair_colour[1]),
                                        Function(cheat_appearance)
                                    ]

                        if hair_colour_options and hasattr(editing_target, "hair_style" and "hair_colour"):
                            viewport:
                                mousewheel True
                                scrollbars "vertical"
                                ysize 480

                                vbox:
                                    for x in available_hair_colours:
                                        $ name = x[0].title()
                                        textbutton "[name]":
                                            xfill True
                                            style "textbutton_no_padding_highlight"
                                            text_style "cheat_text_style"

                                            if editing_target.hair_colour[0].lower() == x[0]:
                                                background "#4f7ad6"
                                                hover_background "#4f7ad6"

                                            action [
                                                SetField(editing_target, "hair_colour", x),
                                                SetField(editing_target, "hair_style.colour", x[1]),
                                                Function(cheat_appearance)
                                            ]

                        if pubes_options and hasattr(editing_target, "pubes_style"):
                            for x in available_pubes_styles:
                                textbutton "[x.name]":
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.pubes_style.is_similar(x):
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        SetField(editing_target, "pubes_style.colour", editing_target.pubes_colour),
                                        SetField(editing_target, "pubes_style", x),
                                        Function(cheat_appearance)
                                    ]

                        if pubes_color_options and hasattr(editing_target, "pubes_colour"):
                            viewport:
                                mousewheel True
                                scrollbars "vertical"
                                ysize 480
                                vbox:
                                    for x in available_hair_colours:
                                        $ name = x[0].title()
                                        $ color = x[1][:]
                                        $ color[3] = 0.9
                                        textbutton "[name]":
                                            xfill True
                                            style "textbutton_no_padding_highlight"
                                            text_style "cheat_text_style"

                                            if closest_hair_colour(Color(rgb = editing_target.pubes_colour[:-1])) == x[0]:
                                                background "#4f7ad6"
                                                hover_background "#4f7ad6"

                                            action [
                                                SetField(editing_target, "pubes_colour", color),
                                                SetField(editing_target, "pubes_style.colour", color),
                                                Function(cheat_appearance)
                                            ]

                        if font_color_options and hasattr(editing_target, "name"):
                            viewport:
                                mousewheel True
                                scrollbars "vertical"
                                ysize 480

                                vbox:
                                    $ name = getattr(editing_target, "name")
                                    for c in readable_color_list:
                                        textbutton "{color=[c]}[name]{/color}":
                                            xfill True
                                            style "textbutton_no_padding_highlight"
                                            text_style "cheat_text_style"

                                            if editing_target.char.what_args["color"] == c:
                                                background "#4f7ad6"
                                                hover_background "#4f7ad6"

                                            action [Function(cheat_person_font_color, editing_target, c)]

screen cheat_increase_serum_trait_mastery_button(trait):
    $ trait_title = get_trait_display_title(trait)
    $ trait_side_effects_text = get_trait_side_effect_text(None, trait)
    $ trait_mastery_text = get_trait_mastery_text(trait)

    textbutton "[trait_title]\n{size=14}Mastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text]{/size}":
        text_xalign 0.5
        text_text_align 0.5
        action [
            Hide("trait_tooltip"),
            SetField(trait, "mastery_level", trait.mastery_level + 15)
        ]
        alternate [
            Hide("trait_tooltip"),
            SetField(trait, "mastery_level", (trait.mastery_level - 1) if trait.mastery_level > 2 else 1.0),
        ]
        style "textbutton_style"
        text_style "serum_text_style_traits"
        hovered Show("trait_tooltip",None,trait, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
        unhovered Hide("trait_tooltip")
        xsize 395

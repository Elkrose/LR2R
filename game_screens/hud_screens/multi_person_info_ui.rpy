#Used to display stats for multi people while you're talking to them, takes an array of Actor objects.
init 2 python:
    def multi_person_info_ui_get_formatted_tooltip(person):
        (role_list, fetish_list) = person_info_ui_get_special_role_information(person)

        tooltip = [
            f"Happiness: {person.happiness}\n",
            f"Suggestibility: {min(100, person.suggestibility)}%\n",
            f"Age: {person.age}\n",
            f"Height: {height_to_string(person.height)}\n",
            f"Cup size: {person.tits}\n",
            f"Weight: {get_person_weight_string(person)}\n",
            f"Novelty: {person.novelty:.0f}%\n",
        ]
        tooltip.insert(0, f"Job: {person_info_ui_get_job_title(person)}\n")
        if fetish_list:
            tooltip.append(f"Fetishes: {', '.join(fetish_list)}\n")
        if role_list:
            tooltip.append(f"{', '.join(role_list)}\n")
        return "".join(tooltip)

screen multi_person_info_ui(actors):
    tag master_tooltip
    layer "solo"
    zorder 200

    frame:
        background "empty_token_small"
        xsize 1100
        ysize 200
        yalign 0.0
        xalign 0.5
        xanchor 0.5

        hbox:
            xanchor 0.5
            xalign 0.5
            spacing 10
            xsize 1000
            xoffset 50

            for actor in sorted(actors, key=lambda a: a.sort_order):
                use actor_info_block(actor)

screen actor_info_block(actor):
    python:
        love_label = person_info_ui_get_label_tag(actor.person, "Love", "Love")
        obedience_label = person_info_ui_get_label_tag(actor.person, "Obedience", "Obedience")
        slut_label = person_info_ui_get_label_tag(actor.person, "Sluttiness", "Slut")
        energy_label = person_info_ui_get_label_tag(actor.person, "Energy", "Energy")
        love_info = get_love_hearts(actor.person.love, 5)
        sluttiness_info = get_heart_image_list(actor.person.sluttiness, actor.person.effective_sluttiness())
        obedience_info = f"{actor.person.obedience} {{image=triskelion_token_small}} {get_obedience_string(actor.person.obedience)}"

    frame:
        background Frame("multiboxVT")
        xsize 360
        ysize 210
        #padding (10, 10)
        xmaximum 360
        xminimum 360
        xalign 0.5
        xanchor 0.5
        
        vbox:
            hbox:
                textbutton "{image=question_mark_small}":
                    yoffset 4
                    style "transparent_style"
                    tooltip multi_person_info_ui_get_formatted_tooltip(actor.person)
                    action NullAction()

                text format_titles_short(actor.person) style "menu_text_style" size 30 ysize 30
                use favourite_toggle_button(actor.person)

                if actor.person.serum_tolerance == 0:
                    textbutton "{image=serum_vial3}":
                        xoffset 4
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "Warning: this person has no tolerance for serums\n" + person_info_ui_get_serum_info_tooltip(actor.person)
                        action NullAction()
                elif actor.person.serum_effects:
                    textbutton (f"{{image=serum_vial3}} +{min(100, actor.person.suggestibility)}%" if actor.person.active_serum_count > actor.person.serum_tolerance
                            else f"{{image=serum_vial2}} +{min(100, actor.person.suggestibility)}%" if actor.person.active_serum_count == actor.person.serum_tolerance
                            else f"{{image=serum_vial}} +{min(100, actor.person.suggestibility)}%"):
                        xoffset 4
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip person_info_ui_get_serum_info_tooltip(actor.person)
                        action NullAction()
                if actor.person.bc_status_known and actor.person.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception"):
                    imagebutton:
                        pos(0, 50)
                        idle "beezee"
                        action NullAction()
                        tooltip f"{{image=beezee_token_small}} She is ovulating and has a higher chance of getting pregnant, based on birth control and desire to get pregnant."

            textbutton f"Arousal: {get_arousal_with_token_string(actor.person.arousal, actor.person.max_arousal)}":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip f"When a girl is brought to 100% arousal she will start to climax. Climaxing will increase sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider.\nCurrently: {get_arousal_number_string(actor.person.arousal, actor.person.max_arousal)}"
                action NullAction()

            textbutton f"[energy_label]: {get_energy_string(actor.person.energy, actor.person.max_energy)}":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip f"Energy is spent while having sex, with more energy spent on positions that give the man more pleasure. Some energy comes back each turn, and a lot of energy comes back overnight.\nCurrently {get_energy_number_string(actor.person.energy, actor.person.max_energy)}"
                action NullAction()

            textbutton "[love_label]: [love_info]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip f"Girls who love you will be more willing to have sex when you're in private (as long as they aren't family) and be more devoted to you. Girls who hate you will have a lower effective sluttiness regardless of the situation.\nWhen a girl is not part of your harem, she will slowly lose love until it reaches 80, having sex once every five days will stop the love bleed.\nLove: {get_attention_number_string(actor.person.love, 100)}"
                action NullAction()

            hbox:
                textbutton f"[obedience_label]: [obedience_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, and low obedience girls are likely to refuse altogether."
                    action NullAction()

                if bool(actor.person.situational_obedience):
                    textbutton "{image=question_mark_small}":
                        style "transparent_style"
                        tooltip person_info_ui_get_formatted_obedience_tooltip(actor.person)
                        action NullAction()

            hbox:
                textbutton f"[slut_label]: [sluttiness_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "The higher a girls sluttiness the more slutty actions she will consider acceptable and normal. Her arousal adds a temporary sluttiness ({image=red_heart_token_small}). Her base sluttiness ({image=gold_heart_token_small}) is permanent, but can be increased by situational modifiers."
                    action NullAction()

                if bool(actor.person.situational_sluttiness):
                    textbutton "{image=question_mark_small}":
                        style "transparent_style"
                        tooltip person_info_ui_get_formatted_tooltip(actor.person)
                        action NullAction()

            hbox:
                xpos 50
                ypos 5
            #### Virgin Tracker starts here ####
                $ dayslastsex = 0
                $ daysince = ""
                if actor.person.has_event_day("last_insemination") and actor.person.days_since_event("last_insemination") < 4:
                    if actor.person.days_since_event("last_insemination") > 1:
                        $ dayslastsex = 4 - actor.person.days_since_event("last_insemination") 
                        if dayslastsex == 1:
                            $ daysince = "\nMy womb feels empty!"
                        else:
                            $ daysince = "\nYour sperm in me for "+str(dayslastsex)+" more days!\n Such warm butterflies!"
            #### Virgin UI ####
                if getattr(persistent, "HUDVT")==1:
                #### Relationship Status
                    if getattr(persistent, "relationship")==1:
                        $ VTrelationshipst = "norelations"
                        $ VTrelationshiptt = f"{{image=dontknow_token_small}} Has no romantic relations with you."
                        if actor.person.has_relation_with_mc:
                            if actor.person.is_slave:
                                if actor.person.has_role(harem_role):
                                    if actor.person.has_role(affair_role):
                                        $ VTrelationshipst = "parapolyslave"
                                        $ VTrelationshiptt = f"{{image=parapolyslave_small}} She is your slave, part of your polycule, and your paramour."
                                    else:
                                        if actor.person.is_family:
                                            $ VTrelationshipst = "polyfamiliaslave"
                                            $ VTrelationshiptt = f"{{image=polyfamiliaslave_small}} She is "+actor.person.relation_possessive_title+",\n slave, and part of your polycule."
                                        else:
                                            $ VTrelationshipst = "polyslave"
                                            $ VTrelationshiptt = f"{{image=polyslave_small}} She is your slave and part of your polycule."
                                else:
                                    if actor.person.has_role(affair_role):
                                        $ VTrelationshipst = "paraslave"
                                        $ VTrelationshiptt = f"{{image=paraslave_small}} She is your slave and paramour."
                                    else:
                                        if actor.person.is_family:
                                            $ VTrelationshipst = "gffamiliaslave"
                                            $ VTrelationshiptt = f"{{image=gffamiliaslave_small}} She is "+actor.person.relation_possessive_title+",\nand your slave."
                                        else:
                                            $ VTrelationshipst = "gfslave"
                                            $ VTrelationshiptt = f"{{image=gfslave_small}} She is your girlfriend and your slave."
                            else:
                                if actor.person.has_role(harem_role):
                                    if actor.person.has_role(affair_role):
                                        $ VTrelationshipst = "parapoly"
                                        $ VTrelationshiptt = f"{{image=parapoly_token_small}} She is part of your polycule, and your paramour."
                                    else:
                                        if actor.person.is_family:
                                            $ VTrelationshipst = "familypoly"
                                            $ VTrelationshiptt = f"{{image=familypoly_small}} She is "+actor.person.relation_possessive_title+",\nand part of your polycule."
                                        else:
                                            $ VTrelationshipst = "polyamorous"
                                            $ VTrelationshiptt = f"{{image=harem_token_small}} She is part of your polycule."
                                else:
                                    if actor.person.has_role(affair_role):
                                        $ VTrelationshipst = "paramour"
                                        $ VTrelationshiptt = f"{{image=paramour_token_small}} She is your paramour."
                                    else:
                                        if actor.person.is_family:
                                            $ VTrelationshipst = "familylove"
                                            $ VTrelationshiptt = f"{{image=familylove_small}} She is "+actor.person.relation_possessive_title+",\nand your girlfriend."
                                        else:
                                            $ VTrelationshipst = "girlfriend"
                                            $ VTrelationshiptt = f"{{image=gf_token_small}} She is your girlfriend."
                        else:
                            if actor.person.is_family:
                                if actor.person.is_slave:
                                    $ VTrelationshipst = "familiaslave"
                                    $ VTrelationshiptt = f"{{image=familiaslave_small}} She is "+actor.person.relation_possessive_title+", and your slave."
                                else:
                                    $ VTrelationshipst = "familycircle"
                                    $ VTrelationshiptt = f"{{image=familycircle_small}} She is "+actor.person.relation_possessive_title+"."
                            else:
                                if actor.person.is_slave:
                                    $ VTrelationshipst = "slave"
                                    $ VTrelationshiptt = f"{{image=slave_small}} She is your slave."
                                else:
                                    $ VTrelationshipst = "norelations"
                                    $ VTrelationshiptt = f"{{image=dontknow_token_small}} Has no romantic relations with you."
                        imagebutton:
                            pos(0, 0)
                            idle VTrelationshipst
                            action NullAction()
                            tooltip VTrelationshiptt
            ###### Birth Control Status
                    if getattr(persistent, "knowbirthcontrol")==1:
                        $ VTbcat = "talking"
                        $ VTbcst = "knowbirthcontrol"
                        $ VTbctt = f"{{image=knowbc_token_small}} Is she on birth control?"
                        $ VTpro = ""
                        if actor.person.bc_status_known:
                            if actor.person._birth_control and actor.person.on_birth_control:
                                $ VTbcst = "birthcontrol"
                                $ VTbctt = f"{{image=bc_image_small}} She is on birth control."
                                $ VTpro = " protected"
                            else:
                                $ VTbcst = "nobirthcontrol"
                                $ VTbctt = f"{{image=nobc_image_small}} She is not on birth control."
                                $ VTpro = " defenseless"
                                if actor.person.is_infertile:
                                    $ VTpro = " infertile"
                                #needed an exception for Erica... core issue (Needs better way of preventing story chars from getting knocked up before story done)
                                if not actor.person._birth_control and actor.person.on_birth_control and actor.person.name=="Erica":
                                    $ VTbcst = "birthcontrol"
                                    $ VTbctt = f"{{image=bc_image_small}} She is on birth control."
                                    $ VTpro = " protected"
                        else:
                            $ VTbcst = "knowbirthcontrol"
                            $ VTbctt = f"{{image=knowbc_token_small}} Is she on birth control?"
                        $ VTbreedfertile = ""
                        if actor.person.bc_status_known and actor.person.is_highly_fertile and not actor.person.on_birth_control and perk_system.has_ability_perk("Ovulation Cycle Perception") and persistent.pregnancy_pref > 0:
                            $ VTbreedfertile = " highly fertile"
                        #the interactive icons during sex stuff
                        if 'position_choice' in globals():
                            $ VTbcat = "sexualized"
                        #PREGNANCY HAXX
                        if actor.person.knows_pregnant:
                                $ VTbcst = "pregnant"
                                $ VTbctt = f"{{image=vtcherries_small}} She is pregnant."
                                $ VTpro = ""
                                $ VTbreedfertile = " pregnant"

                        imagebutton:
                            pos(0, 0)
                            idle VTbcst
                            action NullAction()
                            tooltip VTbctt
                        if actor.person.bc_status_known and not actor.person.on_birth_control and actor.person.is_highly_fertile and perk_system.has_ability_perk("Ovulation Cycle Perception") and persistent.pregnancy_pref > 0:
                            $ VTbctt += f"\n{{image=beezee_token_small}} She is highly fertile."
                            imagebutton:
                                pos(-32, 0)
                                idle "beezee"
                                action NullAction()
                                tooltip VTbctt
            ####### Wants Condom
                    if getattr(persistent, "knowcondom")==1:
                        $ VTcondomat = "talking"
                        $ VTcondommc = "condom"
                        $ VTcondomst = "vtcherries"
                        $ VTcondomtt = f"{{image=vtcherries_small}} You are currently not wearing a condom."
                        #the interactive icons during sex stuff
                        if 'position_choice' in globals():
                            if hasattr(position_choice, 'skill_tag'):
                                $ VTcondomat = "sexualized"
                                if mc.condom == False:
                                    $ VTcondomst = "vtcherries"
                                    $ VTcondommc = "condomoff"
                                    $ VTcondomtt = f"{{image=vtcherries_small}} You are natural."
                                else:
                                    $ VTcondomst = "wearcondom"
                                    $ VTcondomtt = f"{{image=wearcondom_token_small}} You are wearing a condom."

                        if VTcondomat=="sexualized":
                            if VTcondommc == "condomoff" and actor.person.days_since_event("last_insemination")<1 and actor.person.vaginal_cum >0:
                                $ VTcondomst = "creamcherry"
                                $ VTcondomtt = f"{{image=vtcherries_small}} You are natural and well oiled."
                            imagebutton:
                                pos(0, 0)
                                idle VTcondomst
                                action NullAction()
                                tooltip VTcondomtt

                        if VTcondomat=="talking":
                            if mc.condom == False and actor.person.days_since_event("last_insemination")<1 and actor.person.vaginal_cum >0:
                                $ VTcondomst = "creamcherry"
                                $ VTcondomtt = f"{{image=vtcherries_small}} You are natural and well oiled."
                            imagebutton:
                                pos(0, 0)
                                idle VTcondomst
                                action NullAction()
                                tooltip VTcondomtt                    
            ### Oral Virgin Flag
                    if getattr(persistent, "knowlips")==1:
                        $ VToralat = "talking"
                        $ VToralst = "bitelip"
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
                                    if actor.person.oral_cum >0:
                                        if actor.person.oral_cum == 1:
                                            if actor.person.arousal_perc >= 59:
                                                $ VToralst = "ahegaoface"
                                                $ VToraltt = f"She seems lost in her bliss and panting. \n{{image=ahegaomouth_small}}She has a dose of your protein in her belly."
                                            else:
                                                $ VToralst = "bitelip"
                                                $ VToraltt = f"She looks at you with lust \n in her innocent hungry eyes. \n{{image=ahegaomouth_small}}She has a dose of your protein in her belly."
                                        else:
                                            if actor.person.oral_cum >3:
                                                if actor.person.arousal_perc >= 59:
                                                    $ VToralst = "ahegaoface"
                                                    $ VToraltt = f"*She hungrily gazes at you for more cum.*\n{{image=ahegaomouth_small}} She has "+ str(actor.person.oral_cum) +" doses of your cum \n swimming in her stomach, causing a bit of a bulge."
                                                else:
                                                    $ VToralst = "ahegaomouth"
                                                    $ VToraltt = f"{{image=ahegaomouth_small}} "+ str(actor.person.oral_cum) +" doses of your cum \n swimming in the slight bulge of her belly."
                                            else:
                                                if actor.person.arousal_perc >= 59:
                                                    $ VToralst = "ahegaoface"
                                                    $ VToraltt = f"*She hungrily gazes at you for more cum.*\n{{image=ahegaomouth_small}} She has "+ str(actor.person.oral_cum) +" doses of your cum \n swimming in her belly."
                                                else:
                                                    $ VToralst = "bitelip"
                                                    $ VToraltt = f"{{image=ahegaomouth_small}} "+ str(actor.person.oral_cum) +" doses of your cum \nswimming in her belly."
                                    else:
                                        $ VToralst = "bitelip"
                                        if actor.person.oral_virgin == 0:
                                            $ VToraltt = f"{{image=virgin_oral_small}} She plays with her innocent hungry fresh pussy.\nShe bites her lip coyly."
                                        else:
                                            if actor.person.oral_first == mc.name:
                                                $ VToraltt = f"{{image=handprint_token_small}} She locks eyes with you and bite her lip sexily."
                                            else:
                                                $ VToraltt = f"{{image=bitelip_small}} She pants and breathes heavily and bites her lip."
                                        if actor.person.energy <20 and actor.person.had_sex_today:
                                            $ VToraltt += f"{{image=bitelip_small}} She seems lost in her bliss and panting."

                        if VToralat=="talking":
                            if actor.person.arousal_perc >= 59:
                                if actor.person.oral_cum ==0:
                                    $ VToralst = "ahegaoface"
                                    if actor.person.oral_virgin == 0:
                                        $ VToraltt = f"{{image=virgin_oral_small}} She looks at you with lust \n in her innocent hungry eyes."
                                    else:
                                        if actor.person.oral_first == mc.name:
                                            $ VToraltt = f"{{image=handprint_token_small}} She starts to drool \n and undress you with her eyes."
                                        else:
                                            $ VToraltt = f"{{image=bitelip_small}} She looks at you with savage lust in her eyes."
                                    if actor.person.energy <20 and actor.person.had_sex_today:
                                        $ VToraltt = f"{{image=bitelip_small}} She seems lost in her bliss and panting."
                                if actor.person.oral_cum >0:
                                    $ VToralst = "ahegaoface"
                                    if actor.person.energy <20 and actor.person.had_sex_today:
                                        $ VToraltt = f"{{image=bitelip_small}} She seems lost in her bliss and panting."
                                    else:
                                        $ VToraltt = f"{{image=bitelip_small}} She hungrily gazes as you for more cum."
                                    if actor.person.oral_cum == 1:
                                        $ VToraltt += f"\n{{image=ahegaomouth_small}} She has a dose of your protein in her belly."
                                    else:
                                        $ VToraltt += f"\n{{image=ahegaomouth_small}} "+ str(actor.person.oral_cum) +" doses of your cum \n swimming in her belly."
                            else:
                                if actor.person.oral_virgin == 0: #morevisual with virgin
                                    $ VToralst = "virgin_oral"
                                    $ VToraltt = f"{{image=virgin_oral_small}} Her lips look sweet and inexperienced."
                                if actor.person.oral_first == mc.name:
                                    $ VToralst = "claimedmouth"
                                    $ VToraltt = f"{{image=handprint_token_small}} You Claimed this Pie Hole!"
                                else:
                                    if actor.person.oral_first !=None and actor.person.oral_virgin>0:
                                        $ VToralst = "oralclaimed"
                                        $ VToraltt = f"{{image=oralclaimed_small}} Someone else had her lips before you... CLAIM IT!"
                                if actor.person.oral_cum >0:
                                    $ VToralst = "bitelip"
                                    if actor.person.oral_cum == 1:
                                        $ VToraltt += f"\n{{image=ahegaomouth_small}} She has a dose of your protein in her belly."
                                    else:
                                        $ VToraltt += f"\n{{image=ahegaomouth_small}} "+ str(actor.person.oral_cum) +" doses of your cum \n swimming in her belly."

                        imagebutton:
                            pos(0, 0)
                            idle VToralst
                            action NullAction()
                            tooltip VToraltt
            ### Vaginal Virgin Flag
                    if getattr(persistent, "knowvaginal")==1:
                        $ VTvaginalat = "talking"
                        $ VTvaginalst = "spreadvag"
                        $ VTvaginaltt = ""
                        #the interactive icons during sex stuff
                        if 'position_choice' in globals():
                            if hasattr(position_choice, 'skill_tag'):
                                if position_choice.skill_tag == 'Vaginal':
                                    if 'climax_type' in globals():
                                        if climax_type == "pussy":
                                            if mc.condom == False:
                                                if actor.person.hymen ==1:
                                                    $ VTvaginalat = "sexualized"
                                                    $ VTvaginalst = "vaghymen"
                                                    $ VTvaginaltt = f"{{image=handprint_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with your virile seed! \n Her virinity mixes with your cum!"
                                                else:
                                                    $ VTvaginalat = "sexualized"
                                                    $ VTvaginalst = "openvag"
                                                    $ VTvaginaltt = f"{{image=openvag_small}} You flood her"+VTbreedfertile+VTpro+" womb with your seed!"
                                                    if actor.person.vaginal_cum >=1:
                                                        $ VTvaginalst = "ahegaovag"
                                            else:
                                                if actor.person.hymen ==1:
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
                                    if actor.person.vaginal_cum >0:
                                        if actor.person.vaginal_cum == 1:
                                            if actor.person.hymen <=1:
                                                if actor.person.hymen == 0:
                                                    $ VTvaginalst = "vaghymen"
                                                    $ VTvaginaltt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} Marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."                            
                                                else:
                                                    $ VTvaginalst = "vaghymen"
                                                    $ VTvaginaltt += f"{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."
                                            else:
                                                $ VTvaginalst = "openvag"
                                                $ VTvaginaltt = f"{{image=beezee_token_small}} Your seed is in her"+VTbreedfertile+VTpro+" womb."
                                        else:
                                            if actor.person.hymen <=1:
                                                if actor.person.vaginal_cum >3:
                                                    $ VTvaginalst = "ahegaovag"
                                                    $ VTvaginaltt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} Her freshly fucked"+VTbreedfertile+VTpro+" womb \ncan barely contain your "+str(actor.person.vaginal_cum)+ " doses of your seed. \n It is already oozing out."
                                                else:
                                                    $ VTvaginalst = "vaghymen"
                                                    $ VTvaginaltt = f"{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb \n with "+str(actor.person.vaginal_cum)+ " doses of your seed."
                                            else:
                                                if actor.person.vaginal_cum >3:
                                                    $ VTvaginalst = "ahegaovag"
                                                    $ VTvaginaltt = f"{{image=beezee_token_small}} Her pussy can barely contain \nthe "+ str(actor.person.vaginal_cum) +" doses of your cum swimming in \nher"+VTbreedfertile+VTpro+" womb and is already oozing out."+daysince
                                                else:
                                                    $ VTvaginalst = "openvag"
                                                    $ VTvaginaltt = f"{{image=beezee_token_small}} "+ str(actor.person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."+daysince
                                        if actor.person.arousal_perc >= 59:
                                            $ VTvaginaltt += f"\n{{image=spreadvag_small}} *You can really smell her arousal*"
                                    else:
                                        $ VTvaginalst = "spreadvag"
                                        if actor.person.vaginal_virgin == 0:
                                            $ VTvaginaltt = f"{{image=virgin_vaginal_small}} She plays with her fresh innocent hungry pussy."
                                        else:
                                            if actor.person.vaginal_first == mc.name:
                                                $ VTvaginaltt = f"{{image=handprint_token_small}} She locks eyes with you and licks her lips \n and plays with her pussy."
                                            else:
                                                $ VTvaginaltt = f"{{image=spreadvag_small}} She pants heavily as she plays with her pussy."
                                        if actor.person.energy <20 and actor.person.had_sex_today:
                                            $ VTvaginaltt = f"{{image=spreadvag_small}} She seems lost in her bliss and panting."

                        if VTvaginalat=="sexualized":
                            if actor.person.hymen == 0 and actor.person.vaginal_virgin <=1: #morevisual with virgin
                                $ VTvaginalst = "virgin_vaginal"
                                $ VTvaginaltt = f"{{image=virgin_vaginal_small}} She looks so innocent and inexperienced."
                            $ VTvaginalcum = "bc_cum"
                            if actor.person.hymen >1 and actor.person.vaginal_cum >1:
                                $ VTvaginalcum = "bc_cum"
                                $ VTvaginaltt += f"\n{{image=creamcherry_small}} "+ str(actor.person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."+daysince
                            else:
                                if actor.person.hymen <2 and actor.person.vaginal_cum>0:
                                    $ VTvaginalcum = "vaghymen"
                        if VTvaginalat=="talking":
                            if actor.person.hymen == 0 and actor.person.vaginal_virgin <=1: #morevisual with virgin
                                $ VTvaginalst = "virgin_vaginal"
                                $ VTvaginaltt = f"{{image=virgin_vaginal_small}} She looks so innocent and inexperienced."
                            if actor.person.vaginal_first == mc.name:
                                $ VTvaginalst = "claimedvag"
                                $ VTvaginaltt = f"{{image=handprint_token_small}} You Claimed this Pussy!"
                            else:
                                if actor.person.vaginal_first !=None and actor.person.hymen==2:
                                    $ VTvaginalst = "vaginalclaimed"
                                    $ VTvaginaltt = f"{{image=vaginalclaimed_small}} Someone else had this pussy before you... OWN IT!"
                            if actor.person.arousal_perc >= 59 and actor.person.vaginal_cum<=0:
                                $ VTvaginalst = "spreadvag"
                                if actor.person.vaginal_virgin <= 1:
                                    $ VTvaginaltt += f"\n{{image=virgin_vaginal_small}} Her fresh pussy is dripping for you.\n*You can really smell her arousal*"
                                    if actor.person.hymen ==0:
                                        $ VTvaginaltt += f"\n{{image=virgin_vaginal_small}} She is more than ready to be fucked."
                                else:
                                    if actor.person.vaginal_first == mc.name:
                                        $ VTvaginaltt += f"\n{{image=handprint_token_small}} Her pussy is dripping for you.\n*You can really smell her arousal*\nCome take me!"
                                    else:
                                        $ VTvaginaltt += f"\n{{image=vagclosed_small}} Her pussy is dripping down her leg.\n*She is really aroused*"
                            else:
                                if actor.person.vaginal_cum >0:
                                    if actor.person.vaginal_cum == 1:
                                        if actor.person.hymen <=1:
                                            if actor.person.hymen == 0:
                                                $ VTvaginalst = "vaghymen"
                                                $ VTvaginaltt = f"{{image=handprint_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."                            
                                            else:
                                                $ VTvaginalst = "vaghymen"
                                                $ VTvaginaltt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with your seed."
                                        else:
                                            $ VTvaginalst = "openvag"
                                            $ VTvaginaltt += f"\n{{image=beezee_token_small}} Your seed is in her"+VTbreedfertile+VTpro+" womb."
                                    else:
                                        if actor.person.hymen <=1:
                                            if actor.person.vaginal_cum >3:
                                                $ VTvaginalst = "ahegaovag"
                                                $ VTvaginaltt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} Her freshly fucked"+VTbreedfertile+VTpro+" womb can barely contain your "+str(actor.person.vaginal_cum)+ " doses of your seed.\nIt is already oozing out."
                                            else:
                                                $ VTvaginalst = "vaghymen"
                                                $ VTvaginaltt += f"\n{{image=handprint_token_small}}{{image=beezee_token_small}} You marked her fresh"+VTbreedfertile+VTpro+" womb with "+str(actor.person.vaginal_cum)+ " doses of your seed."
                                        else:
                                            if actor.person.vaginal_cum >3:
                                                $ VTvaginalst = "ahegaovag"
                                                $ VTvaginaltt += f"\n{{image=beezee_token_small}} Her pussy can barely contain\n the "+ str(actor.person.vaginal_cum) +" doses of your cum \n swimming \nin her"+VTbreedfertile+VTpro+" womb and is already oozing out."+daysince
                                            else:
                                                $ VTvaginalst = "openvag"
                                                $ VTvaginaltt += f"\n{{image=beezee_token_small}} "+ str(actor.person.vaginal_cum) +" doses of your cum \n swimming in her"+VTbreedfertile+VTpro+" womb."+daysince
                                    if actor.person.arousal_perc >= 59:
                                        $ VTvaginaltt += f"\n{{image=vagclosed_small}} *You can really smell her arousal*"

                        if actor.person.hymen <2 and actor.person.vaginal_cum>0:
                            $ VTvaginalst = "vaghymen"
                        imagebutton:
                            pos(0, 0)
                            idle VTvaginalst
                            action NullAction()
                            tooltip VTvaginaltt
                        $ VTvaginalcum = "bc_cum"
            ### Anal Virgin Flag
                    if getattr(persistent, "knowanal")==1:
                        $ VTanalat = "talking"
                        $ VTanalst = "yespeach"
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
                                                    if actor.person.anal_cum >=1:
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
                                    if actor.person.anal_cum >0:
                                        if actor.person.anal_cum == 1:
                                            if actor.person.arousal_perc >= 59:
                                                $ VTanalst = "handass"
                                                $ VTanaltt = f"{{image=handass_small}} She seems lost in her bliss and panting. \n{{image=handass_small}}She has a dose of your protein in her bowels."
                                            else:
                                                $ VTanalst = "handass"
                                                $ VTanaltt = f"{{image=handass_small}} She looks at you with lust \n in her innocent hungry eyes. \n{{image=ahegaoanal_small}}She has a dose of your protein in her bowels."
                                        else:
                                            if actor.person.anal_cum >3:
                                                if actor.person.arousal_perc >= 59:
                                                    $ VTanalst = "ahegaopeach"
                                                    $ VTanaltt = f"{{image=ahegaoanal_small}} *Hunger in her eyes wants more cum*\n{{image=ahegaoanal_small}} She has "+ str(actor.person.anal_cum) +" doses of your cum \n swimming in her bowels, causing her belly a bit of a bulge."
                                                else:
                                                    $ VTanalst = "ahegaopeach"
                                                    $ VTanaltt = f"{{image=ahegaoanal_small}} "+ str(actor.person.anal_cum) +" doses of your cum \n swimming in the slight bulge of her belly."
                                            else:
                                                if actor.person.arousal_perc >= 59:
                                                    $ VTanalst = "ahegaopeach"
                                                    $ VTanaltt = f"{{image=ahegaoanal_small}} *She hungrily gazes at you for more cum.*\n{{image=ahegaoanal_small}} She has "+ str(actor.person.anal_cum) +" doses of your cum \n swimming in her belly."
                                                else:
                                                    $ VTanalst = "handass"
                                                    $ VTanaltt = f"{{image=ahegaoanal_small}} "+ str(actor.person.anal_cum) +" doses of your cum \n swimming in her belly."
                                    else:
                                        $ VTanalst = "yespeach"
                                        if actor.person.anal_virgin == 0:
                                            $ VTanaltt = f"{{image=virgin_anal_small}} Her ass sways so ripely, ready for the taking!"
                                        else:
                                            if actor.person.anal_first == mc.name:
                                                $ VTanaltt = f"{{image=handprint_token_small}} Her ass sways, hypnotizing you..\nThen she slaps it!"
                                            else:
                                                $ VTanaltt = f"{{image=yesanal_small}} Her ass sways and she spreads her ass for you.\nCome take me!"
                                                if actor.person.anal_virgin >=4:
                                                    $ VTanaltt = f"{{image=yesanal_small}} Her ass sways and she spreads her gaping asshole for you.\nCome take me!"
                                        if actor.person.energy <20 and actor.person.had_sex_today:
                                            $ VTanaltt += f"{{image=handass_small}} She seems lost in her bliss and panting."
                        # if VTanalat=="sexualized":
                            # imagebutton:
                                # pos(0, 0)
                                # idle VTanalst
                                # action NullAction()
                                # tooltip VTanaltt

                        if VTanalat=="talking":
                            $ VTanalst = "yespeach"
                            if actor.person.anal_virgin == 0 and actor.person.anal_cum ==0:
                                $ VTanalst = "virgin_anal"
                                $ VTanaltt = f"{{image=virgin_anal_small}} Her ass sways so ripely, ready for the taking"
                                
                            if actor.person.arousal_perc >= 59:
                                if actor.person.anal_cum ==0:
                                    $ VTanalst = "virgin_anal"
                                    if actor.person.anal_virgin == 0:
                                        $ VTanaltt = f"{{image=virgin_anal_small}} Her ass sways so ripely, ready for the taking!"
                                    else:
                                        $ VTanalst = "yespeach"
                                        if actor.person.anal_first == mc.name:
                                            $ VTanaltt = f"{{image=handprint_token_small}} Her ass sways, hypnotizing you while \nshe rubs it!"
                                        else:
                                            $ VTanaltt = f"{{image=yesanal_small}} Her ass sways and she spreads her ass for you.\nCome take me!"
                                            if actor.person.anal_virgin >=4:
                                                $ VTanaltt = f"{{image=yesanal_small}} Her ass sways and she spreads her gaping asshole for you.\nCome take me!"
                                if actor.person.anal_cum >0:
                                    if actor.person.anal_cum == 1:
                                        $ VTanalst = "handass"
                                        $ VTanaltt += f"\n{{image=ahegaoanal_small}} You painted her bowels with your cum."
                                    else:
                                        $ VTanalst = "ahegaopeach"
                                        $ VTanaltt += f"\n{{image=ahegaoanal_small}} "+ str(actor.person.anal_cum) +" doses of your cum \n coating her bowels."
                            else:
                                $ VTanalst = "yespeach"
                                if actor.person.anal_first == mc.name:
                                    $ VTanalst = "claimedass"
                                    $ VTanaltt = f"{{image=handprint_token_small}} You Claimed this Ass!"
                                else:
                                    if actor.person.anal_first !=None and actor.person.anal_virgin>0:
                                        $ VTanalst = "analclaimed"
                                        $ VTanaltt = f"{{image=analclaimed_small}} Someone else had her ass before you... RECLAIM IT!"
                                if actor.person.anal_cum >0:
                                    $ VTanalst = "bitelip"
                                    if actor.person.anal_cum == 1:
                                        $ VTanalst = "handass"
                                        $ VTanaltt += f"\n{{image=ahegaoanal_small}} You have painted her bowels with your cum."
                                    else:
                                        $ VTanalst = "ahegaopeach"
                                        $ VTanaltt += f"\n{{image=ahegaoanal_small}} "+ str(actor.person.anal_cum) +" doses of your cum \n coating her bowels."

                        imagebutton:
                            pos(0, 0)
                            idle VTanalst
                            action NullAction()
                            tooltip VTanaltt
        ######## Exhibitionist Fetish
                    if getattr(persistent, "knowbody")==1:
                        $ VTexhibitfetishat = "talking"
                        $ VTexhibitfetishst = "bodyconcealed"
                        $ VTexhibitfetishtt = f"{{image=progress_token_small}} She is fully clothed."
                        if actor.person.vagina_available or actor.person.tits_available:
                            $ VTexhibitfetishst = "bodyskimpy"
                            $ VTexhibitfetishtt = f"{{image=progress_token_small}} She is fully clothed."
                            if actor.person.vagina_available and actor.person.tits_available:
                                $ VTexhibitfetishst = "nudebody"
                                $ VTexhibitfetishtt = f"{{image=vtcherries_small}} You can see her tits and pussy."
                                if actor.person.arousal_perc >= 59:
                                    $ VTexhibitfetishtt += f"\n{{image=vtcherries_small}} You can see her aroused nipples and wet hot juicy pussy."
                                if actor.person.vaginal_cum >0:
                                    if actor.person.vaginal_cum >3:
                                        $ VTexhibitfetishtt += f"\n{{image=openvag_small}} You can see your cum oozing from her pussy."
                                    else:
                                        $ VTexhibitfetishtt += f"\n{{image=openvag_small}} You can see your cum starting to drip from her pussy."
                            else:
                                $ VTexhibitfetishtt = f"{{image=vtcherries_small}} She is partly clothed."
                                if actor.person.tits_available:
                                    $ VTexhibitfetishst = "bodypanties"
                                    $ VTexhibitfetishtt += f"\n{{image=vtcherries_small}} You can see her tits."
                                if actor.person.vagina_available:
                                    $ VTexhibitfetishst = "bodybra"
                                    if actor.person.arousal_perc >= 59:
                                        $ VTexhibitfetishtt += f"\n{{image=spreadvag_small}} You can see her wet hot juicy pussy."
                                    else:
                                        $ VTexhibitfetishtt += f"\n{{image=spreadvag_small}} You can see her pussy."
                                    if actor.person.vaginal_cum >0:
                                        if actor.person.vaginal_cum >3:
                                            $ VTexhibitfetishtt += f"\n{{image=openvag_small}} You can see your cum oozing from her pussy."
                                        else:
                                            $ VTexhibitfetishtt += f"\n{{image=openvag_small}} You can see your cum starting to drip from her pussy."
                        else:
                            $ VTexhibitfetishst = "bodyconcealed"
                            $ VTexhibitfetishtt = f"{{image=progress_token_small}} She is fully clothed."

                        imagebutton:
                            pos(0, 0)
                            idle VTexhibitfetishst
                            action NullAction()
                            tooltip VTexhibitfetishtt

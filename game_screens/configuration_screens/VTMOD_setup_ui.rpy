
init 2 python:
    def change_VTMOD_setup_requirement():
        return True

    change_VTMOD_setup_action = Action("VT-Mod Settings", change_VTMOD_setup_requirement, "show_VTMOD_setup_ui", menu_tooltip = "Change VT-Mod Settings, mon cherie!")

init 5 python:
    add_label_hijack("normal_start", "activate_VTMOD_setup_preference")
    add_label_hijack("after_load", "activate_VTMOD_setup_preference")

label activate_VTMOD_setup_preference(stack):
    python:
        bedroom.add_action(change_VTMOD_setup_action)
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_VTMOD_setup_ui():
    $ renpy.call_screen("VTMOD_setup_ui")
    return

init 10 python:
    global vtracker
    global vtpref
    global vtpref_opt

    def vt_switch_preference(pref):
        cs = renpy.current_screen()
        cs.scope["pref_selected"] = pref
        vt_preference_value_changed(pref)
        return

    def vt_preference_value_changed(pref):
        cs = renpy.current_screen()

        total = 0
        for x in VT_Settings[pref]:
            total += getattr(persistent, VT_Settings[pref][x][0])

        cs.scope["current_total"] = total
        return

screen VTMOD_setup_ui():

    add Cherry_background_image
    modal True
    zorder 49

    default pref_selected = "Population"
    default current_total = 100

    frame: # top frame
        background "#4B0303"
        xsize 1200
        ysize 600
        yalign 0.4
        xalign 0.5
        xanchor 0.5

        vbox:
            xanchor 0.5
            xalign 0.5
            yalign 0.3
            spacing 10

            hbox:
                for pref in sorted(VT_Settings):
                    textbutton pref:
                        style "VTtextbutton_style"
                        text_style "menu_text_title_style"
                        xsize 220
                        sensitive pref != pref_selected
                        action [
                            Function(vt_switch_preference, pref)
                        ]
            viewport id "vtvp":
                mousewheel True
                scrollbars "vertical"
                for pref in sorted(VT_Settings):
                    if pref == pref_selected:
                        vbox:
                            for pref_opt in (x[0] for x in sorted(VT_Settings[pref].items(), key = lambda x: x[1][2])):
                                if pref_selected in ["Population", "Virgin Stats"]:
                                    if not pref_opt in ["Teen","Teen - Oral", "Teen - Anal", "Teen - Vaginal","Preteen","Preteen - Oral", "Preteen - Anal", "Preteen - Vaginal"]:
                                        hbox:
                                            spacing 5
                                            vbox:
                                                xsize 300
                                                ysize 50
                                                yoffset 5
                                                text pref_opt style "VTvirgins_text_style" xalign 1.0
                                            vbox:
                                                xsize 600
                                                ysize 50
                                                bar value FieldValue(persistent, VT_Settings[pref][pref_opt][0], 100, step = 1, style = "slider", action = [ Function(vt_preference_value_changed, pref_selected) ]) xsize 600 ysize 45
                                            
                                            vbox:
                                                xsize 60
                                                ysize 50
                                                yoffset 5
                                                text (str(getattr(persistent, VT_Settings[pref][pref_opt][0])) + "%" if getattr(persistent, VT_Settings[pref][pref_opt][0]) > 0 else "None") style "VTmenu_text_style" xsize 100
                                else:
                                    if pref_selected == "Trackers":
                                        $ VTSettingsicon = f"{{image="+str(VT_Settings[pref][pref_opt][0])+"}"
                                        hbox:
                                            spacing 5
                                            vbox:
                                                xsize 50
                                                ysize 50
                                                imagebutton:
                                                    if getattr(persistent, str(VT_Settings[pref][pref_opt][0]))==1:
                                                        idle "gui/extra_images/check_mark.png"
                                                    else:
                                                        idle "gui/extra_images/uncheck_mark.png"
                                                    background ("#449044" if getattr(persistent, str(VT_Settings[pref][pref_opt][0]))==1 else "#904444" )
                                                    hover_background ("#66a066" if getattr(persistent, str(VT_Settings[pref][pref_opt][0]))==1 else "#a06666")
                                                    sensitive True
                                                    action  [ToggleField(persistent, str(VT_Settings[pref][pref_opt][0]), 1, 0)]
                                                    xysize (50, 40)
                                                    padding (9, 4)
                                                    yanchor 0.5 yalign 0.5
                                            vbox:
                                                xsize 50
                                                ysize 50
                                                text VTSettingsicon style "VTtextbutton_icon_style"
                                            vbox:
                                                xsize 300
                                                ysize 50
                                                yoffset 5
                                                text pref_opt style "VTtextbutton_text_style"
                                    else:
                                        hbox:
                                            spacing 5
                                            vbox:
                                                xsize 300
                                                ysize 50
                                                yoffset 5
                                                text pref_opt style "VTtextbutton_text_style"
                                            vbox:
                                                xsize 50
                                                ysize 50
                                                text (str(VT_Settings[pref][pref_opt][1])) style "VTtextbutton_text_style"
            vbar value YScrollValue("vtvp")

            if pref_selected in ["Population"]:
                hbox:
                    text f"Total: {current_total}%":
                        xalign 1.0
                        style "VTmenu_text_style"
            hbox:
                xsize 800
                text "{size=22}You may adjust these anytime." style "warning_text"
            hbox:
                xalign 0.5
                textbutton "Close" action [Return()] style "VTtextbutton_style" text_style "menu_text_title_style" text_text_align 0.5 text_xalign 0.5 xysize (155,60)

style warning_text:
    color "#FFFFFF"
    size 16
    outlines [(2,"#222222",0,0)]
    xalign 0.5

style VTtextbutton_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    padding (5,5)
    margin (2,2)
    background "#792323"
    insensitive_background "#00000088"
    hover_background "#237979"

style VTtextbuttonOFF_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    padding (5,5)
    margin (2,2)
    background "#792323"
    insensitive_background "#00000088"
    hover_background "#237979"

style VTtextbuttonON_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    padding (5,5)
    margin (2,2)
    background "#237979"
    insensitive_background "#00000088"
    hover_background "#792323"

style VTtextbutton_icon_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    size 32
    italic False
    bold False
    color "#A35469"
    outlines [(2,"#222222",0,0)]
    text_align 0.5
    yoffset 2

style VTvirgins_text_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    size 22
    italic False
    bold False
    color "#ffffff"
    outlines [(2,"#222222",0,0)]
    text_align 1.0
    yoffset 2

style VTtextbutton_text_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    size 22
    italic False
    bold False
    color "#ffffff"
    outlines [(2,"#222222",0,0)]
    text_align 0.5
    yoffset 2

style VTmenu_text_style:
    size 24
    italic False
    bold False
    color "#FFFFFF"
    outlines [(2,"#222222",0,0)]
    text_align 0.0
    line_spacing 2

style VTcheckbox_button:
    xysize (50, 50)
    background Solid("#ffff00") # Unchecked
    hover_background Solid("#ffffff") # Unchecked Hovered (I usually increase brightness of the image by 15% unsing im. matrix manipulators)
    insensitive_background Solid("#d3d3d3") # Disabled (May not be required, I usually use im.Sepia() for images)
    selected_idle_background Solid("#00ff00") # Checked
    selected_hover_background Solid("#00ff11") # Checked Hovered
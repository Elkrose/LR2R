
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

            for pref in sorted(VT_Settings):
                if pref == pref_selected:
                    vbox:
                        for pref_opt in (x[0] for x in sorted(VT_Settings[pref].items(), key = lambda x: x[1][2])):
                            hbox:
                                spacing 5
                                vbox:
                                    xsize 340
                                    ysize 50
                                    yoffset 5
                                    text pref_opt style "VTtextbutton_text_style"
                                vbox:
                                    xsize 600
                                    ysize 50
                                    bar value FieldValue(persistent, VT_Settings[pref][pref_opt][0], 100, step = 1, style = "slider", action = [ Function(vt_preference_value_changed, pref_selected) ]) xsize 600 ysize 45
                                vbox:
                                    xsize 60
                                    ysize 50
                                    yoffset 5
                                    text (str(getattr(persistent, VT_Settings[pref][pref_opt][0])) + "%" if getattr(persistent, VT_Settings[pref][pref_opt][0]) > 0 else "None") style "VTmenu_text_style" xsize 100

            hbox:
                text f"Total: {current_total}%":
                    xalign 1.0
                    style "VTmenu_text_style"

            hbox:
                xsize 800
                text "{size=16}Warning: PROOF OF CONCEPT ONLY!!!! CURRENTLY NOT SET FOR VT at the moment, but will get there! :P" style "warning_text"

            hbox:
                xalign 0.5
                textbutton "Close" action [Return()] style "VTtextbutton_style" text_style "menu_text_title_style" text_text_align 0.5 text_xalign 0.5 xysize (155,60)

style warning_text:
    color "#FFFFFF"
    size 16
    xalign 0.5

style VTtextbutton_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    padding (5,5)
    margin (2,2)
    background "#792323"
    insensitive_background "#00000088"
    hover_background "#237979"

style VTtextbutton_text_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    size 22
    italic False
    bold False
    color "#A35469"
    outlines [(2,"#222222",0,0)]
    text_align 0.5
    yoffset 2

style VTmenu_text_style:
    size 18
    italic False
    bold False
    color "#FFFFFF"
    outlines [(2,"#222222",0,0)]
    text_align 0.0
    line_spacing 2

screen cum_screen():
    zorder 300
    frame at cum_effect():
        background "/VTgui/images/background_images/BorderPulse.png"

        xsize 2304
        ysize 1296

        xanchor 0.5
        yanchor 0.5
        xalign 0.5
        yalign 0.5

    timer 0.6 action Show("flash_screen", None, 0.65)
    timer 0.7 action Hide("cum_screen")
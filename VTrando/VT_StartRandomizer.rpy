screen VT_quick_menu_overlay():
    zorder 10000  # increase the z-order to make sure it's on top
    vbox:
        align(1.0, 0.0)
        imagebutton:
            pos (0.8, 0.1) anchor (1.0, 0.0)
            idle cherries01_idle_small_image
            hover cherries01_hover_small_image
            action ToggleScreen("VTMOD_setup_ui")

init python:
    def start_mod():
        renpy.jump("start_mod_label")
    renpy.config.start_callbacks.append(start_mod)

label start_mod_label:
    show screen VT_quick_menu_overlay zorder 10000
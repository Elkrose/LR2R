
label hug_person(the_person):
    python:
        day_part = time_of_day_string(time_of_day)
        if day_part == "early morning":
            day_part = "morning"
        name = renpy.random.choice([the_person.title, the_person.fname])
        renpy.say(mc.name, renpy.random.choice([
            "Catch you later [name].",
            "See you later [name]!",
            "Good [day_part] [name], don't be a stranger!",
            "Good [day_part] [name], have a good one!",
            "Take it easy [name]."
        ]))
    $ mc.change_energy(-5)
    $ kissing.redraw_scene(the_person)
    if the_person.has_relation_with_mc:
        if the_person.love <=40:
            "You pull [the_person.title] towards you and give her a nice hug"
            $ the_person.change_stats(happiness = 2, love = 1, max_love = 40, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
        elif the_person.love <=60:
            "You pull [the_person.title] towards you and give her a nice long hug"
            the_person "MMmm, yes I will miss you too!"
            $ the_person.change_stats(happiness = 2, arousal = 1 + (1 if mc_serum_aura_arousal.is_active else 0), love = 1, max_love = 60, obedience = 0 + (1 if mc_serum_aura_obedience.is_active else 0))
        elif the_person.love <=80:
            "You slide your arms around [the_person.title], and pull her into a nice long hug"
            the_person "MMmm, yes I will see you soon!"
            $ the_person.change_stats(happiness = 2, arousal = 2 + (1 if mc_serum_aura_arousal.is_active else 0), love = 2, max_love = 80, obedience = 0 + (1 if mc_serum_aura_obedience.is_active else 0))
        else:
            "You slide your arms around her waist and pull [the_person.title] towards you, giving her a nice long hug, while running your hands lovingly up her back."
            the_person "MMmm, yes I can't wait to see you again!"
            $ the_person.change_stats(happiness = 2, arousal = 5 + (1 if mc_serum_aura_arousal.is_active else 0), love = 3, max_love = 100, obedience = 0 + (1 if mc_serum_aura_obedience.is_active else 0))
    else:
        the_person "MMmm, bye [the_person.mc_title]!"
        $ the_person.change_stats(happiness = 2, love = 1, max_love = 30, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
    if the_person._follow_mc == True:
        $ shedule_destination = ""
        if the_person.get_destination() is the_person.home:
           $ schedule_destination = "my room"
        elif the_person.get_destination():
           $ schedule_destination = f"the {the_person.get_destination().formal_name}"
        else:
           $ schedule_destination = "somewhere else"
            
        $ the_person.follow_mc = False
        $ the_person.draw_person(position = "walking_away")
        the_person.title "Okay [the_person.mc_title], I'll head over to [schedule_destination]."
        "You tilt your head to watch her walk away."
        $ the_person.run_move()
    $ clear_scene()
    $ keep_talking = False
    return 

label kiss_person(the_person):
    python:
        day_part = time_of_day_string(time_of_day)
        name = renpy.random.choice([the_person.title, the_person.fname])
        if day_part == "early morning":
            day_part = "morning"
        renpy.say(mc.name, renpy.random.choice([
            "Mmmm [name], can't wait till next time.",
            "See you later [name]!",
            "Good [day_part] [name], keep those lips moist for me!",
            "Good [day_part] [name], till our lips meet again!",
            "See you soon, [name]."
        ]))
    $ mc.change_energy(-5)
    $ the_person.draw_person(position="kissing", emotion="happy")
    if the_person.has_relation_with_mc:
        if the_person.love <=40:
            "You step up to [the_person.title] and give her a nice sweet kiss."
            $ the_person.change_stats(happiness = 2, arousal = 1 + (1 if mc_serum_aura_arousal.is_active else 0), love = 1, max_love = 40, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
        elif the_person.love <=60:
            "You pull [the_person.title] towards you and give her a nice long kiss."
            the_person "MMmm, yes I will miss you too!"
            $ the_person.change_stats(happiness = 2, arousal = 1 + (1 if mc_serum_aura_arousal.is_active else 0), love = 1, max_love = 60, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
        elif the_person.love <=80:
            "You step up to [the_person.title] and give her a nice long kiss which lingers."
            the_person "MMmm, yes I will see you soon!"
            $ the_person.change_stats(happiness = 2, arousal = 2 + (1 if mc_serum_aura_arousal.is_active else 0), love = 2, max_love = 80, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
        else:
            "You slide your arms around [the_person.title], pulling her into a deep long kiss which lingers."
            the_person "MMmm, yes I can't wait to see you again!"
            $ the_person.change_stats(happiness = 2, arousal = 5 + (1 if mc_serum_aura_arousal.is_active else 0), love = 3, max_love = 100, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
    else:
        the_person "Mmmmmhmmm, bye [the_person.title]!"
        $ the_person.change_stats(happiness = 2, love = 1, max_love = 30, obedience = 1 if mc_serum_aura_obedience.is_active else 0)

    if the_person._follow_mc == True:
        $ shedule_destination = ""
        if the_person.get_destination() is the_person.home:
           $ schedule_destination = "my room"
        elif the_person.get_destination():
           $ schedule_destination = f"the {the_person.get_destination().formal_name}"
        else:
           $ schedule_destination = "somewhere else"
            
        $ the_person.follow_mc = False
        $ the_person.draw_person(position = "walking_away")
        the_person.title "Okay [the_person.mc_title], I'll head over to [schedule_destination]."
        "You tilt your head to watch her walk away."
        $ the_person.run_move()
    $ clear_scene()
    $ keep_talking = False
    return

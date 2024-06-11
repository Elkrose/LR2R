from __future__ import annotations
import builtins
from game.general_actions.interaction_actions.command_descriptions_definition_ren import demand_strip_naked_requirement, demand_strip_tits_requirement, demand_strip_underwear_requirement
from game.helper_functions.heart_formatting_functions_ren import get_gold_heart
from game.helper_functions.list_functions_ren import get_random_from_list
from game.business_policies.serum_policies_ren import mandatory_unpaid_serum_testing_policy, mandatory_paid_serum_testing_policy
from game.game_roles._role_definitions_ren import onlyfans_role
from game.game_roles.stripclub._stripclub_role_definitions_ren import get_strip_club_foreclosed_stage
from game.game_roles.relationship_role_definition_ren import ask_girlfriend_requirement, evening_date_trigger
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.ActionList_ren import ActionList
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import strip_club, bdsm_room
from renpy import persistent
import renpy

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

opinions_talk_mapping = {
    "skirts": "girls in skirts",
    "pants": "girls wearing pants",
    "dresses": "girls in a dress",
    "high heels": "girls in high heels",
    "boots": "girls wearing boots",
    "sports": "working out",
    "hiking": "going hiking",
    "jazz": "jazz music",
    "make up": "girls who wear makeup",
    "getting head": "licking pussy",
    "giving blowjobs": "getting blowjobs",
    "giving handjobs": "getting handjobs",
    "giving tit fucks": "fucking tits",
    "being fingered": "fingering a girl",
    "showing her tits": "looking at tits",
    "showing her ass": "looking at butts",
    "being submissive": "submissive girls",
    "taking control": "dominant women",
    "drinking cum": "cumming in mouths",
    "cum facials": "cumming on faces",
    "being covered in cum": "covering girls in cum",
    "big dicks": "girls who love big cocks",
    "cheating on men": "having affairs",
}
text_opinion_list = ["I hate", "I don't like", "I have no opinion on", "I like", "I love"]

def always_true_requirement():
    return True

def small_talk_requirement(person: Person):
    if person.event_triggers_dict.get("chatted", 0) <= 0:
        return "Enough small talk"
    if mc.energy < 15:
        return "Requires: {energy=15}"
    return True

def compliment_requirement(person: Person):
    if person.event_triggers_dict.get("complimented", 0) <= 0:
        return "Enough compliments"
    if person.love < 10:
        return "Requires: 10 Love"
    if mc.energy < 15:
        return "Requires: {energy=15}"
    return True

def flirt_requirement(person: Person):
    if person.event_triggers_dict.get("flirted", 0) <= 0:
        return "Enough flirting"
    if person.love < 10:
        return "Requires: 10 Love"
    if mc.energy < 15:
        return "Requires: {energy=15}"
    return True

def date_option_requirement(person: Person):
    if person.love < 20:
        return "Requires: 20 Love"
    return True

def lunch_date_requirement(person: Person):
    love_requirement = 20

    if time_of_day < 2:
        return "Too early to go for lunch"
    if time_of_day > 2:
        return "Too late to go for lunch"
    if person.love < love_requirement:
        return f"Requires: {love_requirement} Love"
    return True

def movie_date_requirement(person: Person):
    if mc.business.event_triggers_dict.get("movie_date_scheduled", False):
        return "Already planned movie date!"
    if day % 7 == 1 and time_of_day >= 3:
        return "Too late to plan movie date"

    love_requirement = 30
    if person.relationship == "Girlfriend":
        love_requirement += 10
    elif person.relationship == "Fiancée":
        love_requirement += 15
    elif person.relationship == "Married":
        love_requirement += 20
    if person.has_significant_other:
        love_requirement += -10 * person.opinion.cheating_on_men
    if love_requirement < 30:
        love_requirement = 30

    if person.love < love_requirement:
        return f"Requires: {love_requirement} Love"
    return True

def dinner_date_requirement(person: Person):
    if mc.business.event_triggers_dict.get("dinner_date_scheduled", False):
        return "Already planned dinner date!"
    if day % 7 == 4 and time_of_day >= 3:
        return "Too late to plan dinner date"

    love_requirement = 40
    if person.relationship == "Girlfriend":
        love_requirement += 20
    elif person.relationship == "Fiancée":
        love_requirement += 30
    elif person.relationship == "Married":
        love_requirement += 40
    if person.has_significant_other:
        love_requirement += -10 * person.opinion.cheating_on_men
    if love_requirement < 40:
        love_requirement = 40

    if person.love < love_requirement:
        return f"Requires: {love_requirement} Love"
    return True

def serum_give_requirement(person: Person):
    if not mc.inventory.has_serum:
        return "Requires: Serum in inventory"
    return True

def hug_requirement(person: Person):
    love_requirement = 10
    if person.sluttiness < 5:
        return False #Don't show the option at all at minimal sluttiness.
    if mc.energy < 5:
        return "Requires: {energy=5}"
    if person.love < love_requirement:
        return f"Requires: {love_requirement} Love"
    return True

def kiss_requirement(person: Person):
    love_requirement = 30
    if person.has_relation_with_mc == False :
        return False  #Don't show if not a girlfriend
    if person.sluttiness < 5:
        return False #Don't show the option at all at minimal sluttiness.
    if mc.energy < 5:
        return "Requires: {energy=5}"
    if person.love < love_requirement:
        return f"Requires: {love_requirement} Love"
    return True

def grope_requirement(person: Person):
    if person.sluttiness < 5:
        return False #Don't show the option at all at minimal sluttiness.
    if person.event_triggers_dict.get("last_groped", (-1, -1)) == (day, time_of_day):
        return "Just groped her"
    if mc.energy < 20:
        return "Requires: {energy=20}"
    return True

def command_requirement(person: Person):
    if person.obedience < 105:
        return "Requires: 105 Obedience"
    if mc.energy < 20:
        return "Requires: {energy=20}"
    return True

def change_titles_requirement(person: Person):
    if person.obedience < 105:
        return "Requires: 105 Obedience"
    return True

def serum_demand_requirement(person: Person):
    if person.is_employee:
        #It's easier to convince her if she works for you
        if person.obedience < 110:
            return "Requires: 110 Obedience"
        if not mc.inventory.has_serum:
            return "Requires: Serum in inventory"
        return True

    if person.obedience < 120:
        return "Requires: 120 Obedience"
    if not mc.inventory.has_serum:
        return "Requires: Serum in inventory"
    return True

def wardrobe_change_requirement(person: Person):
    if person.obedience < 120:
        return "Requires: 120 Obedience"
    return True

def bc_talk_requirement(person: Person):
    if persistent.pregnancy_pref == 0 or person.is_infertile:
        return False
    if person.effective_sluttiness() < 20 and person.love < 20:
        return False
    if person.knows_pregnant:
        return False
    return True

def demand_touch_requirement(person: Person):
    if mc.energy <= 10:
        return "Requires: {energy=10}"
    if person.obedience < 125:
        return "Requires: 125 Obedience"
    return True

def make_onlyfans_together_requirement(person: Person):
    if not person.has_role(onlyfans_role):
        return False
    if not person.is_employee and not person.is_home:
        return "Only at her place"
    if person.is_employee and not (person.is_at_work or person.is_home):
        return "Only at work or her place"
    if time_of_day == 4:
        return "Not enough time"
    if person.obedience < 150:
        return "Requires: 150 Obedience"
    return True

def suck_demand_requirement(person: Person):
    if person.has_taboo("sucking_cock"):
        return False #Doesn't appear until you've broken the taboo in the first place
    elif person.obedience < 150:
        return "Requires: 150 Obedience"
    return True

def bend_over_your_desk_requirement(person: Person):
    if not (person.is_employee and person.is_at_office):
        return False
    if person.is_at_stripclub:  # don't show when moonlighting in stripclub
        return False
    if mc.business.event_triggers_dict.get("employee_over_desk_unlock", False):
        if person.obedience < 130:
            return "Requires: 130 Obedience"
        else:
            return True
    return False

def demand_strip_requirement(person: Person):
    if not (demand_panties_requirement(person) # If there's nothing to strip, don't show action
            or demand_strip_tits_requirement(person)
            or demand_strip_underwear_requirement(person)
            or demand_strip_naked_requirement(person)):
        return False
    if person.obedience < 110:
        return "Requires: 110 Obedience"
    return True

def demand_panties_requirement(person: Person):
    if person.vagina_visible and not person.wearing_panties:
        return False
    if not (person.obedience >= 120 or person.effective_sluttiness() >= 30 or person.love >= 30):
        return "Requires: 120 Obedience\nor 30 Sluttiness or 30 Love"
    return True

def demand_bc_requirement(person: Person):
    if persistent.pregnancy_pref == 0:
        return False
    if person.obedience < 100 or person.is_infertile:
        return False
    if person.knows_pregnant:
        return False
    if person.obedience < 115:
        return "Requires: 115 Obedience"
    return True

#Chat actions shown with all girls. Add to these lists to have options displayed when talking to someone.
#Default actions that are displayed when you are talking to a girl. Remember to set is_fast = False if an event can advance time.
chat_actions = ActionList([
    Action("Make small talk  {energy=-15}", requirement = small_talk_requirement, effect = "small_talk_person",
        menu_tooltip = "A pleasant chat about your likes and dislikes. A good way to get to know someone and the first step to building a lasting relationship. Provides a chance to study the effects of active serum traits and raise their mastery level."),
    Action("Compliment her  {energy=-15}", requirement = compliment_requirement, effect = "compliment_person",
        menu_tooltip = "Lay the charm on thick and heavy. A great way to build a relationship, and every girl is happy to receive a compliment! Provides a chance to study the effects of active serum traits and raise their mastery level."),
    Action("Flirt with her  {energy=-15}", requirement = flirt_requirement, effect = "flirt_person",
        menu_tooltip = "A conversation filled with innuendo and double entendre. Both improves your relationship with a girl and helps make her a little bit sluttier. Provides a chance to study the effects of active serum traits and raise their mastery level."),
    Action("Ask her to be your girlfriend", requirement = ask_girlfriend_requirement, effect = "ask_be_girlfriend_label",
        menu_tooltip = "Ask her to start an official, steady relationship and be your girlfriend.",
        priority = 10),
    Action("Talk about her birth control", requirement = bc_talk_requirement, effect = "bc_talk_label",
        menu_tooltip = "Talk to her about her use of birth control. Ask her to start or stop taking it, or just check what she's currently doing."),
    Action("Ask her on a date", requirement = date_option_requirement, effect = "date_person",
        menu_tooltip = "Ask her out on a date. The more you impress her the closer you'll grow. If you play your cards right you might end up back at her place.",
        is_fast = False),
])

#Default "aggressive" actions that are displayed when talking to a girl.
specific_actions = ActionList([
    Action("Hug goodbye  {energy=-5}", requirement = hug_requirement, effect = "hug_person",
    menu_tooltip = "Be \"friendly\"! A good hug goes a long way."),
    Action("Kiss goodbye  {energy=-5}", requirement = kiss_requirement, effect = "kiss_person",
    menu_tooltip = "Give your sweet gal some loving."),
    Action("Grope her  {energy=-5}", requirement = grope_requirement, effect = "grope_person",
        menu_tooltip = 'Be "friendly" and see how far she is willing to let you take things. May make her more comfortable with physical contact, but at the cost of her opinion of you.'),
    Action("Give her a command", requirement = command_requirement, effect = "command_person",
        menu_tooltip = "Leverage her obedience and command her to do something."),
])
command_actions = ActionList([
    Action("Change how we refer to each other", requirement = change_titles_requirement, effect = "change_titles_person",
        menu_tooltip = "Manage how you refer to her and tell her how she should refer to you. Different combinations of stats, roles, and personalities unlock different titles."),
    Action("Change your wardrobe", requirement = wardrobe_change_requirement, effect = "wardrobe_change_label",
        menu_tooltip = "Add and remove outfits from her wardrobe, or ask her to put on a specific outfit."),
    Action("Drink a dose of serum for me", requirement = serum_demand_requirement, effect = "serum_demand_label",
        menu_tooltip = "Demand she drinks a dose of serum right now. Easier to command employees to test serum."),
    Action("Strip for me", requirement = demand_strip_requirement, effect = "demand_strip_label",
        menu_tooltip = "Command her to strip off some of her clothing."),
    Action("Let me touch you   {energy=-10}", requirement = demand_touch_requirement, effect = "demand_touch_label",
        menu_tooltip = "Demand she stays still and lets you touch her. Going too far may damage your relationship."),
    Action("Suck my cock", requirement = suck_demand_requirement, effect = "suck_demand_label",
        menu_tooltip = "Demand she get onto her knees and worship your cock."),
    Action("Talk about birth control", requirement = demand_bc_requirement, effect = "bc_demand_label",
        menu_tooltip = "Discuss her use of birth control."),
    Action("Make an OnlyFans video together", requirement = make_onlyfans_together_requirement, effect = "make_onlyfans_together_label",
        menu_tooltip = "Order her to make a OnlyFans video together with you."),
    Action("Bend her over her desk", requirement = bend_over_your_desk_requirement, effect = "bend_over_your_desk_label",
        menu_tooltip = "Order her to bend over her desk so you can enjoy her ass."),
])

def sort_display_list(the_item): #Function to use when sorting lists of actions (and potentially people or strings)
    extra_args = None
    if isinstance(the_item, list): #If it's a list it's actually an item of some sort with extra args. Break those out and continue.
        extra_args = the_item[1]
        the_item = the_item[0]

    if isinstance(the_item, Action):
        if the_item.is_action_enabled(extra_args):
            return the_item.priority
        return the_item.priority - 1000 #Apply a ranking penalty to disabled items. They will appear in priority order but below enabled events (Unless something has a massive priority).

    if isinstance(the_item, Person):
        return the_item.sluttiness #Order people by sluttiness? Love? Something else?
    return 0

def build_chat_action_list(person: Person, keep_talking = True):
    chat_list = []
    for act in chat_actions:
        if keep_talking or act.is_fast:
            chat_list.append((act, person))

    chat_list.sort(key = sort_display_list, reverse = True)
    chat_list.insert(0, "Chat with her")
    return chat_list

def build_specific_action_list(person: Person, keep_talking = True):
    specific_actions_list = ["Say goodbye"]
    for act in specific_actions:
        if keep_talking or act.is_fast:
            specific_actions_list.append((act, person))

    specific_actions_list.sort(key = sort_display_list, reverse = True)
    specific_actions_list.insert(0, "Do something specific")
    return specific_actions_list

def build_special_role_actions_list(person: Person, keep_talking = True):
    special_role_actions = []
    # add non-job actions
    for role in (x for x in person.special_role if x not in person.job_roles):
        for act in role.actions:
            if keep_talking or act.is_fast:
                special_role_actions.append((act, person))

    # add job actions
    for act in person.current_job_actions:
        if keep_talking or act.is_fast:
            special_role_actions.append((act, person))

    # add duty actions
    for act in person.current_duty_actions:
        if keep_talking or act.is_fast:
            special_role_actions.append((act, person))

    for act in mc.main_character_actions: #The main character has a "role" that lets us add special actions as well.
        if keep_talking or act.is_fast:
            special_role_actions.append((act, person))

    special_role_actions.sort(key = sort_display_list, reverse = True)
    special_role_actions.insert(0, "Special Actions")
    return special_role_actions

def build_command_action_list(person, keep_talking = True):
    command_actions_list = ["Never mind"]
    for act in command_actions:
        if keep_talking or act.is_fast:
            command_actions_list.append((act, person))
    command_actions_list.sort(key = sort_display_list, reverse = True)
    command_actions_list.insert(0, "Command Her")
    return command_actions_list

def build_person_introduction_titles(person: Person):
    title_tuple = []
    for title in person.get_player_titles():
        title_tuple.append((title, title))
    return title_tuple

def get_date_plan_actions(person: Person):
    lunch_date_action = Action("Ask her out to lunch {image=gui/heart/Time_Advance.png}", lunch_date_requirement, "lunch_date_plan_label",
        menu_tooltip = "Take her out on casual date out to lunch. Gives you the opportunity to impress her and further improve your relationship.")
    movie_date_action = Action("Ask her out to the movies", movie_date_requirement, "movie_date_plan_label",
        menu_tooltip = "Plan a more serious date to the movies. Another step to improving your relationship, and who knows what you might get up to in the dark!")
    dinner_date_action = Action("Ask her out to a romantic dinner", dinner_date_requirement, "dinner_date_plan_label",
        menu_tooltip = "Plan a romantic, expensive dinner with her. Impress her and you might find yourself in a more intimate setting.")

    date_list = [[lunch_date_action, person], [movie_date_action, person], [dinner_date_action, person]]
    for a_role in person.special_role:
        for a_date in a_role.role_dates:
            date_list.append((a_date, person))

    date_list.insert(0, "Select Date")
    date_list.append(("Never mind", None))
    return date_list

def create_movie_date_action(person: Person):
    mc.business.add_mandatory_crisis(
        Action("Movie date", evening_date_trigger, "movie_date_label", args=person, requirement_args=1)
    )
    mc.business.event_triggers_dict["movie_date_scheduled"] = True

def create_dinner_date_action(person: Person):
    mc.business.add_mandatory_crisis(
        Action("Dinner date", evening_date_trigger, "dinner_date_label", args=person, requirement_args=4)
    )
    mc.business.event_triggers_dict["dinner_date_scheduled"] = True

def new_title_menu(person: Person):
    title_tuple = []
    title_choice = None
    for title in person.get_titles():
        title_tuple.append((title, title))
    title_tuple.append(("Do not change her title", "Back"))
    title_choice = renpy.display_menu(title_tuple, True, "Choice")
    return title_choice

def new_mc_title_menu(person: Person):
    title_tuple = []
    title_choice = None
    for title in person.get_player_titles():
        title_tuple.append((title, title))
    title_tuple.append(("Do not change your title", "Back"))
    title_choice = renpy.display_menu(title_tuple, True, "Choice")
    return title_choice

def new_possessive_title_menu(person: Person):
    title_tuple = []
    title_choice = None
    for title in person.get_possessive_titles():
        title_tuple.append((title, title))
    title_tuple.append(("Do not change your title", "Back"))
    title_choice = renpy.display_menu(title_tuple, True, "Choice")
    return title_choice

def get_two_titles_for_person(title_func):
    title_one = get_random_from_list(title_func())
    title_two = get_random_from_list(list(set(title_func()) - {title_one}))
    if title_two is None:
        title_two = title_one
    return (title_one, title_two)

def build_opinion_smalltalk_list(opinion_text, opinion_score):
    opinion_list = []
    for menu_score in builtins.range(5):
        opinion_string = f"{text_opinion_list[4 - menu_score]} {opinion_text}"
        if opinion_score[1] and opinion_score[0] == 2 - menu_score:
            opinion_string = f"{{color=#00E000}}{opinion_string}{{/color}}"
        opinion_list.append((opinion_string, 2 - menu_score))
    opinion_list.insert(0, "Smalltalk")
    return opinion_list

def get_learned_opinion(person: Person):
    # remove randomness for dark chocolate opinion
    if person.opinion("dark chocolate") != person.known_opinion("dark chocolate"):
        opinion_learned = "dark chocolate"
    else:
        opinion_learned = person.get_random_opinion(include_known = True, include_sexy = person.effective_sluttiness() > 50)
        retries = 0
        while opinion_learned == person.event_triggers_dict.get("last_opinion_learned", "unknown") and retries < 3:
            opinion_learned = person.get_random_opinion(include_known = True, include_sexy = person.effective_sluttiness() > 50)
            retries += 1

    talk_opinion_text = opinion_learned
    if opinion_learned in opinions_talk_mapping:
        talk_opinion_text = opinions_talk_mapping[opinion_learned]

    return (opinion_learned, talk_opinion_text)

def serum_give_calculate_chances(person: Person):
    sneak_serum_chance = 70 + (mc.int * 5) - (person.focus * 5)  #% chance that you will successfully give serum to someone sneakily. Less focused people are easier to fool.
    ask_serum_chance = 10 * mc.charisma + 5 * person.int #The more charismatic you are and the more intellectually curious they are the better the chance of success
    demand_serum_chance = mc.charisma * (person.obedience - 90) #The more charismatic you are and the more obedient they are the more likely this is to succeed.

    sneak_serum_chance = 0 if sneak_serum_chance < 0 else 100 if sneak_serum_chance > 100 else sneak_serum_chance
    ask_serum_chance = 0 if ask_serum_chance < 0 else 100 if ask_serum_chance > 100 else ask_serum_chance

    if person.is_employee or (mc.owns_strip_club and person.is_strip_club_employee):
        demand_serum_chance -= 35 #if she doesn't work for you there is a much lower chance she will listen to your demand (unless you are very charismatic or she is highly obedient.)

    demand_serum_chance = 0 if demand_serum_chance < 0 else 100 if demand_serum_chance > 100 else demand_serum_chance

    pay_serum_cost = sum(x.salary for x in person.jobs) * 5
    return [sneak_serum_chance, ask_serum_chance, demand_serum_chance, pay_serum_cost]

def serum_give_chance_color_wrapper(chance):
    color = "#D00000"
    if chance > 80:
        color = "#00D000"
    elif chance > 50:
        color = "#D0D000"

    return f"\n{{size=12}}{{color={color}}}{chance:.0f}% Success Chance{{/color}}{{/size}}"

def serum_give_build_menu_options(person, chances):
    option_list = []
    option_list.append(("Give it to her stealthily" + serum_give_chance_color_wrapper(chances[0]), "stealth"))
    option_list.append(("Demand she takes it" + serum_give_chance_color_wrapper(chances[2]), "demand"))
    if person.is_slave:
        option_list.append(("Order her to take it\n{size=12}{color=#00D000}She is your slave{/color}{/size}", "slave"))
    elif person.is_employee:
        if mandatory_unpaid_serum_testing_policy.is_owned:
            option_list.append(("Ask her to take it\n{size=12}{color=#00D000}Required by Policy{/color}{/size}", "policy"))
        else:
            option_list.append(("Ask her to take it" + serum_give_chance_color_wrapper(chances[1]), "ask"))
            if mandatory_paid_serum_testing_policy.is_owned and mc.business.has_funds(chances[3]):
                option_list.append((f"Pay her to take it\n{{size=12}}{{color=#D00000}}Costs ${chances[3]:.2f}{{/color}}{{/size}}", "paid"))
    else:
        option_list.append(("Ask her to take it" + serum_give_chance_color_wrapper(chances[1]), "ask"))
    option_list.insert(0, "Give Serum")
    return option_list

def manage_bc(person, start, update_knowledge = True):
    if start:
        event_label = "bc_start_event"
    else:
        event_label = "bc_stop_event"

    mc.business.add_mandatory_morning_crisis(
        Action("Change birth control", always_true_requirement, event_label, args = [person, update_knowledge])
    ) # She starts or stops the next morning (morning crisis event triggers only before time_of_day = 0).

def start_birth_control(person: Person, update_knowledge = True):
    person.on_birth_control = True
    if update_knowledge:
        person.update_birth_control_knowledge()

def stop_birth_control(person: Person, update_knowledge = True):
    person.on_birth_control = False
    if update_knowledge:
        person.update_birth_control_knowledge()

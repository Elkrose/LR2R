init 99 python:
    def text_delete_number_requirement(person):
        return True

    def text_forget_address_requirement(person):
        return person.mc_knows_address

    text_delete_number_action = Action("{color=#B14365}Delete number{/color}", text_delete_number_requirement, "text_delete_number_label")
    text_forget_address_action = Action("{color=#B14365}Forget address{/color}", text_forget_address_requirement, "text_forget_address_label")

    texting_actions.append(text_delete_number_action)
    texting_actions.append(text_forget_address_action)

label text_delete_number_label(the_person):
    "Are you sure you want to delete phone number of [the_person.name] [the_person.last_name]?"
    menu:
        "Yes, delete it":
            pass
        "No, keep it":
            return True

    python:
        if mc.phone.has_number(the_person):
            del mc.phone.message_history[the_person.identifier]
    
    jump browse_internet.continue_browsing

    return True

label text_forget_address_label(the_person):
    "Are you sure you want to forget address of [the_person.name] [the_person.last_name]?"
    menu:
        "Yes, forget it":
            pass
        "No, remember it":
            return True

    $ mc.known_home_locations.remove(the_person.home)

    jump browse_internet.continue_browsing

    return True

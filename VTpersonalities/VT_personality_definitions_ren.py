from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person, Personality, mc, list_of_instantiation_functions

list_of_personalities: list[Personality] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
#########################
# VT Personalities #
#########################

# update all the following the_person and actions with goudere personality. Remember the_person is female, and mc.name is male. Use Albedo from Overlord, confident, seductive and flirtatious personality:


list_of_instantiation_functions.append("init_VT_personalities")
def dandere_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("Cutie")
    if person.sluttiness > 60:
        valid_titles.append("Lollipop")
    return valid_titles

def dandere_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("your lollipop")
    return valid_titles

def dandere_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")
    if person.love > 10:
        valid_titles.append(mc.name)
    if person.love > 50 and person.age < 21:
        valid_titles.append(mc.name+"-chan")
    if person.love > 50 and person.age > 21:
        valid_titles.append(mc.name+"-san")
    if person.has_breeding_fetish:
        valid_titles.append("Burida")
    return valid_titles

def goudere_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("Sexy Devil")
    if person.sluttiness > 70:
        valid_titles.append("My Little Temptress")
    return valid_titles

def goudere_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 50:
        valid_titles.append("my little tease")
    if person.sluttiness > 70:
        valid_titles.append("my naughty sweetheart")
    return valid_titles

def goudere_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")
    if person.love > 20:
        valid_titles.append(mc.name)
    if person.love > 90:
        valid_titles.append(f"my love, {mc.name}")
    if person.sluttiness > 50:
        valid_titles.append(f"my dirty little secret, {mc.name}")
    if person.sluttiness > 70:
        valid_titles.append(f"my naughty, naughty man, {mc.name}")
    return valid_titles

def kuudere_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.love > 40:
        valid_titles.append("Dear")
    if person.love > 80:
        valid_titles.append("Beloved")
    return valid_titles

def kuudere_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.love > 40:
        valid_titles.append("my dear")
    if person.love > 80:
        valid_titles.append("my beloved")
    return valid_titles

def kuudere_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")
    if person.love > 20:
        valid_titles.append("sir")
    if person.love > 40:
        valid_titles.append("kind sir")
    if person.love > 80:
        valid_titles.append("my dear sir")
    return valid_titles

def tsundere_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 30:
        valid_titles.append(person.name)
    if person.sluttiness > 50:
        valid_titles.append("Bitch")
    if person.sluttiness > 70:
        valid_titles.append("Whore")
    return valid_titles

def tsundere_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 30:
        valid_titles.append(person.name)
    if person.sluttiness > 50:
        valid_titles.append("your bitch")
    if person.sluttiness > 70:
        valid_titles.append("your dirty fucktoy")
    return valid_titles

def tsundere_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")
    if person.love > 40:
        valid_titles.append(mc.name)
    if person.has_breeding_fetish:
        valid_titles.append("Stud")
    if person.sluttiness > 60:
        valid_titles.append("Your fucktoy")
    if person.obedience > 50:
        valid_titles.append("Your slave")
    return valid_titles

# update all the following the_person and actions with yandere personality. Remember the_person is female, and mc.name is male. Use Yuno Gasai from Future Diary for ideas, keep to the structure and don't use the same dialogs:```
def yandere_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Adorable {person.formal_address}, Beloved of {mc.name}")
    valid_titles.append(person.name)
    valid_titles.append(f"Mine, {person.name}")
    valid_titles.append(f"My Heartbeat")
    if person.sluttiness > 40:
        valid_titles.append("My Sweet Little Sugar Lips")
    if person.sluttiness > 60:
        valid_titles.append("My Bitch")
    valid_titles.append(f"My Obsession")
    valid_titles.append(f"My Dark Angel")
    return valid_titles

def yandere_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"mine, {person.name}")
    valid_titles.append(f"{person.name}, my little treasure")
    if person.sluttiness > 40:
        valid_titles.append("my sweet little sugar lips")
    if person.sluttiness > 60:
        valid_titles.append("my bitch, owned by me")
    valid_titles.append(f"{person.name}, my heartbeat")
    valid_titles.append(f"{person.name}, my obsession")
    valid_titles.append(f"{person.name}, my dark angel")
    valid_titles.append(f"{person.name}, my one and only")
    return valid_titles

def yandere_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mine, {mc.last_name}")
    valid_titles.append(mc.name)
    valid_titles.append(f"Master {mc.last_name}")
    valid_titles.append(f"Sir {mc.last_name}")
    if person.has_breeding_fetish:
        valid_titles.append("My Magnificent Stud")
        valid_titles.append("My Precious Sperm Donor")
    return valid_titles

# update all the following the_person and movements with alluring personality. Use Miss Fortune and Samira from League of Legends for ideas, keep to the structure. Movements in quotations:
def alluring_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.name} {person.last_name}")
    valid_titles.append(f"Sexy {person.name}")
    if person.love > 20:
        valid_titles.append(f"{person.name}, sweetheart")
        valid_titles.append("My lovely")
        valid_titles.append("Beautiful")
    if person.love > 40:
        valid_titles.append("My dear")
        valid_titles.append("Gorgeous")
        valid_titles.append("Stunning")
    if person.love > 60:
        valid_titles.append("My love")
        valid_titles.append("Sweetheart")
        valid_titles.append("Darling girl")
    if person.love > 80:
        valid_titles.append("My beloved, darling")
        valid_titles.append("My everything")
        valid_titles.append("Forever mine")
    return valid_titles

def alluring_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"my sexy {person.name} {person.last_name}")
    if person.love > 20:
        valid_titles.append(f"my lovely {person.name}")
        valid_titles.append("my sweetheart")
    if person.love > 40:
        valid_titles.append("my dear darling")
        valid_titles.append("my gorgeous girl")
    if person.love > 60:
        valid_titles.append("my sweet love")
        valid_titles.append("my beautiful babe")
    if person.love > 80:
        valid_titles.append("my beloved, my everything")
        valid_titles.append("my forever love")
    return valid_titles

def alluring_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"My handsome Mr. {mc.last_name}")
    if person.love > 20:
        valid_titles.append("My sexy sir")
        valid_titles.append("Darling")
    if person.love > 40:
        valid_titles.append("My kind and gorgeous sir")
        valid_titles.append("Sweetheart")
    if person.love > 60:
        valid_titles.append("My lovely master")
        valid_titles.append("Beautiful lover")
    if person.love > 80:
        valid_titles.append("My dear and beloved sir")
        valid_titles.append("Forever mine, my love")
    return valid_titles

# update all the following the_person and movements with gothic personality. Use Wednesday Addams from Addams Family or Lydia Deetz from Beetlejuice, for ideas, keep to the structure. Movements in quotations:
def gothic_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.name} {person.last_name}, Mistress of the Night")
    valid_titles.append(f"Dark {person.name}")
    if person.love > 20:
        valid_titles.append(f"{person.name}, my morbid fascination")
        valid_titles.append("My little ghoul")
        valid_titles.append("Macabre beauty")
    if person.love > 40:
        valid_titles.append("My darkling")
        valid_titles.append("Sinister sweetheart")
        valid_titles.append("Midnight enchantress")
    if person.love > 60:
        valid_titles.append("My eternal darkness")
        valid_titles.append("Forever entwined in shadow")
        valid_titles.append("My phantom love")
    if person.love > 80:
        valid_titles.append("My beloved, damned soul")
        valid_titles.append("My heart, forever lost in the abyss")
        valid_titles.append("Eternally bound to the darkness")
    return valid_titles

def gothic_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"my dark {person.name} {person.last_name}")
    if person.love > 20:
        valid_titles.append(f"my morbidly fascinating {person.name}")
        valid_titles.append("my little ghoul, mine to possess")
    if person.love > 40:
        valid_titles.append("my eternal darkness, my darling")
        valid_titles.append("my sinister sweetheart, forever bound to me")
    if person.love > 60:
        valid_titles.append("my phantom love, my heart's despair")
        valid_titles.append("my macabre beauty, my darkest desire")
    if person.love > 80:
        valid_titles.append("my beloved, my damned soul, forever mine")
        valid_titles.append("my forever entwined in shadow, my love")
    return valid_titles

def gothic_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"My dark and brooding Mr. {mc.last_name}")
    if person.love > 20:
        valid_titles.append("My morbidly fascinating sir")
        valid_titles.append("My darling darkness")
    if person.love > 40:
        valid_titles.append("My sinister and handsome master")
        valid_titles.append("My eternal shadow")
    if person.love > 60:
        valid_titles.append("My phantom love, my dark sir")
        valid_titles.append("My macabre sweetheart")
    if person.love > 80:
        valid_titles.append("My beloved and damned sir, forever mine")
        valid_titles.append("My forever entwined in darkness, my love")
    return valid_titles
# update all the following the_person and movements with bimboed personality. Use Cher Horowitz from Clueless or Elle Woods from Legally Blonde, for ideas, keep to the structure. Movements in quotations:
def bimboed_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.name} {person.last_name}, Total Babe")
    valid_titles.append(f"Sexy {person.name}")
    if person.love > 20:
        valid_titles.append(f"{person.name}, my sweet obsession")
        valid_titles.append("My little cutie")
        valid_titles.append("Totally gorgeous")
    if person.love > 40:
        valid_titles.append("My sweetie pie")
        valid_titles.append("Lovely sweetheart")
        valid_titles.append("My adorable crush")
    if person.love > 60:
        valid_titles.append("My forever sweetheart")
        valid_titles.append("Totally meant to be")
        valid_titles.append("My perfect match")
    if person.love > 80:
        valid_titles.append("My beloved, sweet everything")
        valid_titles.append("My heart, totally yours")
        valid_titles.append("Forever and always, my love")
    return valid_titles

def bimboed_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"my adorable {person.name} {person.last_name}")
    if person.love > 20:
        valid_titles.append(f"my totally gorgeous {person.name}, all mine")
        valid_titles.append("my little cutie, mine to cuddle")
    if person.love > 40:
        valid_titles.append("my lovely sweetheart, my forever darling")
        valid_titles.append("my sexy sweetheart, totally devoted to me")
    if person.love > 60:
        valid_titles.append("my perfect match, my heart's desire")
        valid_titles.append("my sweet obsession, my everything")
    if person.love > 80:
        valid_titles.append("my beloved, my sweet everything, forever mine")
        valid_titles.append("my forever and always, my love, my heart")
    return valid_titles

def bimboed_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"My totally hot Mr. {mc.last_name}")
    if person.love > 20:
        valid_titles.append("My totally gorgeous sir")
        valid_titles.append("My darling sweetheart")
    if person.love > 40:
        valid_titles.append("My sexy and handsome boyfriend")
        valid_titles.append("My forever love")
    if person.love > 60:
        valid_titles.append("My perfect match, my sweet sir")
        valid_titles.append("My lovely sweetheart")
    if person.love > 80:
        valid_titles.append("My beloved and sweet everything, forever mine")
        valid_titles.append("My forever and always, my love")
    return valid_titles

# update all the following the_person and movements with tomboy personality. Use Juno MacGuff from Juno or Wendy Corduroy from Gravity Falls, for ideas, keep to the structure. Movements in quotations:
def tomboy_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.name}, my dude")
    valid_titles.append(f"Awesome {person.name}")
    if person.love > 20:
        valid_titles.append(f"{person.name}, my partner in crime")
        valid_titles.append("My favorite person to hang out with")
        valid_titles.append("Totally cool")
    if person.love > 40:
        valid_titles.append("My go-to guy")
        valid_titles.append("My buddy, my friend")
        valid_titles.append("My awesome accomplice")
    if person.love > 60:
        valid_titles.append("My ride or die")
        valid_titles.append("My main squeeze")
        valid_titles.append("My person, my rock")
    if person.love > 80:
        valid_titles.append("My forever buddy")
        valid_titles.append("My partner in shenanigans")
        valid_titles.append("My favorite human, forever and always")
    return valid_titles

def tomboy_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"my buddy {person.name}")
    if person.love > 20:
        valid_titles.append(f"my partner in crime, {person.name}")
        valid_titles.append("my go-to person, my favorite")
    if person.love > 40:
        valid_titles.append("my ride or die, my main squeeze")
        valid_titles.append("my favorite person to hang out with, my dude")
    if person.love > 60:
        valid_titles.append("my person, my rock")
        valid_titles.append("my favorite human, my best friend")
    if person.love > 80:
        valid_titles.append("my forever buddy, my partner in shenanigans")
        valid_titles.append("my main person, my favorite everything")
    return valid_titles

def tomboy_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"My dude, {mc.last_name}")
    if person.love > 20:
        valid_titles.append("My pretty cool guy")
        valid_titles.append("My sorta-kinda boyfriend")
    if person.love > 40:
        valid_titles.append("My awesome partner in crime")
        valid_titles.append("My favorite person to hang out with")
    if person.love > 60:
        valid_titles.append("My go-to guy for everything")
        valid_titles.append("My person, my dude")
    if person.love > 80:
        valid_titles.append("My ride or die, forever and always")
        valid_titles.append("My main squeeze, my love")
    return valid_titles

# update all the following the_person and movements with foodie personality. Use Hannibal Lecter from Silence of the Lamb or Aziraphale from Good Omens, for ideas, keep to the structure. Movements in quotations:
def foodie_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.name}, my secret ingredient")
    valid_titles.append(f"The delightful {person.name}")
    if person.love > 20:
        valid_titles.append(f"{person.name}, my culinary companion")
        valid_titles.append("My favorite dining partner")
        valid_titles.append("A pinch of perfection")
    if person.love > 40:
        valid_titles.append("My go-to gourmet")
        valid_titles.append("My flavorful friend")
        valid_titles.append("My recipe for romance")
    if person.love > 60:
        valid_titles.append("My sous chef in crime")
        valid_titles.append("My main course")
        valid_titles.append("My feast for the eyes")
    if person.love > 80:
        valid_titles.append("My forever flavor")
        valid_titles.append("My partner in culinary shenanigans")
        valid_titles.append("My favorite dish, forever and always")
    return valid_titles

def foodie_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"my secret ingredient, {person.name}")
    if person.love > 20:
        valid_titles.append(f"my culinary companion, {person.name}")
        valid_titles.append("my favorite flavor, my go-to gourmet")
    if person.love > 40:
        valid_titles.append("my sous chef in crime, my main course")
        valid_titles.append("my favorite dish to share, my partner in culinary delights")
    if person.love > 60:
        valid_titles.append("my feast for the eyes, my culinary rock")
        valid_titles.append("my favorite recipe, my best culinary friend")
    if person.love > 80:
        valid_titles.append("my forever flavor, my partner in culinary shenanigans")
        valid_titles.append("my main ingredient, my favorite culinary everything")
    return valid_titles

def foodie_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"My secret sauce, {mc.last_name}")
    if person.love > 20:
        valid_titles.append("My flavor of the month")
        valid_titles.append("My culinary crush")
    if person.love > 40:
        valid_titles.append("My partner in culinary crime")
        valid_titles.append("My favorite dining companion")
    if person.love > 60:
        valid_titles.append("My go-to gourmet guru")
        valid_titles.append("My culinary soulmate")
    if person.love > 80:
        valid_titles.append("My forever flavor, forever and always")
        valid_titles.append("My main course, my love")
    return valid_titles
# update all the following the_person and movements with cosplay personality. Use Marin Kitagawa from My Dress-Up Darling or Lilysa Amano from 2.5 Dimensional Seduction, for ideas, keep to the structure. Movements in quotations:
def cosplay_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.name}, my cosplay cuisine companion")
    valid_titles.append(f"The deliciously dressed {person.name}")
    if person.love > 20:
        valid_titles.append(f"{person.name}, my anime-inspired chef")
        valid_titles.append("My favorite cosplay café partner")
        valid_titles.append("A dash of moe in my meals")
    if person.love > 40:
        valid_titles.append("My go-to gourmet senpai")
        valid_titles.append("My flavorful cosplay friend")
        valid_titles.append("My recipe for romance, anime-style")
    if person.love > 60:
        valid_titles.append("My cosplay kitchen companion")
        valid_titles.append("My main course manga maiden")
        valid_titles.append("My feast for the eyes, cosplay edition")
    if person.love > 80:
        valid_titles.append("My forever cosplay flavor")
        valid_titles.append("My partner in culinary cosplay adventures")
        valid_titles.append("My favorite dish, served with a side of cosplay love")
    return valid_titles

def cosplay_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"my cosplay cutie, {person.name}")
    if person.love > 20:
        valid_titles.append(f"my anime-inspired darling, {person.name}")
        valid_titles.append("my favorite cosplay companion, my go-to senpai")
    if person.love > 40:
        valid_titles.append("my cosplay partner in crime, my main manga maiden")
        valid_titles.append("my favorite cosplay to share, my partner in otaku delights")
    if person.love > 60:
        valid_titles.append("my cosplay feast for the eyes, my moe masterpiece")
        valid_titles.append("my favorite cosplay recipe, my best otaku friend")
    if person.love > 80:
        valid_titles.append("my forever cosplay, my partner in anime adventures")
        valid_titles.append("my main cosplay ingredient, my favorite otaku everything")
    return valid_titles

def cosplay_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"My cosplay senpai, {mc.last_name}")
    if person.love > 20:
        valid_titles.append("My anime crush")
        valid_titles.append("My manga muse")
    if person.love > 40:
        valid_titles.append("My partner in cosplay adventures")
        valid_titles.append("My favorite otaku companion")
    if person.love > 60:
        valid_titles.append("My go-to cosplay guru")
        valid_titles.append("My moe match made in heaven")
    if person.love > 80:
        valid_titles.append("My forever cosplay companion, forever and always")
        valid_titles.append("My main manga maiden, my love")
    return valid_titles

# update all the following the_person and movements with slutty personality. Use Panty Anarchy from Panty & Stocking with Garterbelt or Naruko Yokoshima from Seitokai Yakuindomo, for ideas, keep to the structure. Movements in quotations:
def slutty_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.name}, my sexpot companion")
    valid_titles.append(f"The sinfully sexy {person.name}")
    if person.love > 20:
        valid_titles.append(f"{person.name}, my sex kitten")
        valid_titles.append("My favorite sex buddy")
        valid_titles.append("A dash of slutty spice in my sex life")
    if person.love > 40:
        valid_titles.append("My go-to sex senpai")
        valid_titles.append("My filthy friend")
        valid_titles.append("My recipe for raunchy romance")
    if person.love > 60:
        valid_titles.append("My bedroom companion")
        valid_titles.append("My main course manga sexpot")
        valid_titles.append("My feast for the cock")
    if person.love > 80:
        valid_titles.append("My forever sex slave")
        valid_titles.append("My partner in kinky adventures")
        valid_titles.append("My favorite sex toy, served with a side of lust")
        valid_titles.append("My ultimate sex fantasy")
    return valid_titles

def slutty_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"my fuck toy, {person.name}")
    if person.love > 20:
        valid_titles.append(f"my sex kitten, {person.name}")
        valid_titles.append("my favorite slut, my go-to sex buddy")
    if person.love > 40:
        valid_titles.append("my partner in kink, my main sexpot")
        valid_titles.append("my favorite to bang, my partner in orgies")
    if person.love > 60:
        valid_titles.append("my sheath for the cock, my sex goddess")
        valid_titles.append("my favorite sex friend")
    if person.love > 80:
        valid_titles.append("my forever sex slave, my partner in fuckery")
        valid_titles.append("my main sex ingredient, my favorite sex everything")
        valid_titles.append("my number one sex doll, my ultimate sex fantasy")
    return valid_titles

def slutty_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"My fuck buddy, {mc.last_name}")
    if person.love > 20:
        valid_titles.append("My sex fantasy")
        valid_titles.append("My stud")
    if person.love > 40:
        valid_titles.append("My partner in kink")
        valid_titles.append("My favorite sex toy")
    if person.love > 60:
        valid_titles.append("My go-to sex guru")
        valid_titles.append("My sex match made in heaven")
    if person.love > 80:
        valid_titles.append("My sex companion, forever and always")
        valid_titles.append("My main sex love")
        valid_titles.append("My number one stud")
        valid_titles.append("My ultimate sex fantasy")
    return valid_titles
# this doesn't read properly, don't use repetitive wording, use different words, and movements. needs to be sexually explicit. Update all the following the_person and movements with pornstar personality. Use Dillion Harper, Alexis Texas, Megan Rain, Riley Reid, Dani Daniels, Naomi Woods for ideas, keep to the structure. Movements in double quotes on a new line: ```

def pornstar_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("Sexy Slut")
        valid_titles.append("Dirty Girl")
        valid_titles.append("Naughty Babe")
    if person.sluttiness > 60:
        valid_titles.append("Dirty Whore")
        valid_titles.append("Cum Dumpster")
        valid_titles.append("Fuck Toy")
    if person.sluttiness > 80:
        valid_titles.append("Total Slut")
        valid_titles.append("Complete Whore")
        valid_titles.append("Absolute Fuck Toy")
    return valid_titles

def pornstar_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("your dirty little secret")
        valid_titles.append("your naughty little girl")
        valid_titles.append("your personal plaything")
    if person.sluttiness > 60:
        valid_titles.append("your personal fuck toy")
        valid_titles.append("your dirty little whore")
        valid_titles.append("your cum dumpster")
    return valid_titles

def pornstar_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")
    if person.love > 10:
        valid_titles.append(mc.name)
    if person.love > 50 and person.age < 21:
        valid_titles.append("Daddy")
        valid_titles.append("Papa")
        valid_titles.append("Old Man")
    if person.love > 50 and person.age > 21:
        valid_titles.append("Master")
        valid_titles.append("Sir")
        valid_titles.append("Lord")
    if person.has_breeding_fetish:
        valid_titles.append("Breeder")
        valid_titles.append("Stud")
        valid_titles.append("Sire")
    return valid_titles

# this doesn't read properly, don't use repetitive wording, use different words, and movements. Update all the following the_person and movements with breeding personality. Use Hitomi Takami from Ane Haramix or Momoko Kuzuryu from Sumomomo, Momomo: The Strongest Bride on Earth, for ideas, keep to the structure. Movements in double quotes and newline:

def breeder_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("Fertile Female")
        valid_titles.append("Breeding Stock")
        valid_titles.append("Mother-to-Be")
    if person.sluttiness > 60:
        valid_titles.append("Cum Receptacle")
        valid_titles.append("Seed Vessel")
        valid_titles.append("Baby Maker")
    if person.sluttiness > 80:
        valid_titles.append("Total Breeding Machine")
        valid_titles.append("Complete Fertility Vessel")
        valid_titles.append("Absolute Baby Factory")
    return valid_titles

def breeder_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("your fertile female")
        valid_titles.append("your breeding stock")
        valid_titles.append("your personal baby maker")
    if person.sluttiness > 60:
        valid_titles.append("your personal cum receptacle")
        valid_titles.append("your seed vessel")
        valid_titles.append("your baby factory")
    return valid_titles

def breeder_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")
    if person.love > 10:
        valid_titles.append(mc.name)
    if person.love > 50 and person.age < 21:
        valid_titles.append("Sire")
        valid_titles.append("Stud")
        valid_titles.append("Sir Breeder")
    if person.love > 50 and person.age > 21:
        valid_titles.append("Master Breeder")
        valid_titles.append("Lord of the Manor")
        valid_titles.append("Patriarch")
    if person.has_breeding_fetish:
        valid_titles.append("Breeding Master")
        valid_titles.append("Fertility God")
        valid_titles.append("Procreation Pro")
    return valid_titles





def init_VT_personalities():
    global dandere_personality
    dandere_personality = Personality("dandere", #Shouko Komi from Komi Can't Communicate style personality
        common_likes = ["skirts", "the weekend", "conservative outfits", "work uniforms", "the colour pink", "classical music", "jazz", "pop music"],
        common_sexy_likes = ["missionary style sex", "kissing", "masturbating", "being submissive", "drinking cum", "cum facials"],
        common_dislikes = ["small talk", "HR work", "marketing work", "pants", "the colour yellow", "research work", "work uniforms", "boots", "dresses", "high heels"],
        common_sexy_dislikes = ["taking control", "sex standing up", "showing her tits", "showing her ass", "bareback sex", "lingerie", "skimpy outfits", "not wearing underwear", "not wearing anything", "public sex", "creampies"],
        titles_function = dandere_titles, possessive_titles_function = dandere_possessive_titles, player_titles_function = dandere_player_titles,
        insta_chance = 0, dikdok_chance = 0)

# update all the following the_person and actions with goudere personality. Remember the_person is female, and mc.name is male. Use Albedo from Overlord, confident, seductive and flirtatious personality:
    global goudere_personality
    goudere_personality = Personality("goudere", #Albedo from Overlord style personality
        common_likes = ["conservative outfits", "punk music", "working", "the colour black", "pants", "boots"],
        common_sexy_likes = ["big dicks", "kissing", "anal sex", "getting head", "giving blowjobs", "masturbating", "anal creampies", "giving tit fucks"],
        common_dislikes = ["skirts", "HR work", "marketing work", "makeup", "flirting", "small talk", "pop music", "high heels"],
        common_sexy_dislikes = ["skimpy outfits", "not wearing underwear", "not wearing anything", "public sex", "lingerie"],
        titles_function = goudere_titles, possessive_titles_function = goudere_possessive_titles, player_titles_function = goudere_player_titles,
        insta_chance = 20, dikdok_chance = 0)

# update all the following the_person and actions with kuudere personality. Remember the_person is female, and mc.name is male. Use Reina Aharen from Aharen-San for ideas:```
    global kuudere_personality
    kuudere_personality = Personality("kuudere", #Reina Aharen from Aharen-San style personality
        common_likes = ["pants", "Mondays", "working", "makeup", "the colour blue", "conservative outfits", "jazz", "classical music", "dresses", "boots"],
        common_sexy_likes = ["missionary style sex", "kissing", "lingerie", "being submissive", "vaginal sex", "creampies", "giving tit fucks"],
        common_dislikes = ["the colour red", "flirting", "skirts"],
        common_sexy_dislikes = ["masturbating", "giving blowjobs", "getting head", "doggy style sex", "public sex", "not wearing underwear", "not wearing anything", "bareback sex", "cum facials"],
        titles_function = kuudere_titles, possessive_titles_function = kuudere_possessive_titles, player_titles_function = kuudere_player_titles,
        insta_chance = 0, dikdok_chance = 0)
# update all the following the_person and actions with tsundere personality. Remember the_person is female, and mc.name is male. Use Asuka Langley from Neon Genesis Evangelion for ideas, keep to the structure and don't use the same dialogs:```
    global tsundere_personality
    tsundere_personality = Personality("tsundere", #Asuka Langley from Neon Genesis Evangelion style personality
        common_likes = ["skirts", "small talk", "Fridays", "the weekend", "the colour red", "makeup", "flirting", "heavy metal music", "punk music", "high heels", "dresses"],
        common_sexy_likes = ["anal creampies", "doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "showing her tits", "showing her ass", "taking control", "not wearing underwear", "creampies", "bareback sex", "threesomes"],
        common_dislikes = ["Mondays", "the colour pink", "conservative outfits", "work uniforms", "pants"],
        common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex", "giving handjobs"],
        titles_function = tsundere_titles, possessive_titles_function = tsundere_possessive_titles, player_titles_function = tsundere_player_titles,
        insta_chance = 40, dikdok_chance = 30)
# update all the following the_person and actions with yandere personality. Remember the_person is female, and mc.name is male. Use Yuno Gasai from Future Diary for ideas, keep to the structure and don't use the same dialogs:```
    global yandere_personality
    yandere_personality = Personality("yandere", #Yuno Gasai from Future Diary style personality
        common_likes = ["skirts", "small talk", "Fridays", "the weekend", "the colour red", "makeup", "flirting", "heavy metal music", "punk music", "high heels", "dresses"],
        common_sexy_likes = ["anal creampies", "doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "showing her tits", "showing her ass", "taking control", "not wearing underwear", "creampies", "bareback sex", "threesomes"],
        common_dislikes = ["Mondays", "the colour pink", "conservative outfits", "work uniforms", "pants"],
        common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex", "giving handjobs"],
        titles_function = yandere_titles, possessive_titles_function = yandere_possessive_titles, player_titles_function = yandere_player_titles,
        insta_chance = 40, dikdok_chance = 30)
# update all the following the_person and movements with alluring personality. Use Miss Fortune and Samira from League of Legends for ideas, keep to the structure. Movements in quotations:
    global alluring_personality
    alluring_personality = Personality("alluring", #Miss Fortune and Samira from League of Legends style personality
        common_likes = ["skirts", "the weekend", "conservative outfits", "work uniforms", "the colour pink", "classical music", "jazz", "pop music"],
        common_sexy_likes = ["missionary style sex", "kissing", "masturbating", "being submissive", "drinking cum", "cum facials"],
        common_dislikes = ["small talk", "HR work", "marketing work", "pants", "the colour yellow", "research work", "work uniforms", "boots", "dresses", "high heels"],
        common_sexy_dislikes = ["taking control", "sex standing up", "showing her tits", "showing her ass", "bareback sex", "lingerie", "skimpy outfits", "not wearing underwear", "not wearing anything", "public sex", "creampies"],
        titles_function = alluring_titles, possessive_titles_function = alluring_possessive_titles, player_titles_function = alluring_player_titles,
        insta_chance = 0, dikdok_chance = 0)
# update all the following the_person and movements with gothic personality. Use Wednesday Addams from Addams Family or Lydia Deetz from Beetlejuice, for ideas, keep to the structure. Movements in quotations:
    global gothic_personality
    gothic_personality = Personality("gothic", #Miss Fortune and Samira from League of Legends style personality
        common_likes = ["dresses", "the weekend", "conservative outfits", "work uniforms", "the colour black", "classical music", "jazz", "pop music"],
        common_sexy_likes = ["missionary style sex", "kissing", "masturbating", "being submissive", "drinking cum", "cum facials"],
        common_dislikes = ["small talk", "HR work", "marketing work", "pants", "the colour yellow", "research work", "work uniforms", "boots", "dresses"],
        common_sexy_dislikes = ["taking control", "sex standing up", "showing her tits", "showing her ass", "bareback sex", "lingerie", "skimpy outfits", "not wearing underwear", "not wearing anything", "public sex", "creampies"],
        titles_function = gothic_titles, possessive_titles_function = gothic_possessive_titles, player_titles_function = gothic_player_titles,
        insta_chance = 0, dikdok_chance = 0)
# update all the following the_person and movements with bimboed personality. Use Cher Horowitz from Clueless or Elle Woods from Legally Blonde, for ideas, keep to the structure. Movements in quotations:
    global bimboed_personality
    bimboed_personality = Personality("bimboed", #Miss Fortune and Samira from League of Legends style personality
        common_likes = ["dresses", "the weekend", "conservative outfits", "work uniforms", "the colour pink", "classical music", "jazz", "pop music"],
        common_sexy_likes = ["missionary style sex", "kissing", "masturbating", "being submissive", "drinking cum", "cum facials"],
        common_dislikes = ["small talk", "HR work", "marketing work", "pants", "the colour yellow", "research work", "work uniforms", "boots", "dresses"],
        common_sexy_dislikes = ["taking control", "sex standing up", "showing her tits", "showing her ass", "bareback sex", "lingerie", "skimpy outfits", "not wearing underwear", "not wearing anything", "public sex", "creampies"],
        titles_function = bimboed_titles, possessive_titles_function = bimboed_possessive_titles, player_titles_function = bimboed_player_titles,
        insta_chance = 0, dikdok_chance = 0)
    # global bimboed_personality
    # bimboed_personality = Personality("bimboed", 
        # common_likes = ["shopping", "fashion", "parties", "gossip", "romantic comedies", "pink sparkly things", "cute animals", " bubblegum pop music"],
        # common_sexy_likes = ["cuddling", "kissing", "being pampered", "receiving massages", "wearing lingerie", "having their hair played with"],
        # common_dislikes = ["math", "science", "reading", "boring things", "ugly clothes", "bad hair days", "being alone"],
        # common_sexy_dislikes = ["being rough", "having sex without romance", "not being in the mood", "not being pampered", "not being treated like a princess"],
        # titles_function = bimboed_titles, possessive_titles_function = bimboed_possessive_titles, player_titles_function = bimboed_player_titles,
        # insta_chance = 0, dikdok_chance = 0)
# update all the following the_person and movements with tomboy personality. Use Juno MacGuff from Juno or Wendy Corduroy from Gravity Falls, for ideas, keep to the structure. Movements in quotations:
    global tomboy_personality
    tomboy_personality = Personality("tomboy", #Miss Fortune and Samira from League of Legends style personality
        common_likes = ["pants", "the weekend", "conservative outfits", "work uniforms", "the colour blue", "heavy metal music", "boots", "pop music"],
        common_sexy_likes = ["missionary style sex", "public sex", "kissing", "masturbating", "taking control", "giving blowjobs", "getting head"],
        common_dislikes = ["small talk", "HR work", "marketing work", "high heels", "the colour pink", "research work", "work uniforms", "skirts", "makeup"],
        common_sexy_dislikes = ["being submissive", "sex standing up", "showing her tits", "showing her ass", "bareback sex", "lingerie", "skimpy outfits", "not wearing underwear", "not wearing anything", "creampies"],
        titles_function = tomboy_titles, possessive_titles_function = tomboy_possessive_titles, player_titles_function = tomboy_player_titles,
        insta_chance = 0, dikdok_chance = 0)

# update all the following the_person and movements with foodie personality. Use Hannibal Lecter from Silence of the Lamb or Aziraphale from Good Omens, for ideas, keep to the structure. Movements in quotations:
    global foodie_personality
    foodie_personality = Personality("foodie", #Miss Fortune and Samira from League of Legends style personality
        common_likes = ["research work", "pants", "the weekend", "conservative outfits", "work uniforms", "the colour blue", "classical music", "boots", "pop music", "the color black", "the color white"],
        common_sexy_likes = ["doggy style sex", "kissing", "masturbating", "taking control", "giving blowjobs", "getting head"],
        common_dislikes = ["small talk", "HR work", "marketing work", "high heels", "the colour pink", "research work", "work uniforms", "skirts", "makeup"],
        common_sexy_dislikes = ["being submissive", "sex standing up", "showing her tits", "showing her ass", "bareback sex", "lingerie", "skimpy outfits", "not wearing underwear", "not wearing anything", "public sex", "creampies"],
        titles_function = foodie_titles, possessive_titles_function = foodie_possessive_titles, player_titles_function = foodie_player_titles,
        insta_chance = 0, dikdok_chance = 0)
# update all the following the_person and movements with cosplay personality. Use Marin Kitagawa from My Dress-Up Darling or Lilysa Amano from 2.5 Dimensional Seduction, for ideas, keep to the structure. Movements in quotations:
    global cosplay_personality
    cosplay_personality = Personality("cosplay", # Marin Kitagawa from My Dress-Up Darling or Lilysa Amano from 2.5 Dimensional Seduction style personality
        common_likes = ["dresses", "small talk", "pants", "skirts", "high heels", "heavy metal music", "makeup", "boots", "pop music", "the weekend"],
        common_sexy_likes = ["doggy style sex", "public sex", "kissing", "showing her tits", "showing her ass",  "taking control", "giving blowjobs", "getting head","lingerie", "skimpy outfits"],
        common_dislikes = ["HR work", "marketing work", "the colour pink", "research work", "conservative outfits", "Mondays"],
        common_sexy_dislikes = ["being submissive", "sex standing up", "bareback sex", "masturbating", "not wearing underwear", "not wearing anything", "creampies"],
        titles_function = cosplay_titles, possessive_titles_function = cosplay_possessive_titles, player_titles_function = cosplay_player_titles,
        insta_chance = 60, dikdok_chance = 30)
# update all the following the_person and movements with slutty personality. Use Panty Anarchy from Panty & Stocking with Garterbelt or Naruko Yokoshima from Seitokai Yakuindomo, for ideas, keep to the structure. Movements in quotations:
    global slutty_personality
    slutty_personality = Personality("slutty", # Panty Anarchy from Panty & Stocking with Garterbelt or Naruko Yokoshima from Seitokai Yakuindomo style personality
        common_likes = ["dresses", "small talk", "pants", "skirts", "high heels", "heavy metal music", "makeup", "boots", "pop music", "the weekend"],
        common_sexy_likes = ["doggy style sex", "public sex", "kissing", "showing her tits", "showing her ass",  "taking control", "giving blowjobs", "getting head","lingerie", "skimpy outfits"],
        common_dislikes = ["HR work", "marketing work", "the colour pink", "research work", "conservative outfits", "Mondays"],
        common_sexy_dislikes = ["being submissive", "sex standing up", "bareback sex", "masturbating", "not wearing underwear", "not wearing anything", "creampies"],
        titles_function = slutty_titles, possessive_titles_function = slutty_possessive_titles, player_titles_function = slutty_player_titles,
        insta_chance = 60, dikdok_chance = 30)
# this doesn't read properly, don't use repetitive wording, use different words, and movements. needs to be sexually explicit. Update all the following the_person and movements with pornstar personality. Use Dillion Harper, Alexis Texas, Megan Rain, Riley Reid, Dani Daniels, Naomi Woods for ideas, keep to the structure. Movements in double quotes on a new line: ```
    global pornstar_personality
    pornstar_personality = Personality("pornstar", # Dillion Harper, Alexis Texas, Megan Rain, Riley Reid, Dani Daniels, Naomi Woods
        common_likes = ["dresses", "small talk", "pants", "boots", "skirts", "high heels", "masturbating", "heavy metal music", "makeup", "pop music", "the weekend"],
        common_sexy_likes = ["doggy style sex", "vaginal sex", "anal sex", "public sex", "kissing", "showing her tits", "showing her ass",  "taking control", "giving blowjobs", "getting head","lingerie", "skimpy outfits"],
        common_dislikes = ["HR work", "marketing work", "the colour pink", "research work", "conservative outfits", "Mondays"],
        common_sexy_dislikes = ["being submissive", "sex standing up", "bareback sex", "not wearing underwear", "not wearing anything", "creampies"],
        titles_function = pornstar_titles, possessive_titles_function = pornstar_possessive_titles, player_titles_function = pornstar_player_titles,
        insta_chance = 60, dikdok_chance = 30)
# this doesn't read properly, don't use repetitive wording, use different words, and movements. Update all the following the_person and movements with breeding personality. Use Hitomi Takami from Ane Haramix or Momoko Kuzuryu from Sumomomo, Momomo: The Strongest Bride on Earth, for ideas, keep to the structure. Movements in double quotes and newline:
    global breeder_personality
    breeder_personality = Personality("breeder", # Hitomi Takami from Ane Haramix or Momoko Kuzuryu from Sumomomo, Momomo: The Strongest Bride on Earth
        common_likes = ["dresses", "small talk", "pants", "boots", "skirts", "high heels", "masturbating", "heavy metal music", "makeup", "pop music", "the weekend"],
        common_sexy_likes = ["doggy style sex", "vaginal sex", "creampies", "public sex", "kissing", "showing her tits", "bareback sex", "being submissive", "getting head","lingerie", "skimpy outfits"],
        common_dislikes = ["HR work", "marketing work", "the colour pink", "research work", "conservative outfits", "Mondays"],
        common_sexy_dislikes = ["anal sex", "taking control", "sex standing up", "skimpy outfits", "not wearing underwear", "not wearing anything", "creampies"],
        titles_function = breeder_titles, possessive_titles_function = breeder_possessive_titles, player_titles_function = breeder_player_titles,
        insta_chance = 0, dikdok_chance = 0)



    list_of_personalities.extend((
        dandere_personality,
        goudere_personality,
        kuudere_personality,
        tsundere_personality,
        yandere_personality,
        alluring_personality,
        gothic_personality,
        bimboed_personality,
        tomboy_personality,
        foodie_personality,
        cosplay_personality,
        slutty_personality,
        pornstar_personality,
        breeder_personality,
    ))


#different words and sexier and  more dangerous yandere personality
#add more dangerous yandere personality, use different words, and movements on a new line in quotations.
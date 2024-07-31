from __future__ import annotations
import renpy
from renpy.display import im
from renpy.display.im import Image
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -100 python:
"""

modpath = "/VTgui/extra_images/"

def get_file_handle(file_name: str) -> str | None:
    return next((x for x in renpy.exports.list_files() if file_name in x), None)

#### Background / LR2R Replaced
Cherry_background_image = Image(get_file_handle("Cherry_Background.png"))
information_image = Image(get_file_handle("information.png"))
question_image = Image(get_file_handle("question.png"))
topboxVT_image = Image(get_file_handle("topboxVTMod.png"))

vtcherries_small_image = im.Scale(Image(get_file_handle("vtcherries.png")), 18, 18)
renpy.image("vtcherries_small", vtcherries_small_image)
vtcherries_image = Image(get_file_handle("vtcherries.png"))

##### Relationship Icons #####
girlfriend_image = Image(get_file_handle(modpath+"girlfriend.png"))
gf_token_small_image = im.Scale(Image(get_file_handle(modpath+"girlfriend.png")), 18, 18)
renpy.image("gf_token_small", gf_token_small_image)

paramour_image = Image(get_file_handle(modpath+"paramour.png"))
paramour_token_small_image = im.Scale(Image(get_file_handle(modpath+"paramour.png")), 18, 18)
renpy.image("paramour_token_small", paramour_token_small_image)

polyamorous_image = Image(get_file_handle(modpath+"harem.png"))
harem_token_small_image = im.Scale(Image(get_file_handle(modpath+"harem.png")), 18, 18)
renpy.image("harem_token_small", harem_token_small_image)

parapoly_image = Image(get_file_handle(modpath+"parapoly.png"))
parapoly_token_small_image = im.Scale(Image(get_file_handle(modpath+"parapoly.png")), 18, 18)
renpy.image("parapoly_token_small", parapoly_token_small_image)

dontknow_image = Image(get_file_handle("dontknow.png"))
dontknow_token_small_image = im.Scale(Image(get_file_handle(modpath+"dontknow.png")), 18, 18)
renpy.image("dontknow_token_small", dontknow_token_small_image)

virgin_image = Image(get_file_handle(modpath+"virgin_token.png"))
virgin_token_small_image = im.Scale(Image(get_file_handle(modpath+"virgin.png")), 18, 18)
renpy.image("virgin_token_small", virgin_token_small_image)

familycircle_image = Image(get_file_handle(modpath+"familycircle.png"))
familycircle_small_image = im.Scale(Image(get_file_handle(modpath+"familycircle.png")), 18, 18)
renpy.image("familycircle_small", familycircle_small_image)

familylove_image = Image(get_file_handle(modpath+"familylove.png"))
familylove_small_image = im.Scale(Image(get_file_handle(modpath+"familylove.png")), 18, 18)
renpy.image("familylove_small", familylove_small_image)

familypoly_image = Image(get_file_handle(modpath+"familypoly.png"))
familypoly_small_image = im.Scale(Image(get_file_handle(modpath+"familypoly.png")), 18, 18)
renpy.image("familypoly_small", familypoly_small_image)

parapolyslave_image = Image(get_file_handle(modpath+"parapolyslave.png"))
parapolyslave_small_image = im.Scale(Image(get_file_handle(modpath+"parapolyslave.png")), 18, 18)
renpy.image("parapolyslave_small", parapolyslave_small_image)

polyslave_image = Image(get_file_handle(modpath+"polyslave.png"))
polyslave_small_image = im.Scale(Image(get_file_handle(modpath+"polyslave.png")), 18, 18)
renpy.image("polyslave_small", polyslave_small_image)

polyfamiliaslave_image = Image(get_file_handle(modpath+"polyfamiliaslave.png"))
polyfamiliaslave_small_image = im.Scale(Image(get_file_handle(modpath+"polyfamiliaslave.png")), 18, 18)
renpy.image("polyfamiliaslave_small", polyfamiliaslave_small_image)

paraslave_image = Image(get_file_handle(modpath+"paraslave.png"))
paraslave_small_image = im.Scale(Image(get_file_handle(modpath+"paraslave.png")), 18, 18)
renpy.image("paraslave_small", paraslave_small_image)

gfslave_image = Image(get_file_handle(modpath+"gfslave.png"))
gfslave_small_image = im.Scale(Image(get_file_handle(modpath+"gfslave.png")), 18, 18)
renpy.image("gfslave_small", gfslave_small_image)

slave_image = Image(get_file_handle(modpath+"slave.png"))
slave_small_image = im.Scale(Image(get_file_handle(modpath+"slave.png")), 18, 18)
renpy.image("slave_small", slave_small_image)

familiaslave_image = Image(get_file_handle(modpath+"familiaslave.png"))
familiaslave_small_image = im.Scale(Image(get_file_handle(modpath+"familiaslave.png")), 18, 18)
renpy.image("familiaslave_small", familiaslave_small_image)

gffamiliaslave_image = Image(get_file_handle(modpath+"gffamiliaslave.png"))
gffamiliaslave_small_image = im.Scale(Image(get_file_handle(modpath+"gffamiliaslave.png")), 18, 18)
renpy.image("gffamiliaslave_small", gffamiliaslave_small_image)
##### Age Icons #####
matureteen_image = Image(get_file_handle("matureteen.png"))
matureteen_token_small_image = im.Scale(Image(get_file_handle("matureteen.png")), 18, 18)
renpy.image("matureteen_token_small", matureteen_token_small_image)

whitelotus_image = Image(get_file_handle("white-lotus.png"))
whitelotus_small_image = im.Scale(Image(get_file_handle("white-lotus.png")), 18, 18)
renpy.image("whitelotus_small", whitelotus_small_image)

redlotus_image = Image(get_file_handle("red-lotus.png"))
redlotus_small_image = im.Scale(Image(get_file_handle("red-lotus.png")), 18, 18)
renpy.image("redlotus_small", redlotus_small_image)

pinklotus_image = Image(get_file_handle("pink-lotus.png"))
pinklotus_small_image = im.Scale(Image(get_file_handle("pink-lotus.png")), 18, 18)
renpy.image("pinklotus_small", pinklotus_small_image)

bluelotus_image = Image(get_file_handle("blue-lotus.png"))
bluelotus_small_image = im.Scale(Image(get_file_handle("blue-lotus.png")), 18, 18)
renpy.image("bluelotus_small", bluelotus_small_image)

goldlotus_image = Image(get_file_handle("gold-lotus.png"))
goldlotus_small_image = im.Scale(Image(get_file_handle("gold-lotus.png")), 18, 18)
renpy.image("goldlotus_small", goldlotus_small_image)

###### Threesome - note polyamorous added
ahegaothreesomes_image = Image(get_file_handle("ahegaothreesomes.png"))
ahegaothreesomes_small_image = im.Scale(Image(get_file_handle("ahegaothreesomes.png")), 18, 18)
renpy.image("ahegaothreesomes_small", ahegaothreesomes_small_image)

threesometriad_image = Image(get_file_handle("threesometriad.png"))
opentriad_image = Image(get_file_handle("opentriad.png"))

knowthreesome_image = Image(get_file_handle("knowthreesome.png"))
knowthreesome_small_image = im.Scale(Image(get_file_handle("knowthreesome.png")), 18, 18)
renpy.image("knowthreesome_small", knowthreesome_small_image)

### Personalities #####
bimbo_image = Image(get_file_handle("bimbo.png"))
bimbo_small_image = im.Scale(Image(get_file_handle("bimbo.png")), 18, 18)
renpy.image("bimbo_small", bimbo_small_image)

cougar_image = Image(get_file_handle("cougar.png"))
alpha_image = Image(get_file_handle("alpha.png"))
relaxed_image = Image(get_file_handle("relaxed.png"))
introvert_image = Image(get_file_handle("introvert.png"))
reserved_image = Image(get_file_handle("reserved.png"))
wild_image = Image(get_file_handle("bitelip.png"))

##### Birthcontrol Icons / Pregnancy #####
bc_image = Image(get_file_handle(modpath+"bc_token.png"))
bc_image_small_image = im.Scale(Image(get_file_handle(modpath+"bc_token.png")), 18, 18)
renpy.image("bc_image_small", bc_image_small_image)

nobc_image = Image(get_file_handle(modpath+"nobc_token.png"))
nobc_image_small_image = im.Scale(Image(get_file_handle(modpath+"nobc_token.png")), 18, 18)
renpy.image("nobc_image_small", nobc_image_small_image)

beezee_image = Image(get_file_handle("beezee.png"))
beezee_token_small_image = im.Scale(Image(get_file_handle("beezee.png")), 18, 18)
renpy.image("beezee_token_small", beezee_token_small_image)

knowbc_image = Image(get_file_handle("knowbc_token.png"))
knowbc_token_small_image = im.Scale(Image(get_file_handle("knowbc_token.png")), 18, 18)
renpy.image("knowbc_token_small", knowbc_token_small_image)

pregnant_image = Image(get_file_handle("pregnant.png"))

feeding_bottle_token_small_image = im.Scale(Image(get_file_handle("feeding_bottle.png")), 18, 18)
renpy.image("feeding_bottle_token_small", feeding_bottle_token_small_image)

##### Condom Icons #####
knowcondom_image = Image(get_file_handle("knowcondom.png"))
knowcondom_token_small_image = im.Scale(Image(get_file_handle("knowcondom.png")), 18, 18)
renpy.image("knowcondom_token_small", knowcondom_token_small_image)

nocondom_image = Image(get_file_handle("nocondom.png"))

wearcondom_image = Image(get_file_handle("wearcondom.png"))
wearcondom_token_small_image = im.Scale(Image(get_file_handle("wearcondom.png")), 18, 18)
renpy.image("wearcondom_token_small", wearcondom_token_small_image)

ahegaocondom_image = Image(get_file_handle("ahegaocondom.png"))

#### Tranced ####
ahegaotrance_image = Image(get_file_handle("ahegaotrance.png"))
ahegaotrance_token_small_image = im.Scale(Image(get_file_handle("ahegaotrance.png")), 18, 18)
renpy.image("ahegaotrance_token_small", ahegaotrance_token_small_image)

heavytrance_image = Image(get_file_handle("heavytrance.png"))
heavytrance_token_small_image = im.Scale(Image(get_file_handle("heavytrance.png")), 18, 18)
renpy.image("heavytrance_token_small", heavytrance_token_small_image)

starttrance_image = Image(get_file_handle("starttrance.png"))
starttrance_token_small_image = im.Scale(Image(get_file_handle("starttrance.png")), 18, 18)
renpy.image("starttrance_token_small", starttrance_token_small_image)

donetrain_image = Image(get_file_handle("donetrain.png"))
donetrain_token_small_image = im.Scale(Image(get_file_handle("donetrain.png")), 18, 18)
renpy.image("donetrain_token_small", donetrain_token_small_image)

notrance_image = Image(get_file_handle("notrance.png"))
### Oral Virgin Flag
truevirgin_image = Image(get_file_handle(modpath+"virgin.png"))

knowlips_image = Image(get_file_handle("knowlips.png"))

claimedmouth_image = Image(get_file_handle("claimedmouth.png"))

ahegaoface_image = Image(get_file_handle("ahegaoface.png"))

ahegaomouth_image = Image(get_file_handle("ahegaomouth.png"))
ahegaomouth_small_image = im.Scale(Image(get_file_handle("ahegaomouth.png")), 18, 18)
renpy.image("ahegaomouth_small", ahegaomouth_small_image)

openmouth_image = Image(get_file_handle("openmouth.png"))
openmouth_small_image = im.Scale(Image(get_file_handle("openmouth.png")), 18, 18)
renpy.image("openmouth_small", openmouth_small_image)

pinklips_image = Image(get_file_handle("pinklips.png"))

bitelip_image = Image(get_file_handle("bitelip.png"))
bitelip_small_image = im.Scale(Image(get_file_handle("bitelip.png")), 18, 18)
renpy.image("bitelip_small", bitelip_small_image)

### Vaginal Virgin Flag
claimedvag_image = Image(get_file_handle("claimedvag.png"))

vaghymen_image = Image(get_file_handle("vaghymen.png"))

openvag_image = Image(get_file_handle("openvag.png"))
openvag_small_image = im.Scale(Image(get_file_handle("openvag.png")), 18, 18)
renpy.image("openvag_small", openvag_small_image)

ahegaovag_image = Image(get_file_handle("ahegaovag.png"))
ahegaovag_small_image = im.Scale(Image(get_file_handle("ahegaovag.png")), 18, 18)
renpy.image("ahegaovag_small", ahegaovag_small_image)

spreadvag_image = Image(get_file_handle("spreadvag.png"))
spreadvag_small_image = im.Scale(Image(get_file_handle("spreadvag.png")), 18, 18)
renpy.image("spreadvag_small", spreadvag_small_image)

vagclosed_image = Image(get_file_handle("vagclosed.png"))
vagclosed_small_image = im.Scale(Image(get_file_handle("vagclosed.png")), 18, 18)
renpy.image("vagclosed_small", vagclosed_small_image)

knowvag_image = Image(get_file_handle("knowvag.png"))

### Anal Virgin Flag
claimedass_image = Image(get_file_handle("claimedass.png"))

handass_image = Image(get_file_handle("handass.png"))
handass_small_image = im.Scale(Image(get_file_handle("handass.png")), 18, 18)
renpy.image("handass_small", handass_small_image)

ahegaopeach_image = Image(get_file_handle("ahegaoanal.png"))
ahegaoanal_small_image = im.Scale(Image(get_file_handle("ahegaoanal.png")), 18, 18)
renpy.image("ahegaoanal_small", ahegaoanal_small_image)

yesanal_image = Image(get_file_handle("yesanal.png"))
yesanal_small_image = im.Scale(Image(get_file_handle("yesanal.png")), 18, 18)
renpy.image("yesanal_small", yesanal_small_image)

yespeach_image = Image(get_file_handle("yespeach.png"))
yespeach_small_image = im.Scale(Image(get_file_handle("yespeach.png")), 18, 18)
renpy.image("yespeach_small", yespeach_small_image)

knowpeach_image = Image(get_file_handle("knowpeach.png"))
knowpeach_small_image = im.Scale(Image(get_file_handle("knowpeach.png")), 18, 18)
renpy.image("knowpeach_small", knowpeach_small_image)

#### Had sex today
hadsextoday_image = Image(get_file_handle(modpath+"sex.png"))
hadsextoday_small_image = im.Scale(Image(get_file_handle(modpath+"sex.png")), 18, 18)
renpy.image("hadsextoday_small", hadsextoday_small_image)

### Thermometer - Arousal ####
tempbroke_image = Image(get_file_handle("tempbroke.png"))
temp90_image = Image(get_file_handle("temp90.png"))
temp80_image = Image(get_file_handle("temp80.png"))
temp70_image = Image(get_file_handle("temp70.png"))
tempnormal_image = Image(get_file_handle("tempnormal.png"))
tempblank_image = Image(get_file_handle("tempblank.png"))

######## Exhibitionist Fetish
knowbody_image = Image(get_file_handle("knowbody.png"))

ahegaoex_image = Image(get_file_handle("ahegaoex.png"))

nudebody_image = Image(get_file_handle("nudebody.png"))

underwear_image = Image(get_file_handle("underwear.png"))

bodyconcealed_image = Image(get_file_handle("bodyconcealed.png"))

bodyskimpy_image = Image(get_file_handle("bodyskimpy.png"))

bodypanties_image = Image(get_file_handle("bodypanties.png"))

bodybra_image = Image(get_file_handle("bodybra.png"))

###### Cum Fetish ##############

###### Anal Fetish ##############

###### Breeding Fetish ##############

###### Creampie Filling ##############

openpeach_image = Image(get_file_handle("openpeach.png"))

##### overtop Icons #####
bc_cum_image = Image(get_file_handle(modpath+"bc_cum.png"))
bc_cum_small_image = im.Scale(Image(get_file_handle(modpath+"bc_cum.png")), 18, 18)
renpy.image("bc_cum_image_small", bc_cum_small_image)

dislike_image = Image(get_file_handle("dislike.png"))
dislike_small_image = im.Scale(Image(get_file_handle(modpath+"dislike.png")), 18, 18)
renpy.image("dislike_small", dislike_small_image)

##### Status Icons #####
labbook_image = Image(get_file_handle("labbook.png"))
labbook_token_small_image = im.Scale(Image(get_file_handle("labbook.png")), 18, 18)
renpy.image("labbook_token_small", labbook_token_small_image)

creamcherry_small_image = im.Scale(Image(get_file_handle("creamcherry.png")), 18, 18)
renpy.image("creamcherry_small", creamcherry_small_image)
creamcherry_image = Image(get_file_handle("creamcherry.png"))

handprint_token_small_image = im.Scale(Image(get_file_handle("handprint.png")), 18, 18)
renpy.image("handprint_token_small", handprint_token_small_image)


bareback_image = Image(get_file_handle("bareback.png"))
bareback_small_image = im.Scale(Image(get_file_handle("bareback.png")), 18, 18)
renpy.image("bareback_small", bareback_small_image)
### deleted nocream
from __future__ import annotations
import renpy
from pathlib import Path
from renpy.display import im
from renpy.display.im import Image
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -100 python:
"""
#modpathheader = os.getcwd()
#modpathdir = sys.path[0]
#modpath = os.path.join(os.getcwd(), "/gui/extra_images/")
#modpath = r'modpathdir' + "/gui/extra_images/"
modpath = "/VTgui/extra_images/"

def get_file_handle(file_name: str) -> str | None:
    return next((x for x in renpy.exports.list_files() if file_name in x), None)

gf_token_small_image = im.Scale(Image(get_file_handle(modpath+"girlfriend.png")), 18, 18)
renpy.image("gf_token_small", gf_token_small_image)

paramour_token_small_image = im.Scale(Image(get_file_handle(modpath+"paramour.png")), 18, 18)
renpy.image("paramour_token_small", paramour_token_small_image)

harem_token_small_image = im.Scale(Image(get_file_handle(modpath+"harem.png")), 18, 18)
renpy.image("harem_token_small", harem_token_small_image)

parapoly_token_small_image = im.Scale(Image(get_file_handle(modpath+"parapoly.png")), 18, 18)
renpy.image("parapoly_token_small", parapoly_token_small_image)

virgin_token_small_image = im.Scale(Image(get_file_handle(modpath+"virgin.png")), 18, 18)
renpy.image("virgin_token_small", virgin_token_small_image)

matureteen_token_small_image = im.Scale(Image(get_file_handle("matureteen.png")), 18, 18)
renpy.image("matureteen_token_small", matureteen_token_small_image)

beezee_token_small_image = im.Scale(Image(get_file_handle("beezee.png")), 18, 18)
renpy.image("beezee_token_small", beezee_token_small_image)

vtcherries_small_image = im.Scale(Image(get_file_handle("vtcherries.png")), 18, 18)
renpy.image("vtcherries_small", vtcherries_small_image)
vtcherries_image = Image(get_file_handle("vtcherries.png"))

information_image = Image(get_file_handle("information.png"))
question_image = Image(get_file_handle("question.png"))
virgin_image = Image(get_file_handle(modpath+"virgin_token.png"))
bc_image = Image(get_file_handle(modpath+"bc_token.png"))
bc_cum_image = Image(get_file_handle("bc_cum.png"))
nobc_image = Image(get_file_handle(modpath+"nobc_token.png"))
beezee_image = Image(get_file_handle("beezee.png"))
knowbc_image = Image(get_file_handle("knowbc_token.png"))
dontknow_image = Image(get_file_handle("dontknow.png"))
parapoly_image = Image(get_file_handle(modpath+"parapoly.png"))
polyamorous_image = Image(get_file_handle(modpath+"harem.png"))
paramour_image = Image(get_file_handle(modpath+"paramour.png"))
rings_image = Image(get_file_handle(modpath+"rings.png"))
girlfriend_image = Image(get_file_handle(modpath+"girlfriend.png"))

hadsextoday_image = Image(get_file_handle(modpath+"sex.png"))
truevirgin_image = Image(get_file_handle(modpath+"virgin.png"))
dislike_image = Image(get_file_handle("dislike.png"))
vaghymen_image = Image(get_file_handle("vaghymen.png"))
pregnant_image = Image(get_file_handle("pregnant.png"))

ahegaocondom_image = Image(get_file_handle("ahegaocondom.png"))
wearcondom_image = Image(get_file_handle("wearcondom.png"))
nocondom_image = Image(get_file_handle("nocondom.png"))
knowcondom_image = Image(get_file_handle("knowcondom.png"))

bareback_image = Image(get_file_handle("bareback.png"))
nocream_image = Image(get_file_handle("nocream.png"))
knowpeach_image = Image(get_file_handle("knowpeach.png"))
openpeach_image = Image(get_file_handle("openpeach.png"))
yespeach_image = Image(get_file_handle("yespeach.png"))

ahegaomouth_image = Image(get_file_handle("ahegaomouth.png"))
openmouth_image = Image(get_file_handle("openmouth.png"))
bitelip_image = Image(get_file_handle("bitelip.png"))
pinklips_image = Image(get_file_handle("pinklips.png"))
knowlips_image = Image(get_file_handle("knowlips.png"))

ahegaopeach_image = Image(get_file_handle("ahegaoanal.png"))
handass_image = Image(get_file_handle("handass.png"))
yesanal_image = Image(get_file_handle("yesanal.png"))

ahegaovag_image = Image(get_file_handle("ahegaovag.png"))
openvag_image = Image(get_file_handle("openvag.png"))
spreadvag_image = Image(get_file_handle("spreadvag.png"))
vagclosed_image = Image(get_file_handle("vagclosed.png"))
knowvag_image = Image(get_file_handle("knowvag.png"))

ahegaoex_image = Image(get_file_handle("ahegaoex.png"))
nudebody_image = Image(get_file_handle("nudebody.png"))
underwear_image = Image(get_file_handle("underwear.png"))
bodybra_image = Image(get_file_handle("bodybra.png"))
bodypanties_image = Image(get_file_handle("bodypanties.png"))
bodyskimpy_image = Image(get_file_handle("bodyskimpy.png"))
bodyconcealed_image = Image(get_file_handle("bodyconcealed.png"))
knowbody_image = Image(get_file_handle("knowbody.png"))

ahegaothreesomes_image = Image(get_file_handle("ahegaothreesomes.png"))
threesometriad_image = Image(get_file_handle("threesometriad.png"))
opentriad_image = Image(get_file_handle("opentriad.png"))
knowthreesome_image = Image(get_file_handle("knowthreesome.png"))

ahegaotrance_image = Image(get_file_handle("ahegaotrance.png"))
heavytrance_image = Image(get_file_handle("heavytrance.png"))
starttrance_image = Image(get_file_handle("starttrance.png"))
donetrain_image = Image(get_file_handle("donetrain.png"))

ahegaoface_image = Image(get_file_handle("ahegaoface.png"))

ahegaotrance_token_small_image = im.Scale(Image(get_file_handle("ahegaotrance.png")), 18, 18)
renpy.image("ahegaotrance_token_small", ahegaotrance_token_small_image)

heavytrance_token_small_image = im.Scale(Image(get_file_handle("heavytrance.png")), 18, 18)
renpy.image("heavytrance_token_small", heavytrance_token_small_image)

starttrance_token_small_image = im.Scale(Image(get_file_handle("starttrance.png")), 18, 18)
renpy.image("starttrance_token_small", starttrance_token_small_image)

donetrain_token_small_image = im.Scale(Image(get_file_handle("donetrain.png")), 18, 18)
renpy.image("donetrain_token_small", donetrain_token_small_image)

handprint_token_small_image = im.Scale(Image(get_file_handle("handprint.png")), 18, 18)
renpy.image("handprint_token_small", handprint_token_small_image)

labbook_token_small_image = im.Scale(Image(get_file_handle("labbook.png")), 18, 18)
renpy.image("labbook_token_small", labbook_token_small_image)

topboxVT_image = Image(get_file_handle("topboxVT.png"))
labbook_image = Image(get_file_handle("labbook.png"))
matureteen_image = Image(get_file_handle("matureteen.png"))

claimedmouth_image = Image(get_file_handle("claimedmouth.png"))
claimedass_image = Image(get_file_handle("claimedass.png"))
claimedvag_image = Image(get_file_handle("claimedvag.png"))

ahegaoanal_small_image = im.Scale(Image(get_file_handle("ahegaoanal.png")), 18, 18)
renpy.image("ahegaoanal_small", ahegaoanal_small_image)

ahegaovag_small_image = im.Scale(Image(get_file_handle("ahegaovag.png")), 18, 18)
renpy.image("ahegaovag_small", ahegaovag_small_image)

ahegaomouth_small_image = im.Scale(Image(get_file_handle("ahegaomouth.png")), 18, 18)
renpy.image("ahegaomouth_small", ahegaomouth_small_image)

yesanal_small_image = im.Scale(Image(get_file_handle("yesanal.png")), 18, 18)
renpy.image("yesanal_small", yesanal_small_image)

yespeach_small_image = im.Scale(Image(get_file_handle("yespeach.png")), 18, 18)
renpy.image("yespeach_small", yespeach_small_image)

bareback_small_image = im.Scale(Image(get_file_handle("bareback.png")), 18, 18)
renpy.image("bareback_small", bareback_small_image)

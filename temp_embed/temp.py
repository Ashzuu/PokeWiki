import disnake,random
from disnake.ext import commands

def menu_1(poke:list):
    #dico_types = {"Plante":"<:grass:1066792442445180948>","Feu":"<:feu:1066792435360993390>","Eau":"<:water:1066792456005369949>","Ténèbres":"<:tenebres:1066792502109163640>","Spectre":"<:spectre:1066792499617730670>","Fée":"<:fee:1066792430264926251>","Acier":"<:acier:1066792420924198942>","Insecte":"<:insecte:1066792424229318736>","Poison":"<:poison:1066792449151877181>","Roche":"<:roche:1066792453014835311>","Psy":"<:psy:1066792450712158259>","Électrik":"<:electrik:1066792427865776248>","Glace":"<:glace:1066792439534325831>","Combat":"<:fight:1066792433028956291>","Vol":"<:vol:1066792438217318431>","Sol":"<:ground:1066792445033074819>"}
    neutre,efficace,resistant,super_efficace,super_resistant,immunise = [],[],[],[],[],[]
    if poke["resistances"] != None:
        for nb_types in range(len(poke["resistances"])):            
            if poke["resistances"][nb_types]["multiplier"] == 1:
                neutre.append(poke["resistances"][nb_types]["name"])
            elif poke["resistances"][nb_types]["multiplier"] == 2:
                efficace.append(poke["resistances"][nb_types]["name"])
            elif poke["resistances"][nb_types]["multiplier"] == 0.5:
                resistant.append(poke["resistances"][nb_types]["name"])
            elif poke["resistances"][nb_types]["multiplier"] == 0.25:
                super_resistant.append(poke["resistances"][nb_types]["name"])
            elif poke["resistances"][nb_types]["multiplier"] == 0:
                immunise.append(poke["resistances"][nb_types]["name"])
            elif poke["resistances"][nb_types]["multiplier"] == 4:
                super_efficace.append(poke["resistances"][nb_types]["name"])
# ------------------------------------------------------------------------ #
#                                  AFFICHAGE
# ------------------------------------------------------------------------ #
    menu1 = disnake.Embed(
        title="Sensibilités & Stats",
        color=disnake.Colour.blurple()
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png"
    ).set_thumbnail(poke["sprites"]["regular"]
    ).add_field(name="Stats", value="None" if poke["resistances"] == None else "PV : " + str(poke["stats"]["hp"]) + "\nAttaque : " + str(poke["stats"]["atk"]) + "\nDéfense : " + str(poke["stats"]["def"]) + "\nAttaque Spéciale : " + str(poke["stats"]["spe_atk"]) + "\nDéfense Spéciale : " + str(poke["stats"]["spe_def"]) + "\nVitesse : " + str(poke["stats"]["vit"]),inline=False
    ).add_field(name="Neutre : ", value=", ".join(neutre) if neutre != [] else "Aucun"
    ).add_field(name="Efficace : ", value=", ".join(efficace) if efficace != [] else "Aucun"
    ).add_field(name="Pas très efficace : ", value=", ".join(resistant) if resistant != [] else "Aucun"
    ).add_field(name="Super Efficace : ", value=", ".join(super_efficace) if super_efficace != [] else "Aucun"
    ).add_field(name="Très peu efficace : ", value=", ".join(super_resistant) if super_resistant != [] else "Aucun"
    ).add_field(name="Immunisé : ", value=", ".join(immunise) if immunise != [] else "Aucun")
    

    return menu1


def menu_2(poke:list):
    talents = []
    dico_types = {"Plante":"<:grass:1066792442445180948>","Feu":"<:feu:1066792435360993390>","Eau":"<:water:1066792456005369949>","Ténèbres":"<:tenebres:1066792502109163640>","Spectre":"<:spectre:1066792499617730670>","Fée":"<:fee:1066792430264926251>","Acier":"<:acier:1066792420924198942>","Insecte":"<:insecte:1066792424229318736>","Poison":"<:poison:1066792449151877181>","Roche":"<:roche:1066792453014835311>","Psy":"<:psy:1066792450712158259>","Électrik":"<:electrik:1066792427865776248>","Glace":"<:glace:1066792439534325831>","Combat":"<:fight:1066792433028956291>","Vol":"<:vol:1066792438217318431>","Sol":"<:ground:1066792445033074819>","Normal":"<:normal:1066792447490920528>","Dragon":"<:dragontype:1066792425680543754>"}
    shiny_number = random.randint(0,100)
    
    if poke["talents"] != None:
        for nb_talent in range(len(poke["talents"])):
            if poke["talents"][nb_talent]["tc"] == False:
                talents.append(poke["talents"][nb_talent]["name"])
            elif poke["talents"][nb_talent]["tc"] == True:
                talents.append("**_"+ poke["talents"][nb_talent]["name"]+"_** *(Talent caché)*")
    else:
        talents = None
    menu2 = disnake.Embed(
        title="Menu général de " + poke["name"]["fr"],
        description="*(Oh mais, ce ne serait pas un shiny !)*" if shiny_number == 50 and poke["sprites"]["shiny"] != False else "",
        color=disnake.Colour.blurple()
    ).set_thumbnail(poke["sprites"]["regular"] if shiny_number != 50 or poke["sprites"]["shiny"] == False else poke["sprites"]["shiny"]
    ).add_field(name="Type(s)", value= "None" if poke["types"] == None else dico_types[poke["types"][0]["name"]] + " " + poke["types"][0]["name"] if len(poke["types"]) == 1 else dico_types[poke["types"][0]["name"]] +" "+ poke["types"][0]["name"] + "  " + dico_types[poke["types"][1]["name"]] + " " + poke["types"][1]["name"] if len(poke["types"]) == 2 else "None",inline=False
    ).add_field(name="Talents", value=", ".join(talents) if talents != None else "None"
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png")
    return menu2

def menu_3(pkmn:list):
    """
    A changer :

    L'exp doit être afficher avec un espace tout les 3 chiffres
    """
    menu3 = disnake.Embed(
        title="Données complémentaires",
        color=disnake.Colour.random()
    ).add_field(name="EXP to level 100", value=str(pkmn["level_100"]) + " exp" if pkmn["level_100"] != None else "Aucun"
    ).add_field(name="Groupe(s) d'oeuf", value=", ".join(pkmn["egg_groups"]) if pkmn["egg_groups"] != None else "None", inline=False
    ).add_field(name="Taille & Poids", value="Taille : " + pkmn["height"] + "\nPoids : " + pkmn["weight"] if pkmn["height"] and pkmn["weight"] != None else "None"
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png"
    ).add_field(name="Catch rate", value=pkmn["catch_rate"], inline=False
    ).set_thumbnail(pkmn["sprites"]["regular"] if pkmn["sprites"]["regular"] != None else "https://cdn.discordapp.com/attachments/1064496577642766356/1065686675495329832/error.png") 
    return menu3

def erreur(msg:str):
    embed_erreur = disnake.Embed(
        title="Erreur !",
        description=msg,
        color=disnake.Colour.red()
    ).set_footer(text="Made by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png"
    ).set_thumbnail("https://cdn.discordapp.com/attachments/1064496577642766356/1065686675495329832/error.png")

    return embed_erreur


#############################################################################################################################################
##                                                           MENU EVOL                                                                     ##
#############################################################################################################################################

def menu_evol_1(poke:list):
    nb_pre_evol, nb_post_evol = len(poke["evolution"]["pre"]) if poke["evolution"]["pre"] != None else 0, len(poke["evolution"]["next"]) if poke["evolution"]["next"] != None else 0
    name_pre_evol, name_post_evol = [],[]
    
    if nb_pre_evol != 0:
        for nb in range(nb_pre_evol):
            name_pre_evol.append(poke["evolution"]["pre"][nb]["name"])
    if nb_post_evol != 0:
        for nb in range(nb_post_evol):
            name_post_evol.append(poke["evolution"]["next"][nb]["name"])
    embed_menuevol1 = disnake.Embed(
        title=poke["name"]["fr"],
        description="English name : " + poke["name"]["en"] + "\nJapenese Name : " + poke["name"]["jp"],
        color=disnake.Colour.random()

    ).set_thumbnail(poke["sprites"]["regular"]
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png"
    ).add_field(name="Pré", value=str(nb_pre_evol) + " : " +", ".join(name_pre_evol) if nb_pre_evol != 0 else nb_pre_evol
    ).add_field(name="Next",value=str(nb_post_evol) + " : " + ", ".join(name_post_evol) if nb_post_evol != 0 else nb_post_evol
    ).add_field(name="Condition",value=poke["name"]["fr"] + " :arrow_right: " + poke["evolution"]["next"][0]["condition"] + " :arrow_right: " + poke["evolution"]["next"][0]["name"] if nb_post_evol != 0 else "Aucune",inline=False)

   
    return embed_menuevol1

#
#
#

def menu_feedback_avis(titre:str,auteur:str,message:str):
    if auteur == "":
        auteur = "Non mentionné"
    embed_menu = disnake.Embed(
        title=titre,
        description=f"**Message de {auteur} :** \n{message}"
    ).set_footer(text="Message envoyé automatiquement depuis la commande /poke_feedback ou /poke_idee")

    return embed_menu
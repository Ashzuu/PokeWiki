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

#############################################################################################################################################
##                                                           MENU FEEDBACKS                                                                ##
#############################################################################################################################################

def menu_feedback_avis(titre:str,auteur:str,message:str):
    if auteur == "":
        auteur = "Non mentionné"
    embed_menu = disnake.Embed(
        title=titre,
        description=f"**Message de {auteur} :** \n{message}"
    ).set_footer(text="Message envoyé automatiquement depuis la commande /poke_feedback ou /poke_idee")

    return embed_menu


#############################################################################################################################################
##                                                           MENU GAMES                                                                    ##
#############################################################################################################################################

def menu_guess_presentation(types:str):
    embed = disnake.Embed(
        title=f"Devine le poids de ce Pokémon !" if types == "poids" else f"Devine la taille de ce Pokémon !",
        description="Le but est simple : Un Pokémon va apparaitre, et vous devez deviner le poids de celui-ci ! \n:warning: ***Vous devez écrire uniquement un nombre, sans lettres ! (vous pouvez cependant utiliser des nombres à virgules !)***" if types=="poids" else "Le but est simple : Un Pokémon va apparaitre, et vous devez deviner la taille de celui-ci ! \n:warning: ***Vous devez écrire uniquement un nombre, sans lettres ! (vous pouvez cependant utiliser des nombres à virgules !)***",
        color=disnake.Color.blurple()
    ).set_thumbnail(url="https://cdn.discordapp.com/attachments/1064496577642766356/1078769557575041066/Pikaaaa.png"
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png")

    return embed


def menu_guess(pokemon,types):
    embed=disnake.Embed(
        title="Devine le poids de ce Pokémon !" if types=="poids" else "Devine la taille de ce Pokémon !",
        description="Le jeu est simple ! Fais une proposition de son poids ! Tu as le droit à 10 propositions, après tu as perdu !",
        color=disnake.Colour.random()
    ).set_thumbnail(url="https://cdn.discordapp.com/attachments/1064496577642766356/1078769557575041066/Pikaaaa.png"
    ).set_image(pokemon["sprites"]["regular"]
    ).add_field(name=pokemon["name"]["fr"], value="A ton avis, ce Pokémon pèse combien ? \n:warning: **Merci d'écrire seulement un nombre !!**")

    return embed


def menu_win_games(tours,types):
    embed=disnake.Embed(
        title="Bravo !",
        description=f"Vous avez réussi, vous pouvez vous féliciter ! En plus de ça, vous avez trouvé le poids de ce Pokémon en {tours} tours !" if types=="poids" else f"Vous avez réussi, vous pouvez vous féliciter ! En plus de ça, vous avez trouvé la taille de ce Pokémon en {tours} tours !"
    ).set_thumbnail(url="https://cdn.discordapp.com/attachments/1064496577642766356/1078769557575041066/Pikaaaa.png"
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png")

    return embed
    
def menu_loose_games():
    embed=disnake.Embed(
        title="Ah bah bien...",
        description=f"Malgré les 10 tours, et les indications de notre cher bot, vous n'avez pas réussi... Je suis extrêment déçu de votre comportement !"
    ).set_thumbnail(url="https://cdn.discordapp.com/attachments/1064496577642766356/1078769557860266015/pikaa_vener.gif"
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png")

    return embed

def menu_plus_lourd(pokemon1, pokemon2):
    
    embed = disnake.Embed(
        title="Quel Pokemon est le plus lourd ?",
        description="Bienvenue dans un petit jeu ! Le but est de trouver le Pokemon le plus lourd !",
        color=disnake.Colour.random()
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png"
    ).add_field(name="Qui est le plus lourd entre :", value=":one: " + pokemon1["name"]["fr"] + "\n:two: " + pokemon2["name"]["fr"] +"\n\nAttention vous avez 20 secondes pour répondre !")
    
    return embed

def menu_win(pokemon):
    embed=disnake.Embed(
        title="Féliciations !",
        description=f"Oh mais que vois-je ! *Vous avez réussi*, je suis très fier de vous bravo ! Pour rejouer, tu peux exécuter de nouveau la commande, si tu le souhaites bien sûr ! \n**La réponse était donc bien : " + pokemon["name"]["fr"] + "**",
        color=disnake.Colour.green()
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png"
    ).set_thumbnail("https://cdn.discordapp.com/attachments/1064496577642766356/1078769557575041066/Pikaaaa.png")

    return embed

def menu_loose(pokemon):
    embed=disnake.Embed(
        title="Pardon !",
        description=f"Je n'en crois pas mes yeux, vous venez de vous tromper ! Pikachu n'est pas content... Rejouez et changez moi ça, pour que Pikachu soit content !\n**La bonne réponse était donc : " + pokemon["name"]["fr"] + "**",
        color=disnake.Color.red()
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png"
    ).set_thumbnail("https://cdn.discordapp.com/attachments/1064496577642766356/1078769557860266015/pikaa_vener.gif")

    return embed

def menu_guess_pokemon(pokemon):
    embed = disnake.Embed(
        title="Trouve le Pokémon",
        description="Voici un pokémon, tu dois connaitre son nom et l'écrire à la suite de ce message !",
        color=disnake.Colour.blurple()
    ).set_image(url=pokemon["sprites"]["regular"]
    ).set_footer(text="Data provenant de Poképedia \nMade by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png"
    )

    return embed


def log_embed(cas:str):
    embed = disnake.Embed(
        title="Message du bot !",
        description=f"Le bot vous envoie un message pour le cas suivant : {cas}",
        color=disnake.Color.blurple()
    ).set_footer(text="Made by Ashz#6909", icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png")

    return embed


def embed_command():
    embed:disnake.Embed = disnake.Embed(
            title="Commandes disponibles sur le bot",
            color=disnake.Color.blurple()
        ).add_field(name="Commandes Pokédex",value="</poke_info:1078821926706872355> : Afficher les informations générales d'un Pokémon\n</shiny:1078684235935780914> : Afficher le sprite shiny d'un Pokémon\n</poke_evol:1078821926706872358> : Affiche la ligne évolutive d'un Pokémon\n</list_poke:1078821926706872356> Affiche les Pokémon d'une génération donnée\n",inline=False
        ).add_field(name="Général",value="</help:1078821926706872357> : Afficher une page permettant d'obtenir de l'assitance avec le bot !\n</info:1078821926706872352> : Afficher des informations à propos du bot\n</ping:1078821926706872350> Afficher les différentes informations de connexion du bot\n</poke_feedback:1078821926706872351> : Donner votre avis sur le bot\n</poke_idee:1078821926706872354> : Donner des idées concernants le bot",inline=False
        ).add_field(name="Jeux",value="</games:1078985626327732235> : Petits jeux sur le thème de Pokémon",inline=False
        ).add_field(name=":warning: Attention !",value="***Il faut écrire correctement le nom du Pokémon pour toutes les commandes où le Pokémon est demandé, même avec les accents !***",inline=False
        ).set_footer(text="Made by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png")
    
    return embed

#############################################################################################################################################
##                                                           MENU CONSTRUCTOR                                                              ##
#############################################################################################################################################

def constructor_embed(titre:str=None,description:str=None,icon=None,image=None):
    embed1 = disnake.Embed(
        title=titre,
        description=description,
        color=disnake.Colour.blurple()
    ).set_thumbnail(url=icon
    ).set_image(url=image
    ).set_footer(text="Made by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png")

    return embed1
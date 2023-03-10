import disnake
from disnake.ext import commands
import temp_embed.temp as tt
import config as c
"""
A AJOUTER/MODIFIER :

-> Finir l'affichage simple de résumé d'un Pokemon -> FAIT
-> Pouvoir interagir avec le bot -> FAIT

"""
class ShinyModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    @commands.slash_command(name="shiny",description="Affiche le pokemon en version shiny",dm_permission=False)
    async def shiny(self,
                        inter:disnake.CommandInter,
                        choix_poke:str=commands.Param(name="pokemon",description="Choisissez un Pokemon de la génération 1 uniquement !")
                        ):
        print(f"[COMMANDE SHINY] dans le serveur {inter.guild.name}")
        try:    
            await inter.send(content=f"Recherche de {choix_poke} en cours...")
            choix_poke = choix_poke.capitalize()
            data = c.get_url_api()
            id = None
            for i in range(len(data)):
                if data[i]["name"]["fr"] == choix_poke:
                    id = i
            if id == None:
                return await inter.edit_original_message(content="",embed=tt.erreur("Pokemon introuvable dans la base de donnée"))
            pkmn = data[id]
            
            if pkmn["sprites"]["shiny"] == None:
                return await inter.edit_original_message(content="",embed=tt.erreur(f"{choix_poke} n'a pas de version shiny"))
            await inter.edit_original_message(content="",embed=tt.constructor_embed(titre=f":sparkles: _{choix_poke}_ :sparkles:", description=f"Vous avez demandé la version shiny de {choix_poke}, vous l'avez ! Elle est *belle non* ! Non ? Déçu...",image=pkmn["sprites"]["shiny"])
            )
        except:
            print(f"Attention, une erreur est survenue lors de l'exécution de /shiny, ayant comme paramètre(s) : {choix_poke} dans le serveur {inter.guild.name}")
            await inter.edit_original_message(content="", embed=tt.erreur("Une erreur est survenue, veuillez contacter l'administrateur afin de connaitre la cause de ce bug !"),ephemeral=True)
            await inter.delete_original_message(delay=7.0)


        

def setup(self):
    self.add_cog(ShinyModule(self))
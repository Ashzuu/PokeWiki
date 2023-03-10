import disnake,random
from disnake.ext import commands
import temp_embed.temp as tt
import config as c

class Paginator(disnake.ui.View):
    
    message:disnake.Message
    def __init__(self, poke_name:str,list_poke:list):
        self.poke_name = poke_name
        self.pkmn = list_poke
        self.data = c.get_url_api()
        super().__init__(timeout=60.0)

    async def on_timeout(self) -> None:
        await self.message.delete()

    @disnake.ui.button(emoji="⬅️",label="",style=disnake.ButtonStyle.grey)
    async def previous_button(self,button:disnake.ui.Button,inter:disnake.MessageInteraction):
        if self.pkmn["evolution"]["pre"] != None:
            data = self.data
            id_last = self.pkmn["evolution"]["pre"][len(self.pkmn["evolution"]["pre"])-1]["pokedexId"]
            self.pkmn = data[id_last]
            await inter.response.edit_message(embed=tt.menu_evol_1(self.pkmn),view=self) 

    @disnake.ui.button(emoji="➡️",label="",style=disnake.ButtonStyle.grey)
    async def next_button(self,button:disnake.ui.Button,inter:disnake.MessageInteraction):
        if self.pkmn["evolution"]["next"] != None:
            data = self.data
            id_next = self.pkmn["evolution"]["next"][0]["pokedexId"]
            self.pkmn = data[id_next]
            await inter.response.edit_message(embed=tt.menu_evol_1(self.pkmn),view=self)



class EvolModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    @commands.slash_command(name="poke_evol",description="Affiche les évolutions du Pokemon s'il y en a")
    async def evolution(self, inter:disnake.CommandInter, nom:str=commands.Param(name="pokemon")):
        print(f"[COMMANDE POKE_EVOL] sur le server {inter.guild.name}")
        
        try:
            await inter.send(content=f"Chargement du Pokémon {nom} en cours, veuillez patienter !", ephemeral=True)
            nom = nom.capitalize()
            data = c.get_url_api()
        ############################################## FIND_POKE ################################################
            id = None
            shiny_number = random.randint(0,100)
            for i in range(len(data)):
                if data[i]["name"]["fr"] == nom:
                    id = i
            """
            if id == None:
                await inter.edit_original_message(content="Votre Pokemon est introuvable dans la base de données... Vérifiez bien si l'orthographe est correct !")
                await inter.delete_original_message(delay=5)
                return
            """
            pkmn = data[id]
            view = Paginator(nom,pkmn)
            await inter.edit_original_message(content="",embed = tt.menu_evol_1(pkmn),view=view)
            view.message = await inter.original_response()
        except:
            print(f"Attention, une erreur est survenue lors de l'exécution de /poke_evol ayant comme paramètres : {nom} sur le sevreur {inter.guild.name}")
            await inter.edit_original_message(content="", embed=tt.erreur("Une erreur est survenue, veuillez contacter l'administrateur afin de connaitre la cause de ce bug !"))

            

def setup(self):
    self.add_cog(EvolModule(self))

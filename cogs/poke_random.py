import disnake, random
from disnake.ext import commands
import temp_embed.temp as tt
import config as c


class RandomModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    choix_mode = ["Sprite only","Sprite + informations principales sur le Pokémon"]
    @commands.slash_command(name="poke_random",description="Donne un pokémon random du Pokédex !")
    async def random(self, 
                    inter:disnake.CommandInter,
                    choix:str = commands.param(name="mode",description="Choisissez la façon dont vous voulez que le Pokémon apparaisse",choices=choix_mode)):
        print(f"[COMMANDE RANDOM] sur le server {inter.guild.name}")
        await inter.send("*Recherche d'un Pokemon qui pourrait correspondre (ou pas) à vos attentes*", ephemeral=True)
        data = c.get_url_api()
        pkmn = data[random.randint(0,len(data))]
        if choix == "Sprite only":
            await inter.edit_original_message(content="", embed=tt.constructor_embed(pkmn["name"]["fr"], description="Voici un Pokémon parmi tout le Pokédex",image=pkmn["sprites"]["regular"])
            )
        elif choix == "Sprite + informations principales sur le Pokémon":
            await inter.edit_original_message(content="", embed=tt.menu_2(pkmn))
        
def setup(self):
    self.add_cog(RandomModule(self))
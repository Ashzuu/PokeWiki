import disnake
from disnake.ext import commands
import temp_embed.temp as tt

class PingModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    @commands.slash_command(name="ping",description="Commande permettant de connaitre des infos (dont la latence) sur le bot")
    async def ping(self, inter:disnake.CommandInter):
        await inter.send(embed=tt.constructor_embed(titre=f"{self.__bot.user.name}",description=f":robot: La latence de monsieur est de **__{round(self.__bot.latency*1000,0)}ms__**",icon=self.__bot.user.avatar
            ).add_field(name=":computer: Hébergement",value="*Local*"
            ).add_field(name=":bank: API(s)", value="*PokeAPI made by Yarkis*",inline=False
            ).add_field(name=":books: Bibliothèque(s) Python", value="*Disnake*")
    )

def setup(self):
    self.add_cog(PingModule(self))
import disnake
from disnake.ext import commands
import temp_embed.temp as tt

class HelpCommandsModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    @commands.slash_command(name="help_commands",description="Une commande permettant d'obtenir la liste des commandes du bot")
    async def help_commands(self,inter:disnake.CommandInter):
        print(f"[COMMANDE HELP COMMANDS] éxécuté sur {inter.guild.name}")
        await inter.send(embed=tt.embed_command().set_thumbnail(url=self.__bot.user.avatar if self.__bot.user.avatar else "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/1/17/latest/20151017104012/Infernape.png/1200px-Infernape.png"))

def setup(self):
    self.add_cog(HelpCommandsModule(self))
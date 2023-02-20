import disnake,requests,random
from disnake.ext import commands
import temp_embed.temp as tt


class HelpModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    @commands.slash_command(name="help",description="Si vous avez un souci avec le bot, n'hésitez pas à nous le faire savoir !")
    async def evolution(self, inter:disnake.CommandInter):
        print(f"[COMMANDE HELP] sur le server {inter.guild.name}")
        await inter.send(embed=disnake.Embed(
            title="Assistance du bot",
            description="Vous avez un souci avec le bot ? N'hésitez pas à envoyer un message à Ashz#6909, ou bien à rejoindre le serveur support : https://discord.gg/BVnZMzZjSC",
            color=disnake.Color.blurple()
        ).add_field(name="Donnez votre avis", value="``/poke_feedback`` : Une page devrait s'ouvrir et vous pourrez mettre votre avis sur cette page",inline=False
        ).add_field(name="Idées de fonctionnalité",value="``/poke_idees``",inline=False)
        )
        
def setup(self):
    self.add_cog(HelpModule(self))

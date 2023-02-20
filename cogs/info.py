import disnake
from disnake.ext import commands
import temp_embed.temp as tt

class InfoModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    @commands.slash_command(name="info",description="Une commande permettant d'obtenir des informations à propos du bot")
    async def info(self,inter:disnake.CommandInter):
        print(f"[COMMANDE INFO] éxécuté sur {inter.guild.name}")
        await inter.send(embed=disnake.Embed(
            title="Informations sur le bot",
            description="Voici les informations à propos du bot",
            color=disnake.Color.blurple()
        ).add_field(name=":robot: Créateur du bot",value=f"``Ashz#6909``",inline=False
        ).add_field(name=":robot: Serveur support",value=f"https://discord.gg/BVnZMzZjSC",inline=False
        ).add_field(name=":robot: Nombre de serveur", value=f"Je suis actuellement sur {len(inter.bot.guilds)} serveur !",inline=False
        ).add_field(name="Créé le",value="``12/02/2023``",inline=False
        ).set_thumbnail(url=self.__bot.user.avatar if self.__bot.user.avatar else "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/1/17/latest/20151017104012/Infernape.png/1200px-Infernape.png"
        ).set_footer(text="Made by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png")
        )

def setup(self):
    self.add_cog(InfoModule(self))
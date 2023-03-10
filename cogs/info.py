import disnake, datetime, sys
from disnake.ext import commands
import temp_embed.temp as tt

class InfoModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot
        self.time_connected = datetime.datetime.now()


    @commands.slash_command(name="info",description="Une commande permettant d'obtenir des informations à propos du bot")
    async def info(self,inter:disnake.CommandInter):
        print(f"[COMMANDE INFO] éxécuté sur {inter.guild.name}")
        duree_connected = str(datetime.datetime.now() - self.time_connected)
        await inter.send(embed=tt.constructor_embed(titre="Informations sur le bot", description="Voici les informations à propos du bot", icon=self.__bot.user.avatar if self.__bot.user.avatar else "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/1/17/latest/20151017104012/Infernape.png/1200px-Infernape.png"
        ).add_field(name=":robot: Créateur du bot",value=f"``Ashz#6909``",inline=False
        ).add_field(name=":robot: Serveur support",value=f"https://discord.gg/BVnZMzZjSC",inline=False
        ).add_field(name=":robot: Nombre de serveur", value=f"Je suis actuellement sur {len(inter.bot.guilds)} serveur !",inline=False
        ).add_field(name=":robot: Créé le",value="``12/02/2023``",inline=False
        ).add_field(name=":robot: Connecté depuis", value=f"Le bot est connecté depuis {duree_connected[:-7]}")
        )

def setup(self):
    self.add_cog(InfoModule(self))
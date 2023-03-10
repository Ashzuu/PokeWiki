import disnake,random
from disnake.ext import commands
import temp_embed.temp as tt
    
class UserCommandsModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    @commands.user_command(name="attack")
    async def info_usercommand(self,inter:disnake.CommandInter,user:disnake.Member):
        list_gif = [
            "https://cdn.discordapp.com/attachments/1081319750694609006/1081319899051343907/gif1.gif",
            "https://cdn.discordapp.com/attachments/1081319750694609006/1081319899412049970/gif2.gif",
            "https://cdn.discordapp.com/attachments/1081319750694609006/1081319899860844634/gif3.gif",
            "https://cdn.discordapp.com/attachments/1081319750694609006/1081319900267683900/gif4.gif",
            "https://cdn.discordapp.com/attachments/1081319750694609006/1081319900716482711/gif5.gif",
            "https://cdn.discordapp.com/attachments/1081319750694609006/1081319901177847900/gif6.gif",
            "https://cdn.discordapp.com/attachments/1081319750694609006/1081319901542756392/gif7.gif",
            "https://cdn.discordapp.com/attachments/1081319750694609006/1081319901903462441/gif8.gif",
            "https://cdn.discordapp.com/attachments/1081319750694609006/1081319902306119840/gif9.gif"
        ]

        await inter.send(content=f"{user.mention} Fais gaffe !",embed=tt.constructor_embed(titre="OH !", description="Un Pokémon viens de t'attaquer, esquive !", image=list_gif[random.randint(0,len(list_gif)-1)]
            )
        )


    @commands.user_command(name="pokeban", dm_permission=False)
    async def ban_usercommand(self,inter:disnake.CommandInter, user:disnake.Member):
        print(f"[COMMANDE BAN] a été exécuté sur {inter.guild.name}")
        if user == self.__bot.user:
            return await inter.send(embed=tt.erreur("Vous ne pouvez pas ban le bot !"))
        elif not user.top_role < inter.user.top_role:
            return await inter.send(embed=tt.erreur("Vous ne pouvez pas ban un membre au dessus de vous !"))
        elif not inter.user.guild_permissions.ban_members:
            return await inter.send(embed=tt.erreur("Vous ne pouvez pas ban qui que ce soit, vous n'avez pas les perms ! Noeunoeu !"))
        else:
            await user.ban()
            await inter.send(embed=disnake.Embed(
                title="Ban",
                description=f"{user.name} a été ban !"
            ))


def setup(self):
    self.add_cog(UserCommandsModule(self))
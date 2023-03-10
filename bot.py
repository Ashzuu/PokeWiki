import disnake,os
from disnake.ext import commands
import config as c
import temp_embed.temp as tt

class Bot(commands.InteractionBot):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args,**kwargs)
    

  async def on_connect(self) -> None:
      print(f"Connecté en tant que {self.user}")
      channel:disnake.TextChannel = await self.fetch_channel(1080812921543725108)
      await channel.send(embed=tt.log_embed("Connexion du bot").set_thumbnail(url=self.user.avatar))

  async def on_guild_join(self,guild:disnake.Guild) -> None:
    print(f"Le bot a été ajouté sur un nouveau serveur {guild.name}")
    channel:disnake.TextChannel = await self.fetch_channel(1080812921543725108)
    channel.send(embed=tt.constructor_embed(titre="Nouveau serveur !", description=f"Le bot viens d'être ajouté sur un nouveau serveur, qui est {guild.name}", icon=guild.icon))
  
  async def on_error(self,event:disnake.Event):
    print(f"Attention, il y a eu une erreur de type : {event.name}")
    channel:disnake.TextChannel = await self.fetch_channel(1080812921543725108)
    await channel.send(embed=tt.log_embed(f"Il y a eu une erreur, que voici : {event}").set_thumbnail(url=self.user.avatar))


  async def on_ready(self):
    acivite_streaming = disnake.Activity(name="Venez voir ce stream, je vous promets c'est sympa !",url="https://www.twitch.tv/ashzzzu",type=disnake.ActivityType.streaming)
    await self.change_presence(activity=acivite_streaming)

if __name__ == "__main__":
  intents = disnake.Intents.all()

  bot = Bot(
    intents = intents,
    test_guilds = [1033089314755719178]
  )

  for file in os.listdir("./cogs"):
    if file.endswith(".py"):
      bot.load_extension(f"cogs.{file[:-3]}")
      print(f"Le module {file[:-3]} a bien été chargé")


  bot.run(c.get_token("Pokebot"))
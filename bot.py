import disnake,os
from disnake.ext import commands

class Bot(commands.InteractionBot):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args,**kwargs)

  async def on_connect(self) -> None:
      print(f"Connecté en tant que {self.user}")

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


  bot.run(token)
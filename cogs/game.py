import disnake, random, asyncio
from disnake.ext import commands
import temp_embed.temp as tt
import config as c

class GameModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    list_jeux = {"Devine le poids":1,"Devine la taille":2, "Quel Pokemon est le plus lourd ?":3, "Devine le Pokémon":4}
    @commands.slash_command(name="games",description="Une commande permettant de jouer avec le bot")
    async def games(self,inter:disnake.CommandInter, games:int=commands.Param(name="jeu",description="A quel jeu voulez-vous jouer ?",choices=list_jeux)):
        print(f"[COMMANDE GAME] éxécuté avec le choix {games} sur {inter.guild.name}")
        
        def checkEmoji(reaction:disnake.Reaction,user:disnake.Member):
            return inter.user == user and message.id == reaction.message.id and str(reaction.emoji) == "1️⃣" or str(reaction.emoji) == "2️⃣"
        
        def checkButton(inter:disnake.MessageInteraction):
            return inter.component.custom_id == "ready" or inter.component.custom_id == "stop"
        
        def checkButton_restart(inter:disnake.MessageInteraction):
            return inter.component.custom_id == "restart"
        
        def checkMessage(message:disnake.Message):
            return inter.author.name == message.author.name 
        


        data = c.get_url_api()

        number1 = random.randint(0, len(data))
        number2 = random.randint(0, len(data))
        pokemon1 = data[number1]
        pokemon2 = data[number2]
            
        if games==1:
            buttons = [
                disnake.ui.Button(label="J'ai peur !", style=disnake.ButtonStyle.danger, custom_id="stop"),
                disnake.ui.Button(label="Je suis prêt !", style=disnake.ButtonStyle.success, custom_id="ready")
            ]
            await inter.send(embed=tt.menu_guess_presentation("poids"),components=buttons)
            buttoninter:disnake.MessageInteraction = await self.__bot.wait_for(event="button_click", check=checkButton)
            if buttoninter.component.custom_id == "ready":
                pkmn = data[random.randint(0,len(data))]
                weight_pkmn:float = float(pkmn["weight"][:-3].replace(",","."))
                i = 0
                await inter.edit_original_message(embed=tt.menu_guess(pkmn,"poids"), components=None)
                while i < 10:
                    message:disnake.Message = await self.__bot.wait_for("message", check=checkMessage)
                    i+= 1
                    #print(message.content)
                    try:
                        proposition = float(message.content.replace(',',"."))
                    except:
                        proposition = 50.0
                    await message.delete()
                    if proposition > weight_pkmn:
                        await inter.send(content=f"{proposition}kg est trop grand ! Il vous reste {10-i} propositions !",embed=None, ephemeral=True, delete_after=5.0)
                    elif proposition < weight_pkmn:
                        await inter.send(content=f"{proposition}kg est trop petit ! Il vous reste {10-i} propositions !",embed=None, ephemeral=True, delete_after=5.0)
                    else:
                        await inter.delete_original_message()
                        await inter.send(embed=tt.menu_win_games(i,"poids"))
                        return
                    await inter.delete_original_message()
                    await inter.send(embed=tt.menu_loose_games())
            elif buttoninter.component.custom_id == "stop":
                return await inter.send(embed=tt.erreur("L'utilisateur a décidé d'arrêter le jeu !"),delete_after=10.0)

            
        elif games == 2:
            buttons = [
                disnake.ui.Button(label="J'ai peur !", style=disnake.ButtonStyle.danger, custom_id="stop"),
                disnake.ui.Button(label="Je suis prêt !", style=disnake.ButtonStyle.success, custom_id="ready")
            ]
            await inter.send(embed=tt.menu_guess_presentation("taille"),components=buttons)
            buttoninter:disnake.MessageInteraction = await self.__bot.wait_for(event="button_click", check=checkButton)
            if buttoninter.component.custom_id == "ready":
                pkmn = data[random.randint(0,len(data))]
                weight_pkmn:float = float(pkmn["height"][:-2].replace(",","."))
                i = 0
                await inter.edit_original_message(embed=tt.menu_guess(pkmn,"taille"), components=None)
                while i < 10:
                    message:disnake.Message = await self.__bot.wait_for("message", check=checkMessage)
                    i+= 1
                    #print(message.content)
                    try:
                        proposition = float(message.content.replace(',',"."))
                    except:
                        proposition = 50.0
                    await message.delete()
                    if proposition > weight_pkmn:
                        await inter.send(content=f"{proposition}m est trop grand ! Il vous reste {10-i} propositions !",embed=None, ephemeral=True, delete_after=5.0)
                    elif proposition < weight_pkmn:
                        await inter.send(content=f"{proposition}m est trop petit ! Il vous reste {10-i} propositions !",embed=None, ephemeral=True, delete_after=5.0)
                    else:
                        await inter.delete_original_message()
                        await inter.send(embed=tt.menu_win_games(i,"taille"))
                        return
                await inter.delete_original_message()
                await inter.send(embed=tt.menu_loose_games())
            elif buttoninter.component.custom_id == "stop":
                return await inter.send(embed=tt.erreur("L'utilisateur a décidé d'arrêter le jeu !"),delete_after=10.0)

        elif games==3:  
            weight_pkmn1:float = float(pokemon1["weight"][:-3].replace(",","."))
            weight_pkmn2:float = float(pokemon2["weight"][:-3].replace(",","."))  
            await inter.send(embed=tt.menu_plus_lourd(pokemon1,pokemon2))
            message = await inter.original_response()
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            try:
                await asyncio.sleep(1)
                reaction, user = await self.__bot.wait_for("reaction_add",timeout=20.0, check=checkEmoji)
                if weight_pkmn1 > weight_pkmn2:
                    if reaction.emoji == "1️⃣":
                        await inter.edit_original_response(embed=tt.menu_win(pokemon1))
                    else:
                        await inter.edit_original_response(embed=tt.menu_loose(pokemon1))
                elif weight_pkmn1 < weight_pkmn2:
                    if reaction.emoji == "2️⃣":
                        await inter.edit_original_response(embed =tt.menu_win(pokemon2))
                    else:
                        await inter.edit_original_response(embed =tt.menu_loose(pokemon2))
                await message.clear_reactions()
            except:
                await inter.delete_original_message()
                await inter.send(embed=tt.erreur(msg="Une erreur s'est produite !"),ephemeral=True)
        elif games==4:
            await inter.send(embed=tt.menu_guess_pokemon(pokemon1))
            message:disnake.Message = await self.__bot.wait_for("message", check=checkMessage)
            await message.delete(delay=0.5)
            print(message.content)
            if message.content == pokemon1["name"]["fr"]:
                await inter.edit_original_message(embed=tt.menu_win(pokemon1))
            elif message.content != pokemon1["name"]["fr"]:
                await inter.edit_original_message(embed=tt.menu_loose(pokemon1))
def setup(self):
    self.add_cog(GameModule(self))
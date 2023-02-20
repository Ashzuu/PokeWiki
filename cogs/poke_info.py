import disnake,requests,random
from disnake.ext import commands
import temp_embed.temp as tt
import config as c


class Paginator(disnake.ui.View):
    message:disnake.Message
    def __init__(self, pokemon_id:int,liste_poke:list):
        self.pokemon_id = pokemon_id
        self.pkmn = liste_poke
        super().__init__(timeout=60.0)

    async def on_timeout(self) -> None:
        await self.message.delete()

    @disnake.ui.button(emoji="⬅️",label="- 1",style=disnake.ButtonStyle.blurple)
    async def previous_button(self,button:disnake.ui.Button,inter:disnake.MessageInteraction):
        if self.pokemon_id != 0:
            self.pokemon_id -=1
        else:
            self.pokemon_id = 1008
        self.afficheur.label = f"ID : {self.pokemon_id}"
        await inter.response.edit_message(embed=tt.menu_2(self.pkmn[self.pokemon_id]),view=self)

    @disnake.ui.button(emoji="🔥",label="Page 1",style=disnake.ButtonStyle.red)
    async def page_1(self,button:disnake.ui.button,inter:disnake.MessageInteraction):
        await inter.response.edit_message(embed=tt.menu_1(self.pkmn[self.pokemon_id]),view=self)

    @disnake.ui.button(label=f"ID:",style=disnake.ButtonStyle.blurple)
    async def afficheur(self,button:disnake.ui.Button,inter:disnake.MessageInteraction):
        self.afficheur.label = f"ID : {self.pokemon_id}"
        await inter.response.edit_message(embed=tt.menu_2(self.pkmn[self.pokemon_id]),view=self)

    @disnake.ui.button(emoji="🍃",label="Page 2",style=disnake.ButtonStyle.green)
    async def page_2(self,button:disnake.ui.button,inter:disnake.MessageInteraction):
        await inter.response.edit_message(embed=tt.menu_3(self.pkmn[self.pokemon_id]),view=self)

    @disnake.ui.button(emoji="➡️",label="+ 1",style=disnake.ButtonStyle.blurple)
    async def next_button(self,button:disnake.ui.Button,inter:disnake.MessageInteraction):
        if self.pokemon_id != 1008:
            self.pokemon_id +=1
        else:
            self.pokemon_id = 0
        self.afficheur.label = f"ID : {self.pokemon_id}"
        await inter.response.edit_message(embed=tt.menu_2(self.pkmn[self.pokemon_id]),view=self)


class PokeInfo_Module(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    @commands.slash_command(name="poke_info",description="Sélectionner un Pokemon pour afficher son résumé général",dm_permission=False)
    async def poke_info(self,
                        inter:disnake.CommandInter,
                        choix_poke:str=commands.Param(name="pokemon",description="Choisissez un Pokemon de la génération 1 uniquement !")
                        ):
        print(f"[COMMANDE POKE_INFO] dans le serveur {inter.guild.name}")
        try:    
            lien_api_final = c.get_url_api()
            await inter.send(f"*En cours de chargement... Nous cherchons {choix_poke} dans notre petite base de donnée* (enfin petite petite... Tout est relatif)")
            choix_poke = choix_poke.capitalize()
            data = requests.get(lien_api_final).json()
        ############################################## FIND_POKE ################################################
            id = None
            shiny_number = random.randint(0,100)
            for i in range(len(data)):
                if data[i]["name"]["fr"] == choix_poke or data[i]["name"]["en"] == choix_poke:
                    id = i
            if id == None:
                await inter.edit_original_message(content="", embed=tt.erreur(msg="Votre Pokemon est introuvable dans la base de données... Vérifiez bien si l'orthographe est correct !"))
                await inter.delete_original_message(delay=7)
                return
            pkmn = data[id]
        ############################################# RESISTANCES ################################################
            neutre,efficace,resistant,super_efficace,super_resistant,immunise = [],[],[],[],[],[]
            for nb_types in range(len(pkmn["resistances"])):            
                if pkmn["resistances"][nb_types]["multiplier"] == 1:
                    neutre.append(pkmn["resistances"][nb_types]["name"])
                elif pkmn["resistances"][nb_types]["multiplier"] == 2:
                    efficace.append(pkmn["resistances"][nb_types]["name"])
                elif pkmn["resistances"][nb_types]["multiplier"] == 0.5:
                    resistant.append(pkmn["resistances"][nb_types]["name"])
                elif pkmn["resistances"][nb_types]["multiplier"] == 0.25:
                    super_resistant.append(pkmn["resistances"][nb_types]["name"])
                elif pkmn["resistances"][nb_types]["multiplier"] == 0:
                    immunise.append(pkmn["resistances"][nb_types]["name"])
                elif pkmn["resistances"][nb_types]["multiplier"] == 4:
                    super_efficace.append(pkmn["resistances"][nb_types]["name"])
            #print(neutre,efficace,super_efficace,super_resistant,resistant,immunise)
        ############################################### AFFICHAGE ################################################
            view = Paginator(id,data)
            await inter.edit_original_message(content="",embed=tt.menu_2(pkmn),view=view)
            view.message = await inter.original_response()
        except:
            print(f"Attention, une erreur est survenue lors de l'exécution de /poke_info, ayant comme paramètre(s) : {choix_poke} dans le serveur {inter.guild.name}")
            await inter.edit_original_message(content="", embed=tt.erreur(msg="Une erreur est survenue, veuillez contacter l'administrateur afin de connaitre la cause de ce bug !"))


    choix_gen = {"Génération 1":"https://mon-api-pokemon.vercel.app/api/v1/gen/1","Génération 2":"https://mon-api-pokemon.vercel.app/api/v1/gen/2","Génération 3":"https://mon-api-pokemon.vercel.app/api/v1/gen/3","Génération 4":"https://mon-api-pokemon.vercel.app/api/v1/gen/4","Génération 5":"https://mon-api-pokemon.vercel.app/api/v1/gen/5","Génération 6":"https://mon-api-pokemon.vercel.app/api/v1/gen/6","Génération 7":"https://mon-api-pokemon.vercel.app/api/v1/gen/7","Génération 8":"https://mon-api-pokemon.vercel.app/api/v1/gen/8", "Génération 9":"https://mon-api-pokemon.vercel.app/api/v1/gen/9"}
    choix_mode = {"Brut":0,"Ordre Alphabétique (A-Z)":1,"Inverse Ordre Alphabétique (Z-A)":2,"Types":3}
    @commands.slash_command(name="list_poke",description="Donne la liste des Pokemon d'une génération donnée !")
    async def ListePokeModule(self,
                            inter:disnake.CommandInter,
                            gen:str=commands.Param(name="génération",description="Afficher la liste des Pokemon d'une génération donnée !",choices=choix_gen),
                            mode:int=commands.Param(name="mode",description="Choisir un mode d'affichage des Pokémon",choices=choix_mode)
                            ):
        print(f"[COMMANDE LISTE_POKE] effectué dans {inter.guild.me}")
        try:    
            data_gen = requests.get(gen).json()
            list_poke = []
            for i in range(len(data_gen)):
                list_poke.append(data_gen[i]["name"]["fr"])
            if mode == 1 or mode == 2 or mode == 3:
                await inter.send(embed = tt.erreur("Cette fonctionnalité n'est pas encore disponible !"))
            elif mode == 0:
                await inter.send(embed = disnake.Embed(
                    title="Liste Poke",
                    color=disnake.Colour.random(),
                    description=", ".join(list_poke)
                ).add_field(name="Nombre de Pokemon",value=f"{len(list_poke)} Pokemon dans cette génération !"
            ).set_footer(text="Made by Ashz#6909",icon_url="https://cdn.discordapp.com/attachments/1060987754839818314/1060988125494657054/Pdp_Discord.png")
                )
                await inter.delete_original_message(delay=15)
        except:
            await inter.send(embed=tt.erreur(msg="La commande n'a pas pû être exécuté ! Envoyé un message à l'administrateur du bot, ou bien envoyez un ``/feedback`` afin d'expliquer le problème."),ephemeral=True)
                        

def setup(self:commands.AutoShardedBot):
    self.add_cog(PokeInfo_Module(self))


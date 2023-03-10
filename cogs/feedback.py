import disnake
from disnake.ext import commands
import temp_embed.temp as tt


class MenuFeedbacks(disnake.ui.Modal):
    def __init__(self) -> None:
        components = [
            disnake.ui.TextInput(
                label="Votre pseudo : (Facultatif)",
                placeholder="Merci d'indiquer votre pseudo Discord",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                min_length=5,
                max_length=50,
                required=False
            ),
            disnake.ui.TextInput(
                label="Message",
                placeholder="Donnez votre avis sur le bot ici :",
                custom_id="content",
                style=disnake.TextInputStyle.paragraph,
                min_length=5,
                max_length=1024,
            ),
        ]
        super().__init__(title="Fenêtre d'avis", custom_id=f"feedbacks", components=components)

    async def callback(self, inter:disnake.ModalInteraction) -> None:
        tag_name = inter.text_values["name"]
        tag_content = inter.text_values["content"]
        channel = await inter.bot.fetch_channel(1074298382350295051)
        await channel.send(embed=tt.menu_feedback_avis(titre="Menu feedback",auteur=tag_name,message=tag_content).set_thumbnail(inter.user.avatar))
        return await inter.send("Votre message a bien été envoyé, vous remerciant par avance !",ephemeral=True)

    async def on_error(self, error: Exception, inter: disnake.ModalInteraction) -> None:
        print(error)
        return await inter.response.send_message(embed=tt.erreur("Une erreur s'est produite... Contacte l'administrateur du bot si cela est trop fréquent"), ephemeral=True)

class FeedbackModule(commands.Cog):
    def __init__(self,bot:commands.InteractionBot):
        self.__bot = bot

    @commands.slash_command(name="poke_feedback",description="Envoyer votre avis sur le bot en exécutant cette commande")
    async def feedback(self, inter:disnake.CommandInter):
        print(f"[COMMANDE POKE_FEEDBACK] sur le server {inter.guild.name}")
        try:
            await inter.response.send_modal(modal=MenuFeedbacks())
        except:
            print(f"Attention, une erreur est survenue lors de l'exécution de /poke_feedback {inter.guild.name}")
            await inter.send(content="", embed=tt.erreur("Une erreur est survenue, veuillez contacter l'administrateur afin de connaitre la cause de ce bug !"),ephemeral=True)
            await inter.delete_original_message(delay=7.0)


def setup(self):
    self.add_cog(FeedbackModule(self))
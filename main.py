import discord
from discord import app_commands
class rpgshop(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="$",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        await self.tree.sync()
    async def on_ready(self):
        print(f"O bot {self.user} está funcionando.")

bot = rpgshop()


@bot.tree.command(name="olá-mundo", description="Primeiro comando do bot")
async def olamundo(interaction:discord.Interaction): 
    await interaction.response.send_message(f"Olá, {interaction.user.mention}!")

@bot.tree.command(name="soma", description="Comando de soma")
@app_commands.describe(
    numero1="Primeiro número",
    numero2="Segundo número" 
)
async def soma(interaction:discord.Interaction, numero1:int,numero2:int):
    numero_somado = numero1 + numero2
    await interaction.response.send_message(f"Olá, {interaction.user.mention}! O resultado da sua soma é {numero_somado}")

bot.run("token")

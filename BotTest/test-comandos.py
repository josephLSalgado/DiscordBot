import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.', description='Este es un bot servicial :)')

#Ejecuta desde bot su decorador command para crear un comando
@bot.command()
#Se define nueva función para saber que el bot esté conectado al server
#por medio de una corutina
async def saludo(ctx):
    await ctx.send('Hola Spartan!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(
            name='Halo'))
    print('El bot está listo.')

#NO OLVIDES de poner el TOKEN :)
bot.run('TOKEN')
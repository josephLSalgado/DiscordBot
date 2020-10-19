import discord
import datetime
from discord.ext import commands

bot = commands.Bot(command_prefix='.', description='Este es un bot servicial :)')

#Ejecuta desde bot su decorador command para crear un comando
@bot.command()
#Se define nueva función para saber que el bot esté conectado al server
#por medio de una corutina
async def saludo(ctx):
    await ctx.send('Hola Spartan!')

#Información sobre la beta de Cold War
@bot.command()
async def cw(ctx):
    fechaFinal = datetime.datetime.strptime('19/10/2020', '%d/%m/%Y')
    hoy = datetime.datetime.today()
    tiempoRestante = (fechaFinal - hoy).total_seconds()/3600

    if int(tiempoRestante) > 0:
        embed = discord.Embed(title=f'{ctx.guild.name}',
            description=f'La beta de Cold War terminará en: {int(tiempoRestante)} horas. \nLlega al nivel 10 de la beta para recibir Proyecto de subfusil excepcional.')

        embed.set_image(url='https://teamdarkpirates.com/wp-content/uploads/2019/07/Subfusil-Fortnite-r%C3%A1fagas-banner.jpg')

    else:
        embed = discord.Embed(title=f'{ctx.guild.name}',
            description='La beta de Cold War ha terminado.')

    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(
            name='Beta de Cold War con el FrnK'))
    print('El bot está listo.')

#NO OLVIDES de poner el TOKEN :)
bot.run('TOKEN')
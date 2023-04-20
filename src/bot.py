import json

from discord.ext import commands
import discord

from misc import loggers, configs, rcon

ROOT_PATH = configs.ROOT_PATH
LOGGER    = loggers.get_logger()
CONFIG    = configs.CONFIG
TOKEN     = CONFIG.bot_token

app = commands.Bot(command_prefix = '/')
@app.event
async def on_ready():

    LOGGER.info('Bot ready')
    await app.change_presence(status   = discord.Status.online, activity = None)


@app.command()
async def hello(ctx):
    await ctx.send('안녕하세요. 저는 전서구 입니다.')


app.run(TOKEN)


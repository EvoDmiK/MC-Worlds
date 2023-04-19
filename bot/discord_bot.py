import json

from discord.ext import commands
import discord

from misc import loggers, configs
from rcon import *

ROOT_PATH = configs.ROOT_PATH
CONFIG    = configs.CONFIG

app = commands.Bot(command_prefix = '/')

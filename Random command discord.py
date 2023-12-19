import disnake
from disnake.ext import commands
import requests
import discord
import asyncio
import json
import random
import time

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())

@bot.slash_command(description="Команда выдаст рандомное число между выбраными цифрами") #us Translator
async def random_number(ctx, num1: int, num2: int):
    if num1 >= num2:
        await ctx.send("Первое число должно быть меньше второго числа.") #us Translator
        return

    result = random.randint(num1, num2)
    await ctx.send(f"Случайное число между {num1} и {num2}: {result}")

 bot.run(" ") #bot id
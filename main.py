from keys import discord_token, channel_id
from twitter_search import twitter_search

import discord
from discord.ext import commands
from discord.ext.commands import bot
import time
import random


TOKEN = discord_token
CHANNEL_ID = channel_id

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="=" , intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("We building now")
    await bot.change_presence(activity=discord.Game(name="Fortnite"))


@bot.command(pass_content=True)
async def evan(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("https://tenor.com/view/throw-up-dry-heave-vomit-gross-eww-gif-23254765", delete_after=10)

@bot.command(pass_content=True)
async def louis(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("https://tenor.com/view/gigachad-chad-gif-20773266", delete_after=10)

@bot.command(pass_content=True)
async def rant(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    tweets = twitter_search()
    for val in tweets.values():
        val = val + "\n" + "=========================="
        await channel.send(val, delete_after=10)

@bot.event
async def on_member_update(prev, cur):
    channel = bot.get_channel(CHANNEL_ID)
    member = bot.get_guild(prev.guild.id).get_member(prev.id)
    games = ["minecraft", "valorant", "apex legends", "brawlhalla"]
    insult = ["Haha loser!", "What a nerd", "That game sucks", "yUcKY gRosS", "L", "https://tenor.com/view/cejm-cavalcade-rodifa-juhulati-gif-21763328"]
    if cur.activity and cur.activity.name.lower() in games:
        rand = random.randint(0,4)
        print_name = str(member).split("#", 1)[0]
        await channel.send(print_name + " is playing "+  cur.activity.name.capitalize() + " ! " + insult[rand], delete_after=30)
    if str(cur.status) == "online" and str(member) == "Stew#0122":
        await channel.send("Hi Louis! You look so handsome today. This looks like you... https://tenor.com/view/gigachad-chad-gif-20773266", delete_after=30)
    if str(cur.status) == "offline" and str(member) == "Stew#0122":
        await channel.send("Goodnight Louis, sweet dreams <3... https://tenor.com/view/sleep-kirby-cute-gif-13800099", delete_after=30)
    
    


bot.run(TOKEN)

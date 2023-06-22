import discord
import discord.client
from discord.ext import commands


def run_discord_bot():
    TOKEN = "MTEyMTQ2MTAyMzczNjU5ODU2OQ.GI-stR.-ghhP8B3Ui4Px9QFGmC2LzTeIsppdp810xZmsI"
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='.', intents=intents)


    @client.event
    async def on_ready(pass_context=True):
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

    @client.command(pass_context=True)
    async def join(ctx):
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.message.author.voice.channel
            await channel.connect()

        else:
            await ctx.send("You are not in a voice channel.")

    @client.command()
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnet()
            await ctx.send("Okay i leave :'( ")
        else:
            await ctx.send("I'm not in a voice channel")

    client.run(TOKEN)



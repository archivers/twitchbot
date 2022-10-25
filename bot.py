import os
from twitchio.ext import commands

# set up the bot
bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event()
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")

@bot.event()
async def event_channel_joined(channel):
    await channel.send("/me I have arrived")

@bot.event()
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
    # make sure the bot ignores itself and the streamer
    if ctx.author is None:
        return
    elif ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"hello, @{ctx.author.name}!")

@bot.command(name='join')
async def join(ctx):
    #target_channel = ctx.message.content.replace('!join', '').strip()
    #print(target_channel)
    print(ctx.message.content)
    #await bot.join_channels([target_channel])

@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')

@bot.command(name='modcheck')
async def modcheck(ctx):
    if ctx.author.is_mod:
        await ctx.send(f"@{ctx.author.name} is a mod!")
    else:
        await ctx.send(f"@{ctx.author.name} is not a mod!")

@bot.command(name='whisper')
async def whisper(ctx):
   await ctx.author.send("hello")

if __name__ == "__main__":
    bot.run()

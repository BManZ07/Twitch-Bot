import asyncio
import config as cfg
from twitchio.ext import commands

def is_owner(ctx):
    if ctx.message.author.name == '...':
        return True
    else: 
        return False

def is_mod(ctx):
    return ctx.message.author.is_mod

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='oauth:...', client_id='...', nick='...', prefix='!',
                         initial_channels=['...'], client_secret="...")

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        ctx = await bot.get_context(message=message)
        if cfg.useHelloTrigger == True:
            for i in cfg.helloTrigger:
                if str(message.content).lower() == str(i).lower():
                    await ctx.send(f'Hello {ctx.author.name}! Welcome to the stream :)')
        elif cfg.useChatFilter == True:
            for i in cfg.bannedWords:
                if str(message.content).lower() == str(i).lower():
                    await ctx.ban(message.author, "Breach of community rules!")

        await self.handle_commands(message)        
        

    # Commands use a different decorator
    if cfg.useCommandServer == True:
        @commands.command(name='server')
        async def server(self, ctx):
            await ctx.send(f'I am currently playing on NerveRP | discord.gg/nerve')
    if cfg.useCommandCurrent == True:
        @commands.command(name='current')
        async def current(self, ctx):
            stream_info = await ctx.get_stream()
            print(stream_info)

    if cfg.useCommandSlowmode == True:
        @commands.command(name='slowon')
        async def slowon(self, ctx):
            if is_mod(ctx) == True:
                await ctx.send(f'Chat is currently in slowmode!')
                await ctx.slow()

        @commands.command(name='slowoff')
        async def slowoff(self, ctx):
            if is_mod(ctx) == True:
                await ctx.send(f'Slowmode has been disabled!')
                await ctx.slow_off()

    if cfg.useCommandClear == True:
        @commands.command(name='clear')
        async def clear(self, ctx):
            if is_mod(ctx) == True:
                await ctx.clear()
            else:
                print(f"{ctx.author.name} tried to clear chat.")
    #Still being worked on
    if cfg.useCommandTimeout == True:
        @commands.command(name='timeout')
        async def timeout(self, ctx):
            if is_mod(ctx) == True:
                await ctx.timeout(user, duration)
            else:
                print(f"{ctx.author.name} tried to timeout.")

    


    


bot = Bot()
bot.run()
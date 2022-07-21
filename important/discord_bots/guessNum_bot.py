import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix='!')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as - {self.user.name}: {self.user.id}\n-------')

    @bot.command()
    async def hello(ctx, *args):
        for arg in args:
            await ctx.send(arg)


    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('!guess'):
            await message.channel.send('Guess a number between 1 to 10')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()
            
            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                await message.channel.send('Sorry, you took to0 long it was {}'.format(answer))
            
            if int(guess.content) == answer:
                await message.channel.send('YOU ARE RIGHT!')
            else:
                await message.channel.send(f'OOps. It is actually {answer}')
    
client = MyClient()
client.run('ODgxNTIwNzg1ODE3MjEwODgw.YSuCNQ.yueWyiDgKlj9LPvIbI950hu00mA')
import discord
from discord.ext import commands


class MyClient(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # plain message return (not only to you, server including this bot in general)
        print(f'Message from {message.author}: {message.content}')

        # don't answer on your own message
        if message.author == client.user:
            return

        # respond properly when the message starts with hello
        if message.content.startswith('Hello'):
            await message.channel.send(f'Hello {message.author}! I am Discord Bot {self.user}, glad to meet you 🙂')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient("$", intents=intents)
client.run('token')

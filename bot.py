import discord 

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == ('hi'):
            await message.add_reaction('😂')
        
        if message.content.startswith('guards'):
            if message.mentions:
                personToTag = message.mentions[0].mention

                async for msg in message.channel.history(limit=10):
                    if msg.author == message.mentions[0]:
                        last_message = msg
                        break

                await last_message.add_reaction('🍅')
            else:
                return
    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('INSERT TOKEN HERE')

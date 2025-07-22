import discord
import os


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def get_or_create_brazen_bull_channel(self, guild):
        brazen_bull_channel = discord.utils.get(guild.text_channels,
                                                name='brazen-bull')

        if brazen_bull_channel is None:
            try:
                brazen_bull_channel = await guild.create_text_channel(
                    'brazen-bull')
                print(f'Created brazen-bull channel in {guild.name}')
            except discord.Forbidden:
                print(f'No permission to create channel in {guild.name}')
                return None
            except discord.HTTPException:
                print(f'Failed to create channel in {guild.name}')
                return None

        return brazen_bull_channel

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == ('hi'):
            await message.add_reaction('😂')

        if 'guards' in message.content.lower():
            if message.mentions:
                personToTag = message.mentions[0].mention

                async for msg in message.channel.history(limit=100):
                    if msg.author == message.mentions[0]:
                        last_message = msg
                        await last_message.add_reaction('🍅')
                        break
            else:
                return

        if 'leave her alone' in message.content.lower():
            if message.mentions:
                personToTag = message.mentions[0].mention
                await message.channel.send(f'{personToTag} leave her alone')

            else:
                return

        if ('boil him' in message.content.lower()
                or 'boil her' in message.content.lower()) and message.mentions:
            brazen_bull_channel = await self.get_or_create_brazen_bull_channel(
                message.guild)

            if brazen_bull_channel:
                for mentioned_user in message.mentions:
                    await brazen_bull_channel.send(
                        f'{mentioned_user.mention} has been summoned to the brazen bull! 🔥'
                    )


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN'))

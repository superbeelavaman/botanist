# Import discord packet. Good luck Plant Bot!
import discord

#Client(the bot)
client = discord.Client()

@client.event
async def on_ready():
    #Fruit Salad!
    general = client.get_channel(862810154922409997)

    await general.send('fruit salad')

#Run the client

client.run('token')

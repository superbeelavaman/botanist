# Import discord packet. Good luck Plant Bot!
import discord

#Client(the bot)
client = discord.Client()

@client.event
async def on_ready():
    #Fruit Salad!
    generoot = client.get_channel(831967470297677865)

    await generoot.send('fruit salad')

#Run the client

client.run('ODYyODMxNTc4NDY4MTg4MTgy.YOeEhg.A4j0JVlaB1ckTVsbLDzMV_jUksM')
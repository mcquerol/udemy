import discord
import asyncio

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    # start a background task to send messages every 5 minutes
    client.loop.create_task(background_task())

async def background_task():
    await client.wait_until_ready()  # wait for client to be fully logged in
    channel = client.get_channel(1082348929338843267)  # replace with your channel ID
    print(channel)
    while True:
        await channel.send('Hello!')
        await asyncio.sleep(300)  # wait for 5 minutes

client.run('MTA4MjYzOTc2MTE4MjgyNjU4MA.GHXMk-.Vn_Yh5w3bdz_hAXAwJBx1dKp5IujSdwBkb3R4w')  # replace with your bot token

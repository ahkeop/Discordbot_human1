This is a sample Python script.

import discod

client = discod.client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discod.Game("아잉")
    await client.change_presence(status=discod.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startwith("휴먼아"):
        await message.channel.send("ㅎㅇ")

client.run("NzU2MDMxMjE5NjQ0NDk3OTYw.X2L68Q.DXmdDYWXs-oZZZDjlZI2gdL-bUA")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import discord
import asyncio
import os

client = discord.Client()

token = "acess_token"
client = discord.Client()
@client.event
async def on_ready():
    print('Is any one there?')
    print(client.user.name)
    print(client.user.id)




@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("휴먼아 도움말/베타테스팅")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content == '휴먼아 도움말':
        embed = discord.Embed(color=0xff00, title="미먼봇 도움말", description="미먼봇은 단순 장난용으로 만들어진 챗봇입니다\n명령어 목록\n`휴먼아`\n`휴먼아 안녕`\n`휴먼아 ㅗㅗ`\n`휴먼아 와샌즈`\n`휴먼아 누나`", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '휴먼아':
        await message.channel.send("ㅇㅇ 왜")
    if message.content == '휴먼아 ㅗㅗ':
        await message.channel.send('내가 만만해!?, 내가 만만하냐고!!!')
    if message.content == '휴먼아 안녕':
        await message.channel.send('ㅎㅇㅎㅇ')
    if message.content == '휴먼아 누나':
        await message.channel.send('나죽어')
    if message.content == '휴먼아 와샌즈':
        await message.channel.send('아시는구나!!')

acess_token = os.environ["BOT.TOKEN"]
client.run(acess_token)

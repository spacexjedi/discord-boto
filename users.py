import discord

ID = "XXXXX"
TOKEN = "XXXXX"

client = discord.Client()

@client.event
async def on_member_join(member):
  for channel in member.guild.channels:
    if str(channel) == "general":
      await channel.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
  id = client.get_build(ID)
  channels = ["commands"]
  valid_users = ["Ti#9298"]

  if str(message.channel) in channels and str(message.author) in valid_users:
    if message.content.find("!hello")!= -1:
      await message.channel.send("hi")
    elif message.content == "!users":
      await message.channel.send(f"""# of Members: {id.member_count}""")




client.run(TOKEN)

import discord

CLI = "XXXX"
TOKEN = "XXXXXX"

client = discord.Client()

@client.event

async def on_message(message):
  print(message.content)
  client.run(TOKEN)


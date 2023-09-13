import os
import logging
import discord
from dotenv import load_dotenv
load_dotenv()

defaultPrefix: str = os.getenv('DEFAULT_CMD_PREFIX')
print(defaultPrefix)
intents: object = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False               #Sets up the intents necessary for this bot's purpose
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(defaultPrefix+"hello"):
        print("Found hello command")
        await message.channel.send("Hello!")


if __name__ == "__main__":
    load_dotenv()
    token: str = os.getenv('DISCORD_TOKEN')
    appID: str = os.getenv('APP_ID')
    pubKey: str = os.getenv('PUBLIC_KEY')

    handler: object = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    
    #Setup what Client is.....
    client.run(token, log_handler=handler, log_level=logging.DEBUG)
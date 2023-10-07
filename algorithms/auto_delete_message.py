import discord

# Initialize a bot client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Your bot token
TOKEN = 'YOUR_BOT_TOKEN'

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    # Check if the message author is the bot itself to avoid an infinite loop
    if message.author == client.user:
        return
    
    # Replace 'your_channel_id' with the actual channel ID where you want messages to be deleted
    channel_id = 'your_channel_id'
    
    if str(message.channel.id) == channel_id:
        try:
            await message.delete()
            print(f'Deleted message: "{message.content}" by {message.author.name}')
        except discord.Forbidden:
            print("Bot doesn't have permission to delete messages in this channel.")

# Run the bot with your token
client.run(TOKEN)

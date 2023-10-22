import os
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)
    channel = message.channel

    def check(m):
        return m.content == 'hello' and m.channel == channel

    msg = await bot.wait_for('message', check=check)
    await channel.send(f'Hello {msg.author}!')
    

@bot.event
async def on_member_join(member):
    reaction1 = '✅'
    reaction2 = '❌'
    greeting = "Hi! Welcome to SRC's Official Discord Server! Please enter your IGN(In Game Name)"
    await member.send(greeting)
    
    username_linked = False
    while not username_linked:
        def check(m):
            return m.author == member and m.guild is None
        
        response = await bot.wait_for('message', check=check, timeout=600)
        user_nickname = response.content
        msg = await member.send(f"Is '{user_nickname}' correct?")
        await msg.add_reaction(reaction1)
        await msg.add_reaction(reaction2)

        def confirmation_check(reaction,user):
            return (
                str(reaction.emoji) in ['✅','❌']
            )
        user_confirmation,user = await bot.wait_for("reaction_add", check=confirmation_check, timeout=600)
        
        if str(user_confirmation.emoji) == '✅':
            await member.edit(nick=user_nickname)
            await member.send(f"Your nickname has been changed to '{user_nickname}'.")
            await member.send(f"If you ever want to change your nickname you can use the command '!name_change' to do so.")
            username_linked = True
        elif str(user_confirmation.emoji) == '❌':
            await member.send("Please enter your Main's name again.")
            

@bot.command(pass_context=True)
async def name_change(ctx, usr: discord.Member):
    reaction1 = '✅'
    reaction2 = '❌'
    user = ctx.author
    await user.send("Hi! You've initiated the name change process. Please enter your new IGN.")
    def check(message):
        return message.author == user and message.guild is None
    
    while True:
        response = await bot.wait_for('message', check=check, timeout=600)
        new_nickname = response.content
        confirmation_message = f"Is '{new_nickname}' correct?."
        msg = await user.send(confirmation_message)
        await msg.add_reaction(reaction1)
        await msg.add_reaction(reaction2)
        def confirmation_check(reaction,usr):
            return (
                str(reaction.emoji) in ['✅','❌']
            )
        confirmation_response,userr = await bot.wait_for('reaction_add', check=confirmation_check, timeout=600)
        if str(confirmation_response.emoji) == '✅':
            await usr.edit(nick=new_nickname)
            await user.send(f"Your nickname has been changed to '{new_nickname}'.")
            break
        elif str(confirmation_response.emoji) == '❌':
            await user.send("Please enter your new nickname again.")
bot.run(os.environ["DISCORD_TOKEN"])

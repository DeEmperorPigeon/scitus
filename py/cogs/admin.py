import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import cooldown, BucketType
import random
from pasta import *
from discord.ext import commands
import inspect
#holy shit this could be a massive mistake
#No "has_role"s


"""
editrole
-colour
-name
applyall
"""


#--------------------------------------------------------------------------------------------------------------------------
class Admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None


  @commands.group(
    help="Edits a role"
  )
  async def editrole(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.channel.send("Command can't be used without subcommand.")


#--------------------------------------------------------------------------------------------------------------------------
  #colour
  @editrole.command(
    help="Changes the colour of a role.",
    brief="Changes the colour of a role.",
    case_insensitive = True
  )
  @commands.has_permissions(manage_roles=True)
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def colour(self, ctx, role : discord.Role, colour):
    colour = int(colour, base=16)
    colour = discord.Colour(colour)
    await role.edit(colour=colour)
    await ctx.channel.send("Role colour changed to " + str(colour))



  @colour.error
  async def colour_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      msg = 'This command is on cooldown, please try again in {:.2f}s'.format(error.retry_after)
      await ctx.channel.send(msg)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.channel.send(listsPas.helpPastas[random.randrange(0, len(listsPas.helpPastas) - 1)])
    else:
        raise error


#--------------------------------------------------------------------------------------------------------------------------
  #name
  @editrole.command(
    help="Changes the name of a role.",
    brief="Changes the name of a role.",
    case_insensitive = True
  )
  @commands.has_permissions(manage_roles=True)
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def name(self, ctx, role : discord.Role, *name):
    actualName = list(name)
    realActualName = " ".join(actualName)
    await role.edit(name=str(realActualName))
    await ctx.channel.send("Role name changed to " + str(realActualName))

  @name.error
  async def name_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      msg = 'This command is on cooldown, please try again in {:.2f}s'.format(error.retry_after)
      await ctx.channel.send(msg)

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.channel.send(listsPas.helpPastas[random.randrange(0, len(listsPas.helpPastas) - 1)])

    else:
        raise error


#--------------------------------------------------------------------------------------------------------------------------






#necessities
def setup(bot):
  bot.add_cog(Admin(bot))
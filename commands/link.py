from config import*

info = {
  "name" : ">link",
  "desc" : "For spreading the good word of Robot Man to the masses"
}

async def command(ctx, client):
  await ctx.channel.send(content = "", embed=baseEmbed([["😩"+ctx.author.name+" is taking me somewhere special 😩", "https://discordapp.com/api/oauth2/authorize?client_id=639633583736094759&permissions=1345842241&scope=bot"],["...", "..."]])) 
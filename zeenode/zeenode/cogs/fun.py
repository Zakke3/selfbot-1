import discord, pyfiglet, requests, random, string, aiohttp, io, hashlib, base64
from discord.ext import commands as zeenode 
iain = 'iain#1031'
class Fun(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot
 

    @zeenode.command()
    async def slap(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} slapped {user.mention}!**", color=0x0000)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

        
    @zeenode.command()
    async def hug(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} hugged {user.mention}!**", color=0x0000)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

        
    @zeenode.command(aliases=['dong', 'penis'])
    async def dick(self, ctx, *, user: discord.User = None):
        await ctx.message.delete()
        if user is None:
            em = discord.Embed(title="No user provided.")
            await ctx.send(embed=em)
            
        else:
            size = random.randint(1, 50)
            dong = ""
            for _i in range(0, size):
                dong += "="
            em = discord.Embed(title=f"{user}'s Dick size:", description=f"8{dong}D", colour=0x0000)
            await ctx.send(embed=em)
        

    
    
    @zeenode.command()
    async def kiss(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} kissed {user.mention}!**", color=0x0000)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)
     
   
    
    @zeenode.command()
    async def panda(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/panda").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Panda.", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
        embed.set_image(url=str(r["link"]))
        await ctx.send(embed=embed)    
    
    
    @zeenode.command()
    async def meme(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/meme").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Meme.", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
        embed.set_image(url=str(r["image"]))
        await ctx.send(embed=embed)

        
    @zeenode.command()
    async def cat(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/cat").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Cat.", icon_url="https://cdn.discordapp.com/attachments/796868392095186976/810566027637162034/zeenode_cat.png") 
        embed.set_image(url=str(r["link"]))
        await ctx.send(embed=embed)   
    
    
    @zeenode.command()
    async def dog(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/dog").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Dog." , icon_url="https://cdn.discordapp.com/attachments/796868392095186976/810566380545114172/zeenode_dog.png") 
        embed.set_image(url=str(r["link"]))
        await ctx.send(embed=embed)    
        
    @zeenode.command()
    async def hack(self, ctx, *, user: discord.User = None):
        await ctx.message.delete()
        if user is None:
            user = ctx.author
        else:
            embed = discord.Embed(color=0x0000)
            embed.set_author(name="Iain's Self-Bot", icon_url="https://cdn.discordapp.com/icons/891717404223229972/8ca7701f0ca8406f9349099c7dbea3b2.png?size=4096")
            embed = discord.Embed(title = f"**Successfully hacked user: {user}**", description=" > Found IP address\n > Geolocating IP address\n > Found Full Name\n > *Saving to Hacked.txt*") 
            await ctx.send(embed=embed)
            
    @zeenode.command()
    async def nitro(self, ctx):
            await ctx.message.delete()
            await ctx.send(Nitro())


def Nitro():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"
        
def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))

def setup(bot):
    bot.add_cog(Fun(bot))

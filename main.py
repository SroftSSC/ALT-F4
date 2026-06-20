import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

# Bot Kurulumu
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/" , intents=intents)

# Konfigürasyon
BOT_SAHIBI_ID = int(os.getenv('BOT_SAHIBI_ID', '1123477916920053862'))
SUNUCU_ID = int(os.getenv('SUNUCU_ID', '1517677204509687959'))

# Roller Hiyerarşisi (İzinler)
ROLLE_HIYERARSI = {
    "Kurucu": 15,
    "Asistan": 14,
    "Master III": 13,
    "Master II": 12,
    "Master I": 11,
    "Yeni Master": 11,
    "Rehber III": 9,
    "Rehber II": 8,
    "Rehber I": 7,
    "Yeni Rehber": 6,
    "Sponsor": 4,
    "VIP+": 3,
    "VIP": 2,
    "Üye+": 1,
    "Üye": 0
}

@bot.event
async def on_ready():
    print(f"{bot.user} başarıyla bağlandı!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/sunucu-yap"))

# Komutları Yükle
async def load_commands():
    for filename in os.listdir('./komutlar'):
        if filename.endswith('.py'):
            await bot.load_extension(f'komutlar.{filename[:-3]}')
            print(f"✓ {filename} yüklendi")

async def main():
    async with bot:
        await load_commands()
        await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

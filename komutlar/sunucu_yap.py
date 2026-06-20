import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

BOT_SAHIBI_ID = int(os.getenv('BOT_SAHIBI_ID', '1123477916920053862'))

class SunucuYap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roller_emojiler = {
            "Kurucu": "👑",
            "Asistan": "🛡️",
            "Master III": "🥇",
            "Master II": "🥈",
            "Master I": "🥉",
            "Yeni Master": "⭐",
            "Rehber III": "📚",
            "Rehber II": "📖",
            "Rehber I": "📝",
            "Yeni Rehber": "✏️",
            "Sponsor": "💎",
            "VIP+": "⚜️",
            "VIP": "🌟",
            "Üye+": "➕",
            "Üye": "👤"
        }
        
        self.rolle_hiyerarsi = {
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

    @commands.command(name="sunucu-yap", description="Yeni bir sunucu yapısı oluştur")
    async def sunucu_yap(self, ctx):
        """Discord sunucusunda kanal ve rol yapısını otomatik oluştur"""
        
        # Sadece Bot Sahibi Kontrol
        if ctx.author.id != BOT_SAHIBI_ID:
            embed = discord.Embed(
                title="❌ Yetkisiz Erişim",
                description="Bu komutu sadece bot sahibi kullanabilir!",
                colour=discord.Colour.red()
            )
            await ctx.send(embed=embed)
            return
        
        # Rolleri Oluştur
        await ctx.send("🚀 Sunucu yapısı oluşturuluyor...")
        
        guild = ctx.guild
        olusturulan_roller = {}
        
        # Mevcut rolleri sil (varsa)
        for role in guild.roles:
            if role.name in self.rolle_hiyerarsi:
                try:
                    await role.delete()
                except:
                    pass
        
        # Rolleri oluştur
        for rol_adi, seviye in self.rolle_hiyerarsi.items():
            emoji = self.roller_emojiler.get(rol_adi, "")
            rol_adi_emojili = f"{emoji} {rol_adi}"
            
            # Yetkileri belirle
            if seviye >= 14:  # Kurucu ve Asistan
                permissions = discord.Permissions.all()
            elif seviye == 13:  # Master III
                permissions = discord.Permissions(
                    manage_messages=True,
                    kick_members=True,
                    ban_members=True,
                    manage_roles=True,
                    manage_channels=True,
                    manage_guild=True
                )
            elif seviye == 12:  # Master II
                permissions = discord.Permissions(
                    manage_messages=True,
                    kick_members=True,
                    ban_members=True,
                    manage_roles=False,
                    manage_channels=False
                )
            elif seviye == 11:  # Master I / Yeni Master
                permissions = discord.Permissions(
                    manage_messages=True,
                    kick_members=True,
                    ban_members=False,
                    manage_roles=False
                )
            elif seviye >= 6:  # Rehberler
                permissions = discord.Permissions(
                    manage_messages=True,
                    moderate_members=True
                )
            elif seviye == 4:  # Sponsor
                permissions = discord.Permissions(
                    manage_messages=False,
                    send_messages=True
                )
            elif seviye == 3:  # VIP+
                permissions = discord.Permissions(
                    send_messages=True,
                    speak=True,
                    priority_speaker=True
                )
            elif seviye == 2:  # VIP
                permissions = discord.Permissions(
                    send_messages=True,
                    speak=True
                )
            elif seviye == 1:  # Üye+
                permissions = discord.Permissions(
                    send_messages=True,
                    speak=True
                )
            else:  # Üye
                permissions = discord.Permissions(
                    send_messages=True,
                    view_channel=True
                )
            
            try:
                role = await guild.create_role(
                    name=rol_adi_emojili,
                    permissions=permissions,
                    colour=discord.Colour.random()
                )
                olusturulan_roller[rol_adi] = role
                print(f"✓ {rol_adi_emojili} rolü oluşturuldu")
            except Exception as e:
                print(f"✗ {rol_adi} oluşturulamadı: {e}")
        
        # Kanalları Oluştur
        olusturulan_kanallar = {}
        
        # Mevcut kanalları sil (varsa)
        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                pass
        
        # Kategori ve Kanallar
        kanal_yapisi = {
            "📢 Genel": [
                ("💬-sohbet", "text"),
                ("📢-duyurular", "text"),
                ("📋-kurallar", "text"),
                ("❓-yardim", "text"),
            ],
            "🎮 Eğlence & Oyun": [
                ("🎮-oyunlar", "text"),
                ("🎰-kumar", "text"),
                ("😂-meme", "text"),
                ("🎬-video", "text"),
                ("🎵-müzik", "text"),
                ("📷-fotoğraf", "text"),
                ("🎨-sanat", "text"),
                ("📚-okuma", "text"),
                ("💭-tartışma", "text"),
                ("🔞-18-plus", "text"),
            ],
            "🤖 Bot & Sponsor": [
                ("🤖-bot-komutlar", "text"),
                ("💎-sponsor", "text"),
                ("🎁-giveaway", "text"),
            ],
            "🎙️ Oyun Ses Kanalları": [
                ("🔊-war-thunder-2k", "voice"),
                ("🔊-war-thunder-3k", "voice"),
                ("🔊-war-thunder-4k", "voice"),
                ("🔊-war-thunder-5k", "voice"),
                ("🔊-war-thunder-10k", "voice"),
                ("🔊-cs2-2k", "voice"),
                ("🔊-cs2-3k", "voice"),
                ("🔊-cs2-4k", "voice"),
                ("🔊-cs2-5k", "voice"),
                ("🔊-cs2-10k", "voice"),
                ("🔊-minecraft-2k", "voice"),
                ("🔊-minecraft-3k", "voice"),
                ("🔊-minecraft-4k", "voice"),
                ("🔊-minecraft-5k", "voice"),
                ("🔊-minecraft-10k", "voice"),
                ("🔊-fortnite-2k", "voice"),
                ("🔊-fortnite-3k", "voice"),
                ("🔊-fortnite-4k", "voice"),
                ("🔊-fortnite-5k", "voice"),
                ("🔊-fortnite-10k", "voice"),
                ("🔊-valorant-2k", "voice"),
                ("🔊-valorant-3k", "voice"),
                ("🔊-valorant-4k", "voice"),
                ("🔊-valorant-5k", "voice"),
                ("🔊-valorant-10k", "voice"),
                ("🔊-lol-2k", "voice"),
                ("🔊-lol-3k", "voice"),
                ("🔊-lol-4k", "voice"),
                ("🔊-lol-5k", "voice"),
                ("🔊-lol-10k", "voice"),
                ("🔊-rust-2k", "voice"),
                ("🔊-rust-3k", "voice"),
                ("🔊-rust-4k", "voice"),
                ("🔊-rust-5k", "voice"),
                ("🔊-rust-10k", "voice"),
                ("🔊-roblox-2k", "voice"),
                ("🔊-roblox-3k", "voice"),
                ("🔊-roblox-4k", "voice"),
                ("🔊-roblox-5k", "voice"),
                ("🔊-roblox-10k", "voice"),
                ("🔊-gta5-2k", "voice"),
                ("🔊-gta5-3k", "voice"),
                ("🔊-gta5-4k", "voice"),
                ("🔊-gta5-5k", "voice"),
                ("🔊-gta5-10k", "voice"),
                ("🔊-l4d2-2k", "voice"),
                ("🔊-l4d2-3k", "voice"),
                ("🔊-l4d2-4k", "voice"),
                ("🔊-l4d2-5k", "voice"),
                ("🔊-l4d2-10k", "voice"),
                ("🔊-among-us-2k", "voice"),
                ("🔊-among-us-3k", "voice"),
                ("🔊-among-us-4k", "voice"),
                ("🔊-among-us-5k", "voice"),
                ("🔊-among-us-10k", "voice"),
                ("🔊-terraria-2k", "voice"),
                ("🔊-terraria-3k", "voice"),
                ("🔊-terraria-4k", "voice"),
                ("🔊-terraria-5k", "voice"),
                ("🔊-terraria-10k", "voice"),
                ("🔊-rdr2-2k", "voice"),
                ("🔊-rdr2-3k", "voice"),
                ("🔊-rdr2-4k", "voice"),
                ("🔊-rdr2-5k", "voice"),
                ("🔊-rdr2-10k", "voice"),
                ("🔊-ets2-2k", "voice"),
                ("🔊-ets2-3k", "voice"),
                ("🔊-ets2-4k", "voice"),
                ("🔊-ets2-5k", "voice"),
                ("🔊-ets2-10k", "voice"),
                ("🔊-peak-2k", "voice"),
                ("🔊-peak-3k", "voice"),
                ("🔊-peak-4k", "voice"),
                ("🔊-peak-5k", "voice"),
                ("🔊-peak-10k", "voice"),
                ("🔊-garrys-mod-2k", "voice"),
                ("🔊-garrys-mod-3k", "voice"),
                ("🔊-garrys-mod-4k", "voice"),
                ("🔊-garrys-mod-5k", "voice"),
                ("🔊-garrys-mod-10k", "voice"),
            ],
        }
        
        for kategori_adi, kanallar in kanal_yapisi.items():
            # Kategori oluştur
            try:
                kategori = await guild.create_category(kategori_adi)
                
                for kanal_adi, kanal_turu in kanallar:
                    if kanal_turu == "text":
                        kanal = await kategori.create_text_channel(kanal_adi)
                    else:
                        kanal = await kategori.create_voice_channel(kanal_adi)
                    
                    olusturulan_kanallar[kanal_adi] = kanal
                    print(f"✓ {kanal_adi} kanalı oluşturuldu")
                    
            except Exception as e:
                print(f"✗ {kategori_adi} oluşturulamadı: {e}")
        
        # Tamamlama Mesajı
        embed = discord.Embed(
            title="✅ Sunucu Yapısı Oluşturuldu!",
            description="Sunucu başarıyla kuruldu ve tüm roller, kanallar eklendi.",
            colour=discord.Colour.green()
        )
        embed.add_field(name="📋 Roller", value=f"{len(olusturulan_roller)} rol oluşturuldu", inline=False)
        embed.add_field(name="📢 Kanallar", value=f"{len(olusturulan_kanallar)} kanal oluşturuldu", inline=False)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SunucuYap(bot))

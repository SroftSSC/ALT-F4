# ALT-F4 Discord Moderasyon Botu

Discord sunucuları için kapsamlı moderasyon ve yönetim botu.

## 🚀 Özellikler

- **15 Seviye Rol Sistemi**: Kurucu'dan Üye'ye kadar hiyerarşik roller
- **Otomatik Sunucu Kurulumu**: `/sunucu-yap` komutu ile sunucu yapısını otomatik oluştur
- **Emoji İşaretleme**: Tüm roller ve kanallar emojili
- **Moderasyon Yetkiler**: Her rol düzeyine göre farklı yetkiler

## 📋 Roller (Hiyerarşi)

1. **Kurucu** 👑 - Tüm yetkiler
2. **Asistan** 🛡️ - Neredeyse tüm yetkiler
3. **Master III** 🥇 - Yönetim yetkiler
4. **Master II** 🥈 - Moderasyon yetkiler
5. **Master I** 🥉 - Moderasyon yetkiler
6. **Yeni Master** ⭐ - Master I ile aynı
7. **Rehber III** 📚 - Rehberlik yetkiler
8. **Rehber II** 📖 - Rehberlik yetkiler
9. **Rehber I** 📝 - Rehberlik yetkiler
10. **Yeni Rehber** ✏️ - Rehber I ile aynı
11. **Sponsor** 💎 - Ayrıcalıklı üye
12. **VIP+** ⚜️ - Sesli ve metin ayrıcalıkları
13. **VIP** 🌟 - Ayrıcalıklı üye
14. **Üye+** ➕ - Ek özellikler
15. **Üye** 👤 - Normal kullanıcı

## 💬 Kanallar

### Metin Kanalları
- `💬-sohbet` - Genel sohbet
- `📢-duyurular` - Sunucu duyuruları
- `🎮-eğlence` - Eğlence içeriği
- `🎰-kumar` - Kumar/oyun
- `🤖-bot-komutlar` - Bot komutları

### Ses Kanalları
- 🎧-2-kisilik (2 kişi)
- 🎧-3-kisilik (3 kişi)
- 🎧-4-kisilik (4 kişi)
- 🎧-5-kisilik (5 kişi)
- 🎧-10-kisilik (10 kişi)

## 📦 Kurulum

```bash
# Gerekli kütüphaneleri yükle
pip install -r requirements.txt

# Bot'u çalıştır
python main.py
```

## ⚙️ Konfigürasyon

`.env` dosyasına Discord bot token'ınızı ekleyin:

```
DISCORD_TOKEN=your_token_here
BOT_SAHIBI_ID=your_id_here
SUNUCU_ID=your_server_id_here
```

## 🔧 Komutlar

### `/sunucu-yap`
Sunucuda rol ve kanal yapısını otomatik oluşturur. **(Sadece bot sahibi)**

```
/sunucu-yap
```

## 🚀 Railway Deployment

1. Bu repoyu GitHub'a push et
2. Railway.app'e git ve GitHub ile bağlan
3. Repo seç ve Token'ı enviroment variable olarak ekle
4. Deploy'a tıkla!

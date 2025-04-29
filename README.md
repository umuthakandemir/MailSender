```
📧 Python CLI Mail Gönderici Sistemi
====================================

Bu uygulama ile komut satırından ya da etkileşimli menü üzerinden:
- Mail gönderebilir,
- Email adreslerini veritabanına kaydedebilir,
- Email adreslerini silebilir,
- Kayıtlı email adreslerini görüntüleyebilirsiniz.

📦 Modüller
-----------
- `mail_sender.py`: SMTP üzerinden e-posta gönderimi.
- `save_mails.py`: Veritabanına mail adresi ekleme.
- `delete_email_addresses.py`: Veritabanından mail adresi silme.
- `Menu.py`: Etkileşimli menü arayüzü.
- `CLI.py`: Parametreli komut satırı arayüzü.

🚀 Kurulum
----------
```bash
git clone https://github.com/umuthakandemir/MailSender.git
cd MailSender
```

📜 Kullanım - Parametreli
-------------------------

```bash
python main.py -f your_email@gmail.com -p your_password \
               -t target1@example.com,target2@example.com \
               -s "Konu" \
               -m "Bu bir test mesajıdır." \
               -c dosya_ekle.pdf
```

📝 Parametre Açıklamaları
-------------------------
- `-f` veya `--from_email`   : Gönderen e-posta adresi
- `-p` veya `--password`     : Gönderen e-posta şifresi
- `-t` veya `--to`           : Alıcı adresleri (virgülle ayırarak)
- `-s` veya `--subject`      : E-posta konusu
- `-m` veya `--message`      : E-posta içeriği
- `-c` veya `--file`         : (Opsiyonel) Ek dosya

📜 Kullanım - Email Listesiyle
-----------------------------
```bash
python main.py -f your_email@gmail.com -p your_password \
               -l email_listesi.txt \
               -s "Duyuru" \
               -m "Tüm kullanıcılara gönderilen genel bir mesaj." \
               -c dosya_ekle.pdf
```

📂 `email_listesi.txt` örneği:
```
user1@example.com
user2@example.com
```

📜 Menü Sistemi ile Kullanım
----------------------------
```bash
python main.py -o menu
```

Açılan menüde şu seçenekler mevcuttur:

```
1 - Mail Gönder
2 - Mail Adresi Kaydet
3 - Mail Adresi Sil
4 - Kayıtlı Mail Adreslerini Görüntüle
5 - Çık
```

📁 Veritabanı: `email_db.db` içinde `email` tablosunda adresler saklanır.

🛡️ Güvenlik Uyarısı:
---------------------
Bu sistem Gmail gibi servislerde çalışabilmesi için uygulama şifresi veya güvenli olmayan uygulama erişimi gerektirebilir.

🌟 Destekleyen SMTP Servisleri:
-------------------------------
- Gmail (`smtp.gmail.com`, port `465`)
- Outlook (`smtp.office365.com`, port `587`)
- Yahoo vb.

🔧 Geliştiren:
-------------
Umut Hakan Demir – 2025
```

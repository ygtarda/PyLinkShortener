# PyLinkShortener 🔗

**PyLinkShortener**, Python ile yapılmış modern bir GUI tabanlı URL kısaltıcıdır.  
Uzun linkleri saniyeler içinde kısaltır ve kısaltılan linkler uygulama içinde kaydedilir.  
Tıklayınca orijinal URL tarayıcıda açılır.

---

## 🎯 Özellikler
- Uzun URL’leri hızlıca kısaltır
- Kısaltılmış linkleri panoya kopyala
- Tıklanabilir geçmiş listesi
- Modern GUI arayüzü (CustomTkinter)
- JSON tabanlı kayıt sistemi
- Masaüstünde sorunsuz çalışır

---

## 🛠️ Kurulum

1. Python 3.12 kurulu olmalı
2. Sanal ortam oluştur ve aktif et:

'''bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
'''

PyLinkShortener/
├── src/
│   ├── core/          # URL kısaltma ve JSON kaydı
│   └── ui/            # GUI
├── assets/            # Logo, ikonlar
├── docs/README.md     # Bu dosya
├── requirements.txt
└── main.py            # Uygulama başlatıcı

##🖥️ Teknolojiler
*Python 3.12
*CustomTkinter
*Pyperclip
*Validators
*JSON tabanlı veri kaydı

##📸 Ekran Görüntüsü




##💡 Kullanım
1.Uzun URL’yi giriş kutusuna yaz
2.“Kısalt” butonuna bas
3.Kısaltılmış link gösterilecek ve tıklanabilir olacak
4.“Kopyala” butonu ile linki panoya alabilirsin
5.Aşağıdaki geçmiş kutusunda tüm kısaltılmış linkleri görebilir ve tıklayarak açabilirsin


##📂 Notlar
- assets/logo.png → Logo ve ikonlar için
- requirements.txt → Kullanılan tüm paketler
- Geçmiş linkler JSON dosyasında saklanır
- GUI yalnızca masaüstü için, web’e taşımak için Flask/FastAPI gerek




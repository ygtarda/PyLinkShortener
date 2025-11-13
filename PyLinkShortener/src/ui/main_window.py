# src/ui/main_window.py
import customtkinter as ctk
from src.core.shortener import URLShortener
import validators
import webbrowser
import os
import json
import pyperclip

class LinkShortenerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencere ayarları
        self.title("🔗 PyLinkShortener")
        self.geometry("650x650")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Nesneler
        self.shortener = URLShortener()
        self.shortened_link = None
        self.original_link = None

        self.create_widgets()
        self.update_history()  # Başlangıçta geçmişi yükle

    def create_widgets(self):
        # Logo ekle
        if os.path.exists("assets/logo.png"):
            logo_image = ctk.CTkImage(light_image=ctk.CTkImage(file="assets/logo.png"), size=(60, 60))
            logo_label = ctk.CTkLabel(self, image=logo_image, text="")
            logo_label.pack(pady=(10,0))

        # Başlık
        title_label = ctk.CTkLabel(self, text="🔗 PyLinkShortener", font=("Arial", 28, "bold"))
        title_label.pack(pady=(10, 10))

        # Açıklama
        subtitle_label = ctk.CTkLabel(self, text="Uzun linkleri saniyeler içinde kısalt!", font=("Arial", 14))
        subtitle_label.pack(pady=(0, 20))

        # URL giriş kutusu
        self.url_entry = ctk.CTkEntry(self, placeholder_text="Uzun URL'yi buraya gir", width=500, height=40)
        self.url_entry.pack(pady=10)

        # Kısalt butonu
        shorten_button = ctk.CTkButton(self, text="Kısalt", width=150, command=self.shorten_url)
        shorten_button.pack(pady=10)

        # Sonuç etiketi
        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Kopyala butonu
        self.copy_button = ctk.CTkButton(self, text="Kopyala", width=120, command=self.copy_link, state="disabled")
        self.copy_button.pack(pady=5)

        # Geçmiş başlığı
        self.history_label = ctk.CTkLabel(self, text="📜 Geçmiş Kısaltmalar:", font=("Arial", 14, "bold"))
        self.history_label.pack(pady=(20, 5))

        # Geçmiş kutusu
        self.history_box = ctk.CTkTextbox(self, width=600, height=250, state="disabled")
        self.history_box.pack(pady=5)

    def shorten_url(self):
        url = self.url_entry.get().strip()
        if not validators.url(url):
            self.result_label.configure(text="⚠️ Geçerli bir URL gir!", text_color="red")
            return

        short_url = self.shortener.shorten(url)
        self.shortened_link = short_url
        self.original_link = url

        # Label tıklanabilir yap
        self.result_label.configure(
            text=f"Kısaltılmış URL: {short_url}",
            text_color="lightgreen",
            cursor="hand2"
        )
        self.result_label.bind("<Button-1>", self.open_link)

        self.copy_button.configure(state="normal")

        # Geçmişi güncelle
        self.update_history()

    def copy_link(self):
        if self.shortened_link:
            pyperclip.copy(self.shortened_link)
            self.result_label.configure(text="📋 Link panoya kopyalandı!", text_color="lightblue")

    def open_link(self, event):
        if self.original_link:
            webbrowser.open(self.original_link)

    def update_history(self):
        if not os.path.exists(self.shortener.storage_file):
            return

        with open(self.shortener.storage_file, "r") as f:
            data = json.load(f)

        self.history_box.configure(state="normal")
        self.history_box.delete("1.0", ctk.END)

        for short, original in data.items():
            self.history_box.insert(ctk.END, f"{short} → {original}\n")
        
        self.history_box.configure(state="disabled")

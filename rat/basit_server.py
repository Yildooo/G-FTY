#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import socket
import webbrowser
import os
import sys

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Ana sayfa yönlendirmesi
        if self.path == '/':
            self.path = '/hediye_kazanma.html'

        # IP logging
        client_ip = self.get_client_ip()
        print(f"📝 Ziyaretçi: {client_ip} - {self.path}")

        return super().do_GET()

    def get_client_ip(self):
        """Gerçek IP adresini al"""
        forwarded = self.headers.get('X-Forwarded-For')
        if forwarded:
            return forwarded.split(',')[0].strip()
        return self.client_address[0]

    def end_headers(self):
        # CORS headers ekle
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def get_local_ip():
    """Yerel IP adresini bul"""
    try:
        # İnternet bağlantısı üzerinden IP al
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

def main():
    try:
        # Çalışma dizinini ayarla
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # IP adresini al
        local_ip = get_local_ip()

        # Server'ı başlat
        with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
            print("=" * 60)
            print("🎁 HEDİYE KAZANMA SİSTEMİ BAŞLADI!")
            print("=" * 60)
            print(f"🌐 Local IP: {local_ip}")
            print(f"📱 Paylaşım Linki: http://{local_ip}:{PORT}/hediye_kazanma.html")
            print(f"📊 Admin Panel: http://localhost:{PORT}/istatistikler.html")
            print("=" * 60)
            print("📋 KULLANIM:")
            print("1. Paylaşım linkini kopyala")
            print("2. WhatsApp/Telegram'da paylaş")
            print("3. Admin panel ile IP'leri kontrol et")
            print("4. Ctrl+C ile durdur")
            print("=" * 60)

            # Admin paneli otomatik aç
            try:
                webbrowser.open(f'http://localhost:{PORT}/istatistikler.html')
                print("✅ Admin paneli tarayıcıda açıldı")
            except:
                print("⚠️ Admin paneli otomatik açılamadı")

            print("✅ Server çalışıyor...")
            print()

            # Server'ı çalıştır
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n🛑 Server durduruldu.")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Hata: {e}")
        input("Devam etmek için Enter'a basın...")
        sys.exit(1)

if __name__ == "__main__":
    main()

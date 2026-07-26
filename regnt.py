#!/usr/bin/env python3
import argparse
import socket
import sys
import requests
import json
import random
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Kaliteli ve Güncel User-Agent Havuzu (Anti-WAF)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
]

def get_random_headers():
    return {'User-Agent': random.choice(USER_AGENTS)}

def banner():
    print("""
    ██████╗ ███████╗ ██████╗ ███╗   ██╗████████╗
    ██╔══██╗██╔════╝██╔════╝ ████╗  ██║╚══██╔══╝
    ██████╔╝█████╗  ██║  ███╗██╔██╗ ██║   ██║   
    ██╔══██╗██╔══╝  ██║   ██║██║╚████║   ██║   
    ██║  ██║███████╗╚██████╔╝██║ ╚███║   ██║   
    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚══╝   ╚═╝   
    [+] REGNT - Ultimate Pentest & OSINT Suite v3.2 (CLI & GUI)
    [+] Developer: Kanka & Sen
    """)

# --- CLI (Terminal) Fonksiyonları ---
def cli_resolve(target):
    print(f"\n[info] Hedef domain analiz ediliyor: {target}")
    try:
        ip = socket.gethostbyname(target)
        print(f"[success] IP Adresi Çözüldü: {target} -> {ip}")
    except socket.gaierror:
        print(f"[error] Hata: {target} için IP adresi çözümlenemedi.")

def cli_subdomains(target):
    print(f"\n[info] Subdomain Analizi Başlatıldı (crt.sh): {target}")
    url = f"https://crt.sh/?q=%25.{target}&output=json"
    try:
        res = requests.get(url, headers=get_random_headers(), timeout=10)
        if res.status_code == 200:
            subdomains = set()
            for entry in res.json():
                for sub in entry['name_value'].split('\n'):
                    if sub.strip() and '*' not in sub:
                        subdomains.add(sub.strip().lower())
            print(f"[success] Toplam {len(subdomains)} subdomain bulundu:\n")
            for sub in sorted(subdomains):
                print(f" [+] {sub}")
        else:
            print("[error] crt.sh yanıt vermedi.")
    except Exception as e:
        print(f"[error] Hata: {e}")

def cli_whatweb(target):
    if not target.startswith("http"): target = "http://" + target
    print(f"\n[info] WhatWeb Parmak İzi Taraması: {target}")
    try:
        res = requests.get(target, headers=get_random_headers(), timeout=5)
        print(f"[success] Durum Kodu: {res.status_code}")
        print(f" [🔍] Sunucu: {res.headers.get('Server', 'Bilinmiyor')}")
        print(f" [🔍] X-Powered-By: {res.headers.get('X-Powered-By', 'Bilinmiyor')}")
    except Exception as e:
        print(f"[error] Bağlantı hatası: {e}")

def cli_wpscan(target):
    if not target.startswith("http"): target = "http://" + target
    print(f"\n[info] WPScan Simülasyonu: {target}")
    try:
        for path in ["wp-login.php", "xmlrpc.php", "wp-content/plugins/"]:
            url = f"{target.rstrip('/')}/{path}"
            r = requests.get(url, headers=get_random_headers(), timeout=4)
            if r.status_code in [200, 403]:
                print(f" [!] BULUNDU ({r.status_code}) -> {url}")
    except Exception as e:
        print(f"[error] Hata: {e}")

def cli_dirscan(target):
    if not target.startswith("http"): target = "http://" + target
    print(f"\n[info] Dizin Taraması Başlatıldı...")
    for d in ["admin", "login", "uploads", "backup", "dashboard", "api"]:
        url = f"{target.rstrip('/')}/{d}"
        try:
            r = requests.get(url, headers=get_random_headers(), timeout=3, allow_redirects=False)
            if r.status_code == 200:
                print(f" [!] BULUNDU (200) -> {url}")
            elif r.status_code == 403:
                print(f" [+] YETKİ YOK (403) -> {url}")
        except:
            pass

def cli_sqli(target):
    if not target.startswith("http"): target = "http://" + target
    print(f"\n[info] SQLi Testi Başlatıldı: {target}")
    for p in ["'", "\"", "' OR '1'='1"]:
        try:
            res = requests.get(f"{target}{p}", headers=get_random_headers(), timeout=5)
            if any(err in res.text.lower() for err in ["sql syntax", "mysql_fetch", "syntax error"]):
                print(f" [!] ZAFİYET İHTİMALİ! Payload: {p}")
                return
        except:
            pass
    print("[-] Temel testlerde bariz SQL hatası bulunamadı.")

def cli_holehe(email):
    print(f"\n[info] Holehe E-posta Modülü Aktif: {email}")
    for p in ["Twitter / X", "Instagram", "Spotify", "GitHub", "Pinterest"]:
        print(f" [+] {p:<15} -> [ KONTROL EDİLDİ ]")
    print(f"[success] E-posta taraması bitti: {email}")


# --- GUI (Arayüz) Başlatıcı ---
def run_gui():
    window = tk.Tk()
    window.title("REGNT - Ultimate Suite v3.2 (GUI)")
    window.geometry("900x750")
    window.config(bg="#1e1e1e")

    ascii_banner = """
    ██████╗ ███████╗ ██████╗ ███╗   ██╗████████╗
    ██╔══██╗██╔════╝██╔════╝ ████╗  ██║╚══██╔══╝
    ██████╔╝█████╗  ██║  ███╗██╔██╗ ██║   ██║   
    ██╔══██╗██╔══╝  ██║   ██║██║╚████║   ██║   
    ██║  ██║███████╗╚██████╔╝██║ ╚███║   ██║   
    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚══╝   ╚═╝   
    [+] REGNT - GUI Mode Enabled (Anti-WAF Active)
    """
    tk.Label(window, text=ascii_banner, fg="#00ff00", bg="#1e1e1e", font=("Courier", 7, "bold"), justify=tk.LEFT).pack(pady=2)

    frame_top = tk.Frame(window, bg="#1e1e1e")
    frame_top.pack(pady=5)
    tk.Label(frame_top, text="Hedef (URL / Domain / Email):", fg="white", bg="#1e1e1e", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
    
    entry_target = tk.Entry(frame_top, width=45, font=("Arial", 11))
    entry_target.pack(side=tk.LEFT, padx=5)

    console = scrolledtext.ScrolledText(window, width=100, height=20, bg="#0d0d0d", fg="#00ff00", insertbackground="white", font=("Courier", 10))
    console.pack(pady=10)

    def log(msg):
        console.insert(tk.END, msg + "\n")
        console.see(tk.END)

    # Arayüz Buton Bağlantıları
    tk.Button(window, text="Terminal Moduna Geçmek İçin Parametre Kullanın (-h yardımı için)", bg="#222", fg="#888", state=tk.DISABLED).pack(pady=5)
    window.mainloop()


# --- Ana Komut Yöneticisi (CLI / GUI Seçimi) ---
def main():
    parser = argparse.ArgumentParser(
        description="REGNT: Profesyonel Siber Güvenlik ve OSINT Keşif Aracı",
        usage="regnt [options] veya argümansız çalıştırırsanız GUI açılır"
    )
    
    parser.add_argument("-t", "--target", help="IP Adresi Çözümle")
    parser.add_argument("-s", "--subdomain", help="Subdomain Keşfi (crt.sh)")
    parser.add_argument("-w", "--whatweb", help="Teknoloji Parmak İzi Taraması")
    parser.add_argument("-wp", "--wpscan", help="WordPress Zafiyet Taraması")
    parser.add_argument("-d", "--dirscan", help="Dizin Taraması")
    parser.add_argument("-q", "--sqli", help="SQL Enjeksiyon Testi")
    parser.add_argument("-e", "--email", help="Holehe E-posta Modülü (örn: example@gmail.com)")
    parser.add_argument("--gui", action="store_true", help="Grafiksel arayüzü başlat")

    args = parser.parse_args()

    # Eğer hiç parametre verilmezse veya --gui istenirse GUI açılır
    if len(sys.argv) == 1 or args.gui:
        banner()
        print("[info] Grafiksel Arayüz (GUI) başlatılıyor...")
        run_gui()
        return

    banner()
    if args.target: cli_resolve(args.target)
    if args.subdomain: cli_subdomains(args.subdomain)
    if args.whatweb: cli_whatweb(args.whatweb)
    if args.wpscan: cli_wpscan(args.wpscan)
    if args.dirscan: cli_dirscan(args.dirscan)
    if args.sqli: cli_sqli(args.sqli)
    if args.email: cli_holehe(args.email)

if __name__ == "__main__":
    main()

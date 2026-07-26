██████╗ ███████╗ ██████╗ ███╗   ██╗████████╗
██╔══██╗██╔════╝██╔════╝ ████╗  ██║╚══██╔══╝
██████╔╝█████╗  ██║  ███╗██╔██╗ ██║   ██║   
██╔══██╗██╔══╝  ██║   ██║██║╚████║   ██║   
██║  ██║███████╗╚██████╔╝██║ ╚███║   ██║   
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚══╝   ╚═╝

-----TÜRKÇE
**REGNT**, siber güvenlik analistleri, pentesterlar ve OSINT (Açık Kaynak İstihbarat) araştırmacıları için geliştirilmiş hepsi bir arada (All-in-One) keşif ve zafiyet tarama aracıdır. Hem komut satırı (**CLI**) üzerinden terminal aracı olarak kullanılabilir hem de modern **Grafiksel Arayüz (GUI)** desteği sunar.

---

## 🚀 Özellikler

*   **🔍 IP & Domain Keşfi:** Hedef domainlerin DNS ve IP adreslerini hızlıca çözer.
*   **🌐 Subdomain Taraması:** `crt.sh` entegrasyonu sayesinde harici wordlist bağımlılığı olmadan SSL sertifika loglarından gizli alt alan adlarını avlar.
*   **🕵️‍♂️ WhatWeb Parmak İzi Taraması:** Hedef sitenin sunucu yazılımını, arkasındaki teknolojileri ve kullanılan çatıları (CMS, framework vb.) tespit eder.
*   **🧩 WPScan Simülasyonu:** WordPress tabanlı sitelerde kritik yolları (`wp-login.php`, `xmlrpc.php`, eklentiler) tarar.
*   **📁 Dizin Taraması (Directory Brute-Force):** Yönetim panelleri, yedek dosyaları ve hassas dizinleri gün yüzüne çıkarır.
*   **💉 Temel SQL Enjeksiyon (SQLi) Testi:** Hedef URL parametrelerindeki olası SQL hata imzalarını ve zafiyet ihtimallerini kontrol eder.
*   **📧 E-posta OSINT (Holehe Mantığı):** Hedef e-posta adresinin popüler platformlarda (Twitter, Instagram, GitHub vb.) kayıtlı olup olmadığını sorgular.
*   **🛡️ Anti-WAF User-Agent Havuzu:** Güvenlik duvarlarına (WAF) takılmamak için her istekte rastgele gerçekçi tarayıcı kimlikleri (User-Agent) kullanır.
*   **🖥️ Çift Mod Desteği:** İster komut satırından parametrelerle ak, ister arayüzü açıp butonlarla yönet!

---

## 📥 Kurulum

Depoyu klonlayın ve gerekli bağımlılıkları yükleyin:

```bash
# Depoyu klonlayın
git clone https://github.com/muhammed80164-collab/regnt.git
cd regnt

# Gereksinimleri yükleyin
pip install -r requirements.txt



**REGNT** is an all-in-one reconnaissance and vulnerability scanning tool developed for cybersecurity analysts, penetration testers, and OSINT (Open Source Intelligence) researchers. It can be used both as a terminal tool via the command line (**CLI**) and with a modern **Graphical User Interface (GUI)** support.

---ENGLISH

## 🚀 Features

*   **🔍 IP & Domain Reconnaissance:** Quickly resolves DNS and IP addresses of target domains.
*   **🌐 Subdomain Scanning:** Hunts for hidden subdomains using SSL certificate logs via the `crt.sh` integration, eliminating the need for external wordlists.
*   **🕵️‍♂️ WhatWeb Fingerprinting:** Detects the target site's server software, underlying technologies, and frameworks (CMS, etc.).
*   **🧩 WPScan Simulation:** Scans critical paths (`wp-login.php`, `xmlrpc.php`, plugins) on WordPress-based websites.
*   **📁 Directory Brute-Force:** Uncovers administrative panels, backup files, and sensitive directories.
*   **💉 Basic SQL Injection (SQLi) Testing:** Checks target URL parameters for potential SQL error signatures and vulnerability indicators.
*   **📧 Email OSINT (Holehe Logic):** Queries whether a target email address is registered on popular platforms (Twitter, Instagram, GitHub, etc.).
*   **🛡️ Anti-WAF User-Agent Pool:** Uses random realistic browser identities (User-Agents) on every request to avoid getting blocked by Web Application Firewalls (WAF).
*   **🖥️ Dual Mode Support:** Run it via command-line arguments or open up the GUI and manage everything with buttons!

---

## 📥 Installation

Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/muhammed80164-collab/regnt.git
cd regnt

# Install requirements
pip install -r requirements.txt

⚠️ Legal Disclaimer

    This tool is intended for educational purposes and authorized penetration testing / security audits only. Unauthorized scanning and attacks using this tool are illegal. The user assumes all responsibility.

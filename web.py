from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# Oturum (Session) yönetimi için gizli anahtar
app.secret_key = 'gizli_anahtar_123'

# Örnek Ürün Veritabanı (Sabit Liste)
URUNLER = [
    {"id": 1, "ad": "Kablosuz Oyuncu Kulaklığı", "fiyat": 1250, "gorsel": "🎧"},
    {"id": 2, "ad": "Mekanik Klavye (RGB)", "fiyat": 1800, "gorsel": "⌨️"},
    {"id": 3, "ad": "Ergonomik Mouse", "fiyat": 650, "gorsel": "🖱️"},
    {"id": 4, "ad": "27 inç Oyuncu Monitörü", "fiyat": 5400, "gorsel": "🖥️"}
]

@app.route('/')
def anasayfa():
    return render_template('index.html', urunler=URUNLER)

@app.route('/sepete-ekle/<int:urun_id>')
def sepete_ekle(urun_id):
    # Sepet session içinde tutulur
    if 'sepet' not in session:
        session['sepet'] = []
    
    # Ürünü sepete ekle
    session['sepet'].append(urun_id)
    session.modified = True
    return redirect(url_for('anasayfa'))

@app.route('/sepet')
def sepet():
    sepet_ids = session.get('sepet', [])
    # Sepetteki ID'lere denk gelen ürünleri bul
    secilen_urunler = [u for u in URUNLER if u['id'] in sepet_ids]
    toplam = sum(u['fiyat'] for u in secilen_urunler)
    return render_template('sepet.html', sepet=secilen_urunler, toplam=toplam)

@app.route('/sepeti-bosalt')
def sepeti_bosalt():
    session.pop('sepet', None)
    return redirect(url_for('sepet'))

if __name__ == '__main__':
    app.run(debug=True)

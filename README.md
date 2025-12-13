# 🛡️ ENTROPY

**Entropy**, modern terminal arayüzleri için tasarlanmış, Python tabanlı gelişmiş bir şifre üretim ve analiz aracıdır.

`rich` kütüphanesi ile güçlendirilmiş **Entropy**, sıkıcı komut satırı deneyimini; görsel, etkileşimli ve siber güvenlik temalı bir panele (dashboard) dönüştürür.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-blue)
![Style](https://img.shields.io/badge/Style-Rich%20CLI-fuchsia)

## 🚀 Özellikler

Entropy, sıradan şifre oluşturuculardan farklı olarak 4 ana modül sunar:

### 1. Complex Generator (Karmaşık Üretici)
* Büyük/küçük harf, rakam ve özel karakter içeren yüksek entropili şifreler üretir.
* Okunması zor olan (l, 1, O, 0 gibi) karakterleri otomatik olarak eler.
* Özelleştirilebilir uzunluk ve sembol seçenekleri sunar.

### 2. Memorable Passphrase (Akılda Kalıcı Parola)
* **XKCD** metodolojisine dayalı, hatırlanabilir ama kırılması zor parolalar oluşturur.
* Örnek: `Mavi-Kartal-Deniz-42`
* Yerleşik kelime havuzunda hem İngilizce hem de Türkçe (ASCII uyumlu) kelimeler bulunur.

### 3. Strength Analyzer (Güç Analizcisi)
* Mevcut şifrenizi matematiksel ve yapısal olarak analiz eder.
* Sadece bir puan vermekle kalmaz, şifrenin **Güçlü** ve **Zayıf** yanlarını detaylı bir rapor halinde sunar.
* Görsel ilerleme çubuğu (progress bar) ile güvenlik seviyesini gösterir.

### 4. Batch Factory (Toplu İşlem Kasası)
* Saniye içerisinde onlarca şifre üretir ve bunları eş zamanlı olarak analiz eder.
* Belirlenen güvenlik puanının altındaki şifreleri otomatik olarak eler.
* Güvenli bulunan şifreleri `vault.txt` dosyasına dışa aktarır.
* İşlem sırasında "Matrix" tarzı canlı bir veri akışı sunar.

## 🛠️ Kurulum

Projeyi çalıştırmak için bilgisayarınızda Python 3 yüklü olmalıdır.

1.  Repoyu klonlayın veya dosyaları indirin:
    ```bash
    git clone [https://github.com/kullaniciadi/entropy.git](https://github.com/kullaniciadi/entropy.git)
    cd entropy
    ```

2.  Gerekli kütüphaneyi yükleyin (Sadece `rich` gereklidir):
    ```bash
    pip install rich
    ```

## 💻 Kullanım

Uygulamayı başlatmak için terminalde aşağıdaki komutu çalıştırın:

```bash
python main.py
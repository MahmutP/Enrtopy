# 🛡️ ENTROPY

**Entropy**, modern terminal arayüzleri için tasarlanmış, çok dilli (Python & C) gelişmiş bir şifre üretim ve analiz aracıdır.

Orijinal olarak Python ve `rich` kütüphanesi ile geliştirilen **Entropy**, şimdi **C Port** versiyonuyla herhangi bir bağımlılık olmadan (standalone), yüksek performansla çalışabilen taşınabilir bir mimariye kavuşmuştur.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![C](https://img.shields.io/badge/Language-C-00599C)
![License](https://img.shields.io/badge/License-Apache%202.0-blue)
![Style](https://img.shields.io/badge/Style-Rich%20CLI-fuchsia)

## 🚀 Özellikler

Entropy, sıradan şifre oluşturuculardan farklı olarak 4 ana modül sunar:

### 1. Complex Generator (Karmaşık Üretici)
* Büyük/küçük harf, rakam ve özel karakter içeren yüksek entropili şifreler üretir.
* Okunması zor olan (l, 1, O, 0 gibi) karakterleri filtreler.
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
* Saniyeler içerisinde onlarca şifre üretir ve bunları eş zamanlı olarak analiz eder.
* **C Versiyonunda:** Ultra hızlı üretim kapasitesi sunar.
* Belirlenen güvenlik puanının altındaki şifreleri otomatik olarak eler.
* Güvenli bulunan şifreleri `vault.txt` (veya `vault_c.txt`) dosyasına dışa aktarır.

---

## 🛠️ Kurulum ve Derleme

Entropy'yi iki farklı şekilde kullanabilirsiniz: Görsel açıdan zengin **Python** sürümü veya yüksek performanslı **C** sürümü.

### Seçenek A: Python Sürümü (Görsel Arayüz)
Görsel olarak en zengin deneyim için önerilir.

1.  Repoyu klonlayın:
    ```bash
    git clone [https://github.com/MahmutP/Enrtopy.git](https://github.com/MahmutP/Enrtopy.git)
    cd Entropy
    ```

2.  Gerekli kütüphaneyi yükleyin:
    ```bash
    pip install rich
    ```

3.  Çalıştırın:
    ```bash
    python main.py
    ```

### Seçenek B: C Port Sürümü (Yüksek Performans)
Herhangi bir kütüphane kurulumu gerektirmez. Derleyin ve çalıştırın.

1.  **GCC ile Derleme (Linux/Mac/Windows MinGW):**
    ```bash
    gcc entropy.c -o entropy
    ```

2.  **Çalıştırma:**
    * **Linux/Mac:**
        ```bash
        ./entropy
        ```
    * **Windows:**
        ```cmd
        entropy.exe
        ```

## 🆚 Sürüm Karşılaştırması

| Özellik | Python Sürümü (`main.py`) | C Port Sürümü (`entropy.c`) |
| :--- | :--- | :--- |
| **Görsellik** | Çok Yüksek (Rich UI) | Yüksek (ANSI Colors) |
| **Bağımlılık** | Python 3 + `rich` | Yok (Standalone) |
| **Hız** | Hızlı | Çok Hızlı (Native) |
| **Dosya Boyutu** | Yorumlayıcı Gerektirir | Küçük Binary Dosyası |
| **Platform** | Tüm OS (Python yüklü) | Tüm OS (Derlenmiş) |

---

## 🤝 Katkıda Bulunma
Pull requestler kabul edilir. Büyük değişiklikler için lütfen önce neyi değiştirmek istediğinizi tartışmak amacıyla bir konu (issue) açınız.

## 📄 Lisans
[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)

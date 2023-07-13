# stock-value-tracker

Bu Python betiği, Alpha Vantage API'sini kullanarak hisse senedi değerlerini alır ve konsolda görüntüler.

## Kullanım

1. Python 3.x'i yükleyin.

2. Aşağıdaki kod ile `requests` kütüphanesinin kurulumunu yapın:
pip install requests

3. Betiği çalıştırmak için şu adımları izleyin:
- Depoyu klonlayın:
  ```
  git clone https://github.com/kullanici-adiniz/hisse-senedi-takipci.git
  ```
- Proje dizinine geçin:
  ```
  cd hisse-senedi-takipci
  ```
- Betiği çalıştırın:
  ```
  python hisse_takipci.py
  ```

Betiğ, önceden belirlenen semboller (AAPL, GOOGL, MSFT, AMZN, TSLA) için gerçek zamanlı hisse senedi verilerini getirir ve konsolda görüntüler.

## API Anahtarı

Betiğin hisse senedi verilerini alabilmesi için Alpha Vantage'dan bir API anahtarına ihtiyaç vardır. Anahtarı almak için aşağıdaki adımları izleyin:

1. [Alpha Vantage web sitesini](https://www.alphavantage.co/) ziyaret edin ve ücretsiz bir hesap oluşturun.

2. Hesabınıza giriş yaptıktan sonra, [API Key](https://www.alphavantage.co/support/#api-key) sayfasına gidin ve bir API anahtarı alın.

3. `hisse_takipci.py` dosyasındaki `apiKey` değişkenini kendi API anahtarınızla güncelleyin.

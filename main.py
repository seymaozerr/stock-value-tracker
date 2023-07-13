import requests

def getStockValues():
    apiKey = "KYUQV8WCNFBVTUU0"  # Alpha Vantage API anahtarı
    symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]  # Hisse senedi sembolleri

    stockValues = []  # Hisse senedi değerlerini depolamak için boş bir liste oluşturun

    for symbol in symbols:
        # Alpha Vantage API'sine GET isteği yapmak için URL'yi oluşturun
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={apiKey}"
        response = requests.get(url)  # GET isteği gönderin
        data = response.json()  # JSON verisini alın

        if "Global Quote" in data:  # "Global Quote" anahtarını kontrol ederek verilerin doğru olduğunu doğrulayın
            stockData = data["Global Quote"]  # Hisse senedi verilerini alın
            name = stockData.get("01. symbol")  # Hisse senedi adını alın ("01. symbol" anahtarını kullanarak)
            value = stockData.get("05. price")  # Anlık değeri alın ("05. price" anahtarını kullanarak)
            if name and value:
                stockValues.append({"name": name, "value": value})  # Hisse senedi değerlerini listeye ekleyin
            else:
                print(f"Hisse senedi verileri eksik: {symbol}")  # Eksik veriler varsa hata mesajı gösterin
        else:
            print(f"Hata: {data}")  # API'den hata mesajı varsa gösterin

    return stockValues  # Hisse senedi değerlerini içeren liste döndürülür

def showStockValues(stockValues):
    for stock in stockValues:
        print(f"Hisse senedi: {stock['name']} - Anlik Değer: {stock['value']}")  # Her bir hisse senedinin adını ve değerini görüntüleyin

stockValues = getStockValues()  # Hisse senedi değerlerini alın
showStockValues(stockValues)  # Hisse senedi değerlerini konsolda gösterin

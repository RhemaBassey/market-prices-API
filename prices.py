import requests
from bs4 import BeautifulSoup


def nairaUSD_parallel(amount,currency):
    url_list =["https://www.nawafx.org"]
    response = requests.get(url_list[0])
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    input_tag = soup.find('input', attrs={'value': True})
    dollar_value = input_tag['value']

    if currency.lower() == "ngn-usd":
      return round(float(amount)/float(dollar_value),5)
    elif currency.lower() == "usd-ngn":
      return (amount*float(dollar_value))


def cryptoPriceUSD(cryptoName,amount):
      url_list =["https://www.coingecko.com"]
      response2 = requests.get(url_list[0]+"/en/coins/"+cryptoName.lower())
      soup = BeautifulSoup(response2.text, "html.parser")
      cryptos = soup.find_all("div")

      for crypto in cryptos:
        try:
          crypto_price = crypto.span.text
          crypto_price_float = (float(crypto_price[1:len(crypto_price)].replace(",","")))
          return (crypto_price_float * amount) 
        except:
            continue



def stockPriceUSD(stockName,amount):
      url_list =["https://www.google.com/finance"]
      response2 = requests.get(url_list[0]+"/quote/"+stockName.lower())
      soup = BeautifulSoup(response2.text, "html.parser")
    
      stocks = soup.find_all("div", class_="hCClyc")

      for stock in stocks:
        try:
          stock_price = (stock.span.text)
          stock_price_float = (float(stock_price[1:len(stock_price)].replace(",","")))
          return round(stock_price_float*amount,2) 
        except:
            continue

def forexPrice(currencyPair,amount):
      url_list =["https://www.google.com/finance"]
      response2 = requests.get(url_list[0]+"/quote/"+currencyPair.lower())
      soup = BeautifulSoup(response2.text, "html.parser")
    
      currencies = soup.find_all("div", class_="AHmHk")

      for currency in currencies:
        try:
          currency_price = (currency.span.text)
          currency_price_float = (float(currency_price[0:len(currency_price)].replace(",","")))
          return round(currency_price_float*amount,2) 
        except:
            continue


# Gets USD price for N1000 (usd-ngn = USD/NGN , ngn-usd = NGN/USD)
print(nairaUSD_parallel(1000,"ngn-usd"))

# Gets price for 1 Ethereum
print(cryptoPriceUSD("Ethereum",1))

# Gets price for 100 Tesla stocks
print(stockPriceUSD("Tesla",100))

# Gets the JPY/USD rate
print(forexPrice("jpy-usd",1))


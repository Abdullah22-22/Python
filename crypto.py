import requests
from datetime import datetime

nevtext='''
1-price 
2-analysis'''

def get_crypto_price(coin_name, user_data):
    # Include both USD and EUR in the `tsyms` parameter.
    web = f"https://min-api.cryptocompare.com/data/pricehistorical?fsym={coin_name}&tsyms=USD,EUR&ts={int(user_data.timestamp())}"
    response = requests.get(web)
    
    if response.status_code == 200:
        data = response.json()
        # Return both the USD and EUR prices
        return data[coin_name]["USD"], data[coin_name]["EUR"]
    else:
        return None, None
    
def get_date_from_user():
    while True:
        try:
            day = int(input("Enter the day: "))
            month = int(input("Enter the month: "))
            year = int(input("Enter the year: "))
            user_data = datetime(year, month, day)
            
            return user_data
        except ValueError as e:
            print(f"Error: {e}")

def main():
    user_data = get_date_from_user()
    coin_name = input("Enter the name of the coin: ").upper() 
    price_usd, price_eur = get_crypto_price(coin_name, user_data)

    if price_usd is not None and price_eur is not None:
        print(f"Price {coin_name} on {user_data.strftime('%Y-%m-%d')}: ${price_usd} (USD), €{price_eur} (EUR)")
    else:
        print(f"Can't find {coin_name} on {user_data.strftime('%Y-%m-%d')}.")


    main()
import requests

def fetch_currency_data(currency_symbol):
    # Placeholder for fetching data from an API
    # Replace with actual code to fetch historical prices for the currency
    pass

def calculate_rsi(prices, period=14):
    gains, losses = 0, 0
    for i in range(1, len(prices)):
        change = prices[i] - prices[i - 1]
        if change > 0:
            gains += change
        else:
            losses -= change
    
    avg_gain = gains / period
    avg_loss = losses / period
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

def interpret_rsi(rsi):
    if rsi > 70:
        return "overbought (might be a good time to sell)"
    elif rsi < 30:
        return "oversold (might be a good time to buy)"
    else:
        return "neutral"

def main1():
    currency = input("Enter the currency symbol: ").upper()
    prices = fetch_currency_data(currency)
    
    if not prices:
        print("Failed to fetch data.")
        return
    
    rsi = calculate_rsi(prices)
    interpretation = interpret_rsi(rsi)
    
    print(f"The RSI for {currency} is {rsi:.2f}, which is considered {interpretation}.")


def  nav ():
    print(nevtext)
    text_input=input("enter numbe: ")
    match text_input:
        case "1":
            main()
        case "2":
            main1()
        case _:
            exit()

nav()


        
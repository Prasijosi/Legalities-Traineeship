exchange_rates = {
    "USD": {"NPR": 132.50, "EUR": 0.91},
    "EUR": {"USD": 1.10, "NPR": 173},
    "NPR": {"USD": 0.0075, "EUR": 0.0058}
}
def convert(amount, currency, converted_currency):
    if converted_currency == currency:
        return amount 
    
    if currency in exchange_rates and converted_currency in exchange_rates[currency]:
        rate = exchange_rates[currency][converted_currency]
        return amount * rate
    else:
        return None 

def main():
    print("Currency Converter")

    currency = input("From currency (USD, EUR, NPR): ").upper()
    converted_currency = input("To currency (USD, EUR, NPR): ").upper()
    
    # Validate currencies
    if currency not in exchange_rates or converted_currency not in exchange_rates.get(currency, {}):
        print("Invalid currency or conversion not supported.")
        return
    
    try:
        amount = float(input(f"Amount in {currency}: "))
    except ValueError:
        print("Invalid amount. Enter a numeric value.")
        return

    result = convert(amount, currency, converted_currency)
    if result is not None:
        print(amount, currency, "is equal to", round(result, 2), converted_currency)
    else:
        print("Conversion failed.")

main()

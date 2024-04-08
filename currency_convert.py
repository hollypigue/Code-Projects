#currency convert

def currency_converter(amount, from_currency, to_currency):
    exchange_rates = {
        "USD": {"EUR": 0.85, "GBP": 0.75, "JPY": 110.25},
        "EUR": {"USD": 1.18, "GBP": 0.88, "JPY": 129.37},
        "GBP": {"USD": 1.33, "EUR": 1.14, "JPY": 146.89},
        "JPY": {"USD": 0.0091, "EUR": 0.0077, "GBP": 0.0068}
    }

    if from_currency == to_currency:
        return amount
    
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        converted_amount = amount * exchange_rates[from_currency][to_currency]
        return converted_amount
    else:
        return None
    
amount = float(input("Enter amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()

converted_amount = currency_converter(amount, from_currency, to_currency)

if converted_amount is not None:
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
else:
    print("Unsupported currency pair or invalid input.")
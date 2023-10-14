# main.py

class CurrencyExchange:
    def __init__(self):
        self.rates = {
            'USD': {
                'EUR': 0.85,
                'GBP': 0.75,
                'JPY': 110.0
            },
            'EUR': {
                'USD': 1.18,
                'GBP': 0.88,
                'JPY': 129.0
            },
            'GBP': {
                'USD': 1.33,
                'EUR': 1.14,
                'JPY': 147.0
            }
            # ... add more rates as needed
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        
        try:
            rate = self.rates[from_currency][to_currency]
        except KeyError:
            raise ValueError(f"Exchange rate for {from_currency} to {to_currency} not available.")
        
        return amount * rate

    def display_rates(self):
        for from_currency, to_rates in self.rates.items():
            for to_currency, rate in to_rates.items():
                print(f"1 {from_currency} = {rate} {to_currency}")


def main():
    exchange = CurrencyExchange()
    exchange.display_rates()
    
    amount = float(input("\nEnter the amount you want to convert: "))
    from_currency = input("Enter the currency you have (e.g., USD, EUR, GBP): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR, GBP): ").upper()
    
    converted_amount = exchange.convert(amount, from_currency, to_currency)
    
    print(f"\n{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")


if __name__ == '__main__':
    main()

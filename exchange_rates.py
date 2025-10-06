# FINE3300 - Assignment 1 (Part 2)
# ExchangeRates class + user prompts
# Reads USD/CAD from the last row of the CSV and converts CAD<->USD.

import csv

class ExchangeRates:
    def __init__(self, filename):
        self.filename = filename
        self.rate_usd_cad = self._read_latest_usd_cad()

    def _read_latest_usd_cad(self):
        with open (self.filename, "r", newline="") as file:
            rows = list(csv.DictReader(file))
        latest = rows[-1] # last row = latest date
        return float(latest["USD/CAD"])
    
    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if {from_currency, to_currency} != {"USD", "CAD"}:
            raise ValueError("Currencies must be CAD or USD")
        if from_currency == "USD" and to_currency == "CAD":
            return round(amount * self.rate_usd_cad, 2)
        else:  # CAD -> USD
            return round(amount / self.rate_usd_cad, 2)

        
if __name__ == "__main__":
    filename = "BankOfCanadaExchangeRates.csv"
    exchanger = ExchangeRates(filename)
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (CAD/USD): ")
    to_currency = input("To currency (CAD/USD): ")
    result = exchanger.convert(amount, from_currency, to_currency)
    print(f"\nConverted amount: {result} {to_currency.upper()}")

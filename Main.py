# app.py
# One simple menu to run either Part 1 (Mortgage) or Part 2 (Exchange Rates)

from mortgage import MortgagePayment
from exchange_rates import ExchangeRates

CSV_DEFAULT = "BankOfCanadaExchangeRates.csv"

def run_mortgage():
    print("\n=== Part 1: Mortgage Payments ===")
    principal = float(input("Enter the mortgage principal ($): "))
    rate = float(input("Enter the quoted annual rate (%): "))
    years = int(input("Enter the amortization period (years): "))

    m = MortgagePayment(rate, years)
    monthly, semi_m, bi_w, weekly, rapid_bi, rapid_w = m.payments(principal)

    print("\nMortgage Payment Options:")
    print(f"Monthly Payment: ${monthly}")
    print(f"Semi-monthly Payment: ${semi_m}")
    print(f"Bi-weekly Payment: ${bi_w}")
    print(f"Weekly Payment: ${weekly}")
    print(f"Rapid Bi-weekly Payment: ${rapid_bi}")
    print(f"Rapid Weekly Payment: ${rapid_w}")
    print()

def run_exchange():
    print("\n=== Part 2: Exchange Rate Conversion (CAD ↔ USD) ===")
    fname = input(f"CSV filename [{CSV_DEFAULT}]: ").strip() or CSV_DEFAULT

    xr = ExchangeRates(fname)
    amount = float(input("Enter amount: "))
    from_c = input("From currency (CAD/USD): ")
    to_c = input("To currency (CAD/USD): ")

    try:
        result = xr.convert(amount, from_c, to_c)
        print(f"\nConverted amount: {result} {to_c.strip().upper()}\n")
    except Exception as e:
        print(f"\nError: {e}\n")

def main():
    while True:
        print("Choose an option:")
        print("  1) Mortgage payments (Part 1)")
        print("  2) Currency conversion (Part 2)")
        print("  q) Quit")
        choice = input("> ").strip().lower()

        if choice == "1":
            run_mortgage()
        elif choice == "2":
            run_exchange()
        elif choice == "q":
            print("Bye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or q.\n")

if __name__ == "__main__":
    main()

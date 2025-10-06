#FINE3300 - Assignment 1 (Part 1)
#MortgagePayment class + user prompts
#The program asks for principal, quoted annual rate (5), and amortization years
#and prints all required payment options.

class MortgagePayment:
    def __init__ (self, quoted_rate_percent, years):
        # Store nominal quoted annual rate (semi-annual compounding, per Canadian convention)
        self.nominal_rate = quoted_rate_percent / 100
        self.years = years

    def _periodic_rate(self, payments_per_year):
        # Convert semi-annual compounding to an effective annual rate
        semi = self.nominal_rate / 2
        effective_annual = (1 + semi) ** 2 - 1
        # Then convert to the periodic rate for the chosen payment frequency
        return (1 + effective_annual) ** (1 / payments_per_year) - 1
    
    def _payment(self, principal, payments_per_year):
        r = self._periodic_rate(payments_per_year)
        n = self.years * payments_per_year
        # Present value of an annuity factor
        pvaf = (1 - (1 + r) ** (-n)) / r
        return principal / pvaf
    
    def payments(self, principal):
        monthly = self._payment(principal, 12)
        semi_monthly = self._payment(principal, 24)
        bi_weekly = self._payment(principal, 26)
        weekly = self._payment(principal, 52)

        # Accelerated / Rapid payments
        rapid_biweekly = monthly / 2
        rapid_weekly = monthly / 4

        return tuple(round(x, 2) for x in
                     (monthly, semi_monthly, bi_weekly, weekly, rapid_biweekly, rapid_weekly))
    
if __name__ == "__main__":
    principal = float(input("Enter the mortgage principal ($): "))
    rate = float(input("Enter the quoted annual rate (%): "))
    years = int(input("Enter the amortization period (years): "))

    mortgage = MortgagePayment(rate, years)
    monthly, semi_monthly, bi_weekly, weekly, rapid_biweekly, rapid_weekly = mortgage.payments(principal)

def run_mortgage():
    print("\nMortgage payment options:")
    print(f"Monthly Payment: ${monthly}")
    print(f"Semi-monthly Payment: ${semi_monthly}")
    print(f"Bi-weekly Payment: ${bi_weekly}")
    print(f"Weekly Payment: ${weekly}")
    print(f"Rapid Bi-weekly Payment: ${rapid_biweekly}")
    print(f"Rapid Weekly Payment: ${rapid_weekly}")


# Honest Harry's Used Cars
# Author: Matt Reid
# Date: July 11th, 2025

import datetime
from datetime import timedelta
# Set the user inputs 

CustFirstName = "Matt"
CustLastName = "Reid"
PhoneNum = "5555551234"  # Phone number as a string without formatting.
# Format the phone number to (555) 555-1234.
PhoneNumFormat = (f"({PhoneNum[:3]}) {PhoneNum[3:6]}-{PhoneNum[6:9]}")
PlateNum = "GOV678"
CarMake = "Toyota"
CarModel = "Camry"
CarYear = 2020
SellPrice = 25000.00 # Make float for monetary values.
TradeAmt = 5000.00 # Make float for monetary values.
SalespersonName = "John Doe"


# Set the constants for the invoice.
LicFeeLowRate = 75.00
LicFeeHighRate = 165.00
TransFeeRate = 0.01
LuxTaxRate = 0.016

# Calculate the fees and taxes.
LicFee = 0
if SellPrice <= 15000.00:
    LicFee = LicFeeLowRate
elif SellPrice > 15000.00:
    LicFee = LicFeeHighRate

TransFee = SellPrice * TransFeeRate
if SellPrice > 20000.00:
    LuxTax = (SellPrice * LuxTaxRate) + TransFee
else:
    LuxTax = 0

HST = .15



# Set the invoice details.
invoiceDate = datetime.date.today()
Years = 0



# Generate the invoice number based on initials customer name, last 3 numbers of the plate number, and the last 4 numbers of the phone number.

receiptID = (CustFirstName[0].upper() + CustLastName[0].upper() + "-" + PlateNum [3:6] + "-" + PhoneNum [6:10])

# Set the payment schedule.
finance_options = [
    (1, 12, 999.99, 99999.99, 9999.99),
    (2, 24, 999.99, 99999.99, 9999.99),
    (3, 36, 999.99, 99999.99, 9999.99),
    (4, 48, 999.99, 99999.99, 9999.99),
]
MonPay = (Years * 12) # Total number of months for the payment schedule.

FinanceFee = 39.99 * Years

TotalPrice = SellPrice + FinanceFee + MonPay
Subtotal = SellPrice - TradeAmt + LicFee + TransFee + LuxTax

# Calculate the first payment date.

def CalculateFirstPaymentDate(today = None):
    # Use today's date if no date is provided.
    today = datetime.date.today()
    if today is None:
        today = datetime.today()

    # Determine if the program should skip to the month after next.

    if today.day >= 25:
        NextMonth = (today.replace(day=1) + timedelta(days=32)).replace(day=1)
    # Make sure to add enough days to ensure that we move to the next month.
        NextMonth = today.replace(day=1) + timedelta(days=31).replace(day=1)
    else:
        NextMonth = today.replace(day=1) + timedelta(days=32)
        NextMonth = NextMonth.replace(day=1)    
    # Return the first payment date.
    return NextMonth

print()
print("Honest Harry Used Cars            Invoice Date:  {invoiceDate}")
print("Used Car Sale and Receipt.        Receipt No: {receiptID}")
print()
print(f"                            Sale price:              ${SellPrice:,.2f}")
print(f"Sold to:                    Trade Allowance:         ${TradeAmt:,.2f}")
print(f"                            --------------------------")
print(f"     {CustFirstName} {CustLastName}          Price after Trade:        ${SellPrice - TradeAmt:,.2f}")
print(f"       {PhoneNumFormat}                    License Fee:            ${LicFee:,.2f}")
print(f".                                          Transfer Fee:           ${TransFee:,.2f}"
      )
print(f"                                         ---------------------------")
print(f"Car Details:                    Subtotal:               ${Subtotal:,.2f}")
print(f".               ${HST:,.2f}")
print(f"Make: {CarMake}  Model: {CarModel}  Year: {CarYear}  Plate: {PlateNum}  ---------------------------")
print(f"                              Total sales Price:            ${TotalPrice:,.2f}")
print(f"----------------------------------------------------------------------------")
print(f"     # Years     # Payments.    Financing Fee     Total Price    Monthly Payment")
print(f"----------------------------------------------------------------------------")
print(f"        {Years:>2}            {MonPay:>2}         ${FinanceFee:>10,.2f}     ${TotalPrice:>10,.2f}        ${TotalPrice / MonPay:>10,.2f}")
print(f"----------------------------------------------------------------------------")
print(f"First Payment Date: {CalculateFirstPaymentDate()}") 
print(f"-----------------------------------------------------------------------------")
print(f".                   Best used cars at the best prices!")




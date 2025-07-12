# Honest Harry's Used Cars
# Author: Matt Reid
# Date: July 11th, 2025

import datetime
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

print(LicFee)
print(TransFee)
print(LuxTax)

# Set the invoice details.
invoiceDate = datetime.date.today()



# Generate the invoice number based on initials customer name, last 3 numbers of the plate number, and the last 4 numbers of the phone number.

receiptID = (CustFirstName[0].upper() + CustLastName[0].upper() + "-" + PlateNum [3:6] + "-" + PhoneNum [6:10])

print(receiptID)


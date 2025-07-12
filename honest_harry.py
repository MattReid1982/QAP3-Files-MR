# Honest Harry's Used Cars
# Author: Matt Reid
# Date: July 11th, 2025

import datetime
# Set the user inputs 

CustFirstName = "Matt"
CustLastName = "Reid"
PhoneNum = "555-1234"
PlateNum = "ABC123"
CarMake = "Toyota"
CarModel = "Camry"
CarYear = 2020
SellPrice = 20000.00
TradeAmt = 5000.00
SalespersonName = "John Doe"


# Set the invoice details.
invoiceDate = datetime.date.today()

# Generate the invoice number based on customer name, plate number and phone number.
receiptID = (CustFirstName[0].upper() + CustLastName[0].upper() + PlateNum [3:6] + PhoneNum [6:9])

print(receiptID)


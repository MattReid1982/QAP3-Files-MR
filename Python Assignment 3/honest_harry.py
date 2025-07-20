# Title: Honest Harry's Used Cars
# Author: Matt Reid
# Date: July 11th, 2025


from datetime import timedelta, datetime

while True:
    def Greeting(name):
        name = input("Enter your name: ")
        if not name:
            valueError("Name cannot be empty.")
        if not name.isalpha():
            raise ValueError("Name must contain only alphabetic characters.")
        if len(name) > 20:
            raise ValueError("Name must be 20 characters or less.")
        return (f"Hello, {name}! Welcome to Honest Harry's Used Cars.")
    # Call the greeting function.
    print(Greeting("Matt")) 




    # Set the user inputs. 
    CustFirstName = input("Enter the customer's first name: ").upper()
    CustLastName = input("Enter the customer's last name: ").upper()
    PhoneNum = input("Enter the customer's phone number: ")  # Phone number as a string without formatting.
    # Format the phone number to (555) 555-1234.
    PhoneNumFormat = (f"({PhoneNum[:3]}) {PhoneNum[3:6]}-{PhoneNum[6:10]}")
    PlateNum = input("Enter the vehicle's license plate number: ").upper()
    CarMake = input("Enter the vehicle's make: ")
    CarModel = input("Enter the vehicle's model: ")
    CarYear = int(input("Enter the vehicle's year: "))
    SellPrice = float(input("Enter the selling price of the vehicle: ")) # Make float for monetary values.
    TradeAmt = float(input("Enter the Trade-in amount: ")) # Make float for monetary values.
    SalespersonName = input("Enter the salesperson's name: ").upper()


    # Set the constants for the invoice.
    LIC_FEE_LOW_RATE = 75.00 # If the selling price is less than or equal to $15,000.
    LIC_FEE_HIGH_RATE = 165.00 # If the selling price is greater than $15,000.    
    TRANS_FEE_RATE = 0.01 # Transfer fee rate is 1% of the selling price.
    LUX_TAX_RATE = 0.016  # Luxury tax rate is 1.6% of the selling price if the selling price is greater than $20,000.

    # Calculate the fees and taxes.
    LicFee = 0
    if SellPrice <= 15000.00:
        LicFee = LIC_FEE_LOW_RATE
    elif SellPrice > 15000.00:
        LicFee = LIC_FEE_HIGH_RATE

    TransFee = SellPrice * TRANS_FEE_RATE
    if SellPrice > 20000.00:
        LuxTax = (SellPrice * LUX_TAX_RATE) + TransFee
    else:
        LuxTax = 0
    # Calculate the subtotal and HST.

    Subtotal = SellPrice - TradeAmt + LicFee + TransFee + LuxTax
    HST = .15  # HST rate is 15%.
    HSTAmount = Subtotal * HST 
    TotalPrice = Subtotal + HSTAmount    



    # Set the invoice details.
    today = datetime.today()  # Get today's date.
    invoiceDate = today.strftime("%b %d, %Y")  # Format the date as Month Day, Year.


    # Generate the invoice number based on initials customer name, last 3 numbers of the plate number, and the last 4 numbers of the phone number.

    receiptID = (f"{CustFirstName[0].upper()}{CustLastName[0].upper()}-{PlateNum [3:6]}-{PhoneNum [6:10]}")






    # Calculate the first payment date.

    def CalculateFirstPaymentDate(today=None):
            if today is None:
                today = datetime.now().date()

                # Determine if the program should skip to the month after next.
                # Move to the first of next month if today is the 25th or later.
                NextMonth = (today.replace(day=28) + timedelta(days=4)).replace(day=1)  # This will always give us the first of the next month.

                if today.day >= 25:
                    NextMonth = (NextMonth.replace(day=28) + timedelta(days=4)).replace(day=1)

                # Make sure to add enough days to ensure that we move to the next month.
                    NextMonth = today.replace(day=1) + timedelta(days=31).replace(day=1)
                else:
                    NextMonth = today.replace(day=1) + timedelta(days=32)
                    NextMonth = NextMonth.replace(day=1)    
                # Return the first payment date.
                return NextMonth.strftime("%d-%b-%y")

    def PaymentSchedule(SellPrice, TradeAmt, years):
        MonPay = (years * 12)  # Total number of months for the payment schedule.
        FinanceFee = 39.99 * years
        TotalPrice = SellPrice + FinanceFee + MonPay
        return MonPay, FinanceFee, TotalPrice

    print()
    print(f"Honest Harry Used Cars                                     Invoice Date:   {invoiceDate}")
        
    print(f"Used Car Sale and Receipt                                  Receipt No:      {receiptID}")
    print()
    print(f"                                                         Sale price:         ${SellPrice:,.2f}")
    print(f"Sold to:                                                 Trade Allowance:    ${TradeAmt:,.2f}")
    print(f"                                                         ------------------------------")
    print(f"     {CustFirstName[0]}. {CustLastName}                                             Price after Trade:  ${SellPrice - TradeAmt:,.2f}")
    print(f"      {PhoneNumFormat}                                     License Fee:           ${LicFee:,.2f}")
    print(f"                                                         Transfer Fee:          ${TransFee:,.2f}"
        )
    print(f"                                                         ------------------------------")
    print(f"Car Details:                                             Subtotal:           ${Subtotal:,.2f}")
    print(f"                                                         HST:                 ${HSTAmount:,.2f}")
    print(f"Make: {CarMake}  Model: {CarModel}  Year: {CarYear}  Plate: {PlateNum}    ------------------------------")
    print(f"                                                         Total sales Price:  ${TotalPrice:,.2f}")
    print()
    print(f"---------------------------------------------------------------------------------------")
    print()
    print(f"     # Years     # Payments    Financing Fee     Total Price    Monthly Payment")
    print(f"     --------------------------------------------------------------------------")
    # Set the payment schedule.

    for years in range (1, 5, 1):

        MonPay = (years * 12) # Total number of months for the payment schedule.

        FinanceFee = 39.99 * years
        TotalPrice = SellPrice + FinanceFee + MonPay
        print(f"        {years:>2}            {MonPay:>2}         ${FinanceFee:>10,.2f}     ${TotalPrice:>10,.2f}        ${TotalPrice / MonPay:>10,.2f}")
    print(f"     --------------------------------------------------------------------------")
    print(f"     First Payment Date: {CalculateFirstPaymentDate()}")
    print(f"---------------------------------------------------------------------------------------")
    print()
    print(f"                           Best used cars at the best prices!")

    wait = (f"press enter to continue")


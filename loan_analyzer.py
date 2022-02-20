## Part 2: Automate the Calculations.

# Loan data used
loan_costs = [500, 600, 200, 1000, 450]

# Total number of loans in the list
number_of_loans = len(loan_costs)
print (f"The number of loans is: {number_of_loans}")

# Total of all the loans in the list
total_of_loans = sum(loan_costs)
print (f"The total of the loans is: {total_of_loans}")

# Average loan price
average_loan_price = sum(loan_costs)/len(loan_costs)
print (f"The average loan price is: {average_loan_price}")



## Part 3: Analyze Loan Data.

# Loan data used
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Future value of the loan 
future_value = loan.get("future_value")
print (f"The future value of the loan is: {future_value}")

# Remaining months on the loan
remaining_months = loan.get("remaining_months")
print (f"The remaining months of the loan is: {remaining_months}")

# Present_value of the loan
discount_rate = 0.20
present_value = future_value / (1+discount_rate/12)**remaining_months
print (f"The present value or fair value of the loan is: {present_value}")

# Conditional Statement to decide whether present value represents loan's fair value
loan_price = loan.get("loan_price")
if present_value >= loan_price:
    print ("Buy. Loan is worth at least the cost to buy it")
else:
    print ("Don't Buy. Loan is too expensive and not worth the price")
    
 ##################   Analyze the loan value with a minimum return of 20% in order to determine purchasability of the loan. (5 points)

## Part 4: Perform Financial Calculations

# New_Loan data used
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# New function for calculating present_value
def calculate_present_value (future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1+annual_discount_rate/12)**remaining_months
    return present_value

# Calculate present value of the new_loan
annual_discount_rate = 0.2
new_loan_present_value = calculate_present_value (new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)

print(f"The present value of the loan is: {new_loan_present_value}")



## Part 5: Conditionally filter lists of loans

# Loan data used
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Creating Filter if loan_price <= 500 and add it to the inexpensive_loans list
inexpensive_loans=[]
for row in loans:
    loan_price = row.get("loan_price")
    if loan_price <= 500:
        inexpensive_loans.append(loan_price)
print(f"The list of loans that are less than 500 are: {inexpensive_loans}")

# Create CSV file for inexpensive_loans
# Import csv and pathlib package
import csv
from pathlib import Path     

# #################################################
csvpath = path("inexpensive_loans_list.csv")
with open(csvpath, 'w', newline='') as inexpensive_loans_list:
    csvwriter = csv.writer(inexpensive_loans_list.csv)
    for loans in inexpensive_loans
        cvswriter.writerow(loans.values())

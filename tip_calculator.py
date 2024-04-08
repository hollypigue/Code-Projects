#tip calculator
import math

#tip function
def tip_calculation(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    return tip_amount, total_amount

#main funtion
def main():
    bill_amount = float(input("Enter the total amount of your bill: $"))
    tip_percentage = float(input("Enter the tip percentage of your choice (10, 15, 20): "))

    tip_amount, total_amount = tip_calculation(bill_amount, tip_percentage)

    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total bill amount: ${total_amount:.2f}")
main()
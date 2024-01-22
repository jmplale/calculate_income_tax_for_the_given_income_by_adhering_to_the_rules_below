# make a def function
def tax(income):
    tax_to_pay = 0

    # make an if statement
    if income < 10000:
        tax_to_pay = 0
        print("There's no income tax you need to pay.")
    # make in elif statement
    elif income > 10000 and income <= 20000:
        tax_to_pay = (income - 10000) * 0.1
        print(f"The income tax that you need to pay is ${tax_to_pay}")
 
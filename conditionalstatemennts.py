# # if... else.. statement
votes = 2501
if votes > 2500:
    print("You've won the election.")
    print("You are the governor elect!")
else:
    print("You've lost the election!")


marks = 74

if marks >80:
    print("you've have an A!")
elif marks >70:
    print("you've have a B!")
elif marks >60:
    print("you've have a C!")
elif marks >50:
    print("you've have a D!")
elif marks >40:
    print("you've have an E!")
else:
    print("you've have failed!")


# Use if else to create an atm machine that pops up a toast when a
# condition is fulfilled. if one withdraws above 20,000 output should be,
# "you have witdrawn above the recommendation." above 10,000
# "you have witdrawn above the recommendation," and below 10,000
# "you have withdrawn less." use users input.

# ATM MACHINE SIMULATION
def atm_witdrawal():
    amount = float(input("Enter the amount you want to withdraw: "))
    if amount > 20000:
        print("you've have withdrawn above recommended value")
    elif amount > 10000:
        print("you've have withdrawn above recommended value")
    else:
        print("you have withdrawn less.")

# for ...Loop
# while ....loop
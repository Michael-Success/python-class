from itertools import filterfalse
from multiprocessing.connection import answer_challenge

print("Michael Success")
print("Welcome to class")
print(345)

# variables
# "NAME" here is our variable, while Michael Success is the "VALUE".
name= "Michael Success"
print(name)
age= 18
print(age)
# "AGE" here is our variable, while 18 is the "VALUE".
marks= 78.4
print(marks)
a = 5
b = "school"
print(a)
print(b)

# data types
# integer - any value that is odd number is an integer.
d = 8788
print(d)
# string - the value for string is a text of alphabet.
g = "please come here"
print(g)
print("please knock first")
# boolean - this is to indentify whether something is "true" or "false"
is_boy = True
print(is_boy)
is_girl = False
print(is_girl)
# float - is any value with a decimal number
l = 23.54
print(l)

# input from user
last_name = input("WHat is your  last name?")
print(last_name)
age = input("How old are you?")
print(age)
height = input("How tall are you?")
print("you are" + height + "inches tall")
weight = input("How much do you weigh?")
print("you are" + weight)
family_name = input("What is your family name?")
print("Good morning" + family_name)


# assignment
first_name = "Peter"
last_name = "Njuguna"
professor = "professor"

# using f-string to format the message
message = f"hello {first_name} {last_name} you are a {professor}"
print(message)

# Type Conversion
first_number = int(input("enter first number; "))
print (int(first_number))
second_number = int(input("enter second number; "))
print(int(second_number))
sum = first_number + second_number
print("Total: " + str(sum))
subtract = int(first_number) - int(second_number)
print("Subtraction: " + str(subtract))

y= float(input("enter first mark: "))
x=float(input("enter second mark: "))
minus = y-x
print("minus: " + str(minus))

# take in a person height and weight and
# calculate the BMI of the individual,
# # then display the BMI to the person
# answer_challenge
height = float(input("enter your height in meters: "))
weight = float(input("enter your weight in kilograms: "))

bmi = weight/(height ** 2)
print(f"Your BMI is:  + {bmi: .2f}")

if bmi <= 16:
    print("You are very underweight")
elif bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You are healthy")
elif bmi <= 30:
    print("You are overweight")
else:
    print("You are very overweight")

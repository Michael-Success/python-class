def my_function():
    print("Hello, welcome to my function")
    print("Hello, welcome to my function")
    print("Hello, welcome to my function")
my_function()

def my_string():
    hello = "Good Morning, welcome back"
    print(hello)
my_string()

def my_variable(name):
    print(name)
my_variable('Bob')
my_variable('John')
my_variable('Israel')

def my_conc(firstname):
    print('Hello ' + firstname + ' Please enter!')
my_conc('Esther')
my_conc('Vivian')


def two(name,age):
    print('Hello ' + name + ' you are ' + str(age) + ' years old')
two('Pauline', 45)
two('Jane', 34)
two('Evan', 28)


def welcome(firstname, lastname, age):
    print('Hello ' + firstname + ' ' + lastname + ' you are ' + str(age) + ' years old')
welcome('Allan', 'Doe', 24)
welcome('George', 'Kitti', 27)
welcome('Njuguna', 'David', 36)

def add_five(age):
    new_age = age + 5
    return new_age
print(add_five(36))


def promoted(name,age):
    if age > 5 and age <7:
        return f"{name} You are promoted to grade 1"
    elif age == 7:
        return f"{name} You are promoted to grade 2"
    elif age > 8:
        return f"{name} You are promoted to grade 3"
    else:
        return f"{name} You are promoted to grade 4"
print(promoted(' John', 9))

def greet(name):
    if name == 'Alice':
        return "Hello Alice! It's great to see you!"
    elif name == 'Bob':
        return "Hello Bob! How is it going?"
    else:
        return f"Hello {name}, nice to meet you!"
print(greet('Alice'))
print(greet('Bob'))
print(greet('Charlie'))



# Class work
# Create a function that takes two numbers and performs the summation then display the summation.



# This is staticmethod
# from index import first_name


class Student:
    first_name = 'John'
    last_name = 'Kamau'
    gender = 'male'
    age = 23

class Person:
    def __init__(self, name, gender, marital_status, residence):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.residence = residence

    def salutation(self):
        print(f'Hello {self.name} you are {self.marital_status}')


# Class exercise 1
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f'{self.name} says hello!'

class Dog(Animal):
    def __init__(self, name, breed, species='Dog'):
        super().__init__(name, species)
        self.breed = breed

    def speak(self):
        return f'{self.name}, the {self.breed}, barks!'


# Inheritance
class Employee():
    def __init__(self, name, age, salary, gender,):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender


def init(name, age, salary, gender, education_level):
    pass


class Manager(Employee):
    def __init__(self, name, age, salary, gender, education_level):
        super(). __init__(name, age, salary, gender)
        self.education_level = education_level


class Developer(Employee):
    def __init__(self, name, age, salary, gender, prog_lang):
        super(). __init__(name, age, salary,gender)
        self.prog_lang = prog_lang


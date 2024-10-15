from classes import Student
from classes import Person
from classes import Animal
from classes import Dog
from classes import Employee
from classes import Manager
from classes import Developer



student1 = Student ()
print(student1.first_name)
print(student1.last_name)
print(student1.gender)
print(student1.age)


person1 = Person('Alex', 'male', 'married', 'Nairobi')
print(person1.name)

print(person1.gender)
print(person1.marital_status)
print(person1.residence)
person1.salutation()


person2 = Person('Alice', 'female', 'single', 'Kisumu')
print(person2.name)
print(person2.gender)
print(person2.marital_status)
print(person2.residence)
print(person2.salutation())

person3 = Person('Christopher', 'male', 'Divorced', 'Mombasa')
print(person3.name)
print(person3.gender)
print(person3.marital_status)
print(person3.residence)
person3.salutation()


# class exercise 1
animal1 = Animal('leo', 'Lion')
print(animal1.speak())

animal2 = Animal('Ella', 'Elephant')
print(animal2.speak())

dog = Dog('Rex', 'German Shepherd')
print(dog.speak())


# inheritance
employee1 = Employee('judy', '34', 100000, 'female')
print(employee1.name)
print(employee1.age)
print(employee1.salary)
print(employee1.gender)

print(f'Name: {employee1.name}, '
      f'Age: {employee1.age}, '
      f'Salary: {employee1.salary}, '
      f'Gender: {employee1.gender}' )

# child of Employee
manager1 = Manager('Paul', '36', 250000,
                   'Male', 'Degree')
print(f'Name: {manager1.name}, Age: {manager1.age}, Gender: {manager1.gender}, {manager1.salary}, {manager1.education_level}')

developer1 = Developer('Thomas', '34',
                       560000, 'male', 'Kotlin')

developer2 = Developer('Ann', '27',
                       500000, 'female', 'Python')

developer3 = Developer('Esther', '26',
                       320000, 'female', 'Javascript')



# print(f'Name: {developer1.name}, Age: {developer1.gender}, {developer1.salary},')
# print(f'Name: {developer2.name}, Age: {developer2.gender}, {developer2.salary},')
# print(f'Name: {developer3.name}, Age: {developer3.gender}, {developer3.salary},')

print(f'Name: {developer3.name}, {developer1.name}, {developer2.name},'
      f' {developer3.salary}, {developer1.salary}, {developer2.salary},'
      f' {developer3.gender}, {developer1.gender}, {developer2.gender}')
# Data structure
# Four data structures are:
from pkg_resources import WorkingSet

# 1. Lists

employees = ['Peter', 'John', 'Smith', 'Esther', 'Ann']
print (employees)
# How to identify an item in a list.
print (employees[2])
print (employees[0])
print (employees[1:5])
print (employees[0:2])

# To change an item in a list.
employees[0] = 'Alex'
print (employees)

employees[3] = 'Success'
print (employees)

# Adding a value to our existing items
employees.append('George')
print(employees)
employees.insert(0,'Susan')
print(employees)

marks = [234, 543, 564, 543, 987]
print(max(marks))
print(min(marks))
print(sum(marks))


# 2. tuples
languages = ('Java', 'Python', 'Javascript')
print(languages)
print(languages[1])
print(languages[1:4])


# 3. sets
mysets = {'Python', 'Java', 'Javascript', 'Php'}
print(mysets)
word = 'Java'
if word in mysets:
    print(word)

if 'Python' in mysets:
    print('Python')
if 'Kotlin' in mysets:
    print('Kotlin')
else:
    print('Not here')

mysets.add('Charlse')

mysets.update(['Php'])
print(mysets)


# 4. dictionary
mydictionary = {
    'Title': 'The Code',
    'Author': 'John Doe',
    'Publisher': 'KBL',
    'Year Published': 2000
}
print(mydictionary)
print(mydictionary['Publisher'])
mydictionary['version'] = 'Three'
print(mydictionary)

if 'school' in mydictionary:
    print("Yes it is present here")
else: print("No it is not present here")


# Class Work
# create a student dictionary with ALL THE NECESSARY items and check existence of the gender of a student.
student = {
    'name': 'John Smith',
    'age': '24',
    'gender': 'male',
    'student_id': 'K123456',
    'major': 'Full-stack',
    'Gpa': 3.9,
    'courses': ['Algorithms', 'Data Structures', 'Machine Learning']
}


# check if gender exists in student dictionary.
if 'gender' in student:
        print("gender exists here")
else:
    print("Gender does not exist")
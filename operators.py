# Arithmetic operators
a = 5
b = 4
print (a+b)
print (a-b)
print (a*b)
print (a%b)
print (a/b)

x = 3
x+=3
print (x)


# comparison operators
age1 = 23
age2 = 45
age3 = (age1>age2)
print (age3)

age4 = 56
age5 = 23
age6 = age4<age5
print (age6)

marks1 = 200
marks2 = 200
marks3 = marks1>=marks2
print (marks3)

marks4 = 242
marks5 = 147
marks6 = marks4<=marks5
print (marks6)

marks7 = 15
marks8 = 8
print (marks7==marks8)
# if they are equal to

marks9 = 65
marks10 = 91
print(marks9!=marks10)
# not equal to

# declare 4 variables and calculate the summation of each pair then do a comparison

a = 10
b = 20
c = 30
d = 40

# calculating the summation of each pair
sum_ab = a+b
sum_cd = c+d

# comparing the sum
if sum_ab > sum_cd:
    print ("Sum of a and b is greater than sum of c and d.")
elif sum_ab < sum_cd:
    print ("Sum of a and b is less than sum of c and d.")
else:
    print("Sum of a and b is equal to sum of c and d.")


# logical operators
student1 = 23
student2 = 67
student3 = 45
student4 = 35

print (student1>student2 and student3>student4)
print (student1<student2 and student3<student4)
print (student1>student2 and student3<student4)
print (student1<student2 and student3>student4)

print (student1>student2 or student3>student4)
print (student1<student2 or student3<student4)
print (student1>student2 or student3<student4)
print (student1<student2 or student3>student4)

print (not(student1>student2 or student3>student4))


# take 4 students age as input and perform logical operations within the keyed in values.
age1 = int(input("Enter your age of student 1: "))
age2 = int(input("Enter your age of student 2: "))
age3 = int(input("Enter your age of student 3: "))
age4 = int(input("Enter your age of student 4: "))

# performing logical operations
all_above_18 = age1 > 18 and age2 > 18 and age3 > 18 and age4 > 18
any_below_18 = age1 < 18 or age2 < 18 or age3 < 18 or age4 < 18
all_same_age = age1 == age2 == age3 == age4

# printing results
print(f"All students are above 18: {all_above_18}")
print(f"At least one student is above 18: {any_below_18}")
print(f"ALl students are of the same age: {all_same_age}")
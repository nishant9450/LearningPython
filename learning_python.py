print("Nishant is greatest Python developer")

# if else
a = 200
b = 333
if a > b:
    print('a is greter then b')
elif a == b:
    print('print a equal b')
else:
    print("b is greater a")

# while loop
i = 1
while i < 6:
    print(i)
    i += 1

# With break statement we can stop the loop even if the condition is still true
i = 5
while i < 15:
    print(i)
    if i == 10:
        break
    i += 1

# With the continue statement we can stop the current iteration, and continue with the next
# Note that number 103 is missing in the result
m = 100
while m < 105:
    m += 1
    if m == 103:
        continue
    print(m)

# else statement
n = 200
while n < 206:
    print(n)
    n += 1
else:
    print("n is longer less then 6")

""" For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
The for loop does not require an indexing variable to set beforehand.
"""
# Print each fruit in a fruit list:

fruit = ['apple', 'orange', 'banana']
for x in fruit:
    print(x)

# Looping Through a String
for x in 'banana':
    print(x)

# With the break statement we can stop the loop before it has looped through all the items:
fruit = ['apple', 'orange', 'banana']
for x in fruit:
    print(x)
    if x == 'orange':
        break

# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruit = ['apple', 'orange', 'banana']
for x in fruit:
    print(x)
    if x == 'orange':
        continue

"""
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number.
"""

for x in range(6):
    print(x)
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

"""
The range() function defaults to 0 as a starting value, however it is possible to specify the starting value 
by adding a parameter: range(2, 6),  which means values from 2 to 6 (but not including 6):
"""

for y in range(100, 105):
    print(y)

"""
The range() function defaults to increment the sequence by 1, however it is possible to specify the 
increment value by adding a third parameter: range(2, 30, 3):
"""

for z in range(1, 30, 3):
    print(z)

"""
Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
"""

for x in range(0, 6):
    print(x)
else:
    print("Finally finished")

for c in range(6):
    if c == 3: break
    print(c)
else:
    print("Finally finished!")

"""
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":
"""

adj = ['red', 'green', 'blue']
car = ['maruti', 'honda', 'BMW']
for x in adj:
    for y in car:
        print(x, y)

"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
In Python a function is defined using the def keyword:
"""


def my_function():
    print("Nishant has 1 cr package")


my_function()

"""
Arguments - Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want,
 just separate them with a comma.
The following example has a function with one argument (fname). When the function is called, we pass along a first name,
 which is used inside the function to print the full name:
"""


def my_full_name(sirname):
    print("Nishant " + sirname)


my_full_name("Gupta")
my_full_name("Mittal")

"""
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

"""
Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2
 arguments, you have to call the function with 2 arguments, not more, and not less.
"""


def fullname(fname, lname):
    print("my full name is " + fname + " " + lname)


fullname("Nishant", "Gupta")

"""Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name 
in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:"""


def my_kids(*kids):
    print("My  kids are " + " and ".join(kids))


my_kids('Dhven', 'Arnav')

"""
Default Parameter Value
The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:
"""


def my_country(country='India'):
    print(f"my country is {country}")


my_country('USA')
my_country()
my_country('Austrlia')

"""
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated 
as the same data type inside the function.
E.g. if you send a List as an argument, it will still be a List when it reaches the function:
"""


def myStapleDiet(food):
    for x in food:
        print(x)


fruits = ['apple', 'orange', 'Banana']

myStapleDiet(fruits)


def mykeyInterest(skill):
    for x in skill:
        print(x)


fortay = ['PO', 'BA', 'Analytics']

mykeyInterest(fortay)

"""
Return Values
To let a function return a value, use the return statement:
"""


def multiplication(n):
    return 5 * n


print(multiplication(2))
print(multiplication(3))


# creating a function to write factorial of a number
def factorial(n):
    num = 1  # Initialize num to 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


print(factorial(5))

"""
Python Lambda
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Syntax
lambda arguments : expression
"""

# adding 10 to a agrument and returning the result
x = lambda a: a + 10
print(x(5))

# Lambda functions can take any number of arguments:
y = lambda a, b: a * b
print(y(3, 5))
print(y(4, 4))

z = lambda m, n, o: m + n - o
print(z(100, 150, 75))

"""
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
"""


def doubler_function(n):
    return lambda a: a * n


doubler = doubler_function(5)
print(doubler(6))


# create a tripler function
def tripler_function(m):
    return lambda n: n * m


tripler = tripler_function(3)
print(tripler(12))

# array
# Creating multiple values in a single variable
cars = ['volvo', 'muruti', 'BMW']

# checking first acr in the list
print(cars[0])

# Return the number of elements in the cars array:
x = cars[0]
print(len(x))

# You can use the for in loop to loop through all the elements of an array.
for x in cars:
    print(x)

# Adding Array Elements
# You can use the append() method to add an element to an array.
cars.append('honda')
print(cars)

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
cars.pop(2)
print(cars)

# You can also use the remove() method to remove an element from the array.
# Note: The list's remove() method only removes the first occurrence of the specified value.
cars.remove('honda')
print(cars)

"""
Python Classes/Objects
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""


# To create a class, use the keyword class:
# Create a class named MyClass, with a property named x:

class MyClass:
    x = 5


"""
Create Object
Now we can use the class named MyClass to create objects:
Create an object named p1, and print the value of x:
"""

p1 = MyClass
print(p1.x)

"""
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do 
when the object is being created
"""


# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p2 = Person('Nishant', 39)

print(p2.name)
print(p2.age)


# The string representation of an object WITHOUT the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p2 = Person('Nishant', 39)
print(p2)


# The string representation of an object WITH the __str__() function:
class Banda:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


p3 = Banda('Deepa', 21)
print(p3)

"""
Objects can also contain methods. Methods in objects are functions that belong to the object.
Let us create a method in the Person class:
"""


# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("My name is" + " " + self.name)
        print(f"My age is" + " " + str(self.age))  # Convert age to a string


p1 = Person('Nishant', 39)
p1.myfunc()

"""
The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to 
the class.
It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any 
function in the class:
"""


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(ubs):
        print("My name is " + ubs.name + " " + "and my age is " + str(ubs.age))
        print("My age is " + str(ubs.age))


p1 = Person('Deepa', 24)
p1.age = 25  # You can modify properties on objects like this
p1.myfunc()
"""
class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(ubs):
        print("My name is " + ubs.name  )
        print("My age is " + str(ubs.age))

p1 = Person('Deepa',24)
del p1.age #You can delete properties on objects by using the del keyword:
p1.myfunc()
"""

"""
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content,
 put in the pass statement to avoid getting an error.
 
class Person:
  pass 
"""

"""
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""


# Create a class named Manus, with firstname and lastname properties, and a printname method:
class Manus:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def myfunc(self):
        print("My full name is" + " " + self.fname + " " + self.lname)


p4 = Manus('Dhven', 'Gupta')
p4.myfunc()


# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Manus):
    pass  # Use the pass keyword when you do not want to add any other properties or methods to the class.


x = Student('Arnav', 'Gupta')
x.myfunc()


# Add a property called graduationyear to the Student class:

class Student(Manus):
    def __init__(self, fname, lname, year):
        super().__init__(fname,
                         lname)  # super() function that will make the child class inherit all the methods and properties from its parent:
        self.graduationyear = 2011

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)


x = Student('Nishant', 'Gupta', 2011)
x.welcome()

# while loop
# print numbers 1 to 100

n = 1
while n <= 100:
    print(n)
    n += 1
print('Loop is finished')

# print numbers 100 to 1
m = 100
while m >= 1:
    print(m)
    m -= 1
print('Loop is finished')

# Print multiplication of a number
# i = 1
# n= int(input("enter a number : "))
# while i <=10:
#     print(n*i)
#     i = i +1
print('Multiplication is completed')

"""
Print the elements of the following list using a while loop
[1,4,9,16,25,36,49,64,81,100]
"""

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
print('code is finished')

# to print the list of peopl
people = ['nishant', 'dhven', 'deepa', 'raj']

b = 0
while b < len(people):
    print(people[b])
    b = b + 1
print('code is finished')

"""
Search for a number x in this tuple using loop:
(1,4,9,16,25,36,49,64,81,100,36)
"""

t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
i = 0
x = 36
while i < len(t):
    if (t[i] == x):
        print("found the number at index ", i)
    else:
        print("finding...")
    i = i + 1
print('completed the code')

# how the key word breaks works
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print("end of loop")

# With cotniue statement you can skin the record in question
i = 0
while i <= 5:
    if (i == 3):
        i = i + 1
        continue  # skip
    print(i)
    i += 1
print('completed the code')

# For loop

# printing a list with the help of for loop
nums = [1, 2, 3, 4, 5]

for x in nums:
    print(x)
print('completed the code')

# print all string with the help of for loop
veggies = ['potato', 'brinjal', 'ladyfinger', 'cucumber']

for x in veggies:
    print(x)
print('completed the code')

# print all tuple with the help of for loop
m = (1, 2, 3, 4, 5)

for x in m:
    print(x)
print('completed the code')

# for loop with else statement

str = "apnacollege"

for x in str:
    print(x)
else:
    print('*** End of loop ***')

for x in str:
    if (x == 'o'):
        print("o found")
        break
    print(x)
else:
    print("End")

print("** end of Code ***")

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
x = 49

idx = 0

for el in num:
    if (el == x):
        print("number found at idx", idx)
    idx += 1

print("** end of Code ***")

# range function

seq = range(5)

for x in seq:
    print(x)

print("** end of Code ***")

for x in range(0, 10, 2):  # 0 is from , 10 is to end number and 2 is skip number (start,end, skip)
    print(x)

print("** end of Code ***")

# print numbers 100 to 1 using for loop


for z in range(100, 0,
               -1):  # the end number is used as 0 since we want to print 1 and skip as -1 since we want to reduce numbers
    print(z)
print("** end of Code ***")
# Print multiplication of a number using for loop

# m = 11
# n = int(input("Input a number whose multiplication is required: "))
# for x in range(1,m):
#     print (x * n)
# print("** end of Code ***")

"""
pass is null statement that does nothing. it is used as a place holder for future code
"""

# find sum of fist n numbers using a for loop
n = 5
sum = 0
for i in range(n + 1):
    sum += i
print(" Total sum is ", sum)
print("** end of Code ***")

n = 10
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(" Total sum is ", sum)
print("** end of Code ***")

# Factorial of a number using for while loop

n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial of a number is ", fact)
print("** end of Code ***")

# Factorial of number using for loop

n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print("factorial of a number", fact)
print("** end of Code ***")

"""
Learning Functionsvia apna college by Shraddha kapra
"""


def sum_calc(a, b):  # here a,b would be parameters
    sum = a + b
    return sum


print(sum_calc(5,
               10))  # here we are calling our sum_calc function which we created earlier & 5,10 would be called arguments

print("** end of Code ***")

# I can call the same function again to perform another calculation
print(sum_calc(500,
               25))  # while calling the function I have to pass the agruments for the parameters passed while creating function

print("** end of Code ***")


# creation a function for multiplication

def multiplication(a, b):
    return a * b


print(multiplication(161000, 1.4))

print("** end of Code ***")


# function to create average of three numbers

def calc_avg(a, b, c):
    return (a + b + c) / 3


print(calc_avg(50, 5, 100))

print("** end of Code ***")

# creating a function with some default values passed in parameters which are used by default in case no argument is passed

def  sum_default(a=5, b= 10):
    return a+b

print(sum_default()) # since no argument is passed, it picks up default values stored in parameters

print("** end of Code ***")

# create a function to pint the length of a list (list is the parameter)

cities = ['Delhi','Mumbai','Indore','Pune','Chennai']
heroes = ['Shahraukh','Salman','Amir','Akshay']

def print_list(list):
    return len(list)

print(print_list(heroes))
print(print_list(cities))

# Print the elements of a list in a single line

def list_singleline(list):
    for x in list:
        print(x, end=" ")
    print()

list_singleline(heroes)

print("** end of Code ***")

# write a function to print the factorial of a number using while loop
def factorial(n):
    num = 1
    while n >=1:
        num = num * n
        n -=1
    return num

print(factorial(5))

print("** end of Code ***")

# write a function to print the factorial of a number using for loop

def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

cal_fact(4)
cal_fact(6)

print("** end of Code ***")

INR_conversion = 83

# Create a function to convert USD to INR
def convertor(USD):
    INR = USD * INR_conversion
    print(USD, "USD =", INR, "INR")

convertor(5)

print("** end of Code ***")

# Create a function to check if  a number is odd or even

def odd_even_checker(n):
    if n%2 == 0:
        print ("even number")
    else:
        print("odd number")

odd_even_checker(10)

print("** end of Code ***")




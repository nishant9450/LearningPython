print("Nishant is greatest Python developer")

# if else
a = 200
b= 333
if a >b:
    print('a is greter then b')
elif a == b:
    print('print a equal b')
else:
    print("b is greater a")

# while loop
i = 1
while i <6:
    print(i)
    i += 1

# With break statement we can stop the loop even if the condition is still true
i = 5
while i <15:
    print(i)
    if i ==10:
        break
    i +=1

# With the continue statement we can stop the current iteration, and continue with the next
# Note that number 103 is missing in the result
m = 100
while m <105:
    m +=1
    if m ==103:
        continue
    print(m)

# else statement
n = 200
while n <206:
    print(n)
    n +=1
else:
    print("n is longer less then 6")

""" For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
The for loop does not require an indexing variable to set beforehand.
"""
# Print each fruit in a fruit list:

fruit = ['apple','orange','banana']
for x in fruit:
    print(x)

# Looping Through a String
for x in 'banana':
    print(x)

# With the break statement we can stop the loop before it has looped through all the items:
fruit = ['apple','orange','banana']
for x in fruit:
    print(x)
    if x == 'orange':
        break

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruit = ['apple','orange','banana']
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

for y in range (100,105):
    print(y)

"""
The range() function defaults to increment the sequence by 1, however it is possible to specify the 
increment value by adding a third parameter: range(2, 30, 3):
"""

for z in range(1,30,3):
    print(z)

"""
Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
"""

for x in range(0,6):
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

adj = ['red','green','blue']
car = ['maruti','honda','BMW']
for x in adj:
    for y in car:
        print(x,y)

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
    print("Nishant "+sirname)

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

def fullname(fname,lname):
    print("my full name is " +fname+" "+lname)

fullname("Nishant","Gupta")

"""Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name 
in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:"""

def my_kids(*kids):
    print("My  kids are "+" and ".join(kids))

my_kids('Dhven','Arnav')

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

fruits=['apple','orange','Banana']

myStapleDiet(fruits)

def mykeyInterest(skill):
    for x in skill:
        print(x)

fortay=['PO','BA','Analytics']

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
    num = 1 # Initialize num to 1
    while n>=1:
        num = num *n
        n = n-1
    return num

print(factorial(5))





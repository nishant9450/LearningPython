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


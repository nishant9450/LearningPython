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


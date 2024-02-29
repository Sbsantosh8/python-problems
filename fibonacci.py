
       # Santosh Basragan

   #Fibonacci Series

number = int(input("Enter a number : "))
x = 0
y = 1

print("Fibonacci Series => ",end=" ")
for i in range(0,number):
     print(x,end=" ")
     c = x + y
     x = y
     y = c


# Reversing a Number

number = int(input("Enter a Number ? "))

rev = 0
temp = number
while(temp>0):
    remainder = temp % 10
    rev = rev*10+remainder
    temp = temp//10

print(rev)

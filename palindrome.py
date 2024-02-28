

x = int(input("Enter a Number to check Palindrome or Not : "))


temp = x
reverse = 0

while(temp > 0):
    remainder = temp%10
    reverse = reverse*10+remainder
    temp = temp//10

if(reverse == x):
    print("Palindrome Number : ",reverse)    

else:
    print("Not Palindrome ")    






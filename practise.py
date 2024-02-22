


x = input("Enter a number 1 : ")
y = input("Enter a number 2 : ")

def greaterNumber(x,y):
    if(x>y):
        return f"{x} is greater than {y}"

    elif(y>x):
        return f"{y} is greater than {x}"

    else:
        return f"{x} and {y} both are equal"


a = greaterNumber(x,y)
print(type(a))
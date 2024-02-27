#                                # Santosh Basragan
  
#                               # (Reversing a List)

# # Method 1
# # Swapping the Elements Using a for loop

# l = [22,33,44,66,92]
# length = len(l)
# l2 = []

# for i in range(0,length//2):
#     l[i],l[length-1-i] = l[length-1-i],l[i]
# print(l)


# # Method 2
# # Using a Reverse iteration 

# for i in range(length-1,-1,-1):
#   l2.append(l[i])

# print(l2)
# 
# def show():
    # print("hello")
# 
# print(show())    
# 

# def selfprint(val="",myend=""):
#     print(val,end=myend)

# selfprint(myend="santosh")
# # selfprint("sahadev")
# 
# def show(*n):
    # print(n)
  #  
# 
# show(10,20)

# def calculate(n1,n2):
#     return n1+n2
    

# def sum(a,b,c=10):
#     print(a + b + c)


# sum(55,5,c=20)    


# def show(**k):
#     print(k)

# show(a=10,b=20)    

# def calculate(n1,n2):
#     yield n1+n2
    # yield n1-n2
    # yield n1*n2
    # yield n1/n2
    # yield n1//n2
    # yield n1%n2
    # yield n1**n2

# print(list(calculate(3,2))) 
# print(type(list(calculate(3,2))))
    

# numbers = [11,20,31,40,51,60]

# def even(x):
#     return x % 2 == 0

# evens = list(filter(even,numbers))

# print("Even number",evens)




# Take a list and sort it without using sort function

givenList = [22,98,36,45]

for i in range(0,len(givenList)):
    for j in range(i,len(givenList)):
        if(givenList[i]>givenList[j]):
            givenList[i],givenList[j] = givenList[j],givenList[i]

print(givenList)

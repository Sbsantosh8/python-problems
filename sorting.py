

     # Santosh Basragan


# Take a list and sort it without using sort function

givenList = [22,98,36,45]

for i in range(0,len(givenList)):
    for j in range(i,len(givenList)):
        if(givenList[i]>givenList[j]):
            givenList[i],givenList[j] = givenList[j],givenList[i]

print(givenList)

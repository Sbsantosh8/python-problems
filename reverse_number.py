numList = [1,22,33,55]

for i in range(0,len(numList)):
    for j in range(0,len(numList)-1):
        if(numList[j] < numList[j+1]):

          numList[j] ,numList[j+1]  = numList[j+1],numList[j]

print(numList)

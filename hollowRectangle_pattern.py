
                #Santosh Basragan
           # Hollow rectangle star pattern
                
rows = 4

for i in range(0,rows):
    for j in range(0,rows):
        if(i==1 and (j==1 or j==2)) or (i==2 and (j==1 or j==2)):
            print(" ",end="")    
        else:
            print("*",end="")    
    print()    

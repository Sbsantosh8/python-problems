

l = [22,33,44,66,92]
length = len(l)
l2 = []

# for i in range(0,length//2):
#     l[i],l[length-1-i] = l[length-1-i],l[i]
# print(l)


for i in range(length-1,-1,-1):
  l2.append(l[i])

print(l2)



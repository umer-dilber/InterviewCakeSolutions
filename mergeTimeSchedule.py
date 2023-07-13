slotTime = 2

tMin = float('inf')
tMax = float('-inf')

schedule = [(1, 10), (2, 6), (3, 5), (7, 9)]
for t in schedule:
    if (t[0]<tMin):
        tMin = t[0]
    if (t[1]>tMax):    
        tMax = t[1]


#calculating total indices
indices = tMax*slotTime

# making all indices default value as False
newScheduleBool = []
for i in range(indices):
    newScheduleBool.append(False)

# making all slots which are fixed as true
for t in schedule:
    index = t[0]
    while index<t[1]:
        newScheduleBool[index] = True
        index += 1

newSchedule = []       
minIndex = tMin
maxIndex = 0
i = 0
while i<tMax:
    while(newScheduleBool[i] == True):
        i+=1
        maxIndex = i
        if i==tMax:
            break
    if not (newScheduleBool[i-1] == False):
        newSchedule.append((minIndex, maxIndex))
    i += 1
    minIndex = i

print(newSchedule)


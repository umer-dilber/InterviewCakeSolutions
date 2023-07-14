def checkOrders(takeout, dineIn, servedorders, tIndex, dIndex, sIndex):
    if (sIndex == len(servedorders)):
        return True
    
    if ((tIndex < len(takeout)) and (takeout[tIndex] == servedorders[sIndex])):
        tIndex += 1
    elif ((dIndex < len(dineIn)) and (dineIn[dIndex] == servedorders[sIndex])):
        dIndex += 1
    else:
        return False
    sIndex += 1

    return checkOrders(takeout, dineIn, servedorders, tIndex, dIndex, sIndex)

print(checkOrders([17, 8, 24], [12, 19, 2], [17, 8, 12, 19, 24, 2],0,0,0))
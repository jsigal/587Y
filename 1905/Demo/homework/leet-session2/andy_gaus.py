def romanToIntCleaner(romanString):
    sumValue = 0
    dictNum = {"I":1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    dictNumSubs = {"IV":4, "IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    stringLength = len(romanString)
    index = stringLength - 1
    while index >= 0:
        char = romanString[index]
        if(index >= 1):
            currentAndPrevString = romanString[index-1:index+1]
            tempVal = dictNumSubs.get(currentAndPrevString,False)
            if(tempVal != False ):
                sumValue += tempVal
                index = index - 2
            else:
                sumValue = sumValue + dictNum.get(char)
                index = index - 1
        else:
            sumValue = sumValue + dictNum.get(char)
            index = index -1
    return sumValue
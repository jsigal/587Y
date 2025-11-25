def roman2int(rNumeral): # rNumeral must be a string
    total = 0
    # finds the length of rNumeral
    strlen = len(rNumeral)

    # roman numeral values dictionary
    valuesDict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    for ix in range(strlen):
        current = valuesDict[rNumeral[ix]]
        # find the largest value to the right of current
        largest = 0
        for i in range(ix + 1, strlen):
            next = valuesDict[rNumeral[i]]
            if next > largest:
                largest = next
        
        # subtract values if largest continues to be greater than current, otherwise add
        if largest > current:
            total -= current
        else:
            total += current

    return total
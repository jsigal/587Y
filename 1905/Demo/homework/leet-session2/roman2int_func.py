def romanToInt_simple(s):
    total = 0
    theDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in s:
        total += theDict[i]

    if "IV" in s:
        total -= 2
    if "IX" in s:
        total -= 2
    if "XL" in s:
        total -= 20
    if "XC" in s:
        total -= 20
    if "CD" in s:
        total -= 200
    if "CM" in s:
        total -= 20
    
    return total    

def romanToInt_prev(s):
	res, prev = 0, 0
	dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	for i in s[::-1]:          # rev the s
		if dict[i] >= prev:
			res += dict[i]     # sum the value iff previous value same or more
		else:
			res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
		prev = dict[i]
	return res

def romanToInt_replace_chain(s):
    roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
    s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    return sum(map(lambda x: roman_to_integer[x], s))

def romanToInt_replace(s):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number

def romanToInt_numlist(s):
    romanDict : dict =  {
                            "I" : 1,
                            "V" : 5,
                            "X" : 10,
                            "L" : 50,
                            "C" : 100,
                            "D" : 500,
                            "M" : 1000
                        }
    
    numList = []

    i = 0
    while (i < len(s)):

        if (i == len(s) - 1):
            numList.append(romanDict[s[i]])
        elif ((s[i] == "I") and (s[i + 1] not in ["V", "X"])):
            numList.append(romanDict[s[i]])
        elif ((s[i] == "I") and (s[i + 1] in ["V", "X"])): 
            numList.append(-romanDict[s[i]])
        elif ((s[i] == "X") and (s[i + 1] not in ["L", "C"])): 
            numList.append(romanDict[s[i]])
        elif ((s[i] == "X") and (s[i + 1] in ["L", "C"])): 
            numList.append(-romanDict[s[i]])
        elif ((s[i] == "C") and (s[i + 1] not in ["D", "M"])): 
            numList.append(romanDict[s[i]])
        elif ((s[i] == "C") and (s[i + 1] in ["D", "M"])): 
            numList.append(-romanDict[s[i]])
        else:
            numList.append(romanDict[s[i]])

        i += 1
    
    return sum(numList)

def romanToInt_negmap(s):
    result = 0
    aDict = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1, "IV": -2, "IX": -2, "XL": -20, "XC": -20, "CD": -200,"CM": -200}
    for k, v in aDict.items(): 
        if k in s:
            result += v*s.count(k)
    return result     

def romanToInt_lookahead(s):
    roman_int_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    for ix in range(len(s)):
        if ix + 1 < len(s) and roman_int_dict[s[ix]] < roman_int_dict[s[ix + 1]]:
            total -= roman_int_dict[s[ix]]
        else:
            total += roman_int_dict[s[ix]]
    return total

def romanToInt_bytwos(s):
    romans = {'I': 1, 'V':  5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    sum = 0
    for i in range(len(s)-1):
        two = s[i:i+2]
        if two in romans.keys():
            sum += romans[two]
            s = s.replace(two, "@@")

    for i in s:
        if i in romans.keys():
            sum = sum + romans[i]

    return sum

def romanToInt_replace_noalg(s):
    values = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")
    total = 0
    for char in s:
        total += values[char]
    return total

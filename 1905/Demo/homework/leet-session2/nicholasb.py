def romanToInteger(s: str) -> int:
    #Method is "romanToInteger" belongs to "Solution" class        
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    #created a dictionary. called hashmap online?        
    res = 0 #Accumulator because the returned values are added together after individually converted        
    for i in range(len(s)):
        #process the characters left to right in a loop           
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            # if: checks for a following char, and: checks if smaller                
            res -= roman[s[i]]
            #subtracts if both statements true            
        else:                
            res += roman[s[i]]
            #adds if false        
    return res# returns all characters converted and added
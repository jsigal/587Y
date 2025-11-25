def roman_to_int(s: str) -> int:
    values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} 
    total_val = 0       #stores the final integer result
    previous_val = 0    #keeps track of the value of the previous Roman numeral as we loop through the string

    for char in reversed(s):  #loops through the string in reverse
        v = values[char]      #numeric value of the current Roman character
        if v < previous_val:
            total_val -= v
        else:
            total_val += v
        previous_val = v     #updates the last numeral to avoid using the initial value 0

    return total_val
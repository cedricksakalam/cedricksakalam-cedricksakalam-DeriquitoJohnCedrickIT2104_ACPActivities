def roman_to_integer(roman):
    roman_values = {'I': 1 , 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else: 
            total += value
            prev_value = value
            
    return total

roman_numeral = input("Enter Roman numeral: ")
integer_value = roman_to_integer(roman_numeral.upper())
print(f"The integer value of '{roman_numeral}' is: {integer_value}")
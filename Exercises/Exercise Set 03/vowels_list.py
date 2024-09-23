input_str = input("Enter a string: ")
vowels = "aeiouAEIOU"

check_vowels = [char for char in input_str if char in vowels]
print(check_vowels)
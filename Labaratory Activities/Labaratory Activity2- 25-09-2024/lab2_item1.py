def palindrome(n):
    s = str(n)

    return s == s[::-1]

test_num = int(input("Enter an integer: "))

if palindrome(test_num):
    print("Palindrome")
else:
    print("Not a Palindrome")

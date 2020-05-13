#Exercise 1.2:
#Given two strings, write a method to decide if one is a permutation of the other.

def permutation(str1, str2):
    UNIQUE_CHARS_ALLOWED_IN_STRING = 27 #26 lowercase letters plus space
    chars1 = [0] * UNIQUE_CHARS_ALLOWED_IN_STRING #index 0 is space, 1 is a, 2 is b, etc
    chars2 = [0] * UNIQUE_CHARS_ALLOWED_IN_STRING

    for char in str1: #count each character in the first string
        asciiValue = ord(char)
        if asciiValue == 32:
            index = 0
        else:
            index = asciiValue - 96
        chars1[index] += 1
    for char in str2: #count each character in the second string
        asciiValue = ord(char)
        if asciiValue == 32:
            index = 0
        else:
            index = asciiValue - 96
        chars2[index] += 1

    return chars1 == chars2 #if the counts of all characters are equal, they are permutations of each other


first = "permutation"
second = "noitatumrep"

if permutation(first, second):
    print("These strings are permutations of each other")
else:
    print("These strings are NOT permutations of each other")
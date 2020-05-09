#Exercise 1.1:
#Implement an algorithm to determine if a string has all unique characters.
#What if you cannot use additional data structures?

strToSearch = "no repats"
allUnique = True
UNIQUE_CHARS_ALLOWED_IN_STRING = 27

#By the pigeonhole principle, a string of length > 27 (assuming the string is only lowercase letters and spaces)
#will be unique. This can be generalized to allow for more kinds of characters.
if len(strToSearch) > UNIQUE_CHARS_ALLOWED_IN_STRING:
    allUnique = False

fromUser = input("Enter 1 to run the algorithm *with* additional data structures, or 2 to run without: ")
withAdditonalData = True
if int(fromUser) == 1:
    withAdditionalData = True
elif int(fromUser) == 2:
    withAdditionalData = False
else:
    print("Invalid input. Running with additional data structures")

#####
#With additional data structures
#runs in O(n) time, with O(n) additional memory

encounteredChars = [False] * UNIQUE_CHARS_ALLOWED_IN_STRING
for char in strToSearch:
    asciiValue = ord(char)
    #97 is the ascii value of lowercase a, 96 allows for the space at index 0
    #32 is the ascii value of a space
    if asciiValue == 32:
        index = 0
    else:
        index = asciiValue - 96

    if encounteredChars[index]:
        allUnique = False
        break

    encounteredChars[index] = True


#####
#With no additional data structures
#runs in O(n^2) time, because of the nested for loop
#O(1) additional memory

if allUnique:
    for i in range(len(strToSearch)): #each character in the string
        if allUnique:
            for j in range(i + 1, len(strToSearch)): #each character after i in the string
                if strToSearch[i] == strToSearch[j]:
                    allUnique = False
                    break

if allUnique:
    print("all characters are unique")
else:
    print("there is at least one repeating character")


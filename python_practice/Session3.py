'''
Exercises of Lab Session 3
'''
'''
Exercise 1
Slicing on a list
'''
myList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
print(f"Complete list: \n{myList}")
print(f"Sliced list from element at index 3 to 7: \n{myList[3:8]}")
#List slicing
#
'''
Exercise 2
Program to swap 2 numbers without using a temp variable
Sum up the 2 numbers
Add the two numbers and assign to 1st number
Subtract 2nd number from the new 1st number and assign to 2nd number
    - gets original 1st number into 2nd number
Subtract the new 2nd number from the new 1st number and assign to 1st number
    - gets original 2nd number into 1st number
'''
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print(f"Original Numbers are \nNumber 1: {number1} Number 2: {number2}")
number1 = number1 + number2 
number2 = number1 - number2
number1 = number1 - number2
print(f"Swapped Numbers are \nNumber 1: {number1} Number 2: {number2}")
#
#
'''
Exercise 3
Identify the number of digits, lowercase letters and uppercase 
letters from the given input
Define reference lists holding lowercase letters, uppercase 
letters and digits
Read the input sentence.  Iterate character by charecter
and based on presence in the reference lists increment 
respective counters
'''
print("\nPrint number digits, small letters & caps in a given sentence: ")
small = ['q', 'b', 'c', 'd', 'e', 'f', 'g','h',
         'i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z']
caps = ['A','B','C','D','E','F','G','H',
        'I','J','K','L','M','N','O','P',
        'Q','R','S','T','U','V','W','X','Y','Z']
digits = ['0','1','2','3','4','5','6','7','8','9']
nums = smalls = bigs = 0
myInput = input("Enter the input sentence to count number of uppercase, lowercase letters and digits: ")
for x in myInput:
    if(x in small):
         smalls += 1
    elif(x in caps):
        bigs += 1
    elif(x in digits):
        nums += 1
#
print(f"Number of lowercase letters: {smalls}")
print(f"Number of uppercase letters: {bigs}")
print(f"Number of digits: {nums}")

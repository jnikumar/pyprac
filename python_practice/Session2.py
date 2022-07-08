'''
Exercises in Session 2 of Python Lab
'''

'''
use while loop to print even numbers in the range 0 to 9
last number less than 10
Using the modulo operator check if the reminder of the number 
divided with 2 is zero.  if the reminder is zero print the number
is even.  If the reminder is not zero print the number is odd 
'''
print("\nPrinting even numbers:")
numb = 0
while numb < 10:
    if(numb % 2 == 0):
        print(f"Number {numb} is an even number")
    else:
        #print(f"Number {numb} is an odd number")
        pass
    numb += 1
#
#print if even using range function
numb1 = 0
while numb1 in range(0,10):
    if(numb1 % 2 == 0):
        print(f"Number {numb1} is even number")
    numb1 += 1

'''
define a list of numbers using list constructor
write a for each loop to iterate each value of the list
print the power of each value using the pow function
pow(num1, num2) gives the value of num1 raised to num2
'''
print("\nPrint squares of numbers in a given list:")
numbers = [1, 3, 5, 6, 4, 10]
for numb in numbers:
    print(f"Square of {numb} is {pow(numb,2)}")
#print squares

'''
Using continue to move to next iteration
break to exit the loop or control structure
Check if number below 10 is odd, 
if it is even continue to next iteration
if it is odd print the number is odd
if the value reaches 7 exit the loop and continue
execution from the next statement after the loop
'''
print("\nPrint odd numbers and exit when 7:")
numb1 = 0
while numb1 < 10:
    numb1 += 1
    if (numb1 % 2 == 0):
        continue
    else:
        print(f"Current value is {numb1} and it is odd")
        if (numb1 == 7):
            break
print("All numbers are printed")
print("\nUsing for loop with range")
for n in range(10):
    #print(f"current value is {n}")
    if(n % 2 == 0):
        continue
    else:
        print(f"Current value is {n} and it is odd")
        if(n == 7):
            break
print("All numbers printed")
'''
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for n in num_list:
    if(n in range(12,23,2)):
        print (f"{n} is in the given range")
'''
print("\nPrint value from Map based on Key:")
marks = {'name1':100, 'name2': 200, 'name3':300}
print(type(marks))
print(marks["name3"])
for student in marks:
    if(student=='name2'):
        print(marks[student])

print("\nPrint number digits, small letters & caps in a given sentence: ")
small = ['q', 'b', 'c', 'd', 'e', 'f', 'g','h',
         'i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z']
caps = ['A','B','C','D','E','F','G','H',
        'I','J','K','L','M','N','O','P',
        'Q','R','S','T','U','V','W','X','Y','Z']
digits = ['0','1','2','3','4','5','6','7','8','9']

countchars = input("Enter the sentense to find number of digits, lower case & upper case letters: ")
nums = smalls = bigs = 0
for x in countchars:
    if(x in digits):
        nums += 1
    elif(x in small):
        smalls += 1
    elif(x in caps):
        bigs += 1
print(f"Number of digits is {nums}, number of lower case letters {smalls} and number of upper case letters is {bigs}")

list2 = [1,2,3,4,1,5,6,3,2,4,5,6,7]
find = int(input("Enter to value to find: "))
times = list2.count(find)
if(times == 0):
    print(f"Item {find} not present in the given list")
else:
    print(f"Item {find}  present in the given list {times} times")
'''
List Exercises
'''
'''
list3 = [13,12]
print(list2 + list3)
print(list3 *2)
print(list3.index(13))
list2.append(11)
print(list2)
list2.extend(list3)
print(list2)
print(list2.pop())
print(list2)
myint = 10
print(type(myint))
'''
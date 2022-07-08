import random
import re
'''
my_str = "teststring.txt"
print(random.choice(my_str))

with open("/users/nijosyula/testfile.txt", "r") as myfile:
    mytxt = myfile.readlines()
#
print(len(mytxt))
'''
 
'''
Substring ='string'
 
 
String1 =''''''We are learning regex with geeksforgeeks
         regex is very useful for string matching.
          It is fast too.''''''
String2 =''''''string We are learning regex with geeksforgeeks
         regex is very useful for string matching.
          It is fast too.''''''
 
# Use of re.search() Method
print(re.search(Substring, String1, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String1, re.IGNORECASE))
 
# Use of re.search() Method
print(re.search(Substring, String2, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String2, re.IGNORECASE))
'''
option = input("Enter R or P or S: ")
find_str = "find"
#print (re.search(("[find in SsRrPp test]"), find_str)) 
print(re.search(find_str, "rfind in SsRrPp test"))
print(re.match("[SsRrPp]", option))

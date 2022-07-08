'''
Assignments in Lab Session 1
'''

#program to calculate volume of a sphere
'''
Accept radius as  input from user
Invoke the function vol_sphere to calculate the volume
Return the volume and print using f'print
'''
def vol_sphere(radius):
    PI = 3.14
    return ((4 * PI * pow(radius, 3))/3)
#
rad = float(input("Enter the radius of the sphere: "))
print(f"Volume of Sphere with radius {rad} is {vol_sphere(rad)}")

#Print warning message if luggage is more than 25Kg in weight
'''
Accept the input on console
compare the input with 25
if greater than 25 print a warning message
'''
permitted_wt = 25
lug_wt = float(input("Enter the wight of the luggage: "))
if lug_wt > permitted_wt:
    print(f"Wight of luggage is {lug_wt} and it is {lug_wt - permitted_wt} more than the permissible limit of 25")
#
'''
Accept total marks obtained as input
Use if, elif, else to compare the input with
Grade qualification and print the correct grade
corresponding to the total marks obtained
'''
total_marks = int(input("Enter the total marks obtained: "))
if total_marks >= 80:
    print(f"Marks obtained is {total_marks} and Grade is EXCELLENT")
elif total_marks >= 65:
    print(f"Marks obtained is {total_marks} and Grade is GOOD")
elif total_marks >= 50:
    print(f"Marks obtained is {total_marks} and Grade is PASS")
else:
    print(f"Marks obtained is {total_marks} and Grade is FAIL")
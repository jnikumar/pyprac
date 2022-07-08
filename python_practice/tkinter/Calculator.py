#q Calculator

def addition ():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0 #Total number enter
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

def subtraction ():
    print("Subtraction");
    n = float(input("Enter the number: "))
    t = 0 #Total number enter
    sum = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

def multiplication ():

    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0 #Total number enter
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

def average():

    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

# main...

while True:

    list = []
    print(" Simple Calculator in python")
    print(" Enter 'a' or 'A' for addition")
    print(" Enter 's' or 'S' for substraction")
    print(" Enter 'm' or 'M' for multiplication")
    print(" Enter 'v' 'V' for average")
    print(" Enter 'q' or 'Q' for quit")
    c = input(" ")
    if c != 'q' or c == 'Q' :
        if c == 'a' or c == 'A':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 's' or c == 'S':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'm' or c == 'M':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'v' or c == 'V':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, invilid character")
    else:
        break

print("1: Check if a number is even or odd.\n "
      "2: Check if something divides evenly into another number.")
check = str(input("Please select option 1 or 2."))

if check == "1":
    num1 = int(input("Please enter the number:"))
    if num1 % 4 == 0:
        print("%s is even AND divisible by 4." % (num1))
    elif num1 % 2 == 0:
        print("%s is even." % (num1))
    else:
        print("%s is odd" % (num1))
elif check =="2":
    num1 = int(input("Please enter the first number:"))
    num2 = int(input("Please enter the second number:"))
    if num1 % num2 == 0:
        print("%s fits into %s evenly.  There are no remainders" % (num2, num1))
    else:
        print("%s does not fit into %s evenly.  There will be a remainder of" % (num2, num1), num1 % num2 )
else:
    print("No viable option detected.  Closing program.")

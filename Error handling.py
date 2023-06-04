#you can add a try/except or finally around the code that generates an error to handle it gracefully
num1 = (input("Enter the first no:"))
num2 = (input("Enter the second no:"))
try:
    result = float(num1) / float(num2)
    print(num1 + " / " + num2 + " = " + str(result))
except:
    print("something went wrong")

# if you want to know what the error was, you can use:
import sys
num1 = (input("Enter the first no:"))
num2 = (input("Enter the second no:"))
try:
    result = float(num1) / float(num2)
    print(num1 + " / " + num2 + " = " + str(result))
except :
    error = sys.exc_info()[0]
    #print("something went wrong")
    print(error)
finally:
    print("i wll always run!!!")

#IF YOU KNOW WHAT ERROR IS OCCURING, YOU CAN SPECIFY HOW TO HANDLE THAT EXACT ERROR
num1 = (input("Enter the first no:"))
num2 = (input("Enter the second no:"))
try:
    result = float(num1) / float(num2)
    print(num1 + " / " + num2 + " = " + str(result))
except ZeroDivisionError:
    print("The answer is infinity")

#IDEALLY YOU HANDLE ONE OR MORE SPECIFIC ERRORS,AND HAVE A GENERIC HANDLER AS WELL
import sys
num1 = (input("Enter the first no:"))
num2 = (input("Enter the second no:"))
try:
    result = float(num1) / float(num2)
    print(num1 + " / " + num2 + " = " + str(result))
except ZeroDivisionError:
    print("The answer is infinity")
#THIS IS A GENERIC HANDLER BELOW:
except :
    error = sys.exc_info()[0]
    print("something went wrong")
    print(error)
    # How to force my program to exit if an error occurs and i dont want to continue
    # you can use the function sys.exit() in the sys library
    sys.exit()
#Always note that the code you put after try or except that is not indented will always run
print("This message always display if there is no error")


#how to use varables and an if statement to control what happens after an error
import sys
num1 = (input("Enter the first no:"))
num2 = (input("Enter the second no:"))
try:
    result = float(num1) / float(num2)
    print(num1 + " / " + num2 + " = " + str(result))
    errorflag = False
except ZeroDivisionError:
    print("The answer is infinity")
    errorflag = True
if not errorflag:
    print("This message only displays if there is no error")

# #is there any code in our program that can give us an error at runtime?
#How do you know what errors will be raised?
#1)you can test it yourself and when an error occurs,use the sys.exc_info() to get the name of error
#There is a list of standard python errors:
#-https://docs.python.org/3/c-api/exceptions.html#standard-exceptions















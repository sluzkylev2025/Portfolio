'''
The Calculator Project
The calculator works endlessly, first an action is requested, and then 2 numbers. If the user enters “stop", the project stops.
Calculator Actions:
- multiplication
- division
- addition
- subtraction
- exponentiation
- finding the whole
- finding the remainder
Calculator Hints:
-Incorrect operation sign!
- You can't divide by 0!

Send the program with the values for verification:
1 test: //, 56, 4
2 test: !, 4, 0
3 test: /, 34, 0

'''

print("Input stop to finish work")
while True:
    s = input("Operation (+,-,*,/,//,%,**): ")
    if s == 'stop':
        break
    x = float(input("x="))
    y = float(input("y="))
    if s == '+':
        print(x+y)
    elif s == '-':
        print(x-y)
    elif s == '*':
        print(x*y)
    elif s == '/':
        if y != 0:
            print(x/y)
        else:
            print("Division by zero!")
    elif s == '//':
        if y != 0:
            print(x//y)
        else:
            print("Division by zero!")
    elif s == '%':
        if y != 0:
            print(x%y)
        else:
            print("Division by zero!")

    elif s == '**':
        print(x**y)
    else:
        print("Uncorrect operation")



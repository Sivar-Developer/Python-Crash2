# Try Except block
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Divided by zero")
    print(err)
except ValueError:
    print("invalid input")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

def division(numb1, numb2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("It's not possible division 0")

print(division(num1, num2))

print("Program completed")
import math
print("Calcule square root")
number = int(input("Enter a valid number: "))

attempts = 0

while number < 0:
    print("wrong number")

    if attempts == 2:
        print("Too many attempts")
        break

    number = int(input("Enter a valid number: "))
    attempts += 1



if attempts < 2:
    solution = math.sqrt(number)
    print(f"the solution is {solution}")




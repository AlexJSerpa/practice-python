number = int(input("Enter a number: "))

count = 0

while number > 0:
    count = count + number

    number = int(input("Enter a number: "))

print("The total sum is: " + str(count))
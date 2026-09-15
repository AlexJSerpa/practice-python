age = int(input("Enter your age: "))

while age < 5 or age > 100 :
    print("Wrong age, try again")
    age = int(input("Enter your age: "))

print("Your age is " + str(age))
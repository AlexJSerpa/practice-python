password = input("Enter the password: ")

counter = 0

for i in password:
    if i == " ":
        counter += 1


if len(password) > 8 and counter == 0:
    print("Password Ok")
else:
    print("Wrong password")

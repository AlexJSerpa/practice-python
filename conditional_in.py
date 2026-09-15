print("Program with in")
print("Select the options: Math, Physics, English")
option = input("Enter the option: ")

subject = option.lower()

if subject in ("math", "physics", "english"):
    print("Subject select: " + subject)
else :
    print("Subject does not exit")
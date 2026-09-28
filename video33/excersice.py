email = input("Enter the email address: ")

if email.count('@') == 1 and not email.startswith('@') and not email.endswith('@'):
    print("Correct email address")
else:
    print("Wrong email")

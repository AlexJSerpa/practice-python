is_valid_email = False 

for i in "alex.serpa@jejej.com":
    if i == '@':
        is_valid_email = True

if is_valid_email:
    print("the email is correct")
else :
    print("The email is not correct")
print("scholarship program")

distance = int(input("Enter the distance to collage: "))

num_brothers = int(input("Enter the numbers of brothers: "))

familiar_salary = int(input("Enter the familiar salary: "))

if distance > 40 and num_brothers > 2 and familiar_salary <= 20_000 :
    print("Scholarship approved")
else:
    print("Scholarship rejected")

    
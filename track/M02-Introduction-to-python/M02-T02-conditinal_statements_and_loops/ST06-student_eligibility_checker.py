marks = int(input("Enter the number:"))
attendance = int(input("Enter the number:"))
project_completed = input("Enter the status:")

if marks >= 60 and attendance >= 75:
    if project_completed == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
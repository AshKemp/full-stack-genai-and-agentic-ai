staff = [("Ashwin",16),("Bhavya",17),("Chitra",15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No staff member is eligible to manage the staff")
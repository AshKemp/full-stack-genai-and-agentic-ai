snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Order confirmed! Enjoy your {snack}.")
else:
    print(f"Order not available for {snack}. Please choose either 'cookies' or 'samosa'.")


# value = 13
# remainder = value % 5

# if remainder:
#     print(f"{value} is not divisible by 5, remainder is {remainder}")


# value = 13
# if (remainder := value % 5):
#     print(f"{value} is not divisible by 5, remainder is {remainder}")

# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Sorry, we don't have {requested_size} size")


flavours = ["masala","ginger","lemon","mint"]
print("Available flavours: ",flavours)

while (flavour := input("Choose a flavour: ")) not in flavours:
    print("Sorry, we don't have that flavour.",flavour)
print(f"Serving {flavour} chai")
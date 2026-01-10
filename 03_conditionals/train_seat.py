seat_type = input("Enter the seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("You have selected a Sleeper seat. No AC beds available.")
    case "ac":
        print("You have selected an AC seat. Enjoy the cool breeze!")
    case "general":
        print("You have selected a General seat. Affordable and comfortable.")
    case "luxury":
        print("You have selected a Luxury seat. Experience the best comfort!")
    case _:
        print("Invalid seat type selected. Please choose from sleeper, AC, general, or luxury.")

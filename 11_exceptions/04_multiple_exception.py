def process_order(item, quantity):
    try:
        price = {"masala": "20"}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry, we don't have that item.")
    except TypeError:
        print("Quantity must be a number.")

process_order("ginger",2)
process_order("masala","two")
process_order("masala",2)
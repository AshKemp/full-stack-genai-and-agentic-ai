class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"Invalid chai flavor: {flavor}")
        if not isinstance(cups, int):
            raise TypeError("Cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for visiting our chai shop!")

bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        # nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print(f"Order updated to {chai_type} Chai")

update_order()  # This will print: Order updated to Kesar Chai
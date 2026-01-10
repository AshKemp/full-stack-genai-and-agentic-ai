def chai_customers():
    print("Welcome! What chai would you like ?")
    order = yield
    while True:
        print(f"Preparing your {order}")
        order = yield

stall = chai_customers()
next(stall)  # Start the generator
stall.send("Masala Chai")
stall.send("Lemon Chai")
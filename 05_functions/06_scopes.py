# def serve_chai():
#     chai_type = "masala" # local scope
#     print(f"Inside function {chai_type}")

# chai_type = "Lemon" # global scope
# serve_chai()
# print(f"Outside function {chai_type}")


def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "ginger"
        print(f"Inner function {chai_order}") # local scope
    print_order()
    print(f"Outer function {chai_order}") # enclosing scope

chai_order = "Tulsi" # global scope
chai_counter()
print(f"Global scope {chai_order}")
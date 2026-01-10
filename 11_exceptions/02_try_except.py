chai_menu = {"masala": 30,"ginger": 40}

try:
    chai_menu["elachi"]
except KeyError:
    print("The specified key is not found in the dictionary.")
print("Hello world")
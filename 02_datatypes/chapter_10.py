chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Initial chai order: {chai_order}")

chai_receipe = {}
chai_receipe["base"] = "black tea"
chai_receipe["liquid"] = "milk"

print(f"Initial Chai receipe: {chai_receipe}")
print(f"Chai receipe base: {chai_receipe['base']}")

# del chai_receipe["liquid"]

# print(f"Chai receipe after deletion: {chai_receipe}")

print(f"Is sugar in chai order? {'sugar' in chai_order}")

chai_order = dict(type="Ginger Chai", size="Medium", sugar=1)
# print(f"Order details (Keys): {chai_order.keys()}")
# print(f"Order details (Values): {chai_order.values()}")
# print(f"Order details (Items): {chai_order.items()}")

# last_item = chai_order.popitem()
# print(f"Last item removed from order: {last_item}")
# print(f"Chai order after popping last item: {chai_order}")

extra_spices = {"cardamom": "crushed","ginger": "sliced"}
chai_receipe.update(extra_spices)
print(f"Updated chai receipe: {chai_receipe}")

customer_note = chai_order.get("size","NO note")
print(f"Chai size is: {customer_note}")
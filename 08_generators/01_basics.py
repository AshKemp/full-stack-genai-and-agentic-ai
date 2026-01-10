def serve_chai():
    yield "Cup1: Masala Chai"
    yield "Cup2: Ginger Chai"
    yield "Cup3: Cardamom Chai"


stall = serve_chai();

# for cup in stall:
#     print(cup)


def get_chai_list():
    return ["Cup1", "Cup2", "Cup3"]

# generator function

def get_chai_gen():
    yield "Cup1"
    yield "Cup2"
    yield "Cup3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))

class BaseChai:
    def __init__(self, _type):
        self.type = _type

    def prepare(self):
        return f"Preparing a cup of {self.type} chai...."
    

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding spices: cardamom, ginger, cloves")

class ChaiShop:
    chai_cls = BaseChai
    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving: {self.chai.type} chai in the shop.")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()
fancy.chai.add_spices()
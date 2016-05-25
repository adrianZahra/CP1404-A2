class Item_info:
    def __init__(self, name="defalut item", condition="default condition", price=0, in_out = "in"):
        self.name = name
        self.condition = condition
        self.price = price
        self.in_out = in_out

    def __str__(self):
        return "{} {} ${} {}".format(self.name, self.condition, self.price, self.in_out)
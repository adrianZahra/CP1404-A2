class Item:
    def __init__(self, item_number=0, name="defalut item", condition="default condition", price=0):
        self.number = item_number
        self.name = name
        self.condition = condition
        self.price = price

    def __str__(self):
        return "{} {} {} ${}".format(self.item_number, self.name, self.condition, self.price)

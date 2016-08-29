type_dessert = ["icecream","apple"]

class Dessert:
    def __init__(self, dessert_name, amount_calories):
        self.dessert_name = dessert_name
        self.amount_calories= amount_calories

    def is_healthy(self):
        if self.dessert_type() == "Fruit" and self.amount_calories <= 400:
            return True
        else:
            return False
    def is_delicious(self):
        if self.is_healthy() == True:
            return "Dessert type is delicious and healthy"
        else:
            return " Dessert type is delicious and not healthy"
    def dessert_type(self):
        if self.dessert_name == type_dessert[0]:
            return "Cake"
        else:
            return "Fruit"

mydessert = Dessert("icecream", 1200)

print mydessert.dessert_type()
print mydessert.is_healthy()
print mydessert.is_delicious()

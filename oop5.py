class MenuItem:
    def __init__(self, food, price):
        self.food = food
        self.price = price

    def __str__(self):
        return f'{self.food}, {self.price}'


burger = MenuItem("Hamburger", 4000)
coke = MenuItem("Coke", 1500)
fries = MenuItem("French fries", 1500)

print(burger)
print(coke)
print(fries)

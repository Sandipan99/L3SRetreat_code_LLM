class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        self.items.append(item * quantity)

    def total_price(self):
        return sum(self.items)
        
cart = ShoppingCart()

cart.add_item(5.99, 4)
cart.add_item(10.99)

total = cart.total_price()

print(total)

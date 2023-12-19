class Order:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

class OrderStack:
    def __init__(self):
        self.stack = []

    def push(self, i, q):
        order = Order(i, q)
        if order.quantity > 0:
            self.stack.append(order)
        else:
            return False

    def pop(self):
        order = self.stack.pop()

    def view(self):
        print("Список замовлень:")
        for order in self.stack:
            print(f"- {order.item} ({order.quantity} одиниць)")

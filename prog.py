from flask import Flask

app = Flask(__name__)

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
        orders_text = "Список замовлень:\n"
        for order in self.stack:
            orders_text += f"- {order.item} ({order.quantity} одиниць)\n"
        return orders_text

order_stack = OrderStack()

@app.route('/')
def home():
    global order_stack
    order_stack.push('item1', 3)
    order_stack.push('item2', 5)

    orders_text = order_stack.view()
    return orders_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

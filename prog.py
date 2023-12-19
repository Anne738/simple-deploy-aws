from flask import Flask, request, redirect, url_for

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
            return True
        else:
            return False

    def pop(self):
        if self.stack:
            order = self.stack.pop()
            return f"Order removed: {order.item} ({order.quantity} units)"
        else:
            return "No orders to remove."

    def view(self):
        return [{"item": order.item, "quantity": order.quantity} for order in self.stack]

order_stack = OrderStack()

@app.route('/', methods=['GET', 'POST'])
def manage_orders():
    if request.method == 'POST':
        action = request.form.get('action')
        item = request.form.get('item')
        quantity_str = request.form.get('quantity')

        if action == 'add':
            try:
                quantity = int(quantity_str)
                if order_stack.push(item, quantity):
                    return redirect(url_for('manage_orders'))
                else:
                    return "Invalid quantity. Quantity must be greater than 0."
            except ValueError:
                return "Invalid quantity. Please enter a valid number."
        elif action == 'remove':
            result = order_stack.pop()
            return f"{result}\nOrders: {order_stack.view()}"

    orders = order_stack.view()
    return f"Orders: {orders}\n\n" \
           f"<form method='post'>" \
           f"<label for='item'>Item:</label>" \
           f"<input type='text' name='item' required>" \
           f"<label for='quantity'>Quantity:</label>" \
           f"<input type='number' name='quantity' required>" \
           f"<button type='submit' name='action' value='add'>Add Order</button>" \
           f"<button type='submit' name='action' value='remove'>Remove Order</button>" \
           f"</form>"

if __name__ == '__main__':
    app.run(debug=True)

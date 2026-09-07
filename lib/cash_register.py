# lib/cash_register.py

class CashRegister:
    def __init__(self, discount=0):
        # validate discount input
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")
            self._discount = 0

        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # update total
        self.total += price * quantity
        # add items
        self.items.extend([item] * quantity)
        # record transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount > 0 and self.total > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.previous_transactions:
            last_transaction = self.previous_transactions.pop()
            # adjust total
            self.total -= last_transaction["price"] * last_transaction["quantity"]
            # remove items
            for _ in range(last_transaction["quantity"]):
                if last_transaction["item"] in self.items:
                    self.items.remove(last_transaction["item"])
        else:
            print("No transaction to void.")

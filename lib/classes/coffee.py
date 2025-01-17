



class Coffee:
    def __init__(self, name):
        self.name = name

        @property
        def name(self):
            return self._name

    def orders(self):
        from classes.order import Order
        return [o for o in Order.all if o.coffee == self]

    def customers(self):
        return list(set([o.customer for o in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
      prices = [o.price for o in self.orders()]
      total= sum(prices)
      return total/len(prices)
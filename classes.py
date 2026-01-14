class Instrument:
    def __init__(self, name, price):
        self.name = name
        self. price = price

    def __str__(self):
        return f"{self.name} (${self.price})"

    def apply_discount(self, percent):
        discount_amount = self.price * percent / 100
        self.price -= discount_amount


a1 = Instrument("Piano", 1000)
a2 = Instrument("Baby Grand Piano", 1500)
a3 = Instrument("Grand Piano", 2000)


def label():
    a1.apply_discount(10)
    print(a1)
    a2.apply_discount(10)
    print(a2)
    a3.apply_discount(10)
    print(a3)


label()

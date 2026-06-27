class Phone:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def display(self):
        print(f"Brand:{self.brand}")
        print(f"Price:{self.price}")
p1=Phone('SAMSUNG',35000)
p2=Phone('Apple',75000)
p1.display()
p2.display()

        
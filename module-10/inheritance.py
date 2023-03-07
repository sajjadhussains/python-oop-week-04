class Device:
    def __init__(self,brand,price,color) -> None:
        self.brand = brand
        self.price = price
        self.color=color
    def run(self):
        print(f'I am price {self.price}')

class Laptop(Device):
    def __init__(self, brand, price, color,disc_size,ram) -> None:
        self.disc_size = disc_size
        self.ram = ram
        super().__init__(brand, price, color)
    def __repr__(self) -> str:
        return f'{self.brand} {self.price} {self.color} {self.disc_size} {self.ram}'

hp = Laptop('hp',35000,'silver','500gb','8gb')
print(hp)
hp.run()

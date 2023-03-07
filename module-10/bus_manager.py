class Vehicle:
    def __init__(self,name,liscence,price) -> None:
        self.name = name
        self.liscence = liscence
        self.price = price
    def start(self):
        print(f'{self.name} is started')

class Bus(Vehicle):
    def __init__(self, name, liscence, price,route,seat) -> None:
        self.route = route
        self.seat = seat
        super().__init__(name, liscence, price)
    def run(self):
        print(f'I run in {self.route}')
    def __repr__(self) -> str:
        return f'{self.name} {self.seat}'
class ACbus(Vehicle):
    def __init__(self, name, liscence, price,route,seat) -> None:
        self.route = route
        self.seat = seat
        super().__init__(name, liscence, price)
    def run(self):
        print(f'I am running in {self.route}')

bus = Bus('nabil',True,800,'Dhaka to Dinajpur',45)
miniBus = ACbus('hstu',True,10,'Dinajpur to Hstu',25)
print(f'{miniBus.name} {miniBus.liscence} {miniBus.seat}')
# Some type of inheritance have:
#   single inheritance(parent-->child)
#   multilevel inheritance(grandpa-->parent-->child)
#   Multiple inheritance(father,mother-->child)
#   Hirarchical inheritance(father-->You,brother,sister)
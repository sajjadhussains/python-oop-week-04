class Car:
    def __init__(self,license,model,color):
        self.license=license
        self.model=model
        self.color=color
    def __repr__(self) -> str:
        return f'{self.license},{self.model},{self.color}'
    
class Garage:
    def __init__(self) -> None:
        self.car_added=[]
        self.spot=10
        self.car_infos={}
        self.bill = 0
        self.ticket=[]
    
    def spots_available(self):
        return self.spot
    
    def add_car_to_garage(self,car):
        self.spot_name=['A1','B1','C1','D1','E1','F1','G1','H1','I1','J1']
        if self.spots_available()>0:
            user_data=str(car).split(",")
            self.spot-=1
            self.car_added.append(user_data)
            self.car_infos={"Tickets":[],"License":[],"model":[],"color":[]}
            ticket=""
            for i,val in enumerate(self.car_added):
                ticket=self.spot_name[i]+user_data[0]
                self.car_infos["Tickets"].append(ticket)
                self.car_infos["License"].append(val[0])
                self.car_infos["model"].append(val[1])
                self.car_infos["color"].append(val[2])
            print(f'successfully parked.Your ticket {ticket}')
        else:
            print("No spots availabel!!!")
    
    def unpark(self,ticket,hours):
        past_spot_len=len(self.car_infos['Tickets'])
        if ticket not in self.car_infos['Tickets']:
            print("No car found!!!")
        else:
            for i,val in enumerate(self.car_infos['Tickets']):
                if val == ticket:
                    print(i)
                    print(f'Your License is {self.car_infos["License"][i]}')
                    print(f'Your Model is {self.car_infos["model"][i]}')
                    print(f'Your Car color is {self.car_infos["color"][i]}')
                    removed_car_index=i
                    self.car_infos['License'].pop(i)
                    self.car_infos['model'].pop(i)
                    self.car_infos['color'].pop(i)
                    self.car_infos['Tickets'].pop(i)
                    self.spot+=1
        if hours>30:
            print(f'Total Bill = ${hours*5 + 100}')
        else:
            print(f'Total Bill = ${hours*5}')
    def total_cars_in_garage(self):
        for i in self.car_infos.items():
            print(i)


my_garage=Garage()
# my_car1=Car('123Wn','Ferari','red')
# my_car2=Car('123Wn','Toyota','blue')
# my_garage.add_car_to_garage(my_car1)
# my_garage.add_car_to_garage(my_car2)
# my_garage.unpark('B1123Wn',10)
# my_garage.total_cars_in_garage()
# my_garage.unpark('A1123Wn',40)
print("********Welcome To Our Parking System********")
while True:
    print("1.Park Your Car \n2.Check Availabe Space \n3.Unpark Your Car")
    choice = int(input("Enter your choice: "))
    if choice==1:
        license_no=input("Give Your License: ")
        model=input("Model No: ")
        color=input("Color : ")
        my_car=Car(license_no,model,color)
        my_garage.add_car_to_garage(my_car)
    if choice==2:
        print(f'Available spots are : {my_garage.spots_available()}')
    if choice==3:
        ticket=input("Your given ticket: ")
        hours=int(input("Parking time: "))
        my_garage.unpark(ticket,hours)

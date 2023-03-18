"""All about mankind"""

class Human:
    def __init__(self,gender,height,weight) -> None:
        self.gender = gender
        self.height = height
        self.weight = weight

class Police(Human):
    def __init__(self, gender, height, weight,case,nationality) -> None:
        super().__init__(gender, height, weight)
        self.case= case
        self.nationality = nationality

class csEngineer(Human):
    def __init__(self, love_to_code,has_gf,gender, height, weight) -> None:
        super().__init__(gender, height, weight)
        self.love_to_code=love_to_code
        self.has_gf=has_gf
if __name__=='__main__':
    police = Police(gender='male',height=5.8,weight=64,case=True,nationality='Bangladeshi')
    print(police.gender)
    print('eng 1')
    eng1 = csEngineer(True,False,"male",74,68)
    print(eng1.height)
    print('eng 2')
    eng2=csEngineer(love_to_code=False,has_gf=False,gender='male',height=70,weight=65)
    print(eng2.height)
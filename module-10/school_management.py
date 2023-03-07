import time


class School:
    def __init__(self,name,address,principle="") -> None:
        self.name=name
        self.address = address
        self.principle = principle
        self.grades = []
    def add_grade(self,name,teacher):
        new_grade = Grade(name,teacher)
        self.grades.append(new_grade)
    def remove_grade(self,name):
        idx = 0
        for i,grade in enumerate(self.grades):
            if grade.name==name:
                idx = i
        del self.grades[idx]
    
class Grade:
    def __init__(self,name,teacher) -> None:
        self.students=[]
        self.name=name
        self.teacher = teacher
    def __repr__(self) -> str:
        return f'{self.name} with {self.teacher}'
    def __del__(self):
        print(f'Deleting {self.name} with {self.teacher}')

oxford = School('Oxford kid Academy','Mirpur','Obayed Alam')
oxford.add_grade('class 3','Osman Goni')
oxford.add_grade('class 5','shohidul Sir')
oxford.add_grade('class 6','Mahafuz sir')
print(oxford.grades)
oxford.remove_grade('class 5')

time.sleep(10)
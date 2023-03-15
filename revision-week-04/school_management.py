# constructor and destructure

class School:
    def __init__(self,name,address,principles="") -> None:
        self.name=name
        self.address = address
        self.principles=principles
        self.grades=[]
    def add_grade(self,name,teacher):
        new_grade = Grade(name,teacher)
        self.grades.append(new_grade)
    def remove_grade(self,name):
        idx=0
        for i,grade in enumerate(self.grades):
            if grade.name==self.name:
                idx = i
            del self.grades[idx]

class Grade:
    def __init__(self,name,teacher) -> None:
        self.students=[]
        self.teacher = teacher
        self.name=name
    def __repr__(self) -> str:
        return f'class {self.name} with {self.teacher}'
    def __del__(self):
        return f'deleting {self.name} with {self.teacher}'
    
oxford = School('bashak adorsho','bahalbaria','bulbul sir')
print(oxford.name)
oxford.add_grade('3','Raja sir')
oxford.add_grade('4','shuvo')
print(oxford.grades)
oxford.remove_grade('3')
print(oxford.grades)
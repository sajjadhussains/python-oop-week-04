class Student:
    def __init__(self,name,id,university):
        self.name=name
        self.id=id
        self.university=university

obj1=Student('shuvo',1802116,'HSTU')
output=vars(obj1)
print(output)
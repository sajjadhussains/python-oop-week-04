# write a python program to find out the number of objects for a certain class

class Student:
    counter = 0
    def __init__(self,name,fathers_name,mothers_name,age) -> None:
        Student.counter+=1
        self.name=name
        self.fathers_name=fathers_name
        self.mothers_name=mothers_name
        self.age=age


obj1=Student('fahim','rahim','rahima',26)
obj2 = Student('Mehedi','karim','karima',27)
obj3= Student('shuvo','kalam','shopna',25)
obj3= Student('shuvo','kalam','shopna',25)
print(Student.counter)
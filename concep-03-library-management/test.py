class A:
    val=[10]
    def __init__(self,v):
        self.val.append(v)

obj1=A(100)
print(obj1.val)
obj2=A(200)
print(obj2.val)
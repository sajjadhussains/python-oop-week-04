"""Node creation in python"""
# class Node:
#     def __init__(self) -> None:
#         self.member=10
#     def check(self):
#         print(self.member)
# def main():
#     obj1 = Node()
#     obj1.check()

# main()

# class Node:
#     def __init__(self,value) -> None:
#         self.value=value
#         self.value+=value
#         print(self.value)
# def main():
#     Node(10)

# main()

class Node:
    def __init__(self,value) -> None:
        self.val=value
        self.next=None
def print_list(obj1):
    while(obj1!=None):
        print(obj1.val,end=" ")
        obj1=obj1.next

def main():
    obj1=Node(10)
    obj2=Node(20)
    obj3=Node(30)
    obj1.next=obj2
    obj2.next=obj3
    print_list(obj1)
main()
"""Linked list in python"""
# 1.creation linked list
# 2.insertion at head,insertion at tail,insertion at any position

class Node:
    def __init__(self,val) -> None:
        self.value=val
        self.next=None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_pos(self,pos,value):
        tmp=self.head
        newNode=Node(value)
        if pos==0:
            newNode.next=self.head
            self.head=newNode
        else:
            for i in range(pos-1):
                tmp=tmp.next
                if tmp==None:
                    print("Out of bound")
                    return
            newNode.next = tmp.next
            tmp.next=newNode
    def insert_at_tail(self,val):
        newNode=Node(val)
        if self.head==None:
            self.head=newNode
        else:
            tmp=self.head
            while tmp.next!=None:
                tmp=tmp.next
            tmp.next=newNode
    def insert_at_head(self,value):
        newNode = Node(value)
        if self.head==None:
            self.head=newNode
        else:
            tmp=self.head
            self.head=newNode
            newNode.next=tmp
# deletion operation in linked ist
    def del_at_pos(self,pos):
        if pos==0:
            tmp=self.head
            self.head=tmp.next
            del tmp
        else:
            tmp=self.head
            for i in range(pos-1):
                tmp=tmp.next
                if tmp==None:
                    print('Output of bound')
                    return
            delNode=tmp.next
            tmp.next=delNode.next
            del delNode

    def print_linked_list(self):
        tmp=self.head
        while tmp!=None:
            print(tmp.value)
            tmp=tmp.next

def main():
    list = Linked_list()
    list.insert_at_tail(10)
    list.insert_at_tail(20)
    list.insert_at_tail(30)
    list.insert_at_head(5)
    list.insert_at_pos(1,15)
    list.del_at_pos(0)
    list.print_linked_list()

main()
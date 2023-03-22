class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def level_order(root):
    q=[]
    q.append(root)
    while len(q) != 0:
        p=q[0]
        q.pop(0)
        print(p)
        if p.left !=None:
            q.append(p.left)
        if p.right != None:
            q.append(p.right)
def main():
    val=int(input())
    root=Node(val)
    q=[]
    q.append(root)
    while len(q)!=0:
        p=q[0]
        q.pop(0)
        a=int(input())
        b=int(input())
        left=None
        right=None

        if a!=-1:
            left=Node(a)
        if b!= -1:
            right=Node(b)
        p.left=left
        p.right=right
        if p.left !=None:
            q.append(p.left)
        if p.right!=None:
            q.append(p.right)
    inorder(root)
    
main()
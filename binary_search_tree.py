class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def Insert(root_value, new_value):
    if root_value==None:
        return Node(new_value)
    if root_value.value < new_value:
        root_value.right=Insert(root_value.right, new_value)
    else:
        root_value.left=Insert(root_value.left, new_value)
    return root_value
tree=None

for i in range (5):
    value=int(input("Enter values you want to add:"))
    tree=Insert(tree,value)

def Pre_t(root):
    print(root.value)
    if root.left!=None:
        Pre_t(root.left)
    if root.right!=None:
        Pre_t(root.right)
    
def Post_t(root):
    if root.left!=None:
        Post_t(root.left)
    if root.right!=None:
        Post_t(root.right)
    print(root.value)

def In_t(root):
    if root.left!=None:
        In_t(root.left)
    print(root.value)
    if root.right!=None:
        In_t(root.right)

Pre_t(tree)
Post_t(tree)
In_t(tree)

def Search(root, value):
    if root.value<value and root.right!=None:
        return Search(root.right, value)
    elif root.value>value and root.left!=None:
        return Search(root.left, value)
    elif root.value==value:
        return True
    else:
        return False

find_value=int(input("Search for a value:"))

print(Search(tree, find_value ))

def Successor(root):
    successor=root.right
    while successor.left!=None:
        successor=root.left
    return successor

def Delete(root, value):
    if root==None:
        return root
    if value>root.value:
        root.right=Delete(root.right, value)
    elif value<root.value:
        root.left=Delete(root.left, value)
    else:
        if root.left==None:
            return root.right
        if root.right==None:
            return root.left
        temp=Successor(root)
        root.value=temp.value
        root.right=Delete(root.right, temp.value)
    return root

delete_value=int(input("Which value to delete:"))
print(Delete(tree,delete_value))

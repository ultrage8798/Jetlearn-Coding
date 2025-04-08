class TN:
    def __init__ (self,k):
        self.data = x
        self.lchild = None
        self.rchild = None

def IOT(root):
        if root is not None:
            if root.lchild is not None:
                IOT(root.lchild)
            print(root.data)
            if root.rchild is not None:
                IOT(root.rchild)

def Insert(root,k):
        if root == None:
            return TN(k)
        if root.data > k:
            root.lchild = Insert(root.lchild, k)
        else:
            root.rchild = Insert(root.rchild, k)
        return root
    
def Search(root,key):
    if root.data == key:
        return root
    elif root.data > key and root.lchild is not None:
        return Search(root.lchild, key)
    elif root.data < key and root.rchild is not None:
         return Search(root.rchild, key)
    else:
         return -1
    
n = int(input("Enter the number of elements you want in the tre - "))
root = None
for i in range(n):
    x=int(input("Enter the node value - "))
    root = Insert(root,x)

IOT(root)

key = int(input("Enter the key to be searched -"))
keyNode = Search(root,key)

if keyNode == -1:
     print("Key does not exist in the tree.")
else:
    print("Key exists", keyNode.data)

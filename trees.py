class TN:
    def __init__(self,data):
        self.data = data
        self.lnode = None
        self.rnode = None

def IT(root):
    if root.lnode != None:
        IT(root.lnode)
    print(root.data)
    if root.rnode != None:
        IT(root.rnode)

def PET(root):
    print(root.data)
    if root.lnode != None:
        PET(root.lnode)
    if root.rnode != None:
        PET(root.rnode)

def POT(root):
    if root.lnode != None:
        POT(root.lnode)
    if root.rnode != None:
        POT(root.rnode)
    print(root.data)

root = TN(5)
root.lnode = TN(4)
root.lnode.lnode = TN(2)

root.rnode = TN(8)
root.rnode.lnode = TN(7)
root.rnode.rnode = TN(9)

IT(root)
PET(root)
POT(root)
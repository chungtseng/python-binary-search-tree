# lets do binary search trees in python
# example taken from derek banas' java bst tutorial

class Node:
    def __init__(self, key, name):
        self.name = name
        self.key = key
        self.leftChild = None
        self.rightChild = None
        
    def printData(self):
        print(self.name + " has a key " + str(self.key))

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def addNode(self, key, name):
        newNode = Node(key, name)
        if self.root == None:
            self.root = newNode
        else:
            focusNode = self.root
            while(True):
                parent = focusNode

                # left branch
                if key < focusNode.key:
                    focusNode = focusNode.leftChild
                    if focusNode == None:
                        parent.leftChild = newNode
                        return
                # right branch
                else:
                    focusNode = focusNode.rightChild
                    if focusNode == None:
                        parent.rightChild = newNode
                        return

    def inOrderTraverseTree(self, focusNode):
        if focusNode != None:
            self.inOrderTraverseTree(focusNode.leftChild)
            focusNode.printData()
            self.inOrderTraverseTree(focusNode.rightChild)

    def preOrderTraverseTree(self, focusNode):
        if focusNode != None:
            focusNode.printData()
            self.preOrderTraverseTree(focusNode.leftChild)
            self.preOrderTraverseTree(focusNode.rightChild)

    def postOrderTraverseTree(self, focusNode):
        if focusNode != None:
            self.postOrderTraverseTree(focusNode.leftChild)
            self.postOrderTraverseTree(focusNode.rightChild)
            focusNode.printData()

    def findNode(self, key):
        focusNode = self.root
        while focusNode.key != key:
            if key < focusNode.key:
                focusNode = focusNode.leftChild
            else:
                focusNode = focusNode.rightChild
            if focusNode == None:
                return None
        focusNode.printData()

    def deleteNode(self, key):

if __name__ == "__main__":
    b = BinarySearchTree()
    b.addNode(50, "Boss")
    b.addNode(25, "VP")
    b.addNode(15, "Office Manager")
    b.addNode(30, "Secretary")
    b.addNode(75, "Sales Manager")

    print("--- In order")
    b.inOrderTraverseTree(b.root)
    print("--- Pre order")
    b.preOrderTraverseTree(b.root)
    print("--- Post order")
    b.postOrderTraverseTree(b.root)

    print("--- Find node 30")
    b.findNode(30)

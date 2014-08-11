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

    def removeNode(self, key):
        focusNode = self.root
        parent = self.root
        isLeftChild = True
        while(focusNode.key != key):
            parent = focusNode

            # go left
            if(key < focusNode.key):
                isLeftChild = True
                focusNode = focusNode.leftChild
            # go right
            else:
                isLeftChild = False
                focusNode = focusNode.rightChild

            if(focusNode == None):
                return False

        if focusNode.leftChild == None and focusNode.rightChild == None:
            if focusNode == self.root:
                self.root = None
            elif isLeftChild:
                parent.leftChild = None
            else:
                parent.rightChild = None

        # no right child
        elif focusNode.rightChild == None:
            if focusNode == self.root:
                root  = focusNode.leftChild
            elif isLeftChild:
                parent.leftChild = focusNode.leftChild
            else:
                parent.rightChild = focusNode.leftChild

        # no left child
        elif focusNode.leftChild == None:
            if focusNode == self.root:
                root = focusNode.rightChild
            elif isLeftchild:
                parent.leftChild = focusNode.rightCHild
            else:
                parent.rightChild = focusNode.rightChild

        else:
            replacement = getReplacementNode(focusNode)
            if focusNode == self.root:
                root = replacement
            elif isLeftChild:
                parent.leftChild = replacement
            else:
                parent.rightChild = replacement
            replacement.leftchild = focusNode.leftChild

        return True

    def getReplacementNode(self, replacedNode):
        replacementParent = replacedNode
        replacement = replacedNode
        focusNode = replacedNode.rightChild

        # move nodes
        while(focusNode != None):
            replacementParent = replacement
            replacement = focusNode
            focusNode = focusNode.leftChild

        if replacement != replacedNode.rightChild:
            replacementParent.leftChild = replacement.rightChild
            replacement.rightChild = replacedNode.rightChild

        return replacement
            

if __name__ == "__main__":
    b = BinarySearchTree()
    b.addNode(50, "Boss")
    b.addNode(25, "VP")
    b.addNode(15, "Office Manager")
    b.addNode(30, "Secretary")
    b.addNode(75, "Sales Manager")
    b.addNode(150, "To be deleted")

    print("--- In order")
    b.inOrderTraverseTree(b.root)
    print("--- Pre order")
    b.preOrderTraverseTree(b.root)
    print("--- Post order")
    b.postOrderTraverseTree(b.root)

    print("--- Find node 30")
    b.findNode(30)

    print("--- Remove key 150")
    b.removeNode(150)

    print("--- In order")
    b.inOrderTraverseTree(b.root)

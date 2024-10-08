class binaryTree:
    def __init__(self,key, leftTree= None, rightTree= None):
        self.key= key
        self.leftTree= leftTree
        self.rightTree= rightTree

    def setKey(self, key):
        self.key= key

    def getKey(self):
        return self.key

    def getLeftTree(self):
        return self.leftTree

    def getRightTree(self):
        return self.rightTree

    def insertLeft(self, key):
        if self.leftTree== None:
            self.leftTree= binaryTree(key)
        else:
            t =binaryTree(key)
            self.leftTree, t.leftTree= t, self.leftTree

    def insertRight(self, key):
        if self.rightTree== None:
            self.rightTree= binaryTree(key)
        else:
            t =binaryTree(key)
            self.rightTree, t.rightTree= t, self.rightTree

    def printInorder(self, level):
        if self.leftTree!= None:
            self.leftTree.printInorder(level+1) #left
        print( str(level*'=') + str(self.key)) #root
        if self.rightTree!= None:
            self.rightTree.printInorder(level+1) #right
            
    def printPreorder(self, level):
        print( str(level*'=') + str(self.key))
        if self.leftTree!= None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree!= None:
            self.rightTree.printPreorder(level+1)    
        
    def printPostorder(self, level):
        if self.leftTree!= None:
            self.leftTree.printPostorder(level+1)
        if self.rightTree!= None:
            self.rightTree.printPostorder(level+1) 
        print( str(level*'=') + str(self.key))   
        

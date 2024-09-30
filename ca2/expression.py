class Node:
    # Constructor
    def __init__(self):
        self.nextNode = None
        
class Expression(Node):
    def __init__(self, expression):
        self.expression = expression
        super().__init__() # creation of self.nextNode
        
    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.expression == otherNode.expression

    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'Expression' and 'NoneType'")
        
        if len(self.expression) < len(otherNode.expression): # compare by length
            return True
        elif len(self.expression) > len(otherNode.expression):
            return False
        else: # self.expression == otherNode.expression
            return self.expression < otherNode.expression # compare by alphabetical order 

    def __str__(self):
        s= f"'{self.expression}'"
        return s
# import statements
import re
from stack import Stack
from binary import binaryTree

#-----------------parse tree--------------------------
class parseTree:

    def buildParseTree(self, exp): #exp must be a string

        exp = exp.replace(" ","") # remove unneccessary spaces

        number_or_symbol =  re.compile(r'([-]\d+[.]\d+|\d+[.]\d+|[-]\d+|[//]+|[%]|[**]+|[()+*/-]|\d+|[..]+)')
        tokens = re.findall(number_or_symbol, exp)

        for i in range(len(tokens)): #check if - is -ve or minus
            if(tokens[i].find("-") == 0): #position of - is first eg -32 is True but 3-2 is false
                if tokens[i-1] not in ['(','+','-','*','/','**', '%', '//'] and (i != 0) and (len(tokens[i])!=1):
                    a = re.compile(r'([-]+|\d+[.]\d+|\d+)') #search for 
                    b = re.findall(a, tokens[i])
                    tokens.pop(i)
                    tokens.insert(i, b[0])
                    tokens.insert(i+1, b[1])

        stack = Stack()
        binary = binaryTree('?') #insert as ? first

        stack.push(binary)
        currentTree= binary

        for t in range(len(tokens)): #use for loop to get each tokens
            if len(re.findall(r'[()]',str(tokens))) < len(re.findall(r'[//]+|[%]|[**]+|[+*/-]',str(tokens))) and re.findall(r'[-]\d+|[-]\d+[.]\d+',str(tokens)) == [] :
                print("Operators should not be more than brackets")
                break

            elif tokens[t-1] in ['+', '-', '*', '**', '/', '%', '//'] and tokens[t+1] in  ['+', '-', '*', '**', '/', '%', '//'] and tokens[t] not in ['+', '-', '*', '**', '/', '%', '//','(',')']:
                print("Expression must be fully parenthesized") #(2+3--2)
                break

            elif len(tokens) == 3: # eg (0) or (553)
                if len(tokens[t+1]) > 2: #eg '///' in (///)
                    if tokens[t+1] not in ['-','+','*','**','/','//','%'] and re.findall(r'[*/]|[.]',str(tokens[t+1])) == []:
                        if tokens[t+1].isnumeric() == True:
                            currentTree.setKey(int(tokens[1]))
                            print(currentTree.getKey()) 
                            break

                        else:
                            currentTree.setKey(float(tokens[1]))
                            print(currentTree.getKey()) 
                            break

                    elif tokens[t+1] not in ['-','+','*','**','/','//','%'] and re.findall(r'[*/]',str(tokens[t+1])) == [] and re.findall(r'\d+[.]\d+|[-]\d+[.]\d+',str(tokens)) != []: #(-0.3)
                        currentTree.setKey(float(tokens[1]))
                        print(currentTree.getKey()) 
                        break

                    else:
                        print("Please check your decimal point or operator (**, //)")
                        break

                elif tokens[t+1] in ['-','+','/','//','*','**','.']: #for '(+)'
                    print("Please continue with a number after bracket")
                    break

                else:
                    if tokens[t].isnumeric() == True:
                        currentTree.setKey(int(tokens[1]))
                        print(currentTree.getKey()) 
                        break

                    else:
                        currentTree.setKey(float(tokens[1]))
                        print(currentTree.getKey()) 
                        break

            elif tokens[t] == '(':
                if t != 0: #not start of the exp
                    if tokens[t-1] == ')' and tokens[t+1].isnumeric() == True:
                        currentTree.setKey(int(tokens[t+1])) 

                    elif tokens[t+1] not in ['+','-','*','**','/', '%', '//','('] and tokens[t+2] not in ['+','-','*','**','/', '%', '//','(']:
                        if tokens[t+1].isnumeric() == True:
                            currentTree.setKey(int(tokens[t+1]))


                        else:
                            currentTree.setKey(float(tokens[t+1])) 
                    elif tokens[t+1] in ['-'] : #(10-(-(2+3)))
                        currentTree.setKey(tokens[t+1])

                    elif tokens[t-2] in [')'] and tokens[t-1] not in ['+', '-', '*', '**', '/', '%', '//','(',')']:
                        print("Number should not be in between )(") #(3-3)3(-2+3)
                        break

                    else:
                        currentTree.insertLeft('?')
                        stack.push(currentTree)
                        currentTree= currentTree.getLeftTree()

                elif tokens[t+1].isnumeric() == True: #if int, no -ve or float
                    currentTree.insertLeft('?')
                    stack.push(currentTree)
                    currentTree= currentTree.getLeftTree()

                else:
                    if tokens[t+1].startswith('-'): #check for -
                        if re.findall(r'([-]\d+|[-]\d+[.]\d+)',tokens[t+1]) == []: #- is [] but -2 is ['-2']
                            if len(tokens[t+1]) == 1:
                                print("Left side of expression cannot be empty")
                                break

                            else:
                                currentTree.setKey(float(tokens[t+1]))

                        else:
                            if tokens[t+2] not in ['+','-','*','**','/', '%', '//','.']:
                                currentTree.setKey(int(tokens[t+1]))

                            else:
                                currentTree.insertLeft('?')
                                stack.push(currentTree)
                                currentTree= currentTree.getLeftTree()

                    elif tokens[t+1] not in ['+', '-', '*', '**', '/', '%', '//', ')','.'] : #eg /// will enter here
                        if len(tokens[t+1]) > 2 and re.findall(r'\d+[.]\d+',str(tokens)) == []: #for '(***9)' n don't let decimal enter
                            print("Please check your decimal point or operator (**, //)")
                            break

                        else:
                            currentTree.insertLeft('?')
                            stack.push(currentTree)
                            currentTree= currentTree.getLeftTree()
                            
                    else: #+ve float
                        currentTree.insertLeft('?')
                        stack.push(currentTree)
                        currentTree= currentTree.getLeftTree()
                
            # If token is operator set key of current node to that operator and add a new node as right child and descend into that node
            elif tokens[t] in ['+', '-', '*', '**', '/', '%', '//']:
                try:
                    currentTree.setKey(tokens[t])
                    currentTree.insertRight('?')
                    stack.push(currentTree)
                    currentTree= currentTree.getRightTree()

                except (ValueError, AttributeError):
                    print("Unable to built parse tree")
                    break
                    
            # If token is number
            elif tokens[t] not in ['+', '-', '*', '**', '/', '%', '//', ')','.'] :
                if len(tokens[t+1]) > 2: #for '8***9'
                    print("Please check your decimal point or operator (**, //)")
                    break

                elif tokens[-2] in ['+', '-', '*', '**', '/', '%', '//'] and tokens[-1] in [')']:
                    print("Please do not end your expression with operators")
                    break

                elif tokens[t-1] not in ['+', '-', '*', '**', '/', '%', '//'] and tokens[t+1] not in ['+', '-', '*', '**', '/', '%', '//'] and tokens[t] != '..': 
                    if tokens[t].isnumeric() == True:
                        currentTree.setKey(int(tokens[t]))
                        parent = stack.pop()
                        currentTree= parent

                    else:
                        currentTree.setKey(float(tokens[t]))
                        parent = stack.pop()
                        currentTree= parent

                elif tokens[t-1] in ['+', '-', '*', '**', '/', '%', '//'] and tokens[t+1] in ['(',')']:
                    if tokens[t].isnumeric() == True:
                        currentTree.setKey(int(tokens[t]))
                        parent = stack.pop()
                        currentTree= parent

                    else:
                        currentTree.setKey(float(tokens[t]))
                        parent = stack.pop()
                        currentTree= parent

                elif tokens[t-1] in ['(',')'] and tokens[t+1] in ['+', '-', '*', '**', '/', '%', '//'] and tokens[t+2] not in ['+', '-', '*', '**', '/', '%', '//'] and re.findall(r'\d+[.]\d+',str(tokens)) != []: #don't allow eg (3-..) to crash
                    if tokens[t].isnumeric() == True:
                        currentTree.setKey(int(tokens[t]))
                        parent = stack.pop()
                        currentTree= parent

                    else:
                        currentTree.setKey(float(tokens[t]))
                        parent = stack.pop()
                        currentTree= parent

                elif tokens[t-1] in ['(',')'] and tokens[t+1] in ['+', '-', '*', '**', '/', '%', '//'] and tokens[t+2] not in ['+', '-', '*', '**', '/', '%', '//'] and re.findall(r'[.]+',str(tokens)) == []: #allow eg 4*4 to work
                    if tokens[t].isnumeric() == True:
                        currentTree.setKey(int(tokens[t]))
                        parent = stack.pop()
                        currentTree= parent

                    else:
                        currentTree.setKey(float(tokens[t]))
                        parent = stack.pop()
                        currentTree= parent

                elif tokens[t-1] in ['(',')'] and tokens[t+1] in ['+', '-', '*', '**', '/', '%', '//'] and tokens[t+2] == '-' :
                    if tokens[t].isnumeric() == True:
                        currentTree.setKey(int(tokens[t]))
                        parent = stack.pop()
                        currentTree= parent

                    else:
                        currentTree.setKey(float(tokens[t]))
                        parent = stack.pop()
                        currentTree= parent

                else: #other errs that did not satisfy above
                    print("Please do not put so many operator/brackets/decimal point consecutively")
                    break
                    
            elif tokens[t] == ')' and t < len(tokens)-1: #for (3)(2)
                if tokens[t+1] == '(':
                    currentTree.setKey(str('*'))
                    currentTree.insertRight('?')
                    stack.push(currentTree)
                    currentTree= currentTree.getRightTree()

                elif tokens[t+1] in ['+','-','*','//','/','%','**']: 
                    currentTree= stack.pop()
                    
                elif tokens[t] == ')': #if normal exp just pop
                    currentTree = stack.pop()

                else:
                    print("Unable to evaluate")
                    break

            # If token is ')' go to parent of current node
            elif tokens[t] == ')':
                currentTree= stack.pop()

            else:
                print("Please check your expression is correct such as decimal points")
                break

        return binary

    def evaluate(self,binary): #tree has to be a valid parse tree
        leftTree= binary.getLeftTree()
        rightTree= binary.getRightTree()
        op = binary.getKey()

        if leftTree!= None and rightTree!= None:
            if op == '+':
                return self.evaluate(leftTree) + self.evaluate(rightTree)

            elif op == '-':
                return self.evaluate(leftTree) - self.evaluate(rightTree)

            elif op == '*':
                return self.evaluate(leftTree) * self.evaluate(rightTree)

            elif op == '**':
                return self.evaluate(leftTree) ** self.evaluate(rightTree)

            elif op == '/':
                if rightTree.getKey() == int(0):
                    return 'Cannot divide by zero'

                else:
                    return self.evaluate(leftTree) / self.evaluate(rightTree)

            elif op == '%':
                if rightTree.getKey() == int(0):
                    return 'Cannot modulo by zero'

                else:
                    return self.evaluate(leftTree) % self.evaluate(rightTree)

            elif op == '//':
                if rightTree.getKey() == int(0):
                    return 'Cannot floor division by zero'

                else:
                    return self.evaluate(leftTree) // self.evaluate(rightTree)

        else:
            if binary.getKey() == '?': #for part2
                return None

            else:
                return binary.getKey()
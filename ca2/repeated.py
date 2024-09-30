# import statements
from pte import parseTree

class Repeated:

    def checkBracket(self, myStr): # check for bracket of exp

        openBracket = ["[","{","("] # put other 2 bracket in case wanna do extra feature
        closeBracket = ["]","}",")"]
        check= []

        for i in range(len(myStr)):
            if myStr[0] not in openBracket: # first bracket
                return "fbrac"

            if myStr[-1] not in closeBracket: # last bracket
                return "lbrac"

            if myStr[i] in openBracket:
                check.append(myStr[i])

            elif myStr[i] in closeBracket:
                pos = closeBracket.index(myStr[i])
                if ((len(check) > 0) and (openBracket[pos] == check[len(check)-1])):
                    check.pop()

                else:
                    return "Unbalanced" # if number of open brackets != number of close brackets

        if len(check) == 0:
            return "Balanced" # if number of open brackets = number of close brackets

    def success(self, choiceOne): #after user successfully input exp

        parse = parseTree()
        binary = parse.buildParseTree(choiceOne)

        #catch for crashed err msg
        try: 
            parse.evaluate(binary)
        except TypeError:
            print('Unable to evaluate. Please check your expression and try again')
            print("\nPress enter key, to continue....")
            input() # press enter can alr
            return 

        if (parse.evaluate(binary) in ['?','-','**','/','+','*','(',')','//', None]):
            print('Unable to evaluate.Please check your expression and try again')
            print("\nPress enter key, to continue....")
            input() # press enter can alr
            return

        else:
            order = input("Enter [a/A] for Inorder, [b/B] for Preorder, or [c/C] for Postorder:") # choose to print preorder, inorder, postorder 

            if order == "a" or order == "A": # if inorder
                print("\nExpression Tree:")
                binary.printInorder(0)
                print("\nExpression evaluates to:")
                print(parse.evaluate(binary))
                print("\nPress enter key, to continue....")
                input() # press enter can alr
                return

            elif order == "b" or order == "B": # if preorder
                print("\nExpression Tree:")
                binary.printPreorder(0)
                print("\nExpression evaluates to:")
                print(parse.evaluate(binary))
                print("\nPress enter key, to continue....")
                input() # press enter can alr
                return
            
            elif order == "c" or order == "C": # if postorder
                print("\nExpression Tree:")
                binary.printPostorder(0)
                print("\nExpression evaluates to:")
                print(parse.evaluate(binary))
                print("\nPress enter key, to continue....")
                input() # press enter can alr
                return
            
            else: # if not preorder, inorder or postorder
                print("\nPlease try again\n")
                return

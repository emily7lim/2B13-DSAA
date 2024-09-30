# import statements
from expression import Expression
from pte import parseTree

class openFiles:

    def readInputFile(self, iList):
        allList = [] # main array
        parse = parseTree()

        for exp in iList: # check expressions line by line
            expList = []
            tree = parse.buildParseTree(exp) # build parse tree
            if tree.getKey() == "?": # if key = ?
                return print("\nERROR!") # err msg

            else:
                expList.append(parse.evaluate(tree)) # evaluate tree
                expList.append(Expression(exp)) # [ VALUE, EXPRESSION ]
                allList.append(expList) # [ [ VALUE, EXPRESSION ], [ VALUE, EXPRESSION ] ]
                expList = []

        return allList


    def readOutputFile(self, allList, choiceOutput):
        outputFile = open(choiceOutput, 'w') # write  a new file / overwrite existing file
        valueList = [] 
        index = 0
        
        for exps in allList:
            valueList.append(exps[0])
            if len(valueList) <= 1:
                outputFile.write("*** Expressions with value => {}\n".format(exps[0]))
                outputFile.write("{} ==> {}\n".format(exps[1].expression, exps[0]))
                index += 1

            elif valueList[index] == valueList[index-1]:
                outputFile.write("{} ==> {}\n".format(exps[1].expression, exps[0]))
                index += 1

            else:
                outputFile.write("\n*** Expressions with value => {}\n".format(exps[0]))
                outputFile.write("{} ==> {}\n".format(exps[1].expression, exps[0]))
                index += 1
                
        outputFile.close()

        return outputFile 

# import statements
from files import openFiles

class Sorting:
    
    def mergeSortAscending(self, l): # sort in ascending order 
        if len(l) > 1:
            mid = int (len(l)/2)
            leftHalf = l[:mid]
            rightHalf = l[mid:]

            self.mergeSortAscending(leftHalf)
            self.mergeSortAscending(rightHalf)

            leftIndex,rightIndex,mergeIndex = 0,0,0

            mergeList = l
            while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
                if leftHalf[leftIndex] < rightHalf[rightIndex]:
                    mergeList[mergeIndex] = leftHalf[leftIndex]
                    leftIndex+=1
                else:
                    mergeList[mergeIndex] = rightHalf[rightIndex]
                    rightIndex+=1
                mergeIndex+=1

            # Handle those items still left in the left Half
            while leftIndex < len(leftHalf):
                mergeList[mergeIndex] = leftHalf[leftIndex]
                leftIndex+=1
                mergeIndex+=1
            # Handle those items still left in the right Half
            while rightIndex < len(rightHalf):
                mergeList[mergeIndex] = rightHalf[rightIndex]
                rightIndex+=1
                mergeIndex+=1
            # print('merge', l) 

    def mergeSortDescending(self, l): # sort in descending order
        if len(l) > 1:
            mid = int (len(l)/2)
            leftHalf = l[:mid]
            rightHalf = l[mid:]

            self.mergeSortDescending(leftHalf)
            self.mergeSortDescending(rightHalf)

            leftIndex,rightIndex,mergeIndex = 0,0,0

            mergeList = l
            while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
                if leftHalf[leftIndex] > rightHalf[rightIndex]:
                    mergeList[mergeIndex] = leftHalf[leftIndex]
                    leftIndex+=1
                else:
                    mergeList[mergeIndex] = rightHalf[rightIndex]
                    rightIndex+=1
                mergeIndex+=1

            # Handle those items still left in the left Half
            while leftIndex < len(leftHalf):
                mergeList[mergeIndex] = leftHalf[leftIndex]
                leftIndex+=1
                mergeIndex+=1
            # Handle those items still left in the right Half
            while rightIndex < len(rightHalf):
                mergeList[mergeIndex] = rightHalf[rightIndex]
                rightIndex+=1
                mergeIndex+=1
            # print('merge', l)

    def evalAndSort(self, iList, choiceOutput): # evaluate and sort the expressions
        allList = openFiles().readInputFile(iList) # reading the input file

        if allList == None: # if any of the evaluated value = None
            print("\nPlease check the expressions in your input file again.\n")
            return 

        else:
            xList = []
            for x in allList:
                if x[0] == None: # if any of the evaluated value = None & shows the expression where they face this error
                    print(x[1], "--> Please check the expressions in your input file again.\n")
                    return 

                else:
                    xList.append(x)

            order = input("\nEnter [a/A] to sort in ascending order, or [b/B] to sort in descending order: ") # allow user to choose to sort in ascending or descending order

            if order == 'a' or order == 'A': # if choose to sort in ascending order
                self.mergeSortAscending(xList) 
                openFiles().readOutputFile(xList, choiceOutput) # print out the outputs into the output file 

            elif order == 'b' or order == 'B': # if choose to sort in descending order
                self.mergeSortDescending(xList)
                openFiles().readOutputFile(xList, choiceOutput) # print out the outputs into the output file

            else:  # if did not choose whether to sort in ascending or descending
                print("\nUnable to do sorting. Please try again.\n")
                print("Press enter key, to continue....")
                input() # press enter can alr
                return

            print("\n>>> Evaluating and sorting started:\n") # display the details in the output file onto the terminal

            output = open(choiceOutput, 'r') # open the output file
            outputContent = output.read() # read the contents of the output file
            print(outputContent) # prints the contents of the output file into the terminal
            output.close() # close output file

            print("\nPress enter key, to continue....")
            input() # press enter can alr
            return
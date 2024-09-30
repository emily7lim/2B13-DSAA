# RUN THIS FILE FOR MAIN PROGRAM

# import statements
import re
import os
from sorting import Sorting
from repeated import Repeated

# prints the introduction, with our names, ids, class & module code & name
def introduction():
    intro = "*" * 56 + "\n"
    intro += "* ST107 DSAA: Expression Evaluator & Sorter" + " " * 12 + "*" + "\n"
    intro += "*" + "-" * 54 + "*" + "\n"
    intro += "*" + " " * 54 + "*" + "\n"
    intro += "*  - Done by: Khairunnurrin(1922459) & Emily(1936207)  *" + "\n"
    intro += "*  - Class DIT/FT/2B/13" + " " * 32 + "*" + "\n"
    intro += "*" * 56 + "\n"
    print(intro)
    
# prints out the choice (1, 2, or 3)
def choice():
    menu = "Please select your choice ('1','2','3'):"
    menu += "\n\t1. Evaluate expression\n\t2. Sort expressions\n\t3. Exit"
    menu += "\nEnter choice: "

    sort = Sorting() # call the sorting function
    repeat = Repeated() # call the repeated function

    choiceSelected = False

    while not choiceSelected:
        userChoice = input(menu)

        if userChoice == "1": # if user chooses choice 1

            choiceOne = input("Please enter the expression you want to evaluate:\n")
            choiceOne = choiceOne.replace(" ","") # clears unnecessary empty spaces

            if re.findall(r'[a-zA-Z!@#$^`&_=\[\]{};\'\"\\|,<>?]+',choiceOne) != []: # if weird input straight away don't evaluate, remove []{} if wanna do extra feature
                print("\nExpression should not have alphabet or special characters") # check for special characters
                print("\nPress enter key, to continue....")
                input() # press enter can alr
                return choice()

            elif re.findall(r'[//]+|[%]|[**]+|[+*/-]',choiceOne) == []: #(3)2(3)
                if ')(' in choiceOne:
                    repeat.success(choiceOne)

                else:
                    print("Expression must have operators") # check for no operators
                    print("\nPress enter key, to continue....")
                    input() # press enter can alr
                    return choice() 

            elif choiceOne[0] != "(" and choiceOne[-1] != ")": #eg 2+3
                choiceOne = '(' + choiceOne 
                choiceOne = choiceOne + ')'
                repeat.success(choiceOne) 

            elif repeat.checkBracket(choiceOne) == "fbrac": # check for first bracket
                print("\nExpression should start with a ( bracket")
                print("\nPress enter key, to continue....")
                input() # press enter can alr
                return choice()
                
            elif repeat.checkBracket(choiceOne) == "lbrac": # check for last bracket
                print("\nExpression should end with a ) bracket")
                print("\nPress enter key, to continue....")
                input() # press enter can alr
                return choice()
                
            elif repeat.checkBracket(choiceOne) == "Balanced": # if the number of open brackets = number of close brackets
                repeat.success(choiceOne)

            else:
                print("\nPlease check your brackets\n") # if missing brackets in any part of the expression
                print("Press enter key, to continue....")
                input() # press enter can alr
                return choice()

        elif userChoice == "2": # if user chooses choice 2

            choiceInput = input("\nPlease enter the input file: ") # gets user's input for their chosen input file

            if choiceInput == "": # if input for input file is empty
                print("\nInvalid input. Please enter an input file.\n")
                print("Press enter key, to continue....")
                input() # press enter can alr
                return choice()

            elif not choiceInput.endswith(".txt"): # if input file does not end with a .txt
                print("\nInvalid input. File name must end with .txt\n")
                print("Press enter key, to continue....")
                input() # press enter can alr
                return choice()
               
            else:
                if os.path.isfile(choiceInput): # if input file ends with a .txt and exists 

                    choiceOutput = input("Please enter output file: ") # get user's input for their chosen output file

                    if choiceOutput == "": # if input for output file is empty
                        print("\nInvalid input. Please enter an output file.\n")
                        print("Press enter key, to continue....")
                        input() # press enter can alr
                        return choice()

                    elif not choiceOutput.endswith(".txt"): # if output file does not end with a .txt
                        print("\nInvalid input. File name must end with .txt\n")
                        print("Press enter key, to continue....")
                        input() # press enter can alr
                        return choice()

                    else:
                        if os.path.isfile(choiceOutput): # if output file ends with a .txt and exists

                            if os.stat(choiceInput).st_size == 0: # if the existing input file contains nothing (empty text file)
                                print("\nInput file is empty! Please try again.\n")
                                return choice()

                            else:
                                choiceInput = open(choiceInput, 'r') # read input file 

                                iList = []
                                for i in choiceInput: # read expressions in input file line by line
                                    i = i.replace("\n", "")
                                    i = i.replace(" ", "")
                                    if re.findall(r'[a-zA-Z!@#$^&_=\[\]{};\'\"\\|,<>?]+',i) != []: #if weird input straight away don't evaluate, remove []{} if wanna do extra feature
                                        print("\nExpression should not have alphabet or special characters. Please check the expressions in your input file again.")
                                        print("\nPress enter key, to continue....")
                                        input() # press enter can alr
                                        return choice()

                                    elif re.findall(r'[//]+|[%]|[**]+|[+*/-]',i) == []: #(3)2(3)
                                        if ')(' in i:
                                            iList.append(i)

                                        else:
                                            print("Expression must have operators. Please check the expressions in your input file again.") # check for operators
                                            print("\nPress enter key, to continue....")
                                            input() # press enter can alr
                                            return choice()

                                    elif i[0] != "(" and i[-1] != ")": #eg 2+3
                                        i = '(' + i 
                                        i = i + ')'
                                        iList.append(i)

                                    elif repeat.checkBracket(i) == "fbrac": # check for first bracket
                                        print("\nExpression should start with a ( bracket. Please check the expressions in your input file again.")
                                        print("\nPress enter key, to continue....")
                                        input()
                                        return choice()

                                    elif repeat.checkBracket(i) == "lbrac": # check for last bracket
                                        print("\nExpression should end with a ) bracket. Please check the expressions in your input file again.")
                                        print("\nPress enter key, to continue....")
                                        input()
                                        return choice()

                                    elif repeat.checkBracket(i) == "Balanced": # if number of open brackets = number of close brackets
                                        iList.append(i)

                                    else:
                                        print("\nPlease check your brackets. Please check the expressions in your input file again.\n") # if missing brackets in any part of the expression
                                        print("Press enter key, to continue....")
                                        input()
                                        return choice()
                                
                                # since output file already exists, prompt user to pick whether to overwrite or not
                                reply = input("\nOutput file already exists. Overwrite this file? Enter [y/Y] for Yes, or [n/N] for No: ")

                                if reply == 'Y' or reply == 'y': # overwriting the file

                                    sort.evalAndSort(iList, choiceOutput) # sort and evaluate, displaying the output 

                                elif reply == 'N' or reply == 'n': # if user does not want to overwrite the existing output file
                                    print("\nPlease enter a different output file.\n")
                                    print("Press enter key, to continue....")
                                    input() # press enter can alr
                                    return choice()

                                else: # if user enters anything but 'y/Y' and 'n/N' (means don't know if want to overwrite or not)
                                    print("\nInvalid input. Unable to complete the task. Please try again.\n")
                                    print("Press enter key, to continue....")
                                    input() # press enter can alr
                                    return choice()
                                
                        else: # if output file ends with a .txt and does not exist

                            choiceInput = open(choiceInput, 'r') # read input file

                            iList = []
                            for i in choiceInput: # read expressions in input file line by line
                                i = i.replace("\n", "")
                                i = i.replace(" ", "")
                                if re.findall(r'[a-zA-Z!@#$^&_=\[\]{};\'\"\\|,<>?]+',i) != []: #if weird input straight away don't evaluate, remove []{} if wanna do extra feature
                                    print("\nExpression should not have alphabet or special characters. Please check the expressions in your input file again.")
                                    print("\nPress enter key, to continue....")
                                    input() # press enter can alr
                                    return choice()

                                elif re.findall(r'[//]+|[%]|[**]+|[+*/-]',i) == []: #(3)2(3)
                                    if ')(' in i:
                                        iList.append(i)

                                    else:
                                        print("Expression must have operators. Please check the expressions in your input file again.") # check for operators
                                        print("\nPress enter key, to continue....")
                                        input() # press enter can alr
                                        return choice()

                                elif i[0] != "(" and i[-1] != ")": #eg 2+3
                                    i = '(' + i 
                                    i = i + ')'
                                    iList.append(i)

                                elif repeat.checkBracket(i) == "fbrac": # check for first bracket
                                    print("\nExpression should start with a ( bracket. Please check the expressions in your input file again.")
                                    print("\nPress enter key, to continue....")
                                    input()
                                    return choice()

                                elif repeat.checkBracket(i) == "lbrac": # check for last bracket 
                                    print("\nExpression should end with a ) bracket. Please check the expressions in your input file again.")
                                    print("\nPress enter key, to continue....")
                                    input()
                                    return choice()

                                elif repeat.checkBracket(i) == "Balanced": # if number of open brackets = number of close brackets
                                    iList.append(i)

                                else:
                                    print("\nPlease check your brackets. Please check the expressions in your input file again.\n") # if missing brackets in any part of the expression
                                    print("Press enter key, to continue....")
                                    input()
                                    return choice()

                            sort.evalAndSort(iList, choiceOutput) # sort and evaluate, displaying the output
                      
                else: # if input file ends with a .txt but does not exist
                    print("\nInput file does not exist. Please try again.\n")
                    print("Press enter key, to continue....")
                    input() # press enter can alr
                    return choice()

        elif userChoice == "3": # if user chooses choice 3
            return print("\nBye, thanks for using ST107 DSAA: Expression Evaluator & Sorter")

        else: # if user enters anything but 1, 2 or 3
            # err msgs
            print("\nYou have entered an invalid input.\n")
            print("Press enter key, to continue....")
            input() # press enter can alr
            return choice()


# Main Program       
introduction()            
choice()
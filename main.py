# Brian Waldron
# G00350150
# Code adapted from Lab exercises

import shunting
import thompson

# os allows for file path manipulation
import os

# User enters directory of txt file
userPath = input("Please enter the directory path: ")
directory = os.listdir(userPath)
directoryPath = os.path.dirname(os.path.realpath(__file__))

# User enters the name of the txt file they wish to find an expression
txtFile = input("Please enter the full name of the text file: ")
txtFileName = os.path.isfile(txtFile)
print(txtFileName)

if txtFileName:
    expressionSearch = input("Please enter the expression: ")
    def expression_search(txtFileName, expressionSearch):
        lineNumber = 0
        results = []

        # "with" keyword used as txt file is properly closed after
        with open(txtFile, "r") as f:
            for line in f:
                lineNumber += 1
                if expressionSearch in line:
                    results.append((lineNumber, line.rstrip()))
        return results
    expressionsFound = expression_search(txtFileName, expressionSearch)
    print("Number of expressions found: ", len(expressionsFound))
    for elem in expressionsFound:
        print("Found on line: ", elem[0], " Expression: ", elem[1])
else:
    print("Sorry, " + txtFile + " does not exist in the directory given.")
    exit()

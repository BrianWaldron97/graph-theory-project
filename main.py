# Brian Waldron
# G00350150
# Code adapted from Lab exercises

import shunting
import thompson

# os allows for file path manipulation (os.path)
import os

# sys allows for runtime manipulation
#import sys

# User enters directory of txt file
userPath = input("Please enter the directory path: ")
directory = os.listdir(userPath)
directoryPath = os.path.dirname(os.path.realpath(__file__))

# User enters the name of the txt file they wish to find an expression
txtFile = input("Please enter the full name of the text file: ")
txtFileName = os.path.isfile(txtFile)

# if the text file is valid
if txtFileName:
    # User enters expression
    expressionSearch = input("Please enter the expression: ")

    # Expression Search function
    def expression_search(txtFileName, expressionSearch):
        # Initializing
        lineNumber = 0
        results = []

        # "with" keyword used as txt file is properly closed after
        with open(txtFile, "r") as f:
            for line in f:
                # Reading each line
                lineNumber += 1
                if expressionSearch in line:
                    # If the expression is found, append
                    results.append((lineNumber, line.rstrip())) # rstrip() removes trailing characters
        return results
    expressionsFound = expression_search(txtFileName, expressionSearch)
    # Prints the amount of expressions found in the text file
    print("Number of expressions found: ", len(expressionsFound))
    for num in expressionsFound:
        # for each num found in expressionFound, print the line number and full line
        print("Found on line: ", num[0], " Expression Line: ", num[1])
# else the text file given is invalid
else:
    print("Sorry, " + txtFile + " does not exist in the directory given.")
    exit()

# Testing 
print("\n========== Testing ==========\n")

if __name__ == "__main__":
    tests = [
        ["(a.b|b)", ["ab","b", "bb", "a"]],
        ["a.(b.b).a", ["aa","abba", "aba"]],
        ["1.(0.0)*.1", ["11","100001", "11001"]]
    ]

    for test in tests:
        infix = test[0]
        print(f"infix:      {infix}")
        postfix = shunting.shunt(infix)
        print(f"postfix:    {postfix}")
        nfa = thompson.re_to_nfa(postfix)
        print(f"thompson:   {nfa}")
        for s in test[1]:
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
        print()
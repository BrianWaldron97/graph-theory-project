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
                    results.append((lineNumber, line.rstrip())) # rstrip() removes trailing characters
        return results
    expressionsFound = expression_search(txtFileName, expressionSearch)
    print("Number of expressions found: ", len(expressionsFound))
    for elem in expressionsFound:
        print("Found on line: ", elem[0], " Expression: ", elem[1])
else:
    print("Sorry, " + txtFile + " does not exist in the directory given.")
    exit()


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


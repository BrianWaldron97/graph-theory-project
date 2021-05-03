# graph-theory-project
This is a Python 3 program that searches a text file using a regualr expression. The user is prompted for the text file directory location, followed by the text file name and lastly, the expression they are searching for. The line number and lines that have the expression in them are then output to the user.

## Description of Repository
The repository includes a .gitignore file, a README file, a text file containing “The adventures of Sherlock Holmes” taken from https://www.gutenberg.org/files/1661/1661.txt, an image folder containing the images of the output of the program, and lastly, the three python files needed to run the program, “main.py”, “shunting.py” and “thompson.py”.

## Instructions
1. Python 3 must be installed
2. Download or clone the git repository to your local machine
   * git clone https://github.com/BrianWaldron97/graph-theory-project.git
3. Once cloned, navigate into the graph-theory-project folder
   * cd graph-theory-project
4. Inside the folder you can now run the “main.py” file to start the program
   * python main.py
5. Once the program starts, you will be prompted to enter the directory path
6. You will then be asked to enter the full name of the text file
7. You will then be prompted to enter an expression
8. If the expression was found, the number of them found will be displayed along with the line they were found in and the full lines they were in also

#### Valid Output
![alt text](https://github.com/BrianWaldron97/graph-theory-project/blob/main/images/outputValid.PNG?raw=true)

#### Invalid Output
![alt text](https://github.com/BrianWaldron97/graph-theory-project/blob/main/images/outputInvalid.PNG?raw=true)

- - - -

### What is a regular expression?
A regular expression, also known as a regex, is a string of characters. This string of characters helps to “match” text when searching for patterns. The pattern can be something very simple or something complex. Something simple may include just one character. Certain characters have their own function, such as the '*' character. If the expression was "a*" for example, that would mean any number of a's in the pattern. There are many other characters with uses like this.

### How do regular expressions differ across implementation?
Regular expressions are implemented by compiling them into NFAs (nondeterministic finite automata). These NFAs are composed of different states of which they can transition between. Each transition may lead to any number of states.

### Can all formal languages be encoded as regular expressions?
Formal languages are mathematical constructions. They are not just used for programming languages but also many other things. One such use is in linguistics to describe the syntax of natural languages eg: English. For the case of English and Python, formal languages are a helpful system for describing both as they both have a similar structured format.
Formal languages can be seen as manipulators of symbols. For exmaple, the equation a + b + c = d has no real inherit meaning but it is possible to manipulate the symbols using the rules of algebra, eg: a + b = d - c, without knowing what the symbols even mean. Giving meaning to the symbols wihin system is known as semantics. If we interpreted the symbols a, b and c as currency, then the equation has meaning.

## Research
* https://docs.python.org/3/tutorial/inputoutput.html
  * Helped with understanding file input and output
* https://linuxhint.com/python_scripts_beginners_guide/
  * This page helped to easily understand the basics of python
* https://realpython.com/python-command-line-arguments/
  * This page was useful for understanding python command line arguments
* https://swtch.com/~rsc/regexp/regexp1.html
  * Helped with understanding and visualizing regular expression matching
* https://www.youtube.com/watch?v=sa-TUpSx1JA
  * Very useful for understanding regular expressions
* https://en.wikipedia.org/wiki/Regular_expression 
  * Helped in understanding regular expressions
* https://www.quora.com/How-are-regular-expressions-implemented
  * Implementation of regular expressions
* https://cs.stackexchange.com/questions/30639/what-is-the-relationship-between-programming-languages-regular-expressions-and#:~:text=In%20a%20nutshell&text=Regular%20expression%20and%20other%20formalisms,sentences%20in%20a%20structured%20way.
  * Information thread on the relationship between programming languages, formal languages and regular expressions

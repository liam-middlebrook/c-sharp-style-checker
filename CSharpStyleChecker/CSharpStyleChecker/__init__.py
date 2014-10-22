import argparse
import os
import re

base_dir = os.path.split(__file__)[0]

regex_egyptianbrace = re.compile(r'\w+.*\{\s*')

def styleCheck(fileContents, fileName):
    """
    Checks the content of fileName
    to see if it is 'valid' C# as
    far as a set of predefined
    standards goes
    """
    
    # Check for egyptian braces
    checkErrorWithRegex(fileContents, fileName, regex_egyptianbrace)

def checkErrorWithRegex(fileContents, fileName, regexCmd):
    """
    """
    regexMsg = regexCmd.findall(fileContents)
    if regexMsg:
        parsedLines = []
        for line in regexMsg:
            printWithLineNumber('001', fileName, line.rstrip(), parsedLines)

def printWithLineNumber(errorCode, fileName, line, parsedLines):
    """
    Takes an error code and a line
    prints out the error code
    with the line number and the
    content of the line in question
    """
    with open(fileName, 'r') as f:
        for num, text in enumerate(f):
	    if line in text and (num+1) not in parsedLines:
	        parsedLines.append(num+1)
		print "Error", errorCode, "on line:", (num+1), '| ', line
		break

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('file', nargs="+", help="File to be parsed")

    args = p.parse_args()

    with open(os.path.join(base_dir, args.file[0]), "r") as codeFile:
	styleCheck(codeFile.read(), args.file[0])


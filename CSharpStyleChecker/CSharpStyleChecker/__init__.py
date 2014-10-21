import argparse
import os
import re

base_dir = os.path.split(__file__)[0]

regex_egyptianbrace = re.compile(r'\w+.*\{\s*')

def styleCheck(fileText):
   """
   Checks the content of fileName
   to see if it is 'valid' C# as
   far as a set of predefined
   standards goes
   """

   regexMsg = regex_egyptianbrace.findall(fileText)
   if regexMsg:
       for line in regexMsg:
           print "Error 001! ", line

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('file', nargs="+", help="File to be parsed")

    args = p.parse_args()

    with open(os.path.join(base_dir, args.file[0]), "r") as codeFile:
	styleCheck(codeFile.read())


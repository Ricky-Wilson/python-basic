# Script Name	: check-file-exists.py
# Author		: Shailendra Patel
# Created		:
# Last Modified	:
# Version		:

# Description	: Read a file after checking if it exists.

import sys
import os

def readFile(filename):
    f = open(filename, 'r')
    line = f.read()
    print(line)

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]                           
        if not os.path.isfile(filename):
            print("File: ", filename, " Doesn't Exist.")
            print("Exiting....")
            exit(0)
        if not os.access(filename, os.R_OK):
            print("Access Denied For: ", filename, ". Please check permissions.")
            print("Exiting....")
            exit(0)
    elif len(sys.argv) > 2:
        print("Give only one argument.")
        print("Exiting....")
        exit(0)
    else:
        print("Specify filename.")
        print("Exiting....")
        exit(0)

    print("Reading from ", filename)
    readFile(filename)

if __name__ == "__main__":
    main()
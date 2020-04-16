#!/usr/bin/env python3

# footnotes.py
# A script to automate the replacement of Delafosse's original footnotes

import os, sys, re

# Save the filename by popping it off what was input via the command line
filename = sys.argv.pop()

# Create buffer for output
pageList = []
output = ""

# Store line number for error reporting
lineNumber = 0

with open(filename, 'r') as inputFile:
    print("Working on file: " + filename)
    
    # Make a list of everything
    inputList = inputFile.read().split("n")
    
    # Loop through it and make a list of only the page-paragraphs
    for line in inputList:
        
        if line.startswith("###"):
            continue
        elif line.starts("\n"):
            continue
        else:
            pageList += line
    
    for page in pageList:
        
        if         footnoteMatch = re.match(r"\s\d\.\s", line)

# Open an output file and write to it
    with open("output.txt", "w") as fileOut:
         fileOut.write(output)

print(">>>>>>> Done!")
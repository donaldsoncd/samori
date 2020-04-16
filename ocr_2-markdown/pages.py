#!/usr/bin/env python3

# pages.py
# A script to apply page numbers as markdown headers
# to the OCR'ed version of the Samori tale

import os, sys

# Save the filename by popping it off what was input via the command line
filename = sys.argv.pop()

# Create buffer for output
output = ""

# Store line number for error reporting
lineNumber = 0

# Store the first page number of the story
pageNumber = 147

with open(filename, 'r') as inputFile:
    print("Working on file: " + filename)
    
    # Make a list of the pages by stripping out blank lines first
    pageList = inputFile.read().replace("\n\n", "\n").splitlines()
    
    # Loop through them and format them in markdown with page numbers as headers
    for page in pageList:
        output += "### " + str(pageNumber) + "\n\n" + page + "\n\n"
        pageNumber += 1

# Open an output file and write to it
    with open("output.txt", "w") as fileOut:
         fileOut.write(output)

print(">>>>>>> Done!")
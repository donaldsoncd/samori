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
    
    pageNumber = 147
    
    # Loop through it and make a list of only the page-paragraphs
    for line in inputFile:
        if line.startswith("###"):
            continue
        elif line == "":
            continue
        else:
            pageList.append(line)
    
    # Loop through the list of page-paragraphs 
    for page in pageList:
        # Split it on the likely footnote marker
        pageParts = re.split("\s\d\.\s", page)
        
        # Output the page's text proper
        output += pageParts[0] + "\n\n"
        
        # Split off the footnote section of the page
        footNoteSection = pageParts[1:]
        
        footnoteNum = 1
        
        # Loop through the footnote section and output it in the new format
        for footnote in footNoteSection:
            output += "[^MD" + str(pageNumber) + "-" + str(footnoteNum) + "]: " + footnote + "\n\n"
            footnoteNum += 1
        
        pageNumber += 1
                
# Open an output file and write to it
    with open("output.txt", "w") as fileOut:
         fileOut.write(output)

print(">>>>>>> Done!")
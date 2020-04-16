#!/usr/bin/env python3

# footnotes.py
# A script to partially automate the replacement of Delafosse's original
# footnotes into the pandoc markdown format

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
    
    # Store the starting page
    pageNumber = 147
    
    # Loop through it and make a list of only the page-paragraphs
    for line in inputFile:
        if line.startswith("###"):
            continue
        elif line == "\n":
            continue
        else:
            pageList.append(line)
    
        
    # Loop through the list of page-paragraphs 
    for page in pageList:
        
        # Split it on the likely footnote marker
        pageParts = re.split("\s\d\.\s", page)
        
        # Split off the footnote section of the page
        footNoteSection = pageParts[1:]
        proseSection = pageParts[0]
        
        # Reinsert the markdown header
        output += "### " + str(pageNumber) + "\n\n"
        
        # Output the page's text proper with potential footnote marker's replaced
        # They are replaced with [^MDX] which can be searched for and edited manually
        output += proseSection.replace("'.", "[^MDX].").replace("*.", "[^MDX].") + "\n\n"
        
        # Loop through the footnote section and output it in the new format
        # That means something like: [^MD147-1] each on its own separate line
        footnoteNum = 1
        for footnote in footNoteSection[0:-1]:
            output += "[^MD" + str(pageNumber) + "-" + str(footnoteNum) + "]: " + footnote + "\n\n"
            footnoteNum += 1
        for footnote in footNoteSection[-1:]:
            output += "[^MD" + str(pageNumber) + "-" + str(footnoteNum) + "]: " + footnote + "\n"
            footnoteNum += 1
            
        # Increment page up by one
        pageNumber += 1
    
# Open an output file and write to it
    with open("output.md", "w") as fileOut:
         fileOut.write(output)

print(">>>>>>> Done!")
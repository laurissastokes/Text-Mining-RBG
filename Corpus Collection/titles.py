#This script searches through all text files in a folder and retrieves content between the html tags <title></title>.
#Example:
    #It it will find:
    #<title>Hemi Group, LLC v. City of New York, 559 U.S. 1, 130 S. Ct. 983, 175 L. Ed. 2d 943, 2010 U.S. LEXIS 768 – CourtListener.com</title>
    #And save it as:
    #Hemi Group, LLC v. City of New York, 559 U.S. 1, 130 S. Ct. 983, 175 L. Ed. 2d 943, 2010 U.S. LEXIS 768
#This script also saves the retrieved content to a file call "titles.txt" that resides in another folder.
#This script does not alter the content of the text files from which it searches and retrieves content.
#I used this for Courtlistener files specifically. But the same idea can be applied to any types of html tags in any of the documents.

import os
import re


path = '.'

for file in os.listdir(path):
    if file.endswith(".txt"):
        with open(file, 'r') as f:
            f2 = f.read()
            #regex = re.compile(r'<title>.+</title>')
            title = re.search(r'<title>.+</title>', f2, re.DOTALL)
            x = title.group()

            #print(x[7:-28])
        with open('/Users/laurissastokes/Projects/casescraper/RBG/titles_courtlistener.txt', 'a') as f3:
            f3.write('\n' + x[7:-28])

            continue

    else:
            continue

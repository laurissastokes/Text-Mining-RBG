#This is the script I used to strip all of the html from each opinion, leaving only text. 

import os
from bs4 import BeautifulSoup


path = '.'    #assumes this script is sitting in the same folder as txt files that are being stripped

for file in os.listdir(path):
    #print(file)
    if file.endswith(".txt"):
        with open(file, 'rb') as f:
            x = f.read()
            soup = BeautifulSoup(x, "html.parser")
            find = soup.get_text()
        for find2 in find:
            filename = (os.path.join(path,file))
            newfilename = '/Users/laurissastokes/Projects/casescraper/RBG/Originaldownloadsofallcases_stripped_of_html/' + file
            with open(newfilename, 'w') as f2:
                f2.write(find)
                continue
    else:
                continue

#This script adds the word BREAK to end of every .txt file contained a folder. This provides a reference marker to split them back into individual files after they've been combined for any reason, e.g. if you want to put them in an application like OpenRefine. 


import os

path = '.'

for file in os.listdir(path):
    if file.endswith(".txt"):
        with open(file,'a') as f:
            f.write('\n' + 'BREAK')
            continue

    else:
            continue

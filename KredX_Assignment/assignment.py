#pdf2txt.py -o vendor1.txt -t text vendor1.pdf
#pdf2txt.py -o vendor2.txt -t text vendor2.pdf
#pdf2txt.py -o vendor3.txt -t text vendor3.pdf
#pdf2txt.py -o vendor5.txt -t text vendor5.pdf

# Run above commands on Command Line

import re

filename = raw_input("Enter a file name:  ")

with open(filename) as input_file:
    for line in input_file:
        if re.search(r'INV-\d+', line) or re.search(r'INV\d+', line) or line.startswith('Invoice No:'):
            if re.search(r'INV\d+', line):
                line = line.split('#')[1]
            if line.startswith('Invoice No:'):
                line = line.split(':')[1]
            inv_no = line
        
        if re.search(r'\b([0-9]{1,2})[-/:]([0-9]{1,2})[-/:]([0-9]{4})\b', line):
            line1 = line.split(':')[1]
            date = line1
        if re.search(r'\b([0-9]{1,2})[-/:](?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[-/:]([0-9]{4})\b', line):
            date = line
        if re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s([0-9]{1,2}),\s([0-9]{4})\b', line):
            date = line

filename1 = filename.split('.')[0]
print "{ " + filename1+".pdf" + ", " + inv_no + "," + date + "}"
         
 


import csv
import os
import re

mydict = {
    'name2' : ['pass2','addr2'] ,
    'name3' : ['pass3','addr3']
#     ...
}

tempfilename = 'ac.csv'

dict={}
myDict={}
with open(tempfilename, mode='r') as infile:
    read = csv.reader(infile, skipinitialspace=True)
    header = next(read)
    header = header
    print(header)
    #for row in read:
     #   myDict = {row[0]: row[1:]}
    #print(myDict)

    dict = {row[0]: row[1:] for row in read}
    print("BEFORE")
    print(dict)

# only add items from my_dict that weren't already present
dict.update({key: value for (key, value) in mydict.items()
                      if key not in dict})
print("AFTER")
print(dict.items())


# create updated version of file
with open(tempfilename, mode='w', newline='') as outfile:
    csv_writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(header)
    for k, v in dict.items():
        csv_writer.writerow([k] + v)




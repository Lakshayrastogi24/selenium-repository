import csv

def getCsvData(filename):
    li=[]
    dataFile=open(filename,'r')
    read=csv.reader(dataFile)
    next(read)
    for lines in read:
        li.append(lines)
    return li
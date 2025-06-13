import sys
def openfile(filename):
    myfile = open(filename)
    count = 0
    for line in myfile:
        mylist = line.split(" ")
        count = count + len(mylist)
    return count



file_name = sys.argv[1]

newcount = openfile(file_name)
print(newcount)
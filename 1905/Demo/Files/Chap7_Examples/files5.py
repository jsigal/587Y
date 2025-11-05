# Using Loops and Iterators for File Access
try:
    with open('C:/Course/1905/Data/simple.txt', 'r') as infile:
        for dataline in infile:
            print(dataline.rstrip())

except IOError as ioe:
    print('Read or Write error on file', ioe.args)

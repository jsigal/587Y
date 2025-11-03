# Reading a Text File Example
try:
    infile = open('C:/Course/1905/Data/simple.txt', 'r')
    print(infile.readline().rstrip())
    print(infile.readlines())
    infile.close()
except IOError as ioe:
    print('Error number', ioe.args[0])
    print('Message', ioe.args[1])

# Using with to Open and Close Files
try:
    with open('C:/Course/1905/Data/simple.txt', 'r') as infile:
        print(infile.readline().rstrip())
        print(infile.readlines())
        infile.write('line 5\n')

except IOError as ioe:
    print('Read or Write error on file', ioe.args)

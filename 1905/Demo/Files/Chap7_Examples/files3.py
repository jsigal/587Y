# Data Handling Exceptions
try:
    infile = open('C:/Course/1905/Data/simple.txt', 'r')
    try:
        print(infile.readline().rstrip())
        print(infile.readlines())
        infile.write('line 5\n')
    except IOError:
        print('Read or Write error on file')
    finally:
        infile.close()
except IOError as ioe:
    print('Failed to open the file', ioe.args)

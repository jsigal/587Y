# Opening Files and Exceptions
try:
    infile = open('Incorrectfilename')
except IOError as ioe:
    print('Unable to open the file')
    print('Error number', ioe.args[0])
    print('Message', ioe.args[1])
    print('Filename in error', ioe.filename)

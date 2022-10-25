# exercise 2 Change the code again to prompt the user for the name of the file to write to. 
# Since the open function takes a string as the parameter, it could be a literal value or a string variable.

fname = input('please choose a file name: ')
if '.' not in fname:
    fname = fname + '.txt'

f = open(fname, 'w')
f.write('I want you to know\n')
f.write('I am happy for you\n')
f. close()




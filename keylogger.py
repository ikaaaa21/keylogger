# storing the keystorkes in a text file
# file handling- how to read, write and append a file

f = open('log.txt', 'w')
f.write('Hello World \n') # write to the file , it takes up reserouces
f.close() #good practice to close the file , gives back the resources to the system

f = open('log.txt', 'r') # read the file
filedata = f.read()
print(filedata)

f = open('log.txt', 'a') # append to the file so that the data is not lost and you can add to it 
f.write('Hey hey hey') # write to the file , it takes up reserouces
f.close()

# r - reading
# w - writing - wont use this as it will overwrite the file so we will use append instead
# a - appending 
# r+ - reading and writing
# w+ - writing and reading
# a+ - appending and reading

# listeners - listen to keystorkes and mouse clicks
# use of the 'with' keyword - releases memroy after the block of code is executed

with open('log.txt', 'a') as f: #as f is the variable saved in the memory
    f.write('Hello  \n') # write to the file 
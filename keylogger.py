# storing the keystorkes in a text file
# file handling- how to read, write and append a file

f = open('log.txt', 'w')
f.write('Hello World') # write to the file , it takes up reserouces
f.close() #good practice to close the file , gives back the resources to the system



# r - reading
# w - writing
# a - appending 
# r+ - reading and writing
# w+ - writing and reading
# a+ - appending and reading
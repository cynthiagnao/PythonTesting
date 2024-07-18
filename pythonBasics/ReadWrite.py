file = open('test.txt')

#print(file.read()) #read all the content of the file
#print(file.read(5)) #read n number of characters by passing parameter #only read first 2 characters of the file

#read one singleline at a time readLine()
'''print(file.readline()) #the 1st line of the file
print(file.readline()) #read the next line
'''

#Print line by line using readLine method
'''line = file.readline()
while line != "":
    print(line)
    line = file.readline() #store the next line that will be checked
'''

#each line will be stored in a list, it will read eahc index
#values = [apple, banana, cat, dog, elephant]
for line in file.readlines():
    print(line)

file.close() # always close the file you opened



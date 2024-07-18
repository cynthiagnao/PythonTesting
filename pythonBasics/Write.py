
#This line opens the file and when the all execution is completed, it will close the file
#Is the file opened in Read 'r' mode or Write 'w' mode ?

#Read the file and stored all the line in list
#Reverse the list
#Write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines() #all the file will be stored in the list  [apple, banana, cat, dog, elephant]
    reversed(content) #the content is reversed  [elephant, dog, cat, banana, apple]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

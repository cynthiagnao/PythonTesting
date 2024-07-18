str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1]) #a #print any character in this string

print(str[0:5]) #Rahul #if you want substring in python

print(str +" " + str1) #concatenate two strings

print(str3 in str) #substring check #is str3 present in str ? return True or False

var = str.split(".")
print(var)
print(var[0])
print(var[1])

str4 = "great "
str5 = " hello "

print(str4.strip()) # strip method remove white space
print(str5.lstrip()) # remove beginning (left) white space
print(str5.rstrip()) # remove end (right) white space


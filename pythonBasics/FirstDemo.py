
# Numeric Data Type, String Data Type

print("Hello")

# comment on a single line
""" comment en several lines 
comment on several lines 
comment on several lines 
"""

# variables
a = 3
print (a)

Str = "Hello word"
print (Str)

b, c, d, e = 5, 2.2, "Great", 100+3j
print (b,c,d)

# print("Value b is : ", b, "\nValue c is : ", c, "\nValue d is: ", d)

print("{} {}".format("Value is", b))

print(type(b)) #int
print(type(d)) #str

# create a variable with float value
print("The type of variable having value", c, "is", type(c))

# create a variable with complex value
print("The type of variable having value", e, "is", type(e), "\n")


a1 = "string in a double quote"
b1 = 'string in a single quote'

print(a1)
print(b1)

# using ',' to concatenate the two or several strings
print(a1,"concatenated with",b1)

# using '+' to concate the two or several strings
print(a1+" concate with "+b1)


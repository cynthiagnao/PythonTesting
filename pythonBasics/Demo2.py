
# LIST DATA TYPE allows multiple values and can be different data types

values = [1, 2.44, "rahul", 4, 100+3j]

print(values[0]) #1
print(values[3]) #4
print(values[-1]) #(100+3j)
print(values[-3]) #"rahul"
print(values[1:3]) # 2 rahul
values.insert(3, "shetty")
print(values) #[1, 2, 'rahul', 'shetty', 4, (100+3j)]
values.append("End")
print(values) #[1, 2, 'rahul', 'shetty', 4, (100+3j), 'End']

values[2] = "RAHUL" #Updating
print(values) #[1, 2.44, 'RAHUL', 'shetty', 4, (100+3j), 'End']

print(type(values[0])) #int
print(type(values[1])) #int
print(type(values[2])) #str
print("The type of variable having value", values[-2], "is", type(values[-2])) #complex

del values[0]
print(values) #[2.44, 'RAHUL', 'shetty', 4, (100+3j), 'End']

del values [-2]
print(values) #[2.44, 'RAHUL', 'shetty', 4, 'End']


# TUPLE - Same as LIST data type but immutable

'''val = (1, 2, "rahul", 4.5)
print(val)
val[2] = "RAHUL"
print(val)
'''

# DICTIONARY

dic = {"a":2, 4:"bcd", "c":"Hello"}
print(dic[4])
print(dic["c"])
print(dic["a"])

dict ={}
dict["firstname"] = "Cynthia"
dict["lastname"] = "Gnao"
dict["gender"] = "female"
print(dict)
print(dict["lastname"])


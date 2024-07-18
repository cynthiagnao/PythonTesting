
ItemsIncart = 0
#2 items will be added to the cart

#Method1
'''
if ItemsIncart != 2: 
    raise Exception("Products Cart count not matching")
'''

#Method2
'''
if ItemsIncart != 2:
    pass

assert(ItemsIncart == 2) #this condition return false
'''

#Method 3
#try, catch (catch is used in Java, C#)
'''
try:
    with open('filelog.txt', 'r') as reader: #there is no file named filelog.txt
        reader.read()

except:
    print("Some how I reached this blocked because there is a failure in try block")
'''

#Method 4
try:
    with open('test.txt', 'r') as reader: #there is no file named filelog.txt
        reader.read()

except Exception as e:
    print(e) #will show the error Python catch, it is more explicit

finally:
    print("cleaning up records") #every time it will print this line either the test succeed or not
#help to left a note at a specific step
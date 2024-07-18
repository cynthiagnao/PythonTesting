# IF ELSE LOOP

greeting = "Good Morning"
a = 4

if greeting == "Good Morning":
    print(" Condition matches")
    print(" second line")
else:
    print("condition do not match")

if a<2:
    print(" Condition matches")
    print(" second line")
else:
    print("condition do not match")

print("if else condition code is completed")


#FOR LOOP

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)
    print(i*2)


#SUM OF FIRST NATURAL NUMBERS 1+2+3+4+5 = 15

summation = 0
#range(i,j) -> i to j-1
for j in range(1, 6): #for(i=0, i<5, i++)
    print(j)
    summation = summation + j
print (summation)

print ("**************************")
#Iteration +2
for k in range(1,10,2):
    print(k)
    print("**************SKIPPING FIRST INDEX****************")
for l in range(10):
    print(l)
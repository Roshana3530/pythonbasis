list={1,2,3,4}
for val in list:
    print(val)

x=["aaa","Sss","ffff","ggg"]
for str in x:
    print(str)


str="Roshanasharma"
for char in str:
    print(char)

str = "Roshanasharma"
for char in str:
    if(char=="o"):
         print("o found")
         break
    print(char)
else:
 print("end")


#print the elements of the following list using a loop.
nums=[1,4,9,16,25,36,49,64,81,100]

for val in nums:
     print(val)


#search for a number x in this tuples using a loop.
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
idx=0
for el in nums:
    if(el==x):
        print("number found at idx ",idx)
    idx+=1




    #range function

# for el in range(1)
#     print el
# for el in range(3,4)
#     print el
#  for el in range(4,5,6)
#      print el

for i in range(5):
    print(i)


for i in  range(1,5):
    print(i)



for i in range(1,10,2): # 1 to 10 ans step size is 2
    print(i)


#print number from 100 to 1
for i in range(100,1):
    print(i)




#print number from 1 to 101.
for i in range(1,101):
    print(i)

 #print number from 100 to 1.
for i in range(100,0,-1):    # for decreasing order we use -ve step size.
     print(i)



n=int(input("enter your number:"))
for i in range(1,11):
    print(n*i)


#pass is a null statement

for i in range(5):
    pass
print("some useful work")


#WAP to find the sum of first n numbers.
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum =",sum)



#WAP to find the factorial of first n numbers.

n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("total sum=", sum)



count=1
while count<=5:
    print("hello")
    count+=1


i=1
while i<=6:
    print("hi")
    i+=1

 #print number from 1 to 7 in reverse order
i=7
while i >=1:
    print(i)
    i-=1
print("loop ended")



#example of continue
i=0
while i<=5:
    if(i==3):
        i +=1
        continue
    print(i)
    i +=1




#odd number
i=0
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1


  #even number
    i = 0
    while (i <= 10):
        if (i % 2 != 0):
            i += 1
            continue
        print(i)
        i += 1



#example of break
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i +=1
print ("end of loop")



 #example of break
nums=(1,4,9,16,25,36,49,64,81,100,36)
x=36
i=0
while i<len(nums):
    if(nums[i] ==x):
        print("Found at idx", i)
        break
    else:
        print("Finding..")
        i += 1
print("end of loop")







# sum of first n number .

n=4
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
    print("total sum=",sum)

#function definiton
def calc_sum(a,b):   #parameter
    sum=a+b
    print(sum)
    return sum
calc_sum(5,10)  #function call; arguments
calc_sum(2,5)



def calc_sum(a,b):
    return a+b
sum=calc_sum(1,2)
print(sum)


def print_hello():
    print("hello")
print_hello()




#function types  Built in function.

print("roshana","sharma")
print("roshana",end="")
print("sharma")

# len()
# type()
# range()


#user defined function

def cal_prod(a=1,b=2):
    print(a*b)
    return a*b
cal_prod()


#waf to print the length of alist(list is the parameter).

cities=["aaa","ssss","ffff","ggggg"]
str=["rrrr","tttt","yyyy","gggg"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(str)

#Waf  to print the elements of a list in a single line(list is the parameter)
cities=["aaa","ssss","ffff","ggggg"]
str=["rrrr","tttt","yyyy","gggg"]
def print_len(list):
    print(len(list))
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(str)
print_list(cities)






#waf to find the factorial of n.(n is the parameter)
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print(fact)
cal_fact(4)


#waf to convert USD to INR.
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")
converter(7)










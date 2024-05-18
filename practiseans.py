# num=int(input("enter your num:"))
# rem=num%2
# if(num%2 == 0):
#     print("num is even")
# else:
#     print("num is odd")
#
#
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))
# if(a>=b and a>=c):
#     print("first number is largest", a)
# if(b>=c):
#     print("second  number is largest",b)
# else:
#  print("third number is largest ",c)
#
#
#  x= int(input("enter your first number:"))  #find greatest of 4 number#
#  y= int(input("enter your second number:"))
#  z= int(input("enter your third number:"))
#  a= int(input("enter your fourth number:"))
# if(x>=y and x>=z and x>=a):
#      print("first number is largest",x)
# if(y>=z and y>=a):
#     print("second number is largest",y)
# if(z>=a) :
#     print("third number is largest",z)
# else:
#     print("fourth number is largest",a)
#
#
#
#
#
# x=int(input("enter your number:"))
# if (x%7==0):
#     print("multiple of 7")
# else:
#     print("not multiple of 7")
#
#
# y= int(input("enter your number:"))      # is a number is multiple of 5 or not#
# if(y%5==0):
#     print("multiple of 5")
# else:
#     print("not multiple of 5")



    #ex of tuple
movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie:")
mov3 = input("enter 3rd movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

tup=["c","d","a","a","b","b","a"]
print(tup.count("a"))
print(tup.sort())
print(tup)




dict= {
      "table":("a piece of furniture","list of facts and figures"),
      "cat":("a small animal"),

}
print(dict)



subject ={
    "python","java","c","c++","javascript","java","c","javascript"
}
print(subject)
print(len(subject))

marks={}
x=int(input("enter phy:"))
marks.update({"phy":x})
y=int(input("enter chem:"))
marks.update({"chem":y})
a=int(input("enter math:"))
marks.update({"math":a})
print(marks)

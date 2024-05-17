marks = [10,20,40,57,89]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))


students=["roshana",7777,"aaaa"]     #in python all data types allowed
print(students)


str=["aaa","hhh",555]          #listing is mutable so we can change like this to replace aaa by nnn
print(str)
str[0]="nnn"
print(str)
 # if there is out of index then it gives error


marks1=[70,40,60,50,66]      #listing slicing
print(marks1[1:2])           #include starting_index but not include ending_index
print(marks1[1:])
print(marks1[:2])
print(marks1[-1:])

list=[1,2,3,4,9,8,7]           #list method
list.append(6)           #append mean to add at last
print(list)
print (list.sort())     # it gives none output bcz original string change
print(list)              #it gives accending order
print(list.sort(reverse=True))     #it gives none
print(list)               #it gives decending order
str=['a','s','r','t']
str.reverse()
print(str)

list=[2,3,5,6]      #index 2 ma new value aauxa ani same order ma hunxa
list.insert(2,7)
print(list)


list1=[1,2,3,6,7]
list1.remove(3)
print(list1)

list2=[1,2,3,4]      #particular index lai delete garne
list2.pop(1)
print(list2)
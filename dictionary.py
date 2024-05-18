# info ={
#     "key" : "value",
#     "name" : "roshana",
#     "course": "python"
# }
# print(info)               #autai line ma output auuxa
# print(type(info))
#
#
#
# info={
#     "name":"apnacollege",
#     "subject":["python", "java", "c+"],
#     "age":24,
#     "is_adult":"True",
#     "marks": 98
# }
# print(info["name"])              #individual output aauxa
# print(info["subject"])
# print(info["age"])
# print(info["is_adult"])
# print(info["marks"])
#
#
# info={
#     "name":"apnacollege",
#     "subject":["python", "java", "c+"],
#     "topics":["dict","set"],
#     "age":24,
#     "is_adult":"True",
#     "marks": 98
# }
# info["name"]= "roshana",
# info["surname"]="sharma",
# print(info)


info={
    "name":"apnacollege",
    "subject":["python", "java", "c+"],
    "topics":["dict","set"],
    "age":24,
    "is_adult":"True",
    "marks": 98,
}
null_dict={}
print(null_dict)


          #nested condition
student={
    "name":"roshana",
    "students" :{
        "phy" :70,
        "chem" :79,
        "math" :90
    }
}
print(student)
print(student["students"])
print(student["students"]["phy"])
print(type("student"))
print(len(student))       # values of keys output dinxa
print(list(student.keys()))  # keys kun kun ho vanera output auxa
print(student.values())
print(list(student.values()))   #list ma values aauxa
print(student.items())


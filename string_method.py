course="python for beginners" #slicing#
print(course[0:3])
print(course[2:])
print(course[:4])
print(course[1:-1])

str="roshana"     #string method#
print(str.capitalize())
print(str.upper())
print(str.count("s"))
print(str.endswith("a"))
print(str.startswith("o"))
print(str.replace("a","t"))
print(str.find("a"))
print(len(course))


place=("Hello") #indixing#
print(place[0])
print(place[4])


a=(" HEllo" "Hi ")      #split and strip#
print(a.split())    # split list ma output#
print(a.strip())    # strip space hataune#
jwt_token="aaa.bbbb.cccc.dddd"
b=jwt_token.split(".")
print(b[0])
place=" adjjkk bbbbsbdn "
c=(place.strip())
d="aaa".join(c)
print(d)
e=place.split()
f="hello". join(e)
print(f)

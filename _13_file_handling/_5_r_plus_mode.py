# file = open("demo.txt","r+")
# file.write("Hello")
# data = file.read()
# print(data)

file = open("demo.txt","r+")
file.write("Hello")
file.seek(0,0)
data = file.read()
print(data)
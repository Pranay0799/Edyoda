file = open("demo.txt","w")
cur_pos = file.tell()
print("Cursor Position : ",cur_pos)
file.write("Hey")
cur_pos = file.tell()
print("Cursor Position : ",cur_pos)
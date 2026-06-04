# Writing to a file
#with open("notes.txt", "w") as f:
 #   f.write("Hello, this is saved!\n")

with open("myname.txt","r") as f:
    content=f.read()
    print(content)
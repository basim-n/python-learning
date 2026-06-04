name = input("Enter your name: ")

with open("myname.txt", "a") as f:
    f.write(f"{name}   \n")
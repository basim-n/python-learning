name=input("Enter your name:")

print(name.upper())
names=name.split()


print(f"First name is {names[0]}")
print(f"Last name is {names[1]}")
print(f"number of characters in name is {len(name.replace(' ',''))}" )
print(f"name reverse is {name[ : :-1]}")
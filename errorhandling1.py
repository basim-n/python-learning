try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("That's not a valid number")
finally:
    print("Program finished")
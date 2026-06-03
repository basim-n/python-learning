def is_palindrome(name):
    if name==name[ : :-1]:
        return True
    else:
        return False





name=input("enter anything:")
is_pal=is_palindrome(name)
if is_pal:
    print("Yes Palindrome")

else:
    print(f"No,not palindrome")
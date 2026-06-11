def is_palindrome(string):
    modstr=string.replace(' ','')
    left=0
    right=len(modstr)-1
    while left< right:
        if modstr[left]==modstr[right]:
            left+=1
            right-=1
        else:
            return False
            break
    return True

string=input("Enter a string:")
if is_palindrome(string):
    print("String is palindrome")
else:
    print("String is not palindrome")
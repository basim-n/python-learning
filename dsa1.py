def balanced_string(string):
    ls=[]
    for i in range(len(string)):
        

        if string[i]=='(':
            ls.append('(')
        elif string[i]==')':
            if len(ls)==0:
                ls.append(')')
                return False
                break
            else:
                ls.pop()

    return len(ls)==0


    

     
    
    
    
                            





string=input("ENTER A STRING:")
if balanced_string(string):
    print(f"String is balanced")
else:
    print("Not balanced")







import json 
def load_contact():
    try:
        with open("contacts.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def saved_contacts(contacts):
    with open("contacts.json","w") as f:
        json.dump(contacts,f)

contacts=load_contact()
print("____CONTACT MANAGER____")
while True:
    print(f"1.ADD CONTACT\n2.View\n3.Search Contact\n4.Update Contact\n5.Delete Contact\n6.View by Category\n7.Explore to  text file\n8.Exit")
    try:
        choice=int(input("Enter your choice:"))
        if choice==1:
            contact={}
            name=input("Enter your name:")
            phone_no=input("Enter your phone number:")
            email=input("Enter your email:")
            category=input("Enter category:")
            contact={"Name":name,"Phone":phone_no,"Email":email,"Category":category}
            contacts.append(contact)
            saved_contacts(contacts)
            print("Contact saved")

        elif choice==2:
            if len(contacts)==0:
                print("NO CONTACT SAVED!")
            else:
                for count,item in enumerate(contacts,1):
                    print(f"{count}. Name:{item['Name']}\n  Phone No:{item['Phone']}\n  Email:{item['Email']}\n  Category:{item['Category']}")
                    print("\n")
        elif choice==3:
            search=input("Search contact:")
            flag=0
            for item in contacts:
                if search.upper() in item["Name"].upper():

                    print(f" Name:{item['Name']}\n  Phone No:{item['Phone']}\n  Email:{item['Email']}\n  Category:{item['Category']}")
                    flag=1
                    
            if flag==0:
                print("Contact not found")
            
        elif choice==4:
             search=input("Search contact:")
             flag=0
             for item in contacts:
                 if search.upper()==item["Name"].upper():
                     print("1. Name\n2. Phone\n3. Email\n4. Category")
                     ch=input("Choose field to update:")
                     fields = {"1": "Name", "2": "Phone", "3": "Email", "4": "Category"}
                     if ch in fields:
                         update=input("Enter updated value:")
                         item[fields[ch]]=update
                         flag=1
                         saved_contacts(contacts)
                         print("Contact updated")
                         break
                     else:
                         print("Invalid field")


 
             if flag == 0:
                 print("Such contact not exist")
            
            


                                 

            
        elif choice==5:
             search=input("Search contact:")
             flag=0
             for item in contacts:
                 if search.upper()==item["Name"].upper():
                     contacts.remove(item)
                     flag=1
                     saved_contacts(contacts)
                     print("contact deleted")
                     break
             if flag==0:
                 print("Contact not exist")
            
                 
        elif choice==6:
            cat=input("Enter category")
            flag=0
            for item in contacts:
                if item["Category"].upper()==cat.upper():
                    print(f" Name:{item['Name']}\n  Phone No:{item['Phone']}\n  Email:{item['Email']}\n  Category:{item['Category']}")
                    flag=1
            if flag ==0:
                print("NO SUCH CATEGORY") 


        elif choice==7:
            with open("contacts_export.txt","w") as f:
                for item in contacts:
                    f.write(f"Name     : {item['Name']}\n")
                    f.write(f"Phone    : {item['Phone']}\n")
                    f.write(f"Email    : {item['Email']}\n")
                    f.write(f"Category : {item['Category']}\n")
                    f.write("-"*20 + "\n")
            print("Contacts exported to contacts_export.txt")
        elif choice==8:
            break
        else:
            print("Choice not available")
    except ValueError:
        print("Invalid choice")

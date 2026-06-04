from datetime import date
today= date.today()

task=input("What have you learned today:")
with open("learned_log.txt","a") as f:
    f.write(f"{today}:{task} \n")


with open("learned_log.txt","r") as f:
    content=f.read()
    print(content)

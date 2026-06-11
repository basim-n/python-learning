def word_count(sentence):
    seen={}
    ls=sentence.split()
    for item in ls:
        if item in seen:
            seen[item]+=1
        else:
            seen[item]=1

    return seen
while True:
    sentence=input("Enter a sentence:")
    seen = word_count(sentence)
    print(seen)
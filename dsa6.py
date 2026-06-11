def is_anagram(word1,word2):
    if len(word1) != len(word2):
        return False
    count1={}
    count2={}
    for i in range(len(word1)):
        if word1[i] in count1:
            count1[word1[i]]+=1
        else:
            count1[word1[i]]=1

    for i in range(len(word2)):
        if word2[i] in count2:
            count2[word2[i]]+=1
        else:
            count2[word2[i]]=1

    for i in word1:
        if i in count2:
            if count1[i]!=count2[i]:
                return False
        else:
            return False
        
    return True


while True:
    word1=input("Enter word1:")
    word2=input("Enter word2:")
    print(is_anagram(word1,word2))
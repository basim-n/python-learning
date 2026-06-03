chr=input("Enter a sentence:")
print(f"CLEANED: {chr.strip()}")
chrmod=chr.split()
print(f"WORDS: {len(chrmod)}")

print(f"LONGEST WORD: {max(chrmod,key=len)}")
print(f"Palindrome check: {chr.replace(' ','')==chr[ : :-1].replace(' ','')}")


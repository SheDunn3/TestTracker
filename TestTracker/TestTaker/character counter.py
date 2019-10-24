x=0

while x==0:
    print("Type/paste the words you want me to count the characters in: ")
    words = input()
    words = words.rstrip()
    print(words)
    numOfChars = len(words.upper())
    print(numOfChars)
    words=None
    numOfChars=None
    
    print("Are there more characters you'd like me to count? (Type Y or N)")
    ans = input()
    if ans.upper() == "N":
        x=1
        



str1=input("Enter a string : ")
wordlist=str1.split()
count=[]
for w in wordlist:
    count.append(wordlist.count(w))
print("Count of occurance "+str(list(zip(wordlist,count))))
    

print("Generate Positive List of Numbers From A given List Of Integers")
list1=[-10,20,-30,40,-50,60,-70,80,-90,100]
re = [num for num in list1 if num>=0]
print(re)
list1 = []
print(sep='\n')


print("SQUARE NUMBERS")
n = int(input("Enter the Limit : "))
for i in range(1,n+1):
 sq=i*i
 list1.append(sq)
print("Square Numbers are : ",list1)
print(sep='\n')


print("PRINT VOWELS IN A GIVEN WORD")
word = str(input("Enter the word : "))
print("WORD is : "+word)
print("Vowels are : ")
for i in word :
    if i in 'aeiouAEIOU':
        print([i])
print(sep='\n')       


print("PRINT ORDINAL VALUES")
w = str(input("Enter the word "))
print("WORD IS : " +w)
print("ORDINAL VALUES ARE ")
for i in w:
    print(i,end=":")
    print(ord(i),end=" ")

a=[]
n=int(input("Enter the limit : "))
for i in range(n):
    b=input("Enter the color :")
    a.append(b)
print(a)
print("First color : " ,a[0])
print("Last color : ",a[n-1])

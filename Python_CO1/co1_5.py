list1=[]
n1=int(input("Enter the limit:"))
for i in range(n1):
  n2=int(input("Enter the number:"))
  if n2>100:
    list1.append("over")
  else:
    list1.append(n2)
print(list1)

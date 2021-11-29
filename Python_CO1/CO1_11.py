x = int(input("Enter the First Number : "))
y = int(input("Enter the Second  Number : "))
z = int(input("Enter the Third Number : "))
if(x>y):
    if(x>z):
        print("Largest is First Number : ",x)
    else:
        print("Largest is Third  Number : ",z)
else:
    if(y>z):
        print("Largest is Second Number : ",y)
    else:
        print("Largest is Third Number : ",z)
        



x = int(input("Enter the value of X : "))
y = int(input("Enter the value of Y : "))
i=1
while(i<=x and i<=y):
    if(x%i==0 and y%i==0):
        gcd=i
    i=i+1
print("GCD",gcd)

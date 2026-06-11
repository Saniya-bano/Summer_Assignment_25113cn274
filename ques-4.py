# first method
A=str(input("enter n:"))
B=list(A)

print(len(B))

# second method
n=input("enter number:")
print(len(n))

# third method
n=int(input("enter the number"))
count=0
while n>0:
    n=n//10
    count=count+1

print("number of digits=",count)    

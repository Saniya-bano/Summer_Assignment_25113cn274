n=int(input("enter n:"))
if n<0:
    print("not possible")
else:    
    fact=1
    for i in range(0,n):
        fact=fact*(i+1)

     print(fact)    

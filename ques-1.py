n=int(input("enter n:"))
# first method for sum of n natural numbers
sum=(n*(n+1))/2
print(sum)
# secondt method for sum of n natural numbers
sum=0
for i in range(1,n+1):
  sum=sum+i

print(sum)

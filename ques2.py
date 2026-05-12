# Question 2
n = int(input("Enter the number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input(f"Enter element {i+1}: ")))
print(lst)
def sum(a,b):
  return a+b;
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
s=sum(a,b)
midindex=int(n/2)
mid=lst[midindex]
if(s>mid):
  print(lst[0:(midindex+1)])
elif(s==mid):
  print(mid,":",lst[mid])
else:
  print(lst[midindex+1:n+1])
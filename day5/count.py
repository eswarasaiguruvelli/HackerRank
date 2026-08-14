n=int(input())
numbers=[]
for i in range(n):
    numbers.append(int(input()))
count=0
for j in range(n):
    if numbers[j]%2==0:
        count+=1
print("no of even numbers:",count)
n=int(input())
numbers=[]
for i in range(n):
    numbers.append(int(input()))
for j in range(n):
    if numbers[j] >=1:
        print(f"{numbers[j]} is positive")
    else:
        print(f"{numbers[j]} is negative")
        
        
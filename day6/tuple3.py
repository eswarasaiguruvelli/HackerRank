n = int(input())
numbers = tuple(map(int, input().split()))
x = int(input())

if x in numbers:
    print("Found")
else:
    print("Not Found")
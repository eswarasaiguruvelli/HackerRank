sub=int(input("enter no of sujects"))
total=0
for i in range (1,sub+1):
  marks=int(input(f"sub{i} marks= "))
  total=total+marks
print(f"total marks = {total}")
avarage=(total/sub)
print(f"avarage = {avarage}")
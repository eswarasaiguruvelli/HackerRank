Amount=int(input())
if Amount <1000:
  print("0% discount")
elif 1000 <= Amount <= 4999:
  print("5% discount")
elif 5000 <= Amount <= 9999:
  print("10% discount")
else:
  print("15% discount")
y=int(input())
if (y % 2 == 0) and (y > 20):
    print("Not Weird")
elif (y % 2 == 0) and (2 <= y <= 5):
    print("Not Weird")
elif (y % 2 == 0) and (6 <= y <= 20):
    print("Weird")
else:
    print("Weird")

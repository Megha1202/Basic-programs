i= int(input())
j = int(input())
k = int(input())
n = int(input())
results = []
for x in list(range(i + 1)):
    for y in list(range(j + 1)):
        for z in list(range(k + 1)):
            if x + y + z != n:
                results.append([x, y, z])
print(results)
n = int(input())
r = []
A = []
j = 0
while j < n:
    x = input()
    y = float(input())
    r.append([x, y])
    A.append(y)
    j += 1

a = min(A)
while (n-1)>=0:
    if r[n-1][1]==a and A[n-1]==a:
        r.remove(r[n-1])
        A.remove(A[n - 1])
    n=n-1



"""while (n-1)>=0:
    if A[n-1]==t:
        A.remove(A[n-1])
    n=n-1
print(A)"""

p = min(A)

h = 0
B=[]
z=len(A)
while h < z:

    if r[h][1] == p:

        B.append(r[h])


    h += 1
v=len(B)
u=[]
s=0
while s<v:
    d=B[s][0]
    u.append(d)
    s+=1



g=0
while g<v:

    f=min(u)
    print(f)
    u.remove(f)
    g+=1


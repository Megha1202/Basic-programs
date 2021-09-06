# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for d in range(n):
    s=input()
    u=list(str(s))
    k=[]
    l=[]
    for i in range(len(u)):

      if i%2==0:
          k.append(u[i])
      else:
          l.append(u[i])
    k="".join(k)
    l="".join(l)
    print(k,l)

n=input().split()
for j in range(len(n)):
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            n[i],n[i+1]=n[i+1],n[i]
print(n)

n=int(input ("enter n"))
i=1
while i<=n:
    j=0
    while j<=i:
        j=j+1
        if j==2:
            continue
        print(j,end="")
        
    print("")
    i=i+1
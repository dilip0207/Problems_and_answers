def frequency(n):
    a=[]
    for i in range(n):
        a.append(int(input()))
    b=[]
    i=0
    while(i<n):
        j=0
        while j<i:
            if(a[j]==a[i]):
                break
            j=j+1
        if j==i:
            b.append(a[i])
        i=i+1
    i=0
    while i<len(b)-1:
        j=i
        while j<len(b):
            if b[i]>b[j]:
                temp=b[i]
                b[i]=b[j]
                b[j]=temp
            j=j+1
        i=i+1
    print(b)
    i=0
    c=[]
    while i<len(b):
        j=0
        count=0
        while j<len(a):
            if a[j]==b[i]:
                count=count+1
            j=j+1
        i=i+1
        c.append(count)
    i=0
    d=c[:]
    print(c)
    while i<len(d)-1:
        j=i
        while j<len(d):
            if(d[i]>d[j]):
                temp=d[i]
                d[i]=d[j]
                d[j]=temp
            j=j+1
        i=i+1
    print(d)
    i=len(d)-1
    while i>=0:
        j=0
        while j<len(c):
            if d[i]==c[j]:
                k=0
                while k<c[j]:
                    print(b[j],end=' ')
                    k=k+1
                c[j]=0
                break
            j=j+1
        i=i-1
                    
        
frequency(int(input()))
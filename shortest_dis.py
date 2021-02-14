def Shortest(name, w1, w2):
    lst=name.split()
    first=0
    last=10000
    diff=10000
    for i in range(len(lst)):
        if lst[i]==w1 and first==0:
            first=i+1
        if lst[i]==w2 and first!=0:
            last=i+1
            first=0
    diff=min((last-first), diff)
    return diff-1


#driver Code
print(Shortest("geeks for geeks contribute practice geeks", "geeks", "practice"))


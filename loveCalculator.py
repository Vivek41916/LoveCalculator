from collections import Counter
import random
def loveCalculator(s1,s2):
    m=len(s1)
    n=len(s2)
    s1=sorted(s1.upper())
    s2=sorted(s2.upper())
    d1=dict(Counter(s1))
    d2=dict(Counter(s2))
    s=["F","L","A","M","E","S"]
    mi=min(m,n)
    c=0
    start=0
    for key,val in d1.items():
        if key in d2.keys() and key!='':
            c+=min(d1[key],d2[key])
    c=c*2
    f=n+m-c
    while(len(s)!=1):
        start=(start+f-1)%(len(s))
        s.remove(s[start])
    if s[0]=="F":
        print("Your Love Percentage is "+str(random.randint(50,55)))
    elif s[0]=="L":
        print("Your Love Percentage is "+str(random.randint(90,100)))
    elif s[0]=="A":
        print("Your Love Percentage is "+str(random.randint(70,80)))
    elif s[0]=="M":
        print("Your Love Percentage is "+str(random.randint(95,100)))
    elif s[0]=="E":
        print("Your Love Percentage is "+str(random.randint(0,5)))
    else:
        print("Your Love Percentage is "+str(random.randint(0,10)))
loveCalculator("abc","bcadda")
        

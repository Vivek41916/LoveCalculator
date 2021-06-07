import random
def loveCalculator(s1,s2):
    s1=(input().upper())
    s2=(input().upper())
    p=len(s1)+len(s2)
    l=['F','L','A','M','E','S']
    for i in range(len(s1)):
        c=s1[i]
        if(c in s2):
            s1=s1.replace(c,'*',1)
            s2=s2.replace(c,'*',1)
            p-=2
    while(len(l)!=1):
        e=(l[(p-1)%(len(l))])
        l=l[(p-1)%(len(l))+1:]+l[:(p-1)%(len(l))]
    if l[0]=="F":
        print("Your Love Percentage is "+str(random.randint(50,55)))
    elif l[0]=="L":
        print("Your Love Percentage is "+str(random.randint(90,100)))
    elif l[0]=="A":
        print("Your Love Percentage is "+str(random.randint(70,80)))
    elif l[0]=="M":
        print("Your Love Percentage is "+str(random.randint(95,100)))
    elif l[0]=="E":
        print("Your Love Percentage is "+str(random.randint(0,5)))
    else:
        print("Your Love Percentage is "+str(random.randint(0,10)))
loveCalculator("abc","bcadda")
        

def depress(l):
    n=len(l)
    for i in range(n):
        l[i]=int(l[i])
    Sum=0
    Count1=0
    Count2=0
    deptype=""
    depsev=""
    for i in range(0,n):
        if(i==0):
            if(l[i]>1):
                Count1+=1
        elif(i==1):
            if(l[i]>1):
                Count1+=1
        else:
            if(i<=7):
                if(l[i]>1):
                    Count2+=1
            else:
                if(l[i]>0):
                    Count2+=1
    if(Count1==2):
        if(Count1+Count2>=4):
            deptype="Depressive Disorder"
            for i in range(0,n):
                Sum+=l[i]
            if(Sum>=1 and Sum<=4):
                depsev="Minimal Depression"
            elif(Sum>=5 and Sum<=9):
                depsev="Mild Depression"
            elif(Sum>=10 and Sum<=14):
                depsev="Moderate Depression"
            elif(Sum>=15 and Sum<=19):
                depsev="Moderately Severe Depression"
            else:
                depsev="Severe Depression"
        else:
            deptype="No Dipression Disorder"
            depsev="Minimal Depression"
    elif(Count1==1):
        if(Count1+Count2>=5):
            deptype="Major Depression"
            depsev="Severe Depression"
        elif((Count1+Count2)>=2 and (Count1+Count2)<=4):
            deptype="Other Dipression"
            depsev="Mild Depression"
        else:
            deptype="No Dipression Disorder"
            depsev="Minimal Depression"
    else:
        deptype="No Dipression Disorder"
        depsev="Minimal Depression"

    return Sum,deptype,depsev


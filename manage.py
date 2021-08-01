from joblib import load
from pandas import DataFrame
class model:
    def __init__(self):
        self.will=[]
        self.religion=0
        self.suicide=0
        self.academic=2
        self.deptype=0
        self.depsev=0
        self.todep=0
        self.tosc=0
        self.alone_bi=0
        self.others_bi=0
        self.type=""
    def predict(self):

        self.deptype,self.depsev=self.change()
        values=[[self.academic,self.religion,self.suicide,self.depsev,self.deptype,self.todep,self.tosc,self.will[3],self.will[4],self.will[5],self.will[6],self.will[7],self.will[8],self.will[9],self.will[0],self.alone_bi,self.others_bi]]
        df=DataFrame(values,columns=["Academic","Religion","Suicide","DepSev","DepType","ToDep","ToSC","Friends","Parents","Relative","Profess"," Phone","Doctor","Reli","Alone","Alone_bi","Others_bi"])
        # load the saved pipleine model
        pipeline = load("stress_classification.joblib")

        pred=pipeline.predict(df)
        pred=self.level(pred)
        return pred

    def depress(self,l):
        self.religion=int(l[0])
        self.b=int(l[1])
        l=l[2:]
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
        self.todep=Sum
        self.depsev=depsev
        self.deptype=deptype
        return Sum,deptype,depsev

    def social(self,l):
        for i in range(len(l)):
            l[i]=int(l[i])
        self.alone_bi=l[0]
        self.others_bi=l[1]
        l=l[2:]
        b=sum(l)
        if(b>=11 and b<=19):
            ToSCTotal=11
        elif(b>=20 and b<=28):
            ToSCTotal=16
        elif(b>=29 and b<=38):
            ToSCTotal=22
        elif(b>=39 and b<=48):
            ToSCTotal=27
        elif(b<=49 and b>=58):
            ToSCTotal=34
        elif(b<=59 and b>=67):
            ToSCTotal=39
        else:
            ToSCTotal=46
        self.tosc=ToSCTotal
        self.will=l
        return ToSCTotal

    def change(self):
        dep1={"No Dipression Disorder":1,"Other Dipression":2,"Major Depression":3,"Depressive Disorder":2}
        dep2={"Minimal Depression":1,"Mild Depression":2,"Moderate Depression":3,"Moderately Severe Depression":4,"Severe Depression":5}
        for i in dep1.keys():
            if(i==self.deptype):
                self.deptype=dep1[i]
        for i in dep2.keys():
            if(i==self.depsev):
                self.depsev=dep2[i]    
        return self.deptype,self.depsev

    def level(self,pred):
        if(pred>=36 and pred <=58):
            return 1
        elif(pred>=59 and pred<=81):
            return 2
        elif(pred>=82 and pred<=103):
            return 3
        elif(pred>=104 and pred<=125):
            return 4
        else:
            return 5
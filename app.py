from flask import Flask,render_template,request
from dep import depress
from manage import model
obj=model()
app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    return render_template("bootstrap-5.0.2-dist/home.html")

@app.route("/quiz",methods=['POST','GET'])
def quiz():
    return render_template("bootstrap-5.0.2-dist/quiz.html")    
    
@app.route("/Submit",methods=['POST','GET'])
def Submit():
    data=request.form.getlist('cars')
    print(data)
    deprate,deptype,depsev=obj.depress(data[2:])
    print(deprate)
    return render_template('bootstrap-5.0.2-dist/depression_page.html',output1=deprate,output2=deptype,output3=depsev)

@app.route("/dep",methods=['POST','GET'])
def dep():
    data=request.form.get('bus')
    obj.type=data
    print(data)
    return render_template("bootstrap-5.0.2-dist/willingness.html")    


@app.route("/Social",methods=['POST','GET'])
def Social():
    data=[]
    value=["alone_bi","others_bi","yourself","other","partner","friends","parents","relatives","professionals","phone","doctors","leader","internet"]
    for i in range(13):
        data.append(request.form.get(value[i]))
    print(data)
    sc=obj.social(data)
    result=obj.predict()
    print(obj.type)
    if(obj.type=="1"):
        return render_template('bootstrap-5.0.2-dist/ResultTime.html',output1=obj.todep,output2=sc,output3=result)
    elif(obj.type=="2"):
        return render_template('bootstrap-5.0.2-dist/ResultAnti.html',output1=obj.todep,output2=sc,output3=result)
    elif(obj.type=="3"):
        return render_template('bootstrap-5.0.2-dist/ResultSituational.html',output1=obj.todep,output2=sc,output3=result)
    return render_template('bootstrap-5.0.2-dist/ResultEncounter.html',output1=obj.todep,output2=sc,output3=result)

if __name__=='__main__':
    app.run()
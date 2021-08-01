# import joblib
from joblib import load
from pandas import DataFrame

# sample tweet text
values=[[2,1,1,1,1,7,11,4,3,1,1,1,1,1,5,2,1]]
df=DataFrame(values,columns=["Academic","Religion","Suicide","DepSev","DepType","ToDep","ToSC","Friends","Parents","Relative","Profess"," Phone","Doctor","Reli","Alone","Alone_bi","Others_bi"])
# load the saved pipleine model
pipeline = load("stress_classification.joblib")

# predict on the sample tweet text
pred=pipeline.predict(df)
print(pred[0])

from flask import Flask,render_template,request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app=Flask(__name__)
model=pickle.load(open('regression_heart1.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('frontend.html')
standard_to=StandardScaler()
@app.route("/predict",methods=['POST'])
def predict():
    if request.method=="POST":
        Age=int(request.form['Age'])
        sex_0=request.form['sex_0']
        if(sex_0=='Female'):
            sex_0=1
            sex_1=0
        else:
            sex_0=0
            sex_1=1
        trestbp=int(request.form['trestbps'])
        cholestrol=int(request.form['chol'])
        maxheartrate=int(request.form['thalach'])
        oldpeaks=float(request.form['oldpeak'])
        cp_0=request.form['cp_0']
        if(cp_0=='typical_angina'):
            cp_0=1
            cp_1=0
            cp_2=0
            cp_3=0
        elif(cp_0=='Atypica_angina'):
            cp_0=0
            cp_1=1
            cp_2=0
            cp_3=0
        elif(cp_0=='Non_anginal'):
            cp_0=0
            cp_1=0
            cp_2=1
            cp_3=0
        else:
            cp_0=0
            cp_1=0
            cp_2=0
            cp_3=1
        fbs_0=request.form['fbs_0']
        if(fbs_0=='True'):
            fbs_0=1
            fbs_1=0
        else:
            fbs_0=0
            fbs_1=1
        restecg_0=request.form['restecg_0']
        if(restecg_0=='normal'):
            restecg_0=1
            restecg_1=0
            restecg_2=0
        elif(restecg_0=='ST-T wave abnormality'):
            restecg_0=0
            restecg_1=1
            restecg_2=0
        else:
            restecg_0=0
            restecg_1=0
            restecg_2=1
        exang_0=request.form['exang_0']
        if(exang_0=='Yes'):
            exang_0=1
            exang_1=0
        else:
            exang_0=0
            exang_1=1
        slope_0=request.form['slope_0']
        if(slope_0=='upsloping'):
            slope_0=1
            slope_1=0
            slope_2=0
        elif(slope_0=='Flat'):
            slope_0=0
            slope_1=1
            slope_2=0
        else:
            slope_0=0
            slope_1=0
            slope_2=1
        ca_0=request.form['ca_0']
        if(ca_0=='0'):
            ca_0=1
            ca_1=0
            ca_2=0
            ca_3=0
            ca_4=0
        elif(ca_0=='1'):
            ca_0=0
            ca_1=1
            ca_2=0
            ca_3=0
            ca_4=0
        elif(ca_0=='2'):
            ca_0=0
            ca_1=0
            ca_2=1
            ca_3=0
            ca_4=0
        elif(ca_0=='3'):
            ca_0=0
            ca_1=0
            ca_2=0
            ca_3=1
            ca_4=0
        elif(ca_0=='4'):
            ca_0=0
            ca_1=0
            ca_2=0
            ca_3=0
            ca_4=1
        thal_0=request.form['thal_0']
        if(thal_0=='0'):
            thal_0=1
            thal_1=0
            thal_2=0
            thal_3=0
        elif(thal_0=='1'):
            thal_0=0
            thal_1=1
            thal_2=0
            thal_3=0
        elif(thal_0=='2'):
            thal_0=0
            thal_1=0
            thal_2=1
            thal_3=0
        else:
            thal_0=0
            thal_1=0
            thal_2=0
            thal_3=1
        prediction=model.predict([[Age,sex_0,sex_1,trestbp,cholestrol,maxheartrate,oldpeaks,cp_0,cp_1,cp_2,cp_3,fbs_0,fbs_1,restecg_0,restecg_1,restecg_2,exang_0,exang_1,slope_0,slope_1,slope_2,ca_0,ca_1,ca_2,ca_3,ca_4,thal_0,thal_1,thal_2,thal_3]])
        result=round(prediction[0],2)
        if(result<1):
            return render_template('positive.html',prediction_text="less chance of heart disease")
        else:
            return render_template('high.html' , prediction_text="heavy chances of getting heart disease")
    else:
        return render_template('frontend.html')
if __name__=="__main__":
    app.run(debug=True)
        
        
        
        
        
        
        
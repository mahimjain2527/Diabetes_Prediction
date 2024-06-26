from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

def home(request):
    return render(request , 'home.html')


def predict(request):
    return render(request , 'predict.html')


def result(request):
    data=pd.read_csv(r'C:\Users\lenovo\Desktop\python individual\python\diabetes.csv')
    x = data.drop("Outcome",axis=1)
    y = data["Outcome"]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    
    lr=LogisticRegression()
    lr.fit(x_train,y_train)

    val1=float(request.GET['n1'])
    val2=float(request.GET['n2'])
    val3=float(request.GET['n3'])
    val4=float(request.GET['n4'])
    val5=float(request.GET['n5'])
    val6=float(request.GET['n6'])
    val7=float(request.GET['n7'])
    val8=float(request.GET['n8'])
    
    pred=lr.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    
    result2=""
    if pred==[1]:
        result2="Positive"
    else:
        result2="Negative"    
    
    return render(request , 'predict.html', {"result2":result2})
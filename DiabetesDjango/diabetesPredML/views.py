from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    #return HttpResponse("This is Home")
    return render(request,"home.html")

def result(request):
    cls = joblib.load('final_model.sav')

    lis=[]
    lis.append(request.GET['P'])
    lis.append(request.GET['G'])
    lis.append(request.GET['BP'])
    lis.append(request.GET['ST'])
    lis.append(request.GET['I'])
    lis.append(request.GET['BMI'])
    lis.append(request.GET['DPF'])
    lis.append(request.GET['A'])

    ans = cls.predict([lis])

    return render(request, "result.html", {'ans':ans, 'lis':lis})

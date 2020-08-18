from django.shortcuts import render

# Create your views here.

def index(request):
    data={'stock1':{'name':'Stock1','opening':45346,'closing':1234,'currentVal':56},
    'stock2':{'name':'Stock2','opening':1889,'closing':234235,'currentVal':56},
    'stock3':{'name':'Stock3','opening':1883,'closing':5346,'currentVal':56},
    'stock4':{'name':'Stock4','opening':1884,'closing':56457,'currentVal':56},
    'stock5':{'name':'Stock5','opening':1881,'closing':56457,'currentVal':56},
    
    }   
    context={'data':data,'tableheader':['name','opening','closing','currentVal']}
    return render(request,'index.html',context)
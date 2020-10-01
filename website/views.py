from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{})

def post(request):
    return render(request,'post.html',{})

def fashion(request):
    return render(request,'fashion.html',{})

def gadgets(request):
    return render(request,'gadgets.html',{})

def lifestyle(request):
    return render(request,'lifestyle.html',{})

def kitchen(request):
    return render(request,'kitchen.html',{})

def micam(request):
    return render(request,'micam.html',{})

def nikon(request):
    return render(request,'nikon.html',{})
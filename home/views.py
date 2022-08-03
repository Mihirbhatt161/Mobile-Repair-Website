from django.shortcuts import render,HttpResponse
from home.models import contact
# Create your views here.
def index(request):
    context={
        "variable":"this is very conjush man on earth"
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method=="POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        desc= request.POST.get("desc")
        contact=contact(name="name",email="email",desc="desc")
        contact.save()
        
    
    return render(request, 'contact.html')
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index1.html')

def admin(request):
    return render(request, 'admin.html')
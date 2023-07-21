from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def admin(request):
    return render(request, 'admin.html')

def research_dir(request):
    return render(request, 'research.html')

def team_t_s(request):
    return render(request, 'team_t_s.html')

def thesis(request):
    return render(request, 'thesis.html')

def personnel_training(request):
    return render(request, 'train.html')

def news(request):
    return render(request, 'news.html')

def project(request):
    return render(request, 'project.html')

def patents(request):
    return render(request, 'patents.html')

def writings(request):
    return render(request, 'writings.html')

def call_us(request):
    return render(request, 'call_us.html')
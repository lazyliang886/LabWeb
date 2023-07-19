from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def admin(request):
    return render(request, 'admin.html')

def research_dir(request):
    return render(request, 'research.html')

def team_t_s(request):
    return render(request, 'team_t_s.html')
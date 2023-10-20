from django.shortcuts import render

# Create your views here.
def register_candidate(request):
    return render(request, 'authuser/candidateregister.html')
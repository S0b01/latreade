from django.shortcuts import render
from django.http import HttpResponse



def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'titl': 'Home',
        'content': 'Главная страница - Home',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': False
        
        }   
    return render(request, 'main/index.html', context)
    
    
def about(request) -> HttpResponse:
    return HttpResponse('About page')

# Create your views here.

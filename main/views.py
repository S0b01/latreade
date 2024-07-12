from django.shortcuts import render
from django.http import HttpResponse



def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'titl': 'Home - Главная',
        'content': "Магазин мебели HOME"
        
        
        }   
    return render(request, 'main/index.html', context)
    
    
def about(request) -> HttpResponse:
    context: dict[str, str] = {
        'titl': 'Проект - О нас',
        'content': "О нас",
        'text_on_page': "Текст зачем нужен этот агрегатор торговли"
    }   
    return render(request, 'main/about.html', context)

# Create your views here.

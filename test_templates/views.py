from django.shortcuts import render
from datetime import datetime
from django.contrib import messages

def test_view(request):
    my_list = ["Mouse", "Laptop", "Teclado", "Audifonos", "Multicontactos", "Celular"]
    context = {
        "view_title":"MI TITULO INCREIBLE",
        "my_number":675,
        "my_number2":2000,
        "today": datetime.now().today(),
        "my_list": my_list,
    }
    template = "test_templates/detail-view.html"

    messages.add_message(request, messages.INFO, 'Mesaje de Prueba 1')
    messages.add_message(request, messages.INFO, 'Mesaje de Prueba 2')
    return render(request, template, context)

def home_view(request):
    productos = [
        {'nombre': 'Carro', 'precio': 1400 },
        {'nombre': 'Avión', 'precio': 5600},
        {'nombre': 'Barco', 'precio': 3200},
        {'nombre': 'Tanque', 'precio': 15000},
    ]
    context = {
        'productos': productos,
        'today': datetime.now().today()
    }
    template = "test_templates/home.html"

    messages.add_message(request, messages.INFO, 'Mesaje de Prueba 1')
    messages.add_message(request, messages.INFO, 'Mesaje de Prueba 2')
    return render(request, template, context)
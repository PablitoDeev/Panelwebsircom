from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    links = [
        {"name": "Reconocimiento Facial", "url": "https://tu-servidor/reconocimiento", "btn": "primary"},
        {"name": "Gestión de Impresoras", "url": "https://tu-servidor/impresoras", "btn": "success"},
        {"name": "Portainer", "url": "https://panel.sircom.cl:9443", "btn": "dark"},
    ]
    return render(request, "dashboard/index.html", {"links": links})

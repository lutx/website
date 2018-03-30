from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Witaj, to jest widok strony głównej </h1>")
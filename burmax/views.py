from django.http import HttpResponse
from django.template import loader
from .models import *



def index(request):
    all_shapes= Shapes.objects.all()
    template = loader.get_template('burmax/index.html')
    context= {
        'all_shapes': all_shapes,
    }
    return HttpResponse(template.render(context, request))


def detail(request, shapes_id):
    return HttpResponse("<h2>Details for Shapes id:" + str(shapes_id) + "</h2>")
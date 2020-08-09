from django.http import HttpResponse
from turnstyle_storage import models
from django.template import loader

def index(request):
    return HttpResponse("index")


def turnstyles(request):
    turnstyle_list = models.Turnstyle.objects.order_by('id')
    output = ', '.join([t.name for t in turnstyle_list])
    template = loader.get_template('turnstyles_storage/turnstyles.html')
    context = {
        'turnstyle_list': turnstyle_list,
    }
    return HttpResponse(template.render(context, request))


def materials(request):
    return HttpResponse("materials")
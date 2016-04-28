from django.template.response import TemplateResponse
from django.http import HttpResponse

def welcome(request):
    html = TemplateResponse(request,'base.html',{})
    return HttpResponse(html.render())
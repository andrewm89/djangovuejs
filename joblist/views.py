from django.template.response import TemplateResponse
from django.http import HttpResponse
from .models import JobList

# Create your views here.
def job_list(request):
    context = {}
    context['jobs'] = JobList.objects.all()

    html = TemplateResponse(request, 'joblist.html', context)
    return HttpResponse(html.render())

from django.template.response import TemplateResponse
from django.http import HttpResponse
from .models import JobList
from rest_framework import viewsets
from .serializers import JobsSerializer

# Create your views here.
def job_list(request):
    context = {}
    context['jobs'] = JobList.objects.all()

    html = TemplateResponse(request, 'joblist.html', context)
    return HttpResponse(html.render())

class JobsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = JobList.objects.all()
    serializer_class = JobsSerializer
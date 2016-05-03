from models import JobList
from rest_framework import serializers

class JobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobList
        fields = ('jobtitle', 'jobdescription', 'postdate')

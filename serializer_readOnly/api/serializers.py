from django.db.models import fields
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True)
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_field = ['name', 'roll']
        extra_kwrgs = {'name':{'read_only': True}}
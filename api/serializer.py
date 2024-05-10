from rest_framework import serializers
from work.models import Employeemodel


class Emp_serializer(serializers.ModelSerializer):
    class Meta:
        model=Employeemodel
        fields= "__all__"
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import DepartmentSerializer
from .models import Department
from rest_framework.permissions import IsAdminUser

# Create your views here.


class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAdminUser,)

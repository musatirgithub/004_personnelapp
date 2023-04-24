from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import DepartmentSerializer, PersonnelSerializer
from .models import Department, Personnel
from rest_framework.permissions import IsAdminUser

# Create your views here.


class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAdminUser,)


class PersonnelView(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

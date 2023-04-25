from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .serializers import DepartmentSerializer, PersonnelSerializer, DepartmentPersonnelSerializer
from .models import Department, Personnel
from rest_framework.permissions import IsAdminUser
from .permissions import IsOwner

# Create your views here.


class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAdminUser,)


class PersonnelView(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = (IsOwner,)


class DepartmentPersonnelView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonnelSerializer

    def get_queryset(self):
        name = self.kwargs["department"]
        queryset = Department.objects.filter(name__iexact=name)
        return queryset

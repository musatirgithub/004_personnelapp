from django.urls import path, include
from rest_framework import routers
from .views import DepartmentView

router = routers.DefaultRouter()
router.register('department', DepartmentView)


urlpatterns = [

]

urlpatterns += router.urls

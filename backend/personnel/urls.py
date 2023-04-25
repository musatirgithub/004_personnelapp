from django.urls import path, include
from rest_framework import routers
from .views import DepartmentView, PersonnelView, DepartmentPersonnelView

router = routers.DefaultRouter()
router.register('department', DepartmentView)
router.register('personnel', PersonnelView)


urlpatterns = [
    path("department/<str:department>/", DepartmentPersonnelView.as_view())
]

urlpatterns += router.urls

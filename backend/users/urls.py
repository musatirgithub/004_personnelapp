from django.urls import path, include
from .views import RegisterAPI, ProfileView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path("register/", RegisterAPI.as_view()),
    path("profile/<str:pk>", ProfileView.as_view()),
]

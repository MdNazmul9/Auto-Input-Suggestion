
from django.urls import path,include
from .views import HomeView #, PersonCreateView


urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    # path('create',PersonCreateView, name='create' ),
]

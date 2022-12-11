from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path("",views.IndexView.as_view(),name='index'),
    path("sign_up/",views.sign_up,name='sign_up'),
    path("profile/<int:pk>",views.ProfileDetailView.as_view(),name='profile'),
]

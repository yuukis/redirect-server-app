from django.urls import path
from redirectapp import views

app_name = 'app'

urlpatterns = [
    path('', views.redirect_view, name='redirect'),
]
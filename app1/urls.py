from django.urls import path
from . import views

app_name = 'app1'

urlpatterns =[
    path('', views.index, name='index'),
    path('<int:num>/testview/', views.testview, name='testview'),
]
from django.urls import path

from . import views

app_name = 'reports'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:report_id>/', views.detail, name='detail'),
    path('<int:report_id>/comment/', views.comment, name='comment'),
]
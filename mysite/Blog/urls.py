from django.urls import path
from.import views
urlpatterns = [
    path('', views.index, name='Home'),
    path('removepunc', views.removepunc, name='rempun'),
    path('analyze', views.analyze, name='analyze'),

]

from django.urls import path

from example_django_app.views import index, fragment, process


urlpatterns = [
    path('', index),
    path('fragment', fragment),
    path('process', process),
]

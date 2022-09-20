from django.urls import path

from . import views

urlpatterns = [
    path('get_synth_index/', views.synthetic_index_web_example, name='get_synth_index')
]

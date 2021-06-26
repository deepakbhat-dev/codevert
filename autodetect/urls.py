from django.urls import path

from . import views

urlpatterns = [
	path('home/', views.predict, name='predict'),
	path('convert/', views.convertAjax, name='convert'),
]

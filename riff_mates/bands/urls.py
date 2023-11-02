from django.urls import path

from bands import views

urlpatterns = [
    path('band/<int:band_id>/', views.band, name='band'),
    path('bands/', views.bands, name='bands'),
    path('musician/<int:musician_id>/', views.musician, name='musician'),
    path('musicians/', views.musicians, name='musicians'),
]

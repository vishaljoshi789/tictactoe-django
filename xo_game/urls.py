from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("join/", views.join, name="join"),
    path("game/<str:gameid>/<str:player>", views.game, name="join"),
]

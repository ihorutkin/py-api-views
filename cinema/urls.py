from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet
)

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path(
        "genre/",
        GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "genre/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
    path(
        "actor/",
        ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "actor/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
    path(
        "cinema_hall/",
        CinemaHallList.as_view(),
        name="cinema_hall-list"
    ),
    path(
        "cinema_hall/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinema_hall-detail"
    ),
    path("", include(router.urls)),
]

app_name = "cinema"

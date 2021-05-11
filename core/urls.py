from django.urls import path
from .views import home, viewSongs, viewWorship, viewMissions, viewHolySupper

urlpatterns = [
    path("", home, name="home"),
    path("view_songs/<int:ID_Songs>/", viewSongs, name="view_songs"),
    path("view_worship/", viewWorship, name="view_worship"),
    path("view_missions/", viewMissions, name="view_missions"),
    path("view_holy_supper/", viewHolySupper, name="view_holy_supper"),
]

from django.shortcuts import render
from .models import Songs
from .form import SongsForm


def home(request):
    obj_songs = Songs.objects.all().order_by("ID_Songs").reverse()
    obj_songs_table = Songs.objects.all()
    return render(
        request,
        "index.html",
        {"obj_songs": obj_songs, "obj_songs_table": obj_songs_table},
    )


def viewSongs(request, ID_Songs):
    data = {}
    songs = Songs.objects.get(ID_Songs=ID_Songs)
    form = SongsForm(request.POST or None, instance=songs)
    data["songs"] = songs
    data["form"] = form
    return render(request, "view_songs.html", data)


def viewWorship(request):
    worship = Songs.objects.filter(category="Adoracao")
    return render(request, "view_worship.html", {"worship": worship})


def viewMissions(request):
    missions = Songs.objects.filter(category="Missoes")
    return render(request, "view_missions.html", {"missions": missions})


def viewHolySupper(request):
    holy_supper = Songs.objects.filter(category="Santa Ceia")
    return render(request, "view_holy_supper.html", {"holy_supper": holy_supper})

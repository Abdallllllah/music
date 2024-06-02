from django.shortcuts import render
from django.http import Http404
from .forms import signupf, loginf, playlistf, songsf, editf
from django.contrib.auth.models import User
from django.contrib import auth
from .models import playlist,songs
# Create your views here.
'''
my_songs = [
            {"id": 1, "Track": "thank u, next", "Artist": "Ariana Grande", "Album": "thank u, next", "Length": "3:27","playlist_id": 1},
            {"id": 2, "Track": "One Kiss, next", "Artist": "Dua Lipa, Calvin Harris", "Album": "One Kiss", "Length": "3:34","playlist_id": 1},
            {"id": 3, "Track": "Better Now", "Artist": "Post Malone", "Album": "beerbongs & bentleys", "Length": "3:51","playlist_id": 1},
            {"id": 4, "Track": "The Middle", "Artist": "Grey,Marren Morris, ZEDD", "Album": "The Middle", "Length": "3:04","playlist_id": 1},
            {"id": 5, "Track": "Love Lies", "Artist": "Normani, Khalid", "Album": "Love Lies", "Length": "3:21","playlist_id": 2},
            {"id": 6, "Track": "Rise", "Artist": "Jack & Jack, Jonas Blue", "Album": "Blue", "Length": "3:14","playlist_id": 2},
        ]
        '''
my_playlists= playlist.objects.all()
my_songs = songs.objects.all()

def home(request):
    # music_types=['Pop','Rock','R&B','Soul & Funk','Blues','Reggae','Soundtracks','Dance & EDM','Rap', 'Asian Music','Jazz','Kpop','Metal','Electronic','Classical']
    return render(request,'zing/home.html',{"my_playlists":my_playlists})

def playlist(request,id,name):
    songs=[]
    playlist_name=''
    for playlist in my_playlists:
       if(id == playlist.id):
            playlist_name=playlist.name

    if len(playlist_name)==0:
        raise Http404("Such playlist does not exist")

    for song in my_songs:
        if song.playlist.filter(name=name).exists():
            songs.append(song)
        
    return render(request,'zing/songs.html',{"songs":songs,"playlist_name": playlist_name})
    
def signup(request):
        form = signupf(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            confirm_password = form.cleaned_data.get("confirm_password")
            if password != confirm_password:
                    return render(request, 'zing/signup.html', {'form': form,'status': "Passwords do not match"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'zing/signup.html', {'form': form,'status': "User already exists"})
                else:
                    
                    newu = User.objects.create_user(username = username, email = email, password = password)
                    return render(request, 'zing/signup.html',{'form': form, 'status': "User created successfully"})
        return render(request, 'zing/signup.html', {"form": form})

def login(request):
    form = loginf(request.POST or None)
    status= " "
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            status="You have successfully logged in!"
        else:
            status="You credentials are not valid. Try again!"
    return render(request,'zing/login.html',{"form":form,"status":status})

def create_playlist(request):
    form =  playlistf(request.POST or None)
    status = " "
    if form.is_valid():
        form.save()
        status = "Playlist created successfully!"
        return render(request,'zing/create_playlist.html',{'form':form,'status':status})
    return render(request,'zing/create_playlist.html',{'form':form})

def create_song(request):
    form = songsf(request.POST or None)
    status = " "
    if form.is_valid():
        form.save()
        status = "Song created successfully!"
        return render(request,'zing/create_song.html',{'form':form,'status':status})
    return render(request,'zing/create_song.html',{'form':form})
def edit(request, id):
    form = editf(request.POST or None)
    if form.is_valid():
        track = form.cleaned_data.get("Track")
        album = form.cleaned_data.get("Album")
        artist = form.cleaned_data.get("Artist")
        length = form.cleaned_data.get("Length")
        playlists = form.cleaned_data.get("playlist")

        print(f"Form data: {track}, {album}, {artist}, {length}, {playlists}")

        song = songs.objects.get(id=id)

        song.Track = track
        song.Album = album
        song.Artist = artist
        song.Length = length

        song.playlist.clear()
        song.save() 

        for playlist in playlists:
            song.playlist.add(playlist)


        print(f"Updated song: {song.Track}, {song.Album}, {song.Artist}, {song.Length}, {song.playlist.all()}")

        return render(request, 'zing/edit.html', {"form": form, "status": "Your song is updated successfully!"})

    print("Form is not valid")
    return render(request, 'zing/edit.html', {"form": form})
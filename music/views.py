from django.http import Http404
from django.shortcuts import render, get_object_or_404
#from django.template import loader
#from django.shortcuts import render
from .models import Songs, SongDetails

# Create your views here.

from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h2><i>This is the Music app homepage</i></h2>")
    all_songs = Songs.objects.all()
    #template = loader.get_template('music/index.html')
    ######
    #DICTIONARY TO STORE INFO THAT TEMPLATE NEEDS
    ######

    #context = {
    #'all_songs': all_songs,
#}

    #html = ''
    #for song in all_songs:
    #    url = '/music/' + str(song.songid)
    #    html += '<a href="' + url +'">' + song.songtitle + '</a><br>'
    #return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', {'all_songs': all_songs})

def detail(request, songid):
#    try:
#        song = Songs.objects.get(pk=songid)
#    except Songs.DoesNotExist:
#        raise Http404("Song does not exist")
    #return HttpResponse("<h2> Details for Song ID :" + str(songid) + "</h2>")
    song = get_object_or_404(Songs, pk=songid)
    return render(request, 'music/detail.html', {'song': song} )

#def favourite(request, songid):
#    song = get_object_or_404(Songs, pk=songid)
#    try:
#        selected_song = Songs.objects.get(pk=request.POST['song'])
#    except (KeyError, Song.DoesNotExist):
#        return render(request, 'music/detail.html', {'song': song,
#        error_message: "Not a valid song yo!",} )
#    else:
#        selected_song.is_favourite = True
#        selected_song.save()
#        return render(request, 'music/detail.html', {'song': song} )

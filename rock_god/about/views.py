from django.shortcuts import render, get_object_or_404
from .models import City, RecordDeal, Hospital, Strip, RecordingStudio, Gig, VideoClip, Pub, Fastfood, Index
# Create your views here.

from random import randint
def index(request):
    image = Index.objects.get(pk = randint(1, 4))

    return render(request, 'index.html', context={
        'image': image
    })


def cities(request):
    city_name = City.objects.all()


    return render(request, 'cities.html', context={
        'cities': city_name

    })


def citydetail(request, pk):
    city_name = get_object_or_404(City, pk = pk)

    return render(request, 'citydetail.html', context={
        'cities': city_name,
    })


def gigs(request):
    gigs = Gig.objects.all()


    return render(request, 'gigs.html', context={
        'gigs_': gigs
    })


def gigdetail(request, pk):
    gig_name = get_object_or_404(Gig, pk = pk)

    max_profit = int(gig_name.capacity * gig_name.ticket_value)
    procent_band_raiting = int(gig_name.min_bandrating * 100)

    return render(request, 'gigdetail.html', context= {
        'gigs': gig_name,
        'max_profit': max_profit,
        'procent_band_raiting': procent_band_raiting
    })


def pubdetail(request, pk):
    pub = get_object_or_404(Pub, pk = pk)

    return render(request, 'pubdetail.html', context={
        'pub': pub,
    })


def fastfooddetail(request, pk):
    fastfood = get_object_or_404(Fastfood, pk=pk)


    return render(request, 'fastfooddetail.html', context={
        'fastfood': fastfood
    })


def hospitaldetail(request, pk):
    hospital = get_object_or_404(Hospital, pk = pk)

    return render(request, 'hospitaldetail.html', context={
        'hospital': hospital,
    })

def stripdetail(request, pk):
    strip = get_object_or_404(Strip, pk = pk)

    return render(request, 'stripdetail.html', context={
        'strip': strip,
    })


def entertainments(request):
    pubs = Pub.objects.first()
    hospital = Hospital.objects.first()
    strip = Strip.objects.first()
    fastfood = Fastfood.objects.first()

    return render(request, 'entertainments.html', context={
        'pubs': pubs,
        'hospital': hospital,
        'strip': strip,
        'fastfood': fastfood
    })


def recorddeals(request):
    recorddeals = RecordDeal.objects.all()


    return render(request, 'recorddeals.html', context={
        'recorddeals': recorddeals,

    })


def recordstudios(request):
    recordstudios = RecordingStudio.objects.all()

    return render(request, 'recordstudios.html', context={
        'recordstudios': recordstudios
    })

def videoclip(request):
    videoclip = VideoClip.objects.all()

    return render(request, 'videoclip.html', context={
        'videoclip': videoclip
    })


def recorddealsdetail(request, pk):
    recorddeal = get_object_or_404(RecordDeal, pk=pk)

    minimum_band_rating = int(recorddeal.min_bandrating * 100)
    studio_discount = int(recorddeal.studio_discount * 100)
    videclip_discount = int(recorddeal.videoclip_discount * 100)
    songs_minimum_rating = int(recorddeal.songs_minimum_rating * 100)

    return render(request, 'recorddealsdetail.html', context={
        'recorddeal': recorddeal,
        'minimum_band_rating': minimum_band_rating,
        'studio_discount': studio_discount,
        'videclip_discount': videclip_discount,
        'songs_minimum_rating': songs_minimum_rating
    })

def recordstudiosdetail(request, pk):
    recordstudio = get_object_or_404(RecordingStudio, pk=pk)

    studio_quality = int(recordstudio.studio_quality * 100)
    min_bandrating = int(recordstudio.min_bandrating * 100)
    return render(request, 'recordstudiosdetail.html', context={
        'recordstudio': recordstudio,
        'min_bandrating': min_bandrating,
        'studio_quality': studio_quality
    })

def videoclipdetail(request, pk):
    videoclip = get_object_or_404(VideoClip, pk=pk)

    studio_quality = int(videoclip.studio_quality * 100)
    return render(request, 'videoclipdetail.html', context={
        'videoclip': videoclip,
        'studio_quality': studio_quality
    })
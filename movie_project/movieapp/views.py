from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }

    return render(request, 'index.html', context)


# def detail(request,movie_id):
#     return HttpResponse("movie number: %s" % movie_id)

def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('mname', )
        img = request.FILES['mposter']
        desc = request.POST.get('mdesc', )
        year = request.POST.get('myear', )

        movie = Movie(name=name, desc=desc, img=img, year=year)
        movie.save()

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')

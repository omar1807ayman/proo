from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Film, Rating
from .forms import UserRegistrationForm, RatingForm

def home(request):
    return render(request, 'ratings/home.html')

def film_list(request):
    films = Film.objects.all()
    return render(request, 'ratings/film_list.html', {'films': films})

@login_required
def film_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.film = film
            rating.user = request.user  # Ensure the user is an authenticated User instance
            rating.save()
            return redirect('film_detail', film_id=film.id)
    else:
        form = RatingForm()
    return render(request, 'ratings/film_detail.html', {'film': film, 'form': form})

@login_required
def my_ratings(request):
    ratings = Rating.objects.filter(user=request.user)
    return render(request, 'ratings/my_ratings.html', {'ratings': ratings})

@login_required
def profile(request):
    return render(request, 'ratings/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'ratings/register.html', {'form': form})

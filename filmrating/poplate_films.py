# populate_films.py

import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'filmrating.settings')
django.setup()

from ratings.models import Film

def populate_films():
    films = [
        {
            'title': 'The Dark Knight Rises',
            'description': 'Eight years after the Joker\'s reign of anarchy, Batman, with the help of the enigmatic Selina, is forced from his exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.',
            'release_date': date(2012, 7, 20),
            'image': 'film_images/the_dark_knight_rises.jpg'
        },
        {
            'title': 'The Dark Knight',
            'description': 'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.',
            'release_date': date(2008, 7, 18),
            'image': 'film_images/the_dark_knight.jpg'
        },
        {
            'title': 'Batman Begins',
            'description': 'After training with his mentor, Batman begins his fight to free crime-ridden Gotham City from corruption.',
            'release_date': date(2005, 6, 15),
            'image': 'film_images/Batman_Begins.jpg'
        },
        {
            'title': 'Interstellar',
            'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
            'release_date': date(2014, 11, 7),
            'image': 'film_images/interstellar.jpg'
        },
        {
            'title': 'The Matrix',
            'description': 'A computer hacker learns about the true nature of his reality and his role in the war against its controllers.',
            'release_date': date(1999, 3, 31),
            'image': 'film_images/the_matrix.jpg'
        },
        {
            'title': 'Back to the Future',
            'description': 'Marty McFly, a 17-year-old high school student, is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend, eccentric scientist Doc Brown.',
            'release_date': date(1985, 7, 3),
            'image': 'film_images/back_to_the_future.jpg'
        },
    ]

    for film in films:
        Film.objects.create(**film)

if __name__ == '__main__':
    populate_films()
    print('Films added successfully!')

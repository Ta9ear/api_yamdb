from reviews.models import (Categories, Genres, Titles,
                            TitleGenre, Review, Comment)
from users.models import User
import csv


def run():
    data = ['category.csv', 'comments.csv', 'genre.csv', 'genre_title.csv',
            'review.csv', 'titles.csv', 'users.csv']

    with open(f'static/data/{data[0]}') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            categories = Categories(id=row[0], name=row[1], slug=row[2])
            categories.save()

    with open(f'static/data/{data[2]}') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            genres = Genres(id=row[0], name=row[1], slug=row[2])
            genres.save()

    with open(f'static/data/{data[5]}') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            titles = Titles(id=row[0], name=row[1], year=row[2], category_id=row[3])
            titles.save()

    with open(f'static/data/{data[3]}') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            title_genre = TitleGenre(id=row[0], title_id=row[1], genre_id=row[2])
            title_genre.save()

    with open(f'static/data/{data[6]}') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            users = User(id=row[0], username=row[1], email=row[2], role=row[3])
            users.save()

    with open(f'static/data/{data[4]}') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            reviews = Review(id=row[0], title_id=row[1], text=row[2],
                             author_id=row[3], score=row[4], pub_date=row[5])
            reviews.save()

    with open(f'static/data/{data[1]}') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            comments = Comment(id=row[0], review_id=row[1], text=row[2],
                               author_id=row[3], pub_date=row[4])
            comments.save()

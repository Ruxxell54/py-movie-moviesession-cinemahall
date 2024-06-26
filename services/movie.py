from django.db.models.query import QuerySet

from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids is not None and actors_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids,
                                   actors__id__in=actors_ids)
    elif genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)
    elif actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str, *,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:

    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)

    if genres_ids is not None:
        movie.genres.add(*genres_ids)

    if actors_ids is not None:
        movie.actors.add(*actors_ids)

    return movie

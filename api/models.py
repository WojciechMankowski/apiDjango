from django.db.models import (Model, CharField, DateTimeField, ForeignKey, IntegerField,
                              URLField, CASCADE, FloatField)


class Comment(Model):
    content = CharField(max_length=250)
    user_name = CharField(max_length=250)
    date = DateTimeField("data dodania komentarza")


class DisabilityType(Model):
    type = CharField(max_length=250)
    description = CharField(max_length=250)


class Rating(Model):
    score = FloatField(max_length=250)
    number_of_ratings = IntegerField()
    id_comments = ForeignKey(Comment, CASCADE)


class Place(Model):
    name = CharField(max_length=250)
    address = CharField(max_length=250)
    url_imge = URLField(max_length=250)
    url_map_google = URLField(max_length=250)
    disability_type_id = ForeignKey(DisabilityType, CASCADE)
    ratings = ForeignKey(Rating, CASCADE)
    comments = ForeignKey(Comment, CASCADE)

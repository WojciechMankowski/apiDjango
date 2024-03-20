from django.db.models import Model, CharField, DateTimeField, ForeignKey, IntegerField, URLField, CASCADE, FloatField


class DisabilityType(Model):
    type = CharField(max_length=250)
    description = CharField(max_length=250)


class Place(Model):
    name = CharField(max_length=250)
    address = CharField(max_length=250)
    url_imge = URLField(max_length=250)
    url_map_google = URLField(max_length=250)
    disability_type_id = ForeignKey(DisabilityType, on_delete=CASCADE, related_name='places')


class Comment(Model):
    content = CharField(max_length=250)
    user_name = CharField(max_length=250)
    date = DateTimeField(auto_now_add=True)
    place = ForeignKey(Place, on_delete=CASCADE, related_name='komentarze')


class Rating(Model):
    score = FloatField()
    number_of_ratings = IntegerField()
    place = ForeignKey(Place, on_delete=CASCADE, related_name='ratings')
    disabilitytype = ForeignKey(DisabilityType, on_delete=CASCADE, related_name="DisabilityType")

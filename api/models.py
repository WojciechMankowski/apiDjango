from django.db.models import Model, ManyToManyField, CharField, DateTimeField, ForeignKey, IntegerField, URLField, CASCADE, FloatField


class DisabilityType(Model):
    type = CharField(max_length=250)
    description = CharField(max_length=250)

    def __str__(self):
        return f"Typ: {self.type}"


class Place(Model):
    name = CharField(max_length=250)
    address = CharField(max_length=250)
    url_imge = URLField(max_length=250)
    url_map_google = URLField(max_length=250)
    disability_type_id = ManyToManyField(DisabilityType, related_name="DisabilityType")

    def __str__(self):
        return f'Miejsce o nazwie: {self.name}'
class Comment(Model):
    content = CharField(max_length=250)
    user_name = CharField(max_length=250)
    date = DateTimeField(auto_now_add=True)
    place = ForeignKey(Place, on_delete=CASCADE, related_name='komentarze')

    def __str__(self):
        return f"Komentarz z dnia: {self.date}"

class Rating(Model):
    score = FloatField()
    number_of_ratings = IntegerField()
    place = ForeignKey(Place, on_delete=CASCADE, related_name='ratings')

    def  __str__(self):
        return f"Ocena dla miejsca o id: {self.place}"

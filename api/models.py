from django.db.models import Model, ManyToManyField, CharField, DateTimeField, ForeignKey, IntegerField, URLField, \
    CASCADE, FloatField


class DisabilityType(Model):
    type = CharField(max_length=250)
    description = CharField(max_length=250)

    def __str__(self):
        return f"Typ: {self.type}"


class Place(Model):
    OPTION_CHOICES = [
        (1, 'Urząd'),
        (2, 'Pub'),
        (3, 'Restauracja'),
        (4, 'Muzeum'),
        (5, "Miejsce związane z kulturą")
    ]

    name = CharField(max_length=250)
    address = CharField(max_length=250)
    url_image = URLField(max_length=250)
    url_map_google = URLField(max_length=250)
    type_place = IntegerField(choices=OPTION_CHOICES)
    disability_type_id = ManyToManyField(to='DisabilityType', related_name="places")

    def __str__(self):
        return f'Miejsce o nazwie: {self.name}'


class Rating(Model):
    score = FloatField()
    number_of_ratings = IntegerField()
    place = ForeignKey(Place, on_delete=CASCADE, related_name='ratings', null=True)

    def __str__(self):
        return f"Ocena dla miejsca "


class Comment(Model):
    content = CharField(max_length=250)
    user_name = CharField(max_length=250)
    date = DateTimeField(auto_now_add=True)
    place = ForeignKey(Place, on_delete=CASCADE, related_name='komentarze')

    def __str__(self):
        return f"Komentarz z dnia: {self.date}"

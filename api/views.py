from json import loads
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import *
from math import floor

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            comment = serializer.data.get("content")  # Pobierz wartość 'type' z zapisanej instancji
            message = f"Dodano nowy komentarz: {comment}"
            return Response({'message': message}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DisabilityTypeViewSet(viewsets.ModelViewSet):
    queryset = DisabilityType.objects.all()
    serializer_class = DisabilityTypeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            type_ = serializer.data.get("type")  # Pobierz wartość 'type' z zapisanej instancji
            message = f"Dodano nowy typ: {type_}"
            return Response({'message': message}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()  # Pobranie wszystkich ocen z bazy danych
    serializer_class = RatingSerializer  # Klasa serializera dla ocen
    lookup_field = 'pk'

    def put(self, request, id,  *args, **kwargs):
        data = loads(request.data)
        rarings = list(Rating.objects.filter(id=id).values())
        if len(rarings) > 0:
            rating = Rating.objects.get(id=id)
            rating.score = floor(data['scor'])
            rating.number_of_ratings = data["number_of_ratings"]
            rating.save()
            return Response({'message': "zmieniono ocenę"}, status=status.HTTP_201_CREATED,
                            )
        else:
            return Response(serializers, status=status.HTTP_400_BAD_REQUEST)
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            name_place = serializer.data.get("name")  # Pobierz wartość 'type' z zapisanej instancji
            message = f"Dodano nowe miejsce o nazwie: {name_place}"
            return Response({'message': message}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

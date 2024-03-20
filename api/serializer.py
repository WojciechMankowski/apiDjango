from .models import Comment, Place, Rating, DisabilityType
from rest_framework import serializers


class CommentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", 'content', 'user_name', 'date', "place_id"]

    def create(self, validated_data):
        # Tu możesz dodać niestandardową logikę przed utworzeniem obiektu
        instance = Comment.objects.create(**validated_data)
        # Tu możesz dodać niestandardową logikę po utworzeniu obiektu
        return instance


class DisabilityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DisabilityType
        fields = ['id', 'type', 'description']


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    disability_type_id = DisabilityTypeSerializer(read_only=True)
    comments = CommentSerializers(read_only=True, many=True)

    class Meta:
        model = Place
        fields = ['id', 'name', 'address', 'url_imge',
                  'url_map_google'
                  'ratings',
                  'comments', "disabilitytype", "disability_type_id"]


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    place = PlaceSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'score', 'number_of_ratings', 'place', ]

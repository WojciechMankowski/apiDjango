from .models import Comment, Place, Rating, DisabilityType
from rest_framework import serializers, status


class CommentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", 'content', 'user_name', 'date', "place_id"]


class DisabilityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DisabilityType
        fields = ['id', 'type', 'description']


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", 'score', 'number_of_ratings']


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    disability_type = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='type')

    class Meta:
        model = Place
        fields = "__all__"

#

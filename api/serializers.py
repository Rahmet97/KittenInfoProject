from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Breed, Kitten, Rating


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class KittenSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    breed_id = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all(), source='breed', write_only=True)
    breed = BreedSerializer(read_only=True)

    class Meta:
        model = Kitten
        fields = ['id', 'user', 'color', 'age', 'description', 'breed_id', 'breed']


class RatingGetSerializer(serializers.ModelSerializer):
    kitten = KittenSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ('kitten', 'score', 'user')


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('kitten', 'score')

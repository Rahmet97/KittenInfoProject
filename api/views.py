from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from .models import Breed, Kitten, Rating
from .serializers import BreedSerializer, KittenSerializer, RatingSerializer, RatingGetSerializer
from .documentations import (
    get_data_response_documentation,
    post_data_request_documentation,
    post_data_response_documentation,
    manual_parameters,
    get_detail_response_documentation,
    patch_data_request_documentation,
    put_data_request_documentation,
    rating_request_documentation,
    manual_parameters_rating
)


class BreedListView(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class KittenListView(generics.ListCreateAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        manual_parameters=manual_parameters,
        responses=get_data_response_documentation,
    )
    def get(self, request, *args, **kwargs):
        breed_id = request.query_params.get('breed_id', None)
        if breed_id is not None:
            self.queryset = self.queryset.filter(breed_id=breed_id)
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=post_data_request_documentation,
        responses=post_data_response_documentation
    )
    def post(self, request, *args, **kwargs):
        serializer = KittenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KittenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        responses=get_detail_response_documentation
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=put_data_request_documentation,
        responses={
            **get_data_response_documentation,
            400: 'Bad Request',
            403: 'Forbidden',
        }
    )
    def put(self, request, *args, **kwargs):
        kitten = self.get_object()

        if kitten.user != request.user:
            raise PermissionDenied('You can only update your own kittens.')

        breed_id = request.data.get('breed_id')
        if breed_id:
            kitten.breed_id = breed_id

        serializer = self.get_serializer(kitten, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=patch_data_request_documentation,
        responses={
            **get_data_response_documentation,
            400: 'Bad Request',
            403: 'Forbidden',
        }
    )
    def patch(self, request, *args, **kwargs):
        kitten = self.get_object()

        if kitten.user != request.user:
            raise PermissionDenied('You can only update your own kittens.')

        serializer = self.get_serializer(kitten, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            204: 'No Content',
            403: 'Forbidden',
        }
    )
    def delete(self, request, *args, **kwargs):
        kitten = self.get_object()
        if kitten.user != request.user:
            raise PermissionDenied('You can only delete your own kittens.')
        self.perform_destroy(kitten)
        return Response(status=204)


class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingGetSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=manual_parameters_rating,
        responses={200: rating_request_documentation},
        operation_description="Retrieve a list of ratings."
    )
    def get(self, request, *args, **kwargs):
        kitten_id = request.query_params.get('kitten_id', None)
        if kitten_id is not None:
            self.queryset = self.queryset.filter(kitten_id=kitten_id)
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=RatingSerializer,
        responses={201: rating_request_documentation},
        operation_description="Create a new rating."
    )
    def post(self, request, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)

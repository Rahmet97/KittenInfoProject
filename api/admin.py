from django.contrib import admin
from .models import Kitten, Breed, Rating


admin.site.register((Kitten, Breed, Rating))

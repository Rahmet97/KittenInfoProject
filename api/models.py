from django.contrib.auth.models import User
from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Kitten(models.Model):
    color = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    description = models.TextField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.color} kitten, {self.age} months old"

class Rating(models.Model):
    kitten = models.ForeignKey(Kitten, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    class Meta:
        unique_together = ('kitten', 'user')

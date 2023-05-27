from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    speed = models.IntegerField()
    engine_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.speed}kmh - {self.engine_type}'
    
class Game(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.year} - {self.genre}'

class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name} - {self.genre} - {self.year}'
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()

    def __str__(self) -> str:
        return f"Musician(id={self.id}, last_name={self.last_name})"

    class Meta:
        ordering = ["last_name", "first_name"]


class Venue(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"Venue(if={self.id}, name={self.name})"

    class Meta:
        ordering = ["name"]


class Room(models.Model):
    name = models.CharField(max_length=20)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Room(id={self.id}, name={self.name})"

    class Meta:
        ordering = ["name"]
        unique_together = [["name", "venue"]]


class Band(models.Model):
    name = models.CharField(max_length=20)
    musicians = models.ManyToManyField(Musician)

    def __str__(self) -> str:
        return f"Band(id={self.id}, name={self.name})"

    class Meta:
        ordering = ["name"]

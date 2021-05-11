from django.db import models

# Video URL
from embed_video.fields import EmbedVideoField


class Songs(models.Model):
    CATEGORY_CHOICES = (
        ("Adoracao", "Adoracao"),
        ("Santa Ceia", "Santa Ceia"),
        ("Missoes", "Missoes"),
    )

    ID_Songs = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    singer = models.CharField(max_length=100, help_text="Cantor")
    title = models.CharField(max_length=200)
    lyrics = models.TextField(max_length=2000, help_text="Letra da musica")
    composers = models.CharField(max_length=200, help_text="Compositores/Autores")
    image = models.ImageField(upload_to="img/%y")
    video = EmbedVideoField()

    def __str__(self):
        return self.title

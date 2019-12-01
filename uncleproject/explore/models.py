from django.db import models
import uuid
from django_mysql.models import ListCharField
# Create your models here.

class User(models.Model):
	userID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this user.")
	igName = models.CharField(
        help_text="the user's IG account :"
    )
    userEmail = models.CharField(
        help_text="the user's E-mail account :"
    )
    big5_openness = models.IntegerField()
    big5_conscientiousness = models.IntegerField()
    big5_extraversion = models.IntegerField()
    big5_agreeableness = models.IntegerField()
    big5_neuroticism = models.IntegerField()

    hobby_outdoor = models.IntegerField()
    hobby_water = models.IntegerField()
    hobby_sport = models.IntegerField()
    hobby_music = models.IntegerField()
    hobby_dance = models.IntegerField()
    hobby_photo = models.IntegerField()
    hobby_drama = models.IntegerField()
    hobby_game = models.IntegerField()
    hobby_visual = models.IntegerField()

    imgUrl = ListCharField(base_field = CharField(max_length=10))

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.igName

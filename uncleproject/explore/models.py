from django.db import models
from django.contrib.auth.models import User
import uuid
from .managers import PersonManager
#from django_mysql.models import ListCharField
# Create your models here.

class User(models.Model):
    userID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this user.")
    igName = models.CharField(
        help_text="the user's IG account :",
        max_length=200,
    )
    userEmail = models.CharField(
        help_text="the user's E-mail account :",
        max_length=200,
    )
    big5_openness = models.FloatField()
    big5_conscientiousness = models.FloatField()
    big5_extraversion = models.FloatField()
    big5_agreeableness = models.FloatField()
    big5_neuroticism = models.FloatField()

    hobby_outdoor = models.IntegerField()
    hobby_water = models.IntegerField()
    hobby_sport = models.IntegerField()
    hobby_music = models.IntegerField()
    hobby_dance = models.IntegerField()
    hobby_photo = models.IntegerField()
    hobby_drama = models.IntegerField()
    hobby_game = models.IntegerField()
    hobby_visual = models.IntegerField()

    style_hiking = models.FloatField()
    style_infant = models.FloatField()
    style_studying = models.FloatField()
    style_celebrate = models.FloatField()
    style_firework = models.FloatField()
    style_nightclub = models.FloatField()
    style_sports = models.FloatField()
    style_depressed = models.FloatField()
    style_lonely = models.FloatField()
    style_selfie = models.FloatField()
    style_building = models.FloatField()
    style_delicious = models.FloatField()
    style_books = models.FloatField()


    imgUrl = models.CharField(
        help_text="the profile url:",
        max_length=200,
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.igName

class Group(models.Model):
    groupID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this user.")
    groupName = models.CharField(
        help_text="the group's name :",
        max_length=200,
    )
    hobby_outdoor = models.IntegerField()
    hobby_water = models.IntegerField()
    hobby_sport = models.IntegerField()
    hobby_music = models.IntegerField()
    hobby_dance = models.IntegerField()
    hobby_photo = models.IntegerField()
    hobby_drama = models.IntegerField()
    hobby_game = models.IntegerField()
    hobby_visual = models.IntegerField()

    big5_openness = models.FloatField()
    big5_conscientiousness = models.FloatField()
    big5_extraversion = models.FloatField()
    big5_agreeableness = models.FloatField()
    big5_neuroticism = models.FloatField()

    style_hiking = models.FloatField()
    style_infant = models.FloatField()
    style_studying = models.FloatField()
    style_celebrate = models.FloatField()
    style_firework = models.FloatField()
    style_nightclub = models.FloatField()
    style_sports = models.FloatField()
    style_depressed = models.FloatField()
    style_lonely = models.FloatField()
    style_selfie = models.FloatField()
    style_building = models.FloatField()
    style_delicious = models.FloatField()
    style_books = models.FloatField()
    
    imgUrl = models.CharField(
        help_text="the profile url:",
        max_length=200,
    )

    def __str__(self):
        return self.studentId

class GroupRelation(models.Model):
    userID = models.IntegerField()
    groupID = models.IntegerField()

    def __str__(self):
        return self.groupID



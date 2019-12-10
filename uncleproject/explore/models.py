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

    style_hiking = models.IntegerField()
    style_infant = models.IntegerField()
    style_studying = models.IntegerField()
    style_celebrate = models.IntegerField()
    style_firework = models.IntegerField()
    style_night club = models.IntegerField()
    style_sports = models.IntegerField()
    style_depressed = models.IntegerField()
    style_lonely = models.IntegerField()
    style_selfie = models.IntegerField()
    style_building = models.IntegerField()
    style_delicious = models.IntegerField()
    style_books = models.IntegerField()


    imgUrl = ListCharField(base_field = CharField(max_length=10))

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.igName

class Group(models.Model):
    groupID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this user.")
    groupName = models.CharField(
        help_text="the group's name :"
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

    big5_openness = models.IntegerField()
    big5_conscientiousness = models.IntegerField()
    big5_extraversion = models.IntegerField()
    big5_agreeableness = models.IntegerField()
    big5_neuroticism = models.IntegerField()

    style_hiking = models.IntegerField()
    style_infant = models.IntegerField()
    style_studying = models.IntegerField()
    style_celebrate = models.IntegerField()
    style_firework = models.IntegerField()
    style_night club = models.IntegerField()
    style_sports = models.IntegerField()
    style_depressed = models.IntegerField()
    style_lonely = models.IntegerField()
    style_selfie = models.IntegerField()
    style_building = models.IntegerField()
    style_delicious = models.IntegerField()
    style_books = models.IntegerField()
    
    imgUrl = ListCharField(base_field = CharField(max_length=10))

    def __str__(self):
        return self.studentId

class GroupRelation(models.Model):
    userID = models.IntegerField()
    groupID = models.IntegerField()

    def __str__(self):
        return self.groupID



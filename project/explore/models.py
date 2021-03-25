from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

#from django_mysql.models import ListCharField
# Create your models here.

class myUser(models.Model):
    userID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this user.")
    igName = models.CharField(
        help_text="the user's IG account :",
        max_length=200,
    )
    userEmail = models.CharField(
        help_text="the user's E-mail account :",
        max_length=200,
    )
    total_post = models.IntegerField()

    big5_openness = models.FloatField()
    big5_conscientiousness = models.FloatField()
    big5_extraversion = models.FloatField()
    big5_agreeableness = models.FloatField()
    big5_neuroticism = models.FloatField()

    # hobby_outdoor = models.IntegerField()
    # hobby_water = models.IntegerField()
    # hobby_sport = models.IntegerField()
    # hobby_music = models.IntegerField()
    # hobby_dance = models.IntegerField()
    # hobby_photo = models.IntegerField()
    # hobby_drama = models.IntegerField()
    # hobby_game = models.IntegerField()
    # hobby_visual = models.IntegerField()

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

    style_hiking_like = models.FloatField()
    style_infant_like = models.FloatField()
    style_studying_like = models.FloatField()
    style_celebrate_like = models.FloatField()
    style_firework_like = models.FloatField()
    style_nightclub_like = models.FloatField()
    style_sports_like = models.FloatField()
    style_depressed_like = models.FloatField()
    style_lonely_like = models.FloatField()
    style_selfie_like = models.FloatField()
    style_building_like = models.FloatField()
    style_delicious_like = models.FloatField()
    style_books_like = models.FloatField()

    # hiking_like_percent = models.FloatField()
    # infant_like_percent = models.FloatField()
    # studying_like_percent = models.FloatField()
    # celebrate_like_percent = models.FloatField()
    # firework_like_percent = models.FloatField()
    # nightclub_like_percent = models.FloatField()
    # sports_like_percent = models.FloatField()
    # depressed_like_percent = models.FloatField()
    # lonely_like_percent = models.FloatField()
    # selfie_like_percent = models.FloatField()
    # building_like_percent = models.FloatField()
    # delicious_like_percent = models.FloatField()
    # books_like_percent = models.FloatField()

    user_total_like = models.IntegerField()

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
    total_user = models.IntegerField()
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

    official_hiking_percent = models.FloatField()
    official_infant_percent = models.FloatField()
    official_studying_percent = models.FloatField()
    official_celebrate_percent = models.FloatField()
    official_firework_percent = models.FloatField()
    official_nightclub_percent = models.FloatField()
    official_sports_percent = models.FloatField()
    official_depressed_percent = models.FloatField()
    official_lonely_percent = models.FloatField()
    official_selfie_percent = models.FloatField()
    official_building_percent = models.FloatField()
    official_delicious_percent = models.FloatField()
    official_books_percent = models.FloatField()

    liked_hiking = models.IntegerField()
    liked_infant = models.IntegerField()
    liked_studying = models.IntegerField()
    liked_celebrate = models.IntegerField()
    liked_firework = models.IntegerField()
    liked_nightclub = models.IntegerField()
    liked_sports = models.IntegerField()
    liked_depressed = models.IntegerField()
    liked_lonely = models.IntegerField()
    liked_selfie = models.IntegerField()
    liked_building = models.IntegerField()
    liked_delicious = models.IntegerField()
    liked_books = models.IntegerField()

    def __str__(self):
        return self.groupName

class GroupRelation(models.Model):
    userID = models.IntegerField()
    groupID = models.IntegerField()

    def __str__(self):
        return self.groupID



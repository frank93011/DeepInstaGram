from django.contrib import admin

# Register your models here.
from .models import myUser, Group, GroupRelation

admin.site.register(myUser)
admin.site.register(Group)
admin.site.register(GroupRelation)
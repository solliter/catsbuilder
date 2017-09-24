from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1

    return "%s/%s" %(new_id, filename)

class Cat(models.Model):
    class Meta():
        db_table = "cat"

    paw = models.IntegerField(default=4)
    name = models.CharField(max_length=30, null=False, default='Cat')
    age = models.IntegerField(default=False, null=False)
    species = models.CharField(max_length=50, blank=True)
    hairiness = models.IntegerField(default=False, null=False)
    user = models.ForeignKey('auth.User')
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True,)

    def __str__(self):
        return self.name

class profile(models.Model):
    name = models.CharField(max_length=120)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    description = models.TextField(default="description default text")


    def __str__(self):
        return self.name

def profileCallback(sender, requst, user, **kwags):
    userProfile, is_created = profile.objects.get_or_create(user=user)
    if is_created:
        userProfile.name = user.username
        userProfile.save()


def publish(self):
    self.date = timezone.now()
    self.save()


def __str__(self):
    return self .blog_title

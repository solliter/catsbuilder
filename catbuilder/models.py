from django.db import models

# Create your models here.


class Cat(models.Model):
    class Meta():
        db_table = "cat"

    paw = models.IntegerField(default=4)
    name = models.CharField(max_length=30, null=False, blank=True)
    age = models.IntegerField(default=False, null=False)
    species = models.CharField(max_length=50, blank=True)
    hairiness = models.IntegerField(default=False, null=False, help_text='100 its max')

    def __str__(self):
        return self.name



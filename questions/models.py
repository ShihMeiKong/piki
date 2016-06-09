from django.db import models


# Create your models here.
class Question(models.Model):
    # what you want the question to be
    text = models.CharField(max_length=100)
    # shown on the site or not
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.text
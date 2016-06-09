from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True)
    # image is url string
    image = models.TextField(null=True)
    gender = models.CharField(max_length=10, null=True)


class UserFoodPref(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_peanut = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_lactose = models.BooleanField(default=False)
    is_diabetic = models.BooleanField(default=False)
    is_gluten = models.BooleanField(default=False)
    is_kosher = models.BooleanField(default=False)
    is_alcohol = models.BooleanField(default=False)


class UserMatchPref(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    match_peanut = models.BooleanField(default=False)
    match_vegetarian = models.BooleanField(default=False)
    match_vegan = models.BooleanField(default=False)
    match_lactose = models.BooleanField(default=False)
    match_diabetic = models.BooleanField(default=False)
    match_gluten = models.BooleanField(default=False)
    match_kosher = models.BooleanField(default=False)
    match_alcohol = models.BooleanField(default=False)


class Messages(models.Model):
    # null=True sets all reference objects to null when from_user is deleted
    # two foreign keys need a related_name attribute
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='message_from')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='message_to')
    msg_body = models.TextField()
    created = models.DateField(default=timezone.now)
    # users are not blocked by default, will have to write views logic when user is blocked
    blocked_user = models.BooleanField(default=False)


class Save(models.Model):
    # user who cliked save
    # two foreign keys need a related_name attribute
    user_who_saved = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='save_user_who_saved')
    saved_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='save_saved_user')


# hiding/blocking users
class Hidden(models.Model):
    # two foreign keys need a related_name attribute
    # if Tina 'hides' Kevin in her mathces, Kevin is hidden from Tina's list (hidden_from)
    hidden_from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='hidden_from_user')
    # Subsequently, Tina is hidden "to" Kevin
    hidden_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='hidden_to')

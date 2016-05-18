from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)


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

from django.contrib.auth.models import User
from django.db import models


class UserProfile(User):
    bio = models.TextField()

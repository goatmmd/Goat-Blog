from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(verbose_name='Profile_Pic', upload_to='images/profiles_pic', null=True, blank=True)

    joined_time = models.DateField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"


class UserProfileAttribute(models.Model):
    social = models.CharField(max_length=255, default='URL')
    social_medias = models.ForeignKey(UserProfile, related_name='socials', on_delete=models.CASCADE)

    def __str__(self):
        return self.social

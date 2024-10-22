# myapp/models.py
from django.db import models

# Model for Updates
class Updates(models.Model):
    image = models.ImageField(upload_to='updates_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

# Model for Latest News
class LatestNews(models.Model):
    image = models.ImageField(upload_to='news_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

# Model for Our Team
class OurTeam(models.Model):
    image = models.ImageField(upload_to='team_images/')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    twitter = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# Model for Board Team
class BoardTeam(models.Model):
    name = models.CharField(max_length=100)
    twitter = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

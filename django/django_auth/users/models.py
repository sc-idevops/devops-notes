from django.db import models

class Thought(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50)
    message = models.CharField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.author)

class Like(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    message_id = models.CharField(max_length=50)
    like_count = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.message_id)
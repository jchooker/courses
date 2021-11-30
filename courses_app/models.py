from django.db import models

# Create your models here.
class Description(models.Model):
    notes = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.OneToOneField(Description, related_name="course_desc", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

from django.db import models
from course.models import Course

class Trainee(models.Model):
    name      = models.CharField(max_length=100)
    email     = models.EmailField()
    phone     = models.CharField(max_length=20)
    course    = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    image     = models.ImageField(upload_to='trainee_images/', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)  # Soft Delete flag

    def __str__(self):
        return self.name
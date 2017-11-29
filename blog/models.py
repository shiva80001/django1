from django.db import models
from django.utils import timezone


class post(models.model)
    author = models.Foreignkey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        delf.published_date = timezone.now()
        self.save()
 
    def_str_(self):
       return self.title

# Create your models here.

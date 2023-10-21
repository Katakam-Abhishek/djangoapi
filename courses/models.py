from django.db import models

# Create your models here.
class Course(models.Model):
    name    =   models.CharField(max_length=75)
    language    =   models.CharField(max_length=50)
    price   =   models.CharField(max_length=6)

    def __str__(self) -> str:
        return self.name
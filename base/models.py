from django.db import models

# Create your models here.
class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created = models.TimeField(auto_now_add=True)

    # intergerfields / floatfield

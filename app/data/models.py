from django.db import models


class Plant(models.Model):
    common_name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=300)

    def __str__(self):
        return self.common_name
from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    image = models.URLField()
    release_date = models.DateTimeField(null=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=60, unique=True, db_index=True, verbose_name='URL', blank=True)


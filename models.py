from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Description(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    graph = models.ImageField(blank=True)
    pub_date = models.DateTimeField("date published")
    upd_date = models.DateTimeField("date last updated")
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    image = models.ImageField(upload_to=f'images/', blank=True)

    def __str__(self):
        return self.title




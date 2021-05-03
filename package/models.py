from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=150)
    structure = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.title


class Home(models.Model):
    home = models.CharField(max_length=150)


class Prices(models.Model):
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    periodicity = models.CharField(max_length=150)
    disk_space = models.CharField(max_length=150)
    bandwidth = models.CharField(max_length=150)
    discount = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Prices'

    def __str__(self):
        return self.name
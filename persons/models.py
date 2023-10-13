from django.db import models


class domain(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class subdomain(models.Model):
    domain = models.ForeignKey(domain, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    domain = models.ForeignKey(domain, on_delete=models.SET_NULL, blank=True, null=True)
    subdomain = models.ForeignKey(subdomain, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
    
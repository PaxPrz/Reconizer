from django.db import models

# Create your models here.
class IPv4(models.Model):
    ip = models.CharField(max_length=50)

    def __str__(self):
        return self.ip

class Port(models.Model):
    port = models.IntegerField()
    description = models.CharField(max_length=100)
    vulnerability = models.CharField(max_length=500)

    def __str__(self):
        return str(self.port)

class Domain(models.Model):
    # ip = models.ForeignKey(IPv4, blank=True, null=True, on_delete=models.PROTECT)
    ip = models.ManyToManyField(IPv4)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    entry_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    screenshot = models.ImageField()
    
    def __str__(self):
        return self.name

class SubDomain(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    # ip = models.ForeignKey(IPv4, blank=True, null=True, on_delete=models.PROTECT)
    ip = models.ManyToManyField(IPv4)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    screenshot = models.ImageField()

    def __str__(self):
        return self.name

    
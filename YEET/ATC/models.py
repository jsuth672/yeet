from django.db import models

# Create your models here.

class role(models.Model):
    name = models.CharField(max_length=100)
    isATC = models.BooleanField(default=False)
    isGate = models.BooleanField(default=False)

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100) #TODO: add salt and hash
    role = models.ForeignKey(role)

    def hasATCPerm(self):
        pass
    def hasGatePerm(self):
        pass


class Airport(models.Model):
    name = models.CharField(max_length=100)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

class Plane(models.Model):
    identifier = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    currentPassengerCount = models.IntegerField()
    maxPassengerCount = models.IntegerField()
    airline = models.ForeignKey("Airline")
    gate = models.OneToOneField("Gate")
    runway = models.OneToOneField("Runway")

    def getAriline(self):
        pass
    def getGate(self):
        pass
    def getRunway(self):
        pass

class Runway(models.Model):
    identifier = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    airport = models.ForeignKey(Airport)

    def getPlane(self):
        pass
    def getAirport(self):
        pass

class Airline(models.Model):
    name = models.CharField(max_length=100)
    Airport = models.ManyToManyField("Airport")
    def getPlanes(self):
        pass

class Gate(models.Model):
    identifier = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE())
    def getPlane(self):
        pass
    def getAirport(self):
        pass
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UE(models.Model):
    
    id              = models.AutoField(primary_key=True)
    nom             = models.CharField(max_length=50)
    enseignants     = models.ManyToManyField("Enseignant")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom

class Enseignant(AbstractUser):
    id              = models.AutoField(primary_key=True)
    USERNAME_FIELD  = 'email'
    prenom          = models.CharField(max_length=50)
    email           = models.EmailField(blank=True, unique=True)
    ues             = models.ManyToManyField("UE")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ['username']
    '''def __str__(self):
        return self.nom'''

class Exercice(models.Model):
    
    id              = models.AutoField(primary_key=True)
    nom             = models.CharField(max_length=50)
    ue              = models.ForeignKey("UE", on_delete=models.CASCADE)
    regles          = models.ManyToManyField("Regle")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom

class Regle(models.Model):
    
    id              = models.AutoField(primary_key=True)
    nom             = models.CharField(max_length=50)
    description     = models.TextField(blank=False)
    exercices       = models.ManyToManyField("Exercice")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom
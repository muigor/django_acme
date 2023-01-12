from django.db import models

# Create your models here.
class UE(models.Model):
    
    id              = models.AutoField(primary_key=True)
    nom             = models.CharField(max_length=50)
    enseignants     = models.ManyToManyField("Enseignant")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom

class Enseignant(models.Model):
    
    id              = models.AutoField(primary_key=True)
    nom             = models.CharField(max_length=50)
    prenom          = models.CharField(max_length=50)
    adresse_mail    = models.EmailField(max_length = 254)
    mot_de_passe    = models.CharField(max_length=20)
    ues             = models.ManyToManyField("UE")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom

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
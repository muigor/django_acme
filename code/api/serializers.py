from rest_framework import serializers
from .models import *
import requests
class UESerializer(serializers.ModelSerializer):
    class Meta:
        model = UE
        fields = '__all__'

class EnseignantSerializer(serializers.ModelSerializer):
    #categorie = serializers.ReadOnlyField(source='categorie.type')
    class Meta:
        model = Enseignant
        fields = '__all__'
    
    def validate_id(self, value):
        request = self.context.get("request")
        if request and hasattr(request, "method"):
            method = request.method
        qs = Enseignant.objects.filter(id=value)
        if qs.exists() and request.method == 'POST':
            raise serializers.ValidationError("IdEns deja pris")
        
        return value

class RegleSerializer(serializers.ModelSerializer):
    #client = serializers.ReadOnlyField(source='client.nom')
    #clients = ClientSerializer(many=True, read_only=True)
    #Materiel = serializers.ReadOnlyField(source='Materiel.nom')
    #categorie = serializers.ReadOnlyField(source='categorie.nom')
    class Meta:
        model = Regle
        #fields = ('numero', 'categorie', 'description', 'Materiel','client')
        fields = "__all__"

        
    
    def validate_id(self, value):
        method = None
        request = self.context.get("request")
        if request and hasattr(request, "method"):
            method = request.method
        qs = Regle.objects.filter(id=value)
        
        if qs.exists() and request.method == 'POST':
            raise serializers.ValidationError("Regle déjà associee")
                
        return value

class ExerciceSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Exercice
        fields = '__all__'
        
    def validate_nom(self, value):
        if Exercice.objects.filter(nom=value).exists():
            raise serializers.ValidationError('exerxice already exists')
        return value

class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=200)

    def validate_login(self,value):
        base_url = "https://mi-phpmut.univ-tlse2.fr/~"
        site = "/bassistesCelebres/"
        if len(value) > 20:
            value= value[:20]
        url_index = base_url + value + site + "index.html"
        if requests.get(url_index).status_code != 200:
            print(url_index)
            raise serializers.ValidationError(f"URL incorrecte - le site doit être accessible à l'adresse :\n{base_url}{value}{site}index.html")
        else:
            for dossier in ['images', 'pages', 'styles']:
                if requests.get(base_url + value + site + dossier + '/').status_code != 200:
                    raise serializers.ValidationError(f"Erreur sur le nom de dossier {dossier}")
        return value

        


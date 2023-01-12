from rest_framework import serializers
from .models import *

class UESerializer(serializers.ModelSerializer):
    class Meta:
        model = UE
        fields = '__all__'
    
    def validate_id(self, value):
        method = None
        request = self.context.get("request")
        if request and hasattr(request, "method"):
            method = request.method
        qs = UE.objects.filter(nom__iexact=value)
        if qs.exists() and request.method == 'POST':
            raise serializers.ValidationError("IdUE deja pris")
        
        return value

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
    #salles = SalleSerializer(many=True, read_only=True)
    #salles = serializers.ReadOnlyField(source='salle.numero')
    #salles = SalleSerializer(source='salle_set',many=True, read_only=True)
    class Meta:
        model = Exercice
        #depth = 1
        #fields = ('id', 'nom')
        fields = "__all__"
    
    def validate_id(self, value):
        qs = Exercice.objects.filter(id=value)
        if qs.exists():
            raise serializers.ValidationError("Exercice deja existe")
        
        return value


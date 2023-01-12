from django.shortcuts import render
from rest_framework import generics, status, viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.

# Views de la classe UE
class ueView(generics.ListAPIView):
    queryset = UE.objects.all()
    serializer_class = UESerializer
    
class ueDetailView(APIView):
    serializer_class = UESerializer
    lookup_url_kwarg = 'id'

    def get(self, request):
        id = request.GET.get(self.lookup_url_kwarg)
        if id != None:
            ue = UE.objects.filter(id=id)
            if ue.exists():
                data = UESerializer(ue[0]).data
                return JsonResponse(data, status=status.HTTP_200_OK)
            return JsonResponse({'UE non trouvé': 'Id invalide.'}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)

class ajouterUEView(APIView):
    serializer_class = UESerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            id = serializer.data.get('id')
            
            #what i'm going to add
            queryUE = UE.objects.filter(id=id)
            ex = serializer.data.get('ex')
            queryEx = Exercice.objects.filter(id=ex)
            #queryset = Salle.objects.filter(id=salle)
            queryset = UE.objects.filter(id=id)
            
            if queryset.exists():
                return Response({'Mauvaise requete': 'Données existe deja...'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                ue = ue(id=id,ex=queryEx.first())
                ue.save()
            
                return Response(UESerializer(ue).data, status=status.HTTP_201_CREATED)

        return Response({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)

class supprimerUeView(APIView):
    lookup_url_kwarg = 'id'
    
    def delete(self, request):
        id = request.GET.get(self.lookup_url_kwarg)
        if id != None:
            ue_result = UE.objects.filter(id=id)
            if ue_result.exists():
                ue = ue_result[0]
                ue.delete()
                
                return Response({'Message': 'Success'}, status=status.HTTP_200_OK)
            
            return Response({'UE non trouvé': 'Id invalide.'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)



# ************************************************************************************************
# Views de la classe Regle(Salle)
# ************************************************************************************************

class RegleView(generics.ListAPIView):
    queryset = Regle.objects.all()
    serializer_class = RegleSerializer

class categorieDetailView(APIView):
    serializer_class = RegleSerializer
    lookup_url_kwarg = 'id'

    def get(self, request):
        id = request.GET.get(self.lookup_url_kwarg)
        if id != None:
            regle = Regle.objects.filter(type=type)
            if regle.exists():
                data = RegleSerializer(regle[0]).data
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Regle non trouvée': 'IdRegle invalide.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)

class ajouterRegleView(APIView):
    serializer_class = RegleSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            id = serializer.data.get('id')
            queryset = Regle.objects.filter(id=id)
            if queryset.exists():
                return Response({'Mauvaise requete': 'Données existe deja...'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                regle = Regle(id=id)
                regle.save()
            
                return Response(RegleSerializer(regle).data, status=status.HTTP_201_CREATED)

        return Response({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)

class supprimerRegleView(APIView):
    lookup_url_kwarg = 'id'
    
    def delete(self, request):
        id = request.GET.get(self.lookup_url_kwarg)
        if id != None:
            regle_result = Regle.objects.filter(id=id)
            if regle_result.exists():
                regle = regle_result[0]
                regle.delete()
                
                return Response({'Message': 'Success'}, status=status.HTTP_200_OK)
            
            return Response({'Regle non trouvée': 'IdRegle invalide.'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)


# ************************************************************************************************
# Views de la classe Exercicec(Client)
# ************************************************************************************************

class ExericeView(generics.ListAPIView):
    queryset = Exercice.objects.all()
    serializer_class = ExerciceSerializer

class exerciceDetailView(APIView):
    serializer_class = ExerciceSerializer
    lookup_url_kwarg = 'id'

    def get(self, request):
        id = request.GET.get(self.lookup_url_kwarg)
        if id != None:
            ex = Exercice.objects.filter(id=id)
            if ex.exists():
                data = ExerciceSerializer(ex[0]).data
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Exercice non cree': 'IdExercice invalide.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)

class ajouterExerciceView(APIView):
    serializer_class = ExerciceSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            id = serializer.data.get('id')
            queryset = Exercice.objects.filter(id=id)
            if queryset.exists():
                return Response({'Mauvaise requete': 'Données existe deja...'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                ex = Exercice(id=id)
                ex.save()
            
                return Response(ExerciceSerializer(ex).data, status=status.HTTP_201_CREATED)

        return Response({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)

class supprimerExerciceView(APIView):
    lookup_url_kwarg = 'id'
    
    def delete(self, request):
        id = request.GET.get(self.lookup_url_kwarg)
        if id != None:
            exercice_result = Exercice.objects.filter(id=id)
            if exercice_result.exists():
                ex = exercice_result[0]
                ex.delete()
                
                return Response({'Message': 'Success'}, status=status.HTTP_200_OK)
            
            return Response({'Exercice non trouvé': 'IdExercice invalide.'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)


# ************************************************************************************************
# Views de la classe Enseignant(Categorie)
# ************************************************************************************************
class enseignantView(generics.ListAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class enseignantDetailView(APIView):
    serializer_class = EnseignantSerializer
    lookup_url_kwarg = 'id'

    def get(self, request): #, format=JsonResponse 
        id = request.GET.get(self.lookup_url_kwarg)
        if id != None:
            ens= Enseignant.objects.filter(id=id)
            if ens.exists():
                data = EnseignantSerializer(ens[0]).data
                return JsonResponse(data, status=status.HTTP_200_OK)
            return JsonResponse({'Enseignant(e) non trouvée': 'IdEnseignant invalide.'}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)

class ajouterEnseignantView(APIView):
    serializer_class = EnseignantSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            id = id.data.get('id')
            queryset = Enseignant.objects.filter(id=id)
            if queryset.exists():
                return JsonResponse({'Mauvaise requete': 'Données existe deja...'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                ens = Enseignant(id=id)
                ens.save()
            
                return JsonResponse(EnseignantSerializer(ens).data, status=status.HTTP_201_CREATED)

        return JsonResponse({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)

class supprimerEnseignantView(APIView):
    lookup_url_kwarg = 'id'
    
    def delete(self, request):
        id = request.GET.get(self.lookup_url_kwarg)
        if id != None:
            enseignant_result = Enseignant.objects.filter(id=id)
            if enseignant_result.exists():
                ens = enseignant_result[0]
                ens.delete()
                
                return JsonResponse({'Message': 'Success'}, status=status.HTTP_200_OK)
            
            return JsonResponse({'Enseignant(e) non trouvé(e)': 'IdEnseignant invalide.'}, status=status.HTTP_404_NOT_FOUND)
        
        return JsonResponse({'Mauvaise requete': 'Données invalides...'}, status=status.HTTP_400_BAD_REQUEST)





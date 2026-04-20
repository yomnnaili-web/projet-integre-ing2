from django.contrib import admin
from .models import Domaine, Metier, Question, ChoixReponse, ReponseUtilisateur

@admin.register(Domaine)
class DomaineAdmin(admin.ModelAdmin):
    list_display = ['nom', 'created_at']
    search_fields = ['nom']

@admin.register(Metier)
class MetierAdmin(admin.ModelAdmin):
    list_display = ['nom', 'domaine', 'created_at']
    list_filter = ['domaine']
    search_fields = ['nom', 'description']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['texte', 'ordre']
    ordering = ['ordre']

@admin.register(ChoixReponse)
class ChoixReponseAdmin(admin.ModelAdmin):
    list_display = ['texte', 'question', 'domaine']
    list_filter = ['domaine']

@admin.register(ReponseUtilisateur)
class ReponseUtilisateurAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'choix', 'date_reponse']
    list_filter = ['date_reponse']

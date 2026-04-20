from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('resultats/', views.resultats, name='resultats'),
    path('domaines/', views.domaines_list, name='domaines'),
    path('metiers/', views.metiers_list, name='metiers'),
    path('metiers/<int:domaine_id>/', views.metiers_list, name='metiers_domaine'),
]

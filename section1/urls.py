from django.urls import path
from . import views

urlpatterns = [
    path('', views.section1, name='section1'),
    path('section2/', views.section2, name='section2'),
    path('section3/', views.section3, name='section3'),
    path('section4/', views.section4, name='section4'),
    path('section5/', views.section5, name='section5'),
    path('section6-7/', views.section6, name='section6-7'),

    path('result/', views.result, name='result'),
    path('section8/', views.section8, name='section8'),
    path("company-questionnaire/", views.company_questionnaire, name="company_questionnaire"),
    path("candidate/<int:candidate_id>/", views.candidate_detail, name="candidate_detail"),
    path("save/<int:company_id>/<int:candidate_id>/", views.save_candidate, name="save_candidate"),
    path("saved/<int:company_id>/", views.saved_candidates, name="saved_candidates"),
    path('', views.question_view, name='questions'),
   
]
from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.user_list, name='user-list'),
#   path('visit/', VisitCount.as_view(), name='visit-count'),
    path('add/', views.add_user, name='add-user'),
]

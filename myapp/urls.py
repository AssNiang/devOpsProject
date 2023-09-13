from django.urls import path

from . import views
from .views import UserList

urlpatterns = [
    path('users/', views.user_list, name='user-list'),
    path('user/', UserList.as_view(), name='user-listtest'),
    #   path('visit/', vie, name='visit-count'),
    path('add_user/', views.add_user_api, name='add-api'),
    path('visits/', views.visit_count, name='visit-count'),

]

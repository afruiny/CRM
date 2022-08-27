from unicodedata import name
from django.urls import path 
from leads.views import lead_list
from leads.views import lead_detail
from leads.views import lead_create
from leads.views import lead_delete
from leads.views import lead_update

app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='lead_list'),
    path('<int:pk>/', lead_detail, name='lead_detail'),
    path('<int:pk>/delete/', lead_delete, name='lead_delete'),
    path('<int:pk>/update/', lead_update, name='lead_update'),
    path('create/', lead_create, name='lead_create')
]












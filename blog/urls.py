from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('test/', test, name='testPage'),
    path('cat/<int:category_id>/', get_category, name='categoryPage'),
]
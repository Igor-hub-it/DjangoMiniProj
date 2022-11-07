from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('cat/<int:category_id>/', get_category, name='categoryPage'),
    path('news/<int:post_id>/', view_post, name='view_post'),
]
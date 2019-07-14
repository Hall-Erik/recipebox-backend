from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('api/recipes/', views.RecipeListCreate.as_view(), name='recipe_list_create'),
    path('api/recipes/<id>', views.RecipeRUD.as_view(), name='recipe_rud'),
    path('api/register/', views.RegisterView.as_view(), name='api_register'),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
]
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
# from rest_auth.views import PasswordResetView, PasswordResetConfirmView
from . import views


urlpatterns = [
    path('api/sign_s3/', views.SignS3View.as_view(), name='sign_s3'),

    path('api/recipes/',
         views.RecipeListCreate.as_view(), name='recipe_list_create'),
    path('api/recipes/<id>', views.RecipeRUD.as_view(), name='recipe_rud'),
    path('api/recipes/<id>/made/',
         views.MakeRecipeView.as_view(), name='recipe_make'),

    path('api/register/', views.RegisterView.as_view(), name='api_register'),
    path('api/user/', views.CurrentUserView.as_view(), name='current_user'),

     url(r'^rest-auth/password/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

#     url(r'rest-auth/password/reset/$', PasswordResetView.as_view(), name='password_reset'),
#     url(r'rest-auth/password/reset/confirm/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#          TemplateView.as_view(template_name='recipes/index.html'),
#          name='password_reset_confirm'),
    url(r'rest-auth/', include('rest_auth.urls')),
    
#     url(r'^', include('django.contrib.auth.urls')),
    
    url(r'^.*',
        TemplateView.as_view(template_name='recipes/index.html'), name='home'),
]

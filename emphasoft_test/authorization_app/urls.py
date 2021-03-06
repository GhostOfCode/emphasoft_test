from django.urls import path, include
from .views import Authorization, Profile

urlpatterns = [
    path('auth/', Authorization.as_view()),
    path('', include('social_django.urls')),
    path('', Profile.as_view())
]

from .views import get_frist, get_mostpopular,get_max_wat, get_leastwatch,post_fav
from django.urls import path
urlpatterns=[
     path('frist/',get_frist),
     path('mostpopular /', get_mostpopular ),
     path('wat/',get_max_wat),
     path('watch/',get_leastwatch),
     path('fav/',post_fav),
    


]
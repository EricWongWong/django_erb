from django.urls import path
from . import views

app_name = 'pages'  # Add this line

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about, name='about'),
    # path('login',views.about, name='login'),
]

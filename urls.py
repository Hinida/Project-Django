from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path
from . import views
# from django.contrib.auth.views import login


urlpatterns = [
     path('', views.post_list, name='post_list'),
     path('', views.index_Cats, name='index_Cats'),
	 path('', views.index_Visiteur, name='index_Visiteur'),
	 path('', views.index_Produits, name='index_Produits'),
	 path('', views.index_Users, name='index_Users'),
	 path('', views.index_Profiles_Users, name='index_Profiles_Users'),
	 path('', views.index_Email_Box, name='index_Email_Box'),
	 path('', views.index_Admin, name='index_Admin'),
	 path('', views.index_Profiles_Admin, name='index_Profiles_Admin'),
	 path('', views.index_Command, name='index_Command'),
	 path('', views.index_Comd_Profile, name='index_Comd_Profile'),
	 path('', views.index_Stock, name='index_Stock'),
	 path('', views.index_Cart, name='index_Cart'),
	 path('', views.index_Boite, name='index_Boite'),
	 path('', views.index_Message, name='index_Message'),
     path('',views.connexion,name='connexion'),
     path('', views.login, name='account_login'),
	
]


"""+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"""

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 

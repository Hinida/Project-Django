from django.shortcuts import render
from .models import Post,Cats,Visiteur,Produits,Users,Profiles_Users,Email_Box,Admin,Profiles_Admin,Command,Comd_Profile,Stock,Cart,Boite,Message
from blog import models
from django.contrib.auth import authenticate, login

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'blog/distribution/index.html', locals())

	
def index_Cats(request):
	context={'Cats':models.Cats.objects.all()}
	return render(request,'blog/distribution/index.html', context)
	
def index_Visiteur(request):
	context={'Visiteur':Visiteur.objects.all()}
	return render(request,'blog/distribution/index.html', context)
def index_Produits(request):
	context={'Produits':Produits.objects.all()}
	return render(request,'blog/distribution/index.html', context)
def index_Users(request):
	context={'Users':Users.objects.all()}
	return render(request,'blog/distribution/index.html', context)
def index_Profiles_Users(request):
	context={'Profiles_Users':Profiles_Users.objects.all()}
	return render(request,'blog/distribution/index.html', context)
def index_Email_Box(request):
	context={'Email_Box':Email_Box.objects.all()}
	return render(request,'blog/distribution/index.html', context)
def index_Admin(request):
	context={'Admin':Admin.objects.all()}
	return render(request,'blog/distribution/index.html', context)
def index_Profiles_Admin(request):
	context={'Profiles_Admin':Profiles_Admin.objects.all()}
	return render(request,'blog/distribution/index.html', context)
def index_Command(request):
	context={'Command':Command.objects.all()}
	return render(request,'blog/distribution/index.html', context)	
def index_Comd_Profile(request):
	context={'Comd_Profile':Comd_Profile.objects.all()}
	return render(request,'blog/distribution/index.html', context)
def index_Stock(request):
	context={'Stock':Stock.objects.all()}
	return render(request,'blog/distribution/index.html', context)
def index_Cart(request):
	context={'Cart':Cart.objects.all()}
	return render(request,'blog/distribution/index.html', context)
def index_Boite(request):
	context={'Boite':Boite.objects.all()}
	return render(request,'blog/distribution/index.html', context)	
def index_Message(request):
	context={'Message':Message.objects.all()}
	return render(request,'blog/distribution/index.html', context)		
	
	
def post_list(request):
	context={'Posts':Post.objects.all()}
	return render(request,'blog/distribution/index.html', context)




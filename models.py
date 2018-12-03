from django.db import models
from django.utils import timezone


class Post(models.Model):
         author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
         title = models.CharField(max_length=200)
         text = models.TextField()
         created_date = models.DateTimeField(default=timezone.now)
         published_date = models.DateTimeField(blank=True,null=True)
         def publish(self):
             self.published_date = timezone.now()
             self.save()
         def __str__(self):
             return self.title
class Cats(models.Model):
        CatId =models.CharField(auto_created=True,primary_key=True,max_length=4)
        Cat =models.CharField(max_length=30)
       
        def __str__(self) :
              return self.Cat
	
	# def __str__(self):return self.CatId;

class Visiteur(models.Model):
       VisiteurId=models.AutoField(auto_created=True,primary_key=True,max_length=11)
       visite=models.IntegerField()

class Produits(models.Model):
       CatId=models.ForeignKey(Cats,on_delete=models.CASCADE,max_length=4)
       Poduct_cat=models.CharField(max_length=30)
       Product_id=models.CharField(auto_created=True,primary_key=True,max_length=30)
       Product_name=models.CharField(max_length=30)
       Product_desc=models.CharField(max_length=99)
       Product_price=models.IntegerField()
	   
		
class Users(models.Model):
       uid=models.AutoField(auto_created=True,primary_key=True,max_length=11)
       uname=models.CharField(max_length=30)
       email1=models.CharField(max_length=30)
       upass=models.CharField( max_length=30)
       Sec_name=models.CharField(max_length=50)
       Date_inscrit=models.DateTimeField(default=timezone.now)

class Profiles_Users(models.Model):
       ID=models.AutoField(auto_created=True,primary_key=True,max_length=11)
       uid=models.ForeignKey(Users,on_delete=models.CASCADE,max_length=11)
       Product_id=models.ForeignKey(Produits,on_delete=models.CASCADE,max_length=30)



#class Stock(models.Model):

# Create your models here.
class Email_Box(models.Model):
       uid=models.ForeignKey(Users,on_delete=models.CASCADE)
       email=models.CharField(max_length=30)
       subject=models.CharField(max_length=30)
       msg=models.CharField(max_length=210)
       fichier=models.CharField(max_length=99)
       Date_send=models.DateTimeField(default=timezone.now)
       tel=models.CharField(max_length=30)
class Admin(models.Model):
       admin_id=models.AutoField(auto_created=True,primary_key=True,max_length=11)
       admin_name=models.CharField(max_length=30)
       admin_email=models.CharField(max_length=30)
       admin_pass=models.CharField(max_length=99)
class Profiles_Admin(models.Model):
       admin_id=models.ForeignKey(Admin,on_delete=models.CASCADE,max_length=11)
       adresse=models.CharField(max_length=30)
       email=models.CharField(max_length=30)
       tel=models.CharField(max_length=30)
       sexe=models.CharField(max_length=30)
       ville=models.CharField(max_length=30)
class Command(models.Model):
       id_cmd=models.AutoField(auto_created=True,primary_key=True,max_length=11)
       uid=models.ForeignKey(Users,on_delete=models.CASCADE,max_length=11)
       Date_send=models.DateTimeField(default=timezone.now)
       status=models.CharField(max_length=30)
class Comd_Profile(models.Model):
       id_cmd=models.ForeignKey(Command,on_delete=models.CASCADE,max_length=11)
       Product_id=models.ForeignKey(Produits,on_delete=models.CASCADE,max_length=11)
       qty=models.IntegerField(max_length=11)       
       Product_img=models.CharField(max_length=30) 
class Stock(models.Model):
       Product_id=models.ForeignKey(Produits,on_delete=models.CASCADE,max_length=99)              
       Product_stock=models.IntegerField(max_length=11) 
class Cart(models.Model):
       id_cart=models.AutoField(auto_created=True,primary_key=True,max_length=11)
       Order_id=models.CharField(max_length=99)
       Product_id=models.ForeignKey(Produits,on_delete=models.CASCADE,max_length=99)
       Product_qty=models.IntegerField()
       Order_by=models.CharField(max_length=99)
       date=models.DateTimeField(default=timezone.now)
class Boite(models.Model):
       id_boite=models.AutoField(auto_created=True,primary_key=True,max_length=11)
       uid=models.ForeignKey(Users,on_delete=models.CASCADE,max_length=11)
class Message(models.Model):
       id_boite=models.ForeignKey(Boite,on_delete=models.CASCADE,max_length=11)
       uid_envoyer=models.IntegerField()
       email=models.CharField(max_length=99)
       subject=models.CharField(max_length=30)
       msg=models.CharField(max_length=210)
       fichier=models.CharField(max_length=99)
       Date_send=models.DateTimeField(default=timezone.now)
             


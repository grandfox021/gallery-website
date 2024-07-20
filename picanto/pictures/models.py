from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model) : 
    user = models.OneToOneField(User,null = True ,blank = True, on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=255)
    profile_pic = models.ImageField(default = "profile_pictures/profile_default_picture.jpg",null = True , blank = True)
    date_created = models.DateTimeField(auto_now_add= True , null= True)

    def __str__(self) :
        
        return self.name


class Category(models.Model) :

    
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) :

        return self.name
    

class Customer_Picture(models.Model) :
    


    PRICE_OPTIONS = (

        ('free' , 'Free'),
        ('paid' , 'Paid'),
    )

    category = models.ForeignKey(Category ,on_delete=models.CASCADE, null=True , blank=True)
    description = models.CharField(max_length=200,blank = True)
    customer = models.ForeignKey(Customer ,null=True,on_delete=models.SET_NULL)
    photo = models.ImageField()
    photo_name = models.CharField(max_length=255,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add= True , null= True)
    price = models.CharField(max_length=255,choices=PRICE_OPTIONS,default="Free", null=True)

    def __str__(self) :
        
        return "({}) : ".format(self.customer) +  self.description
    


class Price(models.Model) :

    float_price = models.FloatField(max_length=50 ,blank=True , null=True)
    discounted_price = models.FloatField(max_length=50 ,blank=True , null=True)


class Comment(models.Model) : 

    commenter_name = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    photo = models.ForeignKey(Customer_Picture,on_delete=models.DO_NOTHING,)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) :

        return '%s - %s' % (self.photo.description , self.commenter_name)

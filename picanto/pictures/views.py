from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import Group,User
from .forms import LoginForm,CreateUserForm,ImageForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import Comment_Form
import datetime
# Create your views here.

from .models import *

def homepage(request) : 

    context = {}
    
    return render(request,'base_site/home.html',context)


def register_login(request) :
    
    registerform = CreateUserForm()  
    if request.method == 'POST' and 'signup' in request.POST:
        registerform = CreateUserForm(request.POST)
        if registerform.is_valid() :
            registerform.save()
            username = registerform.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + username)
            return redirect("homepage")
        else :
            messages.error(request, "Unsuccessful registration. Invalid information.")

        registerform = CreateUserForm()    
            
#-------------------------------loginform---------------------------------#

    loginform = LoginForm()            
    if request.method == "POST" and 'signin' in request.POST:
        loginform = LoginForm(data=request.POST)
        if loginform.is_valid():
            
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            
            if user is not None:
                
                login(request,user)
                
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request,"Invalid username or password.")

        loginform = LoginForm()            

            
#-------------------------end of login form---------------------------------------- #   
    context = {
        
        'registerform' : registerform,
        'loginform' : loginform
            
            }
  
    return render(request,'base_site/register.html',context)


# def login(request) :

#     context = {}
    
#     return render(request,'register.html',context)


def logout_request(request) :
    
    logout(request)
    
    return redirect('register')

def display_all_pictures(request) :

    all_pictures = Customer_Picture.objects.all()
    categories = Category.objects.all()
    category = request.GET.get('category')

    if category == None :

        category = Category.objects.all()
        all_pictures = Customer_Picture.objects.all()
    
    else :

        all_pictures = Customer_Picture.objects.filter(category__name__contains = category)



    context = {

        'all_pictures' : all_pictures,
        'categories' : categories,

    }

    return render(request,'pictures_section/all_pictures.html',context)


def customer_profile_view(request,pk) :

    customer = Customer.objects.get(id=pk)

    context = {
    
        'customer' : customer,
        
    }

    return render(request,"base_site/customer_profile_page.html",context)
    

def get_customer_pics(request,pk) :

    categories = Category.objects.all()
    customer_name = Customer.objects.get(id=pk)
    customer_picture = Customer_Picture.objects.filter(customer=customer_name)
    print(customer_name)
    print(customer_picture)

#################################
    category = request.GET.get('category')

    if category == None :

        category = categories
        customer_filtered_pics = customer_picture
    
    else :

        customer_filtered_pics = Customer_Picture.objects.filter(category__name__contains = category,customer=customer_name)
#################################

    context = {
        
        'categories' : categories,
        'category' : category,
        'customer_picture' : customer_picture,   
        'customer_filtered_pics' : customer_filtered_pics,
        
              }

    return render(request, "pictures_section/my_pictures.html", context)

def upload_pic(request,pk) : 

    customer = Customer.objects.get(id=pk)
    prices = Customer_Picture.price
    customer_picture = Customer_Picture.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST' and "uploadbutton" in request.POST :

        description = request.POST.get('description')
        photo = request.FILES.get('photo')

        if request.POST['category'] != 'none' :

            category = Category.objects.get(id = request.POST['category'])

        elif request.POST['category_new'] != '' :

            category , created = Category.objects.get_or_create(name = request.POST['category_new'])

        else : 

            category = None


        picture = Customer_Picture.objects.create(

                customer = customer,
                photo = photo,
                description= description,
                category = category,


        )



    context = {

        'categories' : categories ,
        'customer_picture' : customer_picture ,
        'prices' : prices
    }

    return render(request,"base_site/upload_form.html",context)


    
def view_picture(request,pk) :
    picture = Customer_Picture.objects.get(id=pk)
    comments = Comment.objects.filter(photo=picture)

    if request.method == 'POST' and "comment_submit_button" in request.POST :
        photo = Customer_Picture.objects.get(id=pk)
        name = request.user.customer
        body = request.POST.get('comment_body')

        #body = form.cleaned_data['comment_body']

        comment = Comment(photo=photo,commenter_name = name,comment_body = body,date_added = datetime.datetime.now())

        comment.save()

        

    context = {

        'picture' : picture ,
        'comments' : comments ,

    }

    return render(request,'base_site/view_picture.html',context)







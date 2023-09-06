from account.forms import RegistratioinForm,LoginForm,ProfileForm
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Wishlist
from product.models import Product

# Create your views here.
def usersignup(request):
    if request.method =='POST':
        form = RegistratioinForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')         
    else:
        form = RegistratioinForm()
    return render(request,'signup.html',{'form':form})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page, e.g., user's profile
            return redirect('home')
        
    return render(request, 'login.html')
# def user_login(request):
#     if request.method =='POST':
#         form = LoginForm(request,request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request,username=name,password=password)
#             print(form.cleaned_data)
#             if user is not None:
#                 login(request,user)
#                 return redirect('home')
#             else:
#                 pass
#     else:
#         form = LoginForm()
#     return render(request,'login.html',{'form':form})
@login_required           
def profile(request, id):
    user_profile =User.objects.get(pk=id) 
    print(user_profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('profile',user_profile.id)
    else:
        form = UserCreationForm(instance=user_profile)
    return render(request, 'profile.html', {'form': form})
    
def userLogout(request):
    logout(request)
    return redirect('home')




def wishlist_view(request):
    if not request.user.is_authenticated:
        return redirect('login') 

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    return render(request, 'wishlist.html', {'wishlist': wishlist})

def add_to_wishlist(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login') 

    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.items.add(product)

    return redirect('wishlist')

def remove_from_wishlist(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')  

    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.items.remove(product)

    return redirect('wishlist')

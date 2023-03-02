from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

from django.shortcuts import render,redirect
from django.db.models import Q
# Create your views here.
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm,LoginForm,GalleryForm
from django.contrib.auth import authenticate,login,logout
from .models import Gallery
def regsier_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    context = {}
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.username = request.POST.get('email')
        form.password = make_password(request.POST.get('password'))
        form.save()
        return redirect('login')
        print("done>>>>>>>>>>>>>>>>>>>>>")
    context['form'] = form
    return render(request,"students/register.html",context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    context = {}
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        print(user)

        if user:
            login(request,user)
            return redirect('/')
        else:
            print("Failed")
    context['form'] = form
    return render(request,"students/login.html",context)


def dashboard_view(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.user.user_type == "admin":
        gallery = Gallery.objects.filter()
    if request.user.user_type=="teacher":
        gallery=Gallery.objects.filter(
            Q(Q(user=request.user) | Q(user__user_type='student'))

        )
    if request.user.user_type == "student":
        gallery = Gallery.objects.filter(user=request.user
        )

    form = GalleryForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        print(form.data)
        form= form.save(commit=False)
        form.user=request.user
        form.save()
        return redirect('/')
        context['msg']="Gallery Uplaod successfully"



    context['gallery'] = gallery
    context['form'] = form
    return render(request,"students/dashboard.html",context)



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/login")
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from productstore import forms
from productstore.models import mobiles
from productstore.decorators import signinRequired
from django.views.generic import View,CreateView,TemplateView,ListView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
from productstore.models import User


def add_phone(request):
        form=forms.phoneForm()
        context={"form":form}
        if request.method=="POST":
            form=forms.phoneForm(request.POST,files=request.FILES)
            if form.is_valid():
                mobile=mobiles(phone_name=form.cleaned_data["phone_name"],
                               processor=form.cleaned_data["processor"],
                               ram=form.cleaned_data["ram"],
                               price=form.cleaned_data["price"])
                form.save()
                return redirect("display_phone")
            else:
                context={"form":form}
                return render(request, "addphone.html", context)
        return render(request, "addphone.html", context)

# class addPhone(CreateView):
#     template_name = "addphone.html"
#     model = mobiles
#     form_class =forms.phoneForm
#     success_url = reverse_lazy("display_phone")



@signinRequired
def display(request):
    phones = mobiles.objects.all()
    form=forms.PhoneSearch()
    context = {"products": phones,'form':form}
    if request.method=='POST':
        form=forms.PhoneSearch(request.POST)
        if form.is_valid():
            p_name=form.cleaned_data['phone_name']
            phone=mobiles.objects.filter(phone_name__contains=p_name)
            form=forms.PhoneSearch()
            context={'products':phone,'form':form}
            return render(request, "display.html", context)

    return render(request,"display.html", context)

# class display_phone(ListView):
#     template_name = "display.html"
#     model = mobiles
#     context_object_name ="products"





@signinRequired
def view(request,id):
    phone=mobiles.objects.get(id=id)
    return render(request,"view_list.html",{"phone":phone})

# class View(DetailView):
#     model = mobiles
#     template_name = "view_list.html"
#     context_object_name = "phone"
#     pk_url_kwarg = "id"



#
@signinRequired
def ownerpage(request):
    return render(request,"owner_home.html")
#
# class ownerhome(TemplateView):
#     template_name = "owner_home.html"




@signinRequired
def change_phone(request,id):
    item=mobiles.objects.get(id=id)
    phone={
        "phone_name":item.phone_name,
        "processor":item.processor,
        "ram":item.ram,
        "price":item.price
    }
    form=forms.phoneForm(instance=item)
    if request.method=="POST":
        form=forms.phoneForm(request.POST,instance=item,files=request.FILES)
        if form.is_valid():
            form.save()
            phone=mobiles.objects.get(id=id)
            phone_name=form.cleaned_data["phone_name"]
            processor=form.cleaned_data["processor"]
            ram=form.cleaned_data["ram"]
            price=form.cleaned_data["price"]
            phone.phone_name=phone_name
            phone.processor = processor
            phone.ram = ram
            phone.price = price

            return redirect("display_phone")
        else:
            return render(request,"edit_phone.html",{"form":form})
    return render(request,"edit_phone.html",{"form":form})

# class changePhone(UpdateView):
#     model = mobiles
#     template_name = "edit_phone.html"
#     form_class = forms.phoneForm
#     context_object_name = "form"
#     success_url = reverse_lazy("display_phone")
#     pk_url_kwarg = "id"




#
@signinRequired
def remove_phone(request,id):
    phone=mobiles.objects.get(id=id)
    phone.delete()
    return redirect("display_phone")

# class remove_phone(View):
#     model = mobiles
#     def get(self,request,*args,**kwargs):
#         id=kwargs["id"]
#         phone=mobiles.objects.get(id=id)
#         phone.delete()
#         return redirect("display_phone")



def UserRegistrationForm(request):
    form=forms.UserRegForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            print("account has been created")
            return redirect("login")
        else:
            context={'form':form}
            return render(request, 'registration.html', context)
    return render(request,'registration.html',context)


# class userRegistrationForm(CreateView):
#     model = User
#     form_class = forms.UserRegForm
#     template_name = "registration.html"
    success_url = reverse_lazy("login")

def Signin(request):
    form=forms.SignIn()
    context={'form':form}
    if request.method=='POST':
        form=forms.SignIn(request.POST)
        if form.is_valid():
            uname=form.cleaned_data["username"]
            password=form.cleaned_data['password']
            user=authenticate(request,username=uname,password=password)
            if user:
                login(request,user)
                return redirect("ownerpage")
            else:
                context = {'form': form}
                return render(request,'login.html',context)
    return render(request,'login.html',context)


# class SignIn(TemplateView):
#     model=User
#     template_name = "login.html"
#     context={}
#
#     def get(self,request,*args,**kwargs):
#         context=super().get_context_data(**kwargs)
#         form=forms.SignIn()
#         context["form"]=form
#         return  context
    #
    def post(self,request,*args,**kwargs):
        form=forms.SignIn(request.POST)
        if form.is_valid():
            uname=form.cleaned_data["username"]
            pswd=form.cleaned_data["password"]
            user=authenticate(usename=uname,password=pswd)
            if user:
                    login(request,user)
                    return redirect("ownerpage")






def SignOut(request):
    logout(request)
    return redirect('login')

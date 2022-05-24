from django.shortcuts import render, redirect
from customer import forms
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, ListView
from mobile.models import Mobile, Cart,Orders
from django.contrib import messages


class CHome(TemplateView):
    def get(self, request, *args, **kwargs):
        mobiles = Mobile.objects.all()
        context = {"mobiles": mobiles}
        return render(request, "c_home.html", context)


# def c_home(request):
#     return render(request, "c_home.html")

class SignUpView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm()
        context = {"form": form}
        return render(request, "userregistration.html", context)

    def post(self, request):
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User has been created")
            return redirect("signin")


# def sign_up(request):
#     form = forms.UserRegistrationForm()
#     context = {"form": form}
#     if request.method == "POST":
#         form=forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("user has been created")
#             return redirect("signin")
#
#     return render(request,"userregistration.html",context)

class SignInVIew(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()

        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "login.html", {"form": form})


# def sign_in(request):
#     form=forms.LoginForm()
#     if request.method=="POST":
#         context={"form":form}
#         form=forms.LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data["username"]
#             password=form.cleaned_data["password"]
#
#             user=authenticate(request,username=username,password=password)
#
#             if user:
#                 login(request,user)
#                 return redirect("home")
#             else:
#                 return render(request,"login.html",context)
#     return render(request, "login.html", {"form": form})

def sign_out(request):
    logout(request)
    return render("signin")


class AddToCart(TemplateView):
    model=Cart
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        mobile=Mobile.objects.get(id=id)
        cart=Cart.objects.create(item=mobile,user=request.user)
        cart.save()
        print("Item added to cart")
        return redirect("customer")

class ViewCart(ListView):
    model = Cart
    template_name = "mycartitems.html"

    def get(self, request, *args, **kwargs):
        context = {}
        items = Mobile.objects.filter(user=request.user)
        print(items)
        context["items"] = items
        return render(request, self.template_name, context)


class RemoveCartItem(TemplateView):
    model = Cart

    def get(self, request, *args, **kwargs):
        kwargs["id"] = id
        cart = self.model.objects.get(id=id)
        cart.status = "cancelled"
        cart.save()
        messages.succes(request,"item has been removed from cart")
        return redirect("home")

class MyOrderView(ListView):
    template_name = "myorders.html"
    model = Orders
    context_object_name = "orders"
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset

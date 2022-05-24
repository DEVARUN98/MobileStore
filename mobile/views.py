from django.shortcuts import render, redirect
from mobile.forms import Mobform
from mobile.models import Mobile, Cart, Orders
from django.views.generic import TemplateView, DetailView, ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy


class MobAddView(CreateView):
    model = Mobile
    form_class = Mobform
    template_name = "mob_add.html"
    success_url = reverse_lazy("addmob")


# def AddMob(request):
#     if request.method=="GET":
#         form=Mobform(initial={"price":0,"count":0})
#         context={}
#         context["form"]=form
#         return render(request,"Mob_add.html",context)
#
#     if request.method=="POST":
#         form=Mobform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             # brand=form.cleaned_data["brand"]
#             # m_name=form.cleaned_data["mob_name"]
#             # price=form.cleaned_data["price"]
#             # count=form.cleaned_data["count"]
#             # mobiles=Mobile.objects.create(brand=brand,mob_name=m_name,price=price,count=count)
#             # mobiles.save()
#             return redirect("addmob")
#         else:
#             return render(request,"Mob_add.html",{"form":form})

def home(request):
    return render(request, "home.html")


class MobListView(ListView):
    model = Mobile
    template_name = "list_mobile.html"
    context_object_name = "mobiles"


# def list(request):
#     mobiles=Mobile.objects.all()
#     context={}
#     context["mobiles"]=mobiles
#     return render(request,"list_mobile.html",context)
class MobDelete(DeleteView):
    model = Mobile
    template_name = "mobileremove.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listmob")


# def delete(request,id):
#     mobiles=Mobile.objects.get(id=id)
#     mobiles.delete()
#     return redirect("listmob")

class MobEditView(UpdateView):
    model = Mobile
    form_class = Mobform
    template_name = "edit_mobile.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listmob")


# def edit(request,id):
#     mobiles=Mobile.objects.get(id=id)
#     if request.method=="GET":
#         form=Mobform(instance=mobiles)
#         # form=Mobform(initial={
#         #     "brand":mobiles.brand,
#         #     "mob_name":mobiles.mob_name,
#         #     "price":mobiles.price,
#         #     "count":mobiles.count
#         #
#         # })
#         context={}
#         context["form"]=form
#         return render(request,"edit_mobile.html",context)
#
#     if request.method=="POST":
#         form=Mobform(request.POST,instance=mobiles)
#         if form.is_valid():
#             form.save()
#             # brand=form.cleaned_data["brand"]
#             # mob_name=form.cleaned_data["mob_name"]
#             # price=form.cleaned_data["price"]
#             # count=form.cleaned_data["count"]
#             # mobiles.brand=brand
#             # mobiles.mob_name=mob_name
#             # mobiles.price=price
#             # mobiles.count=count
#             # mobiles.save()
#             return redirect("listmob")


class MobileDetailView(DetailView):
    model = Mobile
    template_name = "mobile_details.html"
    pk_url_kwarg = "id"
    context_object_name = "mobiles"


# def mobile_details(request,id):
#     mobiles=Mobile.objects.get(id=id)
#     context={}
#     context["mobiles"]=mobiles
#     return render(request,"mobile_details.html",context)

class C_Order(ListView):
    model = Orders
    template_name = "customerorders.html"
    # context_object_name = ""

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        neworders = Orders.objects.filter(status="orderplaced")
        context["neworders"]=neworders
        context["neworder_count"]=neworders.count()
        return context

        d_orders = Orders.objects.filter(status="delivered")
        context["d_orders"]=d_orders
        context["d_order_count"]=d_orders.count()
        return context



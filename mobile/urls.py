from django.urls import path
from mobile import views

urlpatterns = [
    path("", views.home, name="home"),
    path("mobadd", views.MobAddView.as_view(), name="addmob"),
    path("list", views.MobListView.as_view(), name="listmob"),
    path("delete/<int:id>", views.MobDelete.as_view(), name="delete"),
    # oru particular value mathram kanikan aaan ID kodukkunnath
    path("edit/<int:id>", views.MobEditView.as_view(), name="edit"),
    path("view/<int:id>", views.MobileDetailView.as_view(), name="viewmobile"),
    path("c_orders", views.C_Order.as_view(), name="c_orders"),

]

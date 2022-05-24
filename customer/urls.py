from django.urls import path
from customer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("home",views.CHome.as_view(),name="home"),
    path("user/signup",views.SignUpView.as_view(),name="useradd"),
    path("user/signin",views.SignInVIew.as_view(),name="signin"),
    path("user/signout",views.sign_out,name="signout"),
    path("viewcart",views.ViewCart.as_view(),name="viewcart"),
    path("addtocart/<int:id>",views.AddToCart.as_view(),name="addtocart"),
    path("remove/<int:id>",views.RemoveCartItem.as_view(),name="removeitem"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
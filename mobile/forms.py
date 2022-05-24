from django import forms
from mobile.models import Mobile
from django.forms import ModelForm

# class Mobform(forms.Form):
#     brand=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
#     mob_name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
#     count=forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()
#         price=cleaned_data["price"]
#         count=cleaned_data["count"]
#
#         if price<0:
#             msg="Invalid price"
#             self.add_error("price",msg)
#
#         if count<0:
#             msg="invalid count"
#             self.add_error("count",msg)
#
class Mobform(ModelForm):
    class Meta:
        model=Mobile
        fields=["brand","mob_name","price","count","image"]
        widgets={
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "mob_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "count":forms.NumberInput(attrs={"class":"form-control"})
        }

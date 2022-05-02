from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shop index home"),
    path("About/", views.about, name="shop about "),
    path("Contact/", views.contacts, name="shop contact"),
    path("Status/", views.Status, name="shop status"),
    path("Cart/", views.Cart, name="shop carts"),
    path("Checkout/", views.checkouts, name="Checkout forms"),
    path("Payment/", views.Payment, name="Payment forms"),
    path("Products/<int:my_id>", views.products, name="shop Products"),

]

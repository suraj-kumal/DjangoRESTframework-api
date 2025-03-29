from django.urls import path
from . import views

urlpatterns = [
    path("", views.getdata),
    path("add/", views.addItem),
    path("<int:id>", views.getSingleItem),
    path("delete/<int:id>", views.deleteItem),
    path("update/<int:id>", views.updateItem),
]

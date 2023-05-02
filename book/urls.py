from django.urls import path
from.import views

urlpatterns=[
    path("name/",views.name, name="name"),
    path("contact/",views.contact,name= "contact"),
    path("view_contact/", views.view_contact , name= "view_contact"),
    path("Edit_contact/" , views.Edit_contact, name= "Edit_contact"),
    path("edit/" , views.edit , name="edit"),
    path("Delete_contact/", views.Delete_contact, name="Delet_contact"),
    path("contact_code/", views.contact_code , name="contact_code")
]
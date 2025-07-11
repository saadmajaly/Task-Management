from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Default_Redirect, name="home"),
    path("<int:sort>", views.home),
    path("addp/", views.addtemp),
    path("addp/add", views.add),
    path("edit/<int:id>/", views.edittemp, name="edit"),
    path("edit/<int:id>/conf/", views.edit, name="conf"),
    path("delete/<int:id>/", views.deleteT, name="delete"),
    path("today/", views.today, name="today"),
    path("today/<int:sort>", views.today),
]

from django.urls import path

from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'category/<slug:parent_slug>/',
        views.menu_item,
        name='parent'
    ),
    path(
        'category/<slug:parent_slug>/<slug:child_slug>/',
        views.menu_item,
        name='child'
    ),
]

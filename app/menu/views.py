from django.shortcuts import render
from menu.models import Menu

def index(request):
    parent_menus = Menu.objects.filter(parent=None)
    return render(request, 'index.html', {'parent_menus': parent_menus})

def menu_item(request, parent_slug, child_slug=None):
    parent_menu = Menu.objects.get(slug=parent_slug)
    return render(request, 'index.html', {'parent_menu': parent_menu})

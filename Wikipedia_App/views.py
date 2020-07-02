from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    return render(request, "index.html",)

def about(request):
    return render(request, "about.html",)

def show(request):
    items = Item.objects.all()
    return render(request, "show.html", {"all_items": items})

def insert(request):
    return render(request, "insert.html",)

def upload(request):
    if request.method == "POST":
        form = ItemForm(request.POST or none)
        if form.is_valid():
            form.save()
            return redirect("show")

        else:
            return insert(request)

def details(request, Item_id):
    item = Item.objects.get(pk=Item_id)
    return render(request, "details.html", {'item': item})


def delete(request, Item_id):
    item = Item.objects.get(pk=Item_id)
    item.delete()
    return redirect("show")

def edit(request, Item_id):
    item = Item.objects.get(pk=Item_id)
    return render(request, "edit.html", {'item': item})

def edit_upload(request, Item_id):
    if request.method == "POST":
        item = Item.objects.get(pk=Item_id)
        form = ItemForm(request.POST or none, instance=item)
        if form.is_valid():
            form.save()
            return redirect("show")

        else:
            return insert(request)

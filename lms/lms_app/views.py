from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
from .forms import BookForm
# Create your views here.


def index(request):
    context = {
        'books': Book.objects.all(),
        'category': Category.objects.all(),
        'form': BookForm()
    }
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index') 

    return render(request, "pages/index.html", context)

def books(request):
    context = {
        'books': Book.objects.all(),
        'category': Category.objects.all(),
    }
    return render(request, "pages/books.html", context)
    

def delete(request):
    context ={
        'category': Category.objects.all(),
    }
    return render(request, "pages/delete.html", context)


def update(request):
    context ={
        'category': Category.objects.all(),
    }
    return render(request, "pages/update.html", context)



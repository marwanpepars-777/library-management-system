from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
from .forms import BookForm, CategoryForm
# Create your views here.


def index(request):
    context = {
        'books': Book.objects.all(),
        'category': Category.objects.all(),
        'form': BookForm(),
        'formcat': CategoryForm(),
    }
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        formcat = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        if formcat.is_valid():
            formcat.save()
            return redirect('index')


    return render(request, "pages/index.html", context)

def books(request):
    context = {
        'books': Book.objects.all(),
        'category': Category.objects.all(),
        'formcat': CategoryForm(),
    }
    if request.method == 'POST':
        formcat = CategoryForm(request.POST)
        if formcat.is_valid():
            formcat.save()
            return redirect('books')

    return render(request, "pages/books.html", context)
    

def delete(request, id):
    book = Book.objects.get(id=id)
    context ={
        'category': Category.objects.all(),
        'formcat': CategoryForm(),
    }
    if request.method == 'POST':
        formcat = CategoryForm(request.POST)
        if formcat.is_valid():
            formcat.save()
            return redirect('index')
    if request.method == 'POST':
        book.delete()
        return redirect('index')
    return render(request, "pages/delete.html", context)


def update(request, id):
    book = Book.objects.get(id=id)
    
    form = BookForm(instance=book)
    
    if request.method == 'POST':
        formcat = CategoryForm(request.POST)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('update')
        if formcat.is_valid():
            formcat.save()
            return redirect('update')
    else:
        form = BookForm(instance=book)

    context ={
        'category': Category.objects.all(),
        'formcat': CategoryForm(),
        'form': form,
    }

    return render(request, "pages/update.html", context)



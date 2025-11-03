from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Book

def home(request):
    return render(request, 'meem/meem.html')

def Book_list(request):
    books = Book.objects.all()
    data = [
        {
            'id': b.id,
            'name': b.name,
            'author': b.author,
            'created_at': b.created_at,
            'image': b.image,
            'price':b.price,
            'description':b.description,
            'file':b.file,
            'number_of_views':b.number_of_views
        }
        for b in books
    ]
    return JsonResponse({"persons": data})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = {
        'id': book.id,
        'name': book.name,
        'author': book.author,
        'created_at': book.created_at,
        'image': book.image,
        'price':book.price,
        'decription':book.description,
        'file':book.file
    }
    return JsonResponse(data)

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        created_date=request.Post.get('created_date')
        description = request.POST.get('description')

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            created_date=created_date,
            description=description,
        )
        return redirect('home')
    return render(request, 'meem/create.html')


def update_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.created_date = request.POST.get('created_date')
        book.description = request.POST.get('description')
        book.save()
        return redirect('home')
    return render(request, 'meem/update.html', {'book': book})


def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'meem/delete.html', {'book': book})

# Create your views here.

import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import *
from .forms import *


def index(request):
    return render(request, 'books/index.html')


def book_list(request):
    books = Books.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()

            # book = Books.objects.create(
            #     title=form.cleaned_data['title'],
            #     author=form.cleaned_data['author'],
            #     description=form.cleaned_data['description'],
            #     year=form.cleaned_data['year']
            # )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'bookListChanged': None,
                        'showMessage': f'{book.title} registrado con éxito.'
                    })
                }
            )
        else:
            return render(request, 'books/add_book.html', {'form': form})
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


def edit_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        form = BookForm(
            request.POST,
            initial={
                'title': book.title,
                'author': book.author,
                'description': book.description,
                'year': book.year,
            }
        )
        if form.is_valid():
            book.title = form.cleaned_data['title']
            book.author = form.cleaned_data['author']
            book.description = form.cleaned_data['description']
            book.year = form.cleaned_data['year']
            book.save()

            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'bookListChanged': None,
                        'showMessage': f'{book.title} actualizado con éxito.'
                    })
                }
            )
        else:
            return render(
                request,
                'books/add_book.html', {
                    'form': form,
                    'book': book,
                })
    else:
        form = BookForm(
            initial={
                'title': book.title,
                'author': book.author,
                'description': book.description,
                'year': book.year,
            }
        )
    return render(
        request,
        'books/add_book.html', {
            'form': form,
            'book': book,
        }
    )


@require_POST
def delete_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    book.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                'bookListChanged': None,
                'showMessage': f'{book.title} eliminado con éxito.'
            })
        }
    )


def delete_book_confirmation(request, pk):
    book = get_object_or_404(Books, pk=pk)
    context = {
        'book': book
    }
    return render(
        request,
        'books/delete_book_confirmation.html',
        context
    )

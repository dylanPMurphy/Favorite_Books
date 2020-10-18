from django.shortcuts import render, redirect, HttpResponse
from .models import *
from login_reg.models import *
# Create your views here.
def index(request):
        if 'userid' in request.session:
            context ={
                'authenticated_user': User.objects.get(id=request.session['userid']),
                'allBooks':Book.objects.all()
            }
            print(request.session)
            print(request.session['userid'])
            return render(request, 'books.html', context)
        else:
            return HttpResponse("ERROR NOT SIGNED IN")

def newBook(request):
    if request.method =="POST":
        Book.objects.create(
            title = request.POST['title'],
            description = request.POST['desc'],
            user_who_posted = User.objects.get(id=request.session['userid']),

        )
        return redirect('/books')

def favBook(request):
    if request.method =="POST":
        targetBook = Book.objects.get(id=request.POST['book_to_fav_id'])
        targetBook.users_who_favorited.add(User.objects.get(id=request.session['userid']))
        return redirect('/books')

def showBook(request, book_id):
    context = {
        'authenticated_user': User.objects.get(id=request.session['userid']),
        'selected_book': Book.objects.get(id=book_id)
    }
    return render(request, 'book_page.html', context)

def updateBook(request):
    selected_book = Book.objects.get(id=request.POST['book_id'])
    print(selected_book)
    selected_book.title = request.POST['title']
    selected_book.description = request.POST['desc']
    selected_book.save()
    return redirect('/books/'+str(selected_book.id))

def deleteBook(request):
    
    selected_book = Book.objects.get(id=request.POST['book_id'])
    selected_book.delete()
    return redirect('/books')
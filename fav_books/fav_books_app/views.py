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
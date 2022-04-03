from django.shortcuts import render

# Create your views here.

def index(request):
    content={
        'title' : "NewsToday"
    }
    return render (request, 'index.html', content)

def contact(request):
    content={
        'title' : "Contact"
    }
    return render (request, 'contact.html', content)

def about(request):
    content={
        'title' : "About"
    }
    return render (request, 'about.html', content)

def login(request):
    content={
        'title' : "Log in to your account | NewsToday"
    }
    return render (request, 'login.html', content)

def signup(request):
    content={
        'title' : "Create a NewsToday account | NewsToday"
    }
    return render (request, 'signup.html', content)
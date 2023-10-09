from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Content, Category, Question
from django.http import JsonResponse


def signup(request):
    if request.method == 'POST':
        username = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']      
        if username=='' or email=='' or password=='': 
            messages.error(request,'please enter all the fields')
            return redirect('/')
        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('/')
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        # messages.info(request, 'Registration successful. Please login.')
        return redirect('home')
    else:
        return render(request, 'signup.html')
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username=='' or password=='':
            messages.error(request,'please fill all the details')
            return redirect('signin')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
            # next_url = request.GET.get('next', '/home')
            # return redirect(next_url)
        else:
            messages.error(request,'invalid credentials')
            return redirect('signin')
    else:
        return render(request,'signin.html')
def logout(request):
    auth.logout(request)
    return redirect('signin')

def home(request):

    contents = Content.objects.all()

    return render(request, 'index.html', {'contents':contents})

def problems(request):

    questions = Question.objects.all()
    print(questions)

    return render(request, 'problems.html', {'questions':questions})


from django.db.models import Q

def search(request):
    query = request.GET.get('query', '')
    
    results = Question.objects.filter(Q(questionHeading__icontains=query))
    
    return render(request, 'search_results.html', {'results': results, 'query': query})


def progress(request):
    return render(request, 'My_progress.html')
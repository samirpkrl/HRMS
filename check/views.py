from django.contrib.auth import login, authenticate, logout
#from django.contrib.sessions import sessions
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import LoginForm,SignUpForm
def chk(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'index.html')
def account(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'account.html')
def log_in(request):
    if request.method == 'POST':
    #form = LoginForm(request.post or None)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect!'})
    else:
        form = LoginForm()
        return render(request, 'login.html',{'form':form})
def log_out(request):
    a_list = [1,2,3,4]
    print(a_list)
    #request.session.flush()
    if request.method=='GET':   #why POST method is not working i don't know need to find it out
        print(a_list)
        logout(request)
        
		#mykey=request.session['mykey']
		#del request.session['mykey']
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
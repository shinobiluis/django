from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view( request ):
    if request.method == 'POST':
        print ('*' * 10);
        username = request.POST['username']
        password = request.POST['password']
        print(username, ':', password)
        print ('*' *  10);
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed');
        else:
            return render(request, 'users/login.html', {'error':'usuario invalido'})
    return render(request, 'users/login.html')
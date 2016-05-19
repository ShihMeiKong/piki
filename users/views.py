from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class Landing(View):
    template_name = "users/landing.html"

    def get(self, request):
        print("In landing get")
        return render(request, self.template_name)


class Register(View):
    # template_name = "users/register.html"
    template_name = "accounts/activate.html"
    index = "users/index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        email = request.POST.get('email')
        print(password)

        valid_username = User.objects.filter(username=username)
        if len(valid_username) > 0:
            return JsonResponse({'Error': 'Username is taken. Please choose another username'})
        user = User.objects.create_user(username=username, email=email, password=password)
        # users/index will redirect to users/users index
        # /users/index sends to index
        return redirect('/accounts/activate')


class Login(View):
    template_name = "registration/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print("user is authenticate")
        if user:
            print("In user")
            request.session['username'] = username
            login(request, user)
            return redirect('/users/index')
        else:
            return JsonResponse({'status': 'Invalid username and/or password'})


class Index(View):
    template_name = "users/index.html"

    def get(self, request):
        return render(request, self.template_name)


class Logout(View):

    def post(self, request):
        logout(request)
        return JsonResponse({
            'status': 'You have logged out'
        })
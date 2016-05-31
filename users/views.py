from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .models import *
from .forms import ProfileImageForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
# from django.core.mail import send_mail
# from django.db.models import Q
# import requests


# Create your views here.
class Landing(View):
    template_name = "users/landing.html"

    def get(self, request):
        print("In landing get")
        return render(request, self.template_name)


class Register(View):
    template_name = "users/register.html"
    # template_name = "accounts/activate.html"
    index = "users/index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        valid_username = User.objects.filter(
            username=username
        )
        if len(valid_username) > 0:
            return JsonResponse({'Error': 'Username is taken. Please choose another username'})
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        default_choices = {
            'is_vegan': False,
            'is_peanut': False,
            'is_vegetarian': False,
            'is_lactose': False,
            'is_diabetic': False,
            'is_gluten': False,
            'is_kosher': False,
            'is_alcohol': False
        }
        match_choices = {
            'match_vegan': False,
            'match_peanut': False,
            'match_vegetarian': False,
            'match_lactose': False,
            'match_diabetic': False,
            'match_gluten': False,
            'match_kosher': False,
            'match_alcohol': False
        }
        UserFoodPref.objects.create(user=user, **default_choices)
        UserMatchPref.objects.create(user=user, **match_choices)
        # users/index will redirect to users/users index
        # /users/index sends to index
        return redirect('/users/index')


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
        # username = (request.session.get('username'))
        # all of user's match pref is another user's foodprefs
        # use kwargs as filter
        user = request.user
        user_match_prefs = UserMatchPref.objects.get(user=user)
        user_own_prefs = UserFoodPref.objects.get(user=user)
        own_pref = user_own_prefs.__dict__
        match_dict = user_match_prefs.__dict__
        print(match_dict)
        match = {}
        for key, value in match_dict.items():
            if "match_" in key and value == True:
                # key is something like 'match_vegan'
                # when the match_vegan is added to the match dict
                # it has the transformed key but the value remains the same
                new_key = key.replace('match', 'is')
                match[new_key] = True
        # import pdb; pdb.set_trace()

        # match == { 'is_vegan': True, 'is_alchohol': True}
        match = UserFoodPref.objects.filter(**match)
        print(match)
        context = {
            'username': user.username,
            # since match is a list of dictionaries
            # have to use list comprehension to get the user out
            'match': [boom.user for boom in match],
        }

        return render(request, self.template_name, context)


class Profile(View):
    template_name = "users/profile.html"

    def get(self, request):
        # need to get the user's preferences first
        # get from database then put into context
        user = request.user
        user_own_prefs = UserFoodPref.objects.get(user=user)
        user_match_prefs = UserMatchPref.objects.get(user=user)
        own_pref = user_own_prefs.__dict__
        match_dict = user_match_prefs.__dict__
        print(own_pref)
        print(match_dict)
        context = own_pref.copy()
        context.update(match_dict)


        # import pdb; pdb.set_trace()
        return render(request, self.template_name, context)


class ProfileImageView(View):
    template_name = 'users/profileimage.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image = ProfileImage(
            # gets all kwargs that was passed in during the post
            # every post has post and files dictionary in the request
            # post has form data
            # files has biniary data, either manipulate or save
            # to get image, need to get file dictionary from kwargs
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id
        return redirect(self.template_name)


class Logout(View):
    template_name = 'users/logout.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        return redirect('/users/logout')


"""
When a user puts in their own food restrictions
its saved in the database
"""

class UserPrefAndMatch(View):

    def post(self, request):
        # We get a request from the user that includes their new user pref choices
        # We want to save it to the userfoodpref table for the user
        print(request.POST)
        # Here is the user
        user = request.user
        print('user', user)
        # user2 = User.objects.get(id=user.id)
        # import pdb; pdb.set_trace()
        # Here we get the user's existing prefs fom DB
        user_own_prefs = UserFoodPref.objects.get(user=user)
        user_match_prefs = UserMatchPref.objects.get(user=user)
        # Here are the new choices the user is sending us
        keys = request.POST.keys()
        choices_dict = {
            'is_vegan': False,
            'is_peanut': False,
            'is_vegetarian': False,
            'is_lactose': False,
            'is_diabetic': False,
            'is_gluten': False,
            'is_kosher': False,
            'is_alcohol': False
        }
        match_dict = {
            'match_vegan': False,
            'match_peanut': False,
            'match_vegetarian': False,
            'match_lactose': False,
            'match_diabetic': False,
            'match_gluten': False,
            'match_kosher': False,
            'match_alcohol': False
        }

        for choice in keys: # ['is_peanut', 'match_vegan']
            if "csrf" not in choice:
                # Is it a 'match_' string?
                if "match" in choice:
                    match_dict[choice] = True
                if "is_" in choice:
                    choices_dict[choice] = True

        print(choices_dict)
        user_own_prefs.__dict__.update(**choices_dict)
        user_match_prefs.__dict__.update(**match_dict)
        user_own_prefs.save()
        user_match_prefs.save()
        # import pdb; pdb.set_trace()
        return redirect('/users/index')

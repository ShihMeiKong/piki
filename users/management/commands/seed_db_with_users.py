from django.contrib.auth.models import User
from users.models import UserProfile, UserFoodPref, UserMatchPref
import requests
import random
from django.core.management.base import NoArgsCommand


# Run like this: ./manage.py seed_db_with_users


def rand_bool():
    if random.randint(0, 1) == 1:
        return True
    else:
        return False


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        """Seed db with User and USerProfile records from randomuser.me."""
        start_number = 1
        max_number = 11
        for number in range(start_number, max_number + 1):
            url = 'http://api.randomuser.me/1.0/?seed='
            response = requests.get(url + str(number))

            json = response.json()
            # json will return a dictionary
            email = json['results'][0]['email']
            gender = json['results'][0]['gender']
            username = json['results'][0]['login']['username']
            password = json['results'][0]['login']['password']
            picture = json['results'][0]['picture']['large']
            print(email, gender, username, password)

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            print('User created', user.id, user, password)

            UserProfile.objects.create(
                user=user,
                gender=gender,
                image=picture
            )
            print('UserProfile created', user)

            """
            since users are created using randomuser, the users skip the default own and match pref
            using the below to link users to match and own pref
            rand_bool gives a true or false which randomly creates food and match prefs
            """
            UserFoodPref.objects.create(
                user=user,
                is_peanut=rand_bool(),
                is_vegetarian=rand_bool(),
                is_vegan=rand_bool(),
                is_lactose=rand_bool(),
                is_diabetic=rand_bool(),
                is_gluten=rand_bool(),
                is_kosher=rand_bool(),
                is_alcohol=rand_bool(),
            )

            UserMatchPref.objects.create(
                user=user,
                match_peanut=rand_bool(),
                match_vegetarian=rand_bool(),
                match_vegan=rand_bool(),
                match_lactose=rand_bool(),
                match_diabetic=rand_bool(),
                match_gluten=rand_bool(),
                match_kosher=rand_bool(),
                match_alcohol=rand_bool(),
            )

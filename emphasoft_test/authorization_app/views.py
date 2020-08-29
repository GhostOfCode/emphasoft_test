from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView

import vk_api


class Authorization(LoginView):
    template_name = 'authorization_app/authorization.html'


class Profile(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(to='/auth')
        friends_list = self.get_friends_list(request.user)
        return render(request, 'authorization_app/profile.html', context={'friends_list': friends_list})

    def get_friends_list(self, user):
        social = user.social_auth.get()
        access_token = social.extra_data['access_token']
        api = vk_api.VkApi(token=access_token, login=user.username).get_api()
        friends_list = api.friends.get(order='random', count=5, fields=['photo_100'])
        return friends_list['items']

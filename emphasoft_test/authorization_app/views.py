from django.shortcuts import render, redirect
from django.template import Context
from django.views import View

import vk_api


class Authorization(View):
    def get(self, request):
        return render(request, 'authorization_app/authorization.html')


class Profile(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(to='/auth')
        friends = self.get_friends_list(request.user)
        return render(request, 'profile.html', context={'friends_list': friends})

    def get_friends_list(self, user):
        social = user.social_auth.get()
        access_token = social.extra_data['access_token']
        api = vk_api.VkApi(token=access_token, login=user.username).get_api()
        friends_list = api.friends.get(order='random', count=5, fields=['photo_100'])
        return friends_list['items']

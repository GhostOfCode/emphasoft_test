from django.shortcuts import render
from django.views import View


class Authorization(View):

    def get(self, request):
        return render(request, 'authorization_app/authorization.html')


class Profile(View):
    def get(self, request):
        print(request)
        return render(request, 'profile.html')

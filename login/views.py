from django.shortcuts import render
from django.views import View


class LoginForm(View):
    def get(self, request):
        return render(request, 'login/index.html')


from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User




class LoginPageView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username)
        if len(user) == 0:
            return redirect('login')

        else:
            user_x = User.objects.all()
            context = {'users': user_x}
            return render(request, 'users/home.html', context)


class RegisterPageView(View):
    def get(self, request):
        return render(request, 'users/register.html')


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']

        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email)
        user.set_password(password)
        user.save()
        return redirect('login')





class ProfilePageView(View):
    def get(self, request):
        user = User.objects.all()
        context = {'users': user}
        return render(request, 'users/home.html', context)


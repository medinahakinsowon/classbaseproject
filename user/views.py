from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.


class SignUpView(View):
    form_class = UserRegistrationForm  #attribute to class, form_class, template_name
    template_name = "auth/signup.html"

    def get(self, request):
        form = self.form_class()
        context = {"form": form}   #self is the class
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST) #if request.method = 'POST'

        if form.is_valid():
            form.save()

            messages.success(request, message="Account created successfully")

            return redirect(reverse("login"))

        context = {"form": form}
        return render(request, self.template_name, context)

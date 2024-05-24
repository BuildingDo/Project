from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from base.forms import CreateUserForm


@login_required
def home(request):
 return render(request, "home.html", {})


def authView(request):
 if request.method == "POST":
  form = CreateUserForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = CreateUserForm()
 return render(request, "registration/signup.html", {"form": form})

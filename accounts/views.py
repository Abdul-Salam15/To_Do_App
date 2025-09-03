from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("accounts:login"))
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect(reverse('tasks:home'))
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})
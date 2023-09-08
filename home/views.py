from django.shortcuts import render, redirect
from .forms import ItemForm
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def signin(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'page.html')

def signup(request):
    return render(request, 'form.html')

def findPage(request):
    return render(request, 'find.html')

def RecievedPage(request):
    return render(request, 'thankyou.html')




# views.py
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemCreateView(generics.CreateAPIView):
    authentication_classes = ()
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# #User Registrations
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.shortcuts import render, redirect

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)  # Log the user in after registration
#             return redirect('home')  # Redirect to the user's profile page
#     else:
#         form = UserCreationForm()
#     return render(request, 'form.html', {'myform': form})

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)  # Log the user in
#             return redirect('home')  # Redirect to the user's profile page
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'myform': form})



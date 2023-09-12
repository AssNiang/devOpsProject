from django.shortcuts import render, redirect

from .forms import UserForm
# Create your views here.

from .models import User, Visit
from .serializers import UserSerializer, VisitSerializer
from rest_framework.response import Response


def user_list(request):
    users = User.objects.all()
    if not users:
        message = "Il n'y a pas d'utilisateurs pour le moment."
        return render(request, 'user/user_list.html', {'message': message})

    return render(request, 'user/user_list.html', {'users': users})


def get(request):
    visit = Visit.objects.first()
    if not visit:
        visit = Visit.objects.create()
    visit.count += 1
    visit.save()
    serializer = VisitSerializer(visit)
    return Response(serializer.data)


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-list')  # Redirect to the user list view after adding the user.
    else:
        form = UserForm()

    return render(request, 'user/add_user.html', {'form': form})



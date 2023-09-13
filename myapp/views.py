from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import generics, status

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


def visit_count(request):
    visit = Visit.objects.first()
    if not visit:
        visit = Visit.objects.create()
    visit.count += 1
    visit.save()
    return JsonResponse({'count': visit.count})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-list')  # Redirect to the user list view after adding the user.
    else:
        form = UserForm()

    return render(request, 'user/add_user.html', {'form': form})


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_user_api(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')  # Retourne 'OK' lorsque l'utilisateur est créé avec succès.
        else:
            return HttpResponseBadRequest('Bad Request')  # Retourne 'Bad Request' si le formulaire n'est pas valide.
    else:
        return HttpResponseBadRequest('Invalid method')  # Retourne 'Invalid method' si la méthode n'est pas POST.

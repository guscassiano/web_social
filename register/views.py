from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import models, authenticate, login, logout, forms, decorators
from register.serializer import RegisterSerializer
from .forms import CustomUserCreationForm, PerfilForm, UserForm
from django.views.generic import UpdateView, DetailView
from .models import Perfil, Follow


class RegisterModelView(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = RegisterSerializer

def register_view(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            login_form = forms.AuthenticationForm()
    else:
        login_form = forms.AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('login')

class PerfilUpatadeView(UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = UserForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        if user_form.is_valid():
            user_form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('perfil', kwargs={'pk': self.object.pk})


class PerfilUsuarioView(DetailView):
    model = models.User
    template_name = 'perfil_users.html'
    context_object_name = 'perfil_usuario'

    def get_object(self):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(models.User, id=user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil_usuario = self.get_object()
        user = self.request.user
        context['is_following'] = Follow.objects.filter(follower=self.request.user, followed=perfil_usuario).exists()
        context['user'] = user

        return context

@decorators.login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(models.User, id=user_id)
    follow, created = Follow.objects.get_or_create(follower=request.user, followed=user_to_follow)

    if not created:
        follow.delete()

    return redirect('perfil_usuario', pk=user_id)


class PerfilUsuarioView(DetailView):
    model = models.User
    template_name = 'perfil_users.html'
    context_object_name = 'perfil_usuario'

    def get_object(self):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(models.User, id=user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil_usuario = self.get_object()

        context['seguidores'] = Follow.objects.filter(followed=perfil_usuario).count()
        context['seguindo'] = Follow.objects.filter(follower=perfil_usuario).count()
        context['is_following'] = Follow.objects.filter(follower=self.request.user, followed=perfil_usuario).exists()

        return context
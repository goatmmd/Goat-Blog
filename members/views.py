from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, FormView, DetailView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from members.forms import SingUpForm, EditProfileVForm, EditProfilePageForm, CreateProfilePageForm
from members.models import UserProfile


class CustomizePasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password-success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(CreateView):
    form_class = SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileVForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class ShowProfilePageView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'


class CreateProfilePageView(LoginRequiredMixin, CreateView):
    form_class = CreateProfilePageForm
    success_url = reverse_lazy('home')
    template_name = 'registration/create_profile.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)


class EditProfilePageView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
    fields = ['bio', 'profile_pic']

    def get(self, request, *args, **kwargs):
        if self.request.user.pk != kwargs['pk']:
            raise Http404
        return super().get(request, *args, **kwargs)
from django.urls import path, re_path

from members.views import UserRegisterView, UserEditView, CustomizePasswordsChangeView, password_success, \
    ShowProfilePageView, EditProfilePageView, CreateProfilePageView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register-user'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', CustomizePasswordsChangeView.as_view(), name='change-password'),
    path('password_success/', password_success, name='password-success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile-page'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create_profile/', CreateProfilePageView.as_view(), name='create-profile-page'),

]

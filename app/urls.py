from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm

urlpatterns =[
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('membre', views.MemberRegistrationView.as_view(), name="membre" ),
    path('all_activity', views.all, name="all_activity"),
    path("detail-activity/<int:pk>", views.detail, name="detail"),
    path('contact', views.ContactView.as_view(), name="contact"),
    path('contribution', views.add_contribution, name="contribution"),
    path('load_departements/', views.load_departements, name='load_departements'),
    path('load_zones/', views.load_zones, name='load_zones'),
    path('load_secteurs/', views.load_secteurs, name='load_secteurs'),
    path('load_comites/', views.load_comites, name='load_comites'),

    #Authentication 
    path('del-registration', views.DelegueRegistrationView.as_view(), name="delegue-registration"),
     path('accounts/login', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='app/password_reset.html', form_class=MyPasswordResetForm),name='password-reset'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(
        template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name='passwordchange'),
    path('logout', views.logout_view, name='logout'),

    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'),name='password-reset'),

    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='app/password_reset.html', form_class=MyPasswordResetForm),name='password-reset'),

    path('password-reset/done', auth_view.PasswordResetView.as_view(
        template_name='app/password_reset_done.html', form_class=MyPasswordResetForm),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetView.as_view(
        template_name='app/password_reset_complete.html', form_class=MyPasswordResetForm),name='password_reset_complete'),


#Profile
    path('profile', views.profile, name="profile")




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

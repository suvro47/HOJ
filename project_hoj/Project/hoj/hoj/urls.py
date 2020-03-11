
from django.contrib import admin
from django.urls import path, re_path, include
from user import views as user_views
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', user_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('standings/', user_views.standings, name='standings'),
    path('profile/', user_views.profile, name='profile'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('problem.urls')),  # problem urls file added 
    path('', include('submission.urls')), # submission urls file added
    path('', include('resources.urls')), # resources urls file added
    path('', include('contest.urls')), # resources urls file added
]

"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main import views
from main.forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'main.views.login', name='login'),
    url(r'^logout/$', 'main.views.logout', name='logout'),
    
    url(r'^recipelist/$', views.RecipeListView.as_view(), name='recipelist'),
    url(r'^recipedetail/(?P<slug>.+)/$', views.RecipeDetailView.as_view(), name='recipedetail'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
       'document_root': settings.MEDIA_ROOT}),

    url(r'^recipelist_dbv/$', 'main.views.recipelist_dbv'),

    url(r'^recipe_search/$', 'main.views.recipe_search', name='recipesearch'),

    url(r'^recipe_list/(?P<starts_with>\w+)/$', 'main.views.recipe_list'),
    url(r'^recipe_detail/(?P<pk>\d+)/$', 'main.views.recipe_detail'),

    url(r'^json_response/$', 'main.views.json_response', name='jsonresponse'),
    url(r'^ajax_view/$', 'main.views.ajax_search', name='ajaxsearch'),

    url(r'^signup/$', 'main.views.signup', name='signup'),

    url(r'^regiser/$', CreateView.as_view(template_name='register.html', form_class=CustomUserCreationForm, success_url='/'))
]

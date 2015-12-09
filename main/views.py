from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.template import RequestContext
from django.db import IntegrityError
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from main.forms import UserSignUp, UserLogin
from main.models import Recipe, CustomUser
from django.core.paginator import Paginator, InvalidPage
import string
# Create your views here.


class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipelist.html'


class RecipeDetailView(DetailView):

    model = Recipe
    slug_field = 'slug'
    context_object_name = 'recipe'
    template_name = 'recipedetail.html'


def signup(request):
    context = {}

    form = UserSignUp

    context['form'] = form

    if request.method == 'POST':
        form = UserSignUp(request.POST)
        
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = CustomUser.objects.create_user(email, password)
                auth_user = authenticate(email=email, password=password)
                login(request, auth_user)

                return HttpResponseRedirect('/recipelist')

            except IntegrityError, e:
                context['valid'] = "No, Because! No"
        else:
            context['valid'] = form.errors

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def logout(request):
    user_logout(request)

    return HttpResponseRedirect('/recipelist')


def login(request, auth_user):
    context = {}

    form = UserLogin()

    context['form'] = form

    print "in login view"

    if request.method == 'POST':

        print "in post"
        form = UserLogin(request.POST)

        print form.errors

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print email
            print password
            auth_user = authenticate(email=email, password=password)
            print auth_user
            if auth_user is not None:
                user_login(request, auth_user)

                print "auth_user is not none"

                return HttpResponseRedirect('/recipelist')
            else:
                context['valid'] = "Please enter a User Name"

        else:
            context['valid'] = "Form is not valid."
    return render_to_response('login.html', context, context_instance=RequestContext(request))


def json_response(request):
    search_string = request.GET.get('search', '')

    objects = Recipe.objects.filter(name__icontains=search_string)

    object_list = []

    for object in objects:

        object_list.append(object.name)

    return JsonResponse(object_list, safe=False)


def ajax_search(request):

    context = {}

    return render_to_response('ajax_view.html', context, context_instance=RequestContext(request))


def recipe_search(request):

    context = {}

    return render_to_response('recipe_search.html', context, context_instance=RequestContext(request))


def recipelist_dbv(request):

    context = {}

    recipe_list = Recipe.objects.all()[:350]

    # context['recipe_list'] = recipe_list

    paginator = Paginator(recipe_list, 30)

    page = int(request.GET.get("page", '1'))

    try:
        recipe_list = paginator.page(page)
    except (InvalidPage, EmptyPage):
        recipe_list = paginator.page(paginator.num_pages)

    context['recipelist'] = recipe_list
    print recipe_list
    return render_to_response('recipelist_dbv.html', context, context_instance=RequestContext(request))


def recipe_list(request, starts_with):
    print starts_with

    page = request.GET.get("page", '1')
    
    letter = request.GET.get('letter', starts_with)

    recipes = Recipe.objects.filter(title__istartswith=letter)

    paginator = Paginator(recipes, 30)

    try:
        recipes = paginator.page(page)
        print 'recipes = paginator'
    except (InvalidPage, EmptyPage):
        recipes = paginator.page(paginator.num_pages)
        print 'error'
    api_dict = {}

    recipe_list = []
    for recipe in recipes:
        
        print recipe

        recipe_list.append({'title': recipe.title,
                            'publisher': recipe.publisher,
                            'recipe_image': recipe.recipe_image.url,
                            'pk': recipe.id
                            })
    
    try:
        api_dict['pervious_page'] = recipes.previous_page_number()
    except:
        pass

    api_dict['recipes'] = recipe_list   

    api_dict['current_page'] = recipes.number

    api_dict['all_pages'] = recipes.paginator.num_pages

    api_dict['letters'] = list(string.ascii_uppercase)

    return JsonResponse(api_dict)


def recipe_detail(request, pk):

    recipe = Recipe.objects.get(pk=pk)
    ingredient_list = []
    for ingredient in recipe.ingredients.all():
            ingredient_list.append(ingredient.name)
            print ingredient.name
    recipe_detail = {'title': recipe.title,
                     'publisher': recipe.publisher,
                     'recipe_image': recipe.recipe_image.url,
                     'social_rank': recipe.social_rank,
                     'recipe_id': recipe.recipe_id,
                     'f2f_url': recipe.f2f_url,
                     'glutenfree': recipe.glutenfree,
                     'ingredients': ingredient_list,
                     'pk': recipe.id
                     }

    return JsonResponse(recipe_detail)
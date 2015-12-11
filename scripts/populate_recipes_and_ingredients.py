#!/usr/bin/env python
import os, sys
import requests
import django
import json
import urllib

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


from django.conf import settings



from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from unidecode import unidecode
from PIL import Image
# from StringIO import StringIOv
from main.models import Recipe, Ingredient
from slugify import slugify

django.setup()


param_dict = {'key': settings.F2FKEY, 'sort': 'r', 'page': '17'}
response = requests.get('http://food2fork.com/api/search/recipes.json', params=param_dict)

response_dict = response.json()


for data in response_dict['recipes']:
    new_recipe, created = Recipe.objects.get_or_create(title=data.get('title'))
    new_recipe.recipe_id = data["recipe_id"]
    rId = new_recipe.recipe_id
    new_recipe.publisher = data["publisher"]
    new_recipe.social_rank = data["social_rank"]
    new_recipe.f2f_url = data["f2f_url"]
    new_recipe.slug = slugify(data['title'])
    param_dict = {'key': settings.F2FKEY, 'rId': rId}
    response = requests.get('http://food2fork.com/api/get/', params=param_dict)

    result = urllib.urlretrieve(data['image_url'])
    
    new_recipe.recipe_image.save(os.path.basename(data['image_url']), File(open(result[0])))
    response_dict = response.json()


    print '================================================='

    for data in response_dict['recipe']['ingredients']:
        print data
        new_ingredient, created = Ingredient.objects.get_or_create(name=data)
        new_ingredient.name = data
        new_recipe.ingredients.add(new_ingredient)
        new_ingredient.save()
    print '================================================='    
    new_recipe.save()
    print 'end'

    
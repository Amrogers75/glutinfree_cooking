#!/usr/bin/env python
import urllib
import urllib2
from lxml import etree
import StringIO
import re, sys, os
import requests
from PIL import Image



sys.path.append("..")

os.environ.setdefault("GLUTINFREE_COOKING_MODULE", "glutinfree_cooking.settings")

from main.models import Recipe, Ingredient
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

result = urllib.urlopen("http://food2fork.com/api/search?key=d044ae6d96bda54d7390a0160e13f27f&q=('image_url')")

html = result.read()

parser = etree.HTMLParser()
tree   = etree.parse(StringIO.StringIO(html), parser)

xpath3 = "//*[@id="main"]/div/div/div[0]/img/div/ul/li/a/@href"


filtered_html3 = tree.xpath(xpath3)

print filtered_html3 = tree.xpath(xpath3)
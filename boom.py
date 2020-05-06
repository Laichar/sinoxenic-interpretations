import json
with open("persian.json") as p:
    persian = p.read()
    persianJson = json.loads(persian)

from sinoxenic.models import Book, Category, Item
from django.utils import timezone

if ("BookName" in 

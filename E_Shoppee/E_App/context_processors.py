# setting every category based links
from .models import Category

def menu_links():
    links = Category.objects.all()
    return dict(links=links)
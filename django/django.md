- install Django and in virtualenv
  pip install django -> pipenv shell -> pip install django

- create project:
  django-admin startproject pyshop .

- start server
  python manage.py runserver

- create app (folder)
  python manage.py startapp products

- setting a view function - response to client
  products -> views.py
  from django.http import HttpResponse
  def index(response): return HttpResponse("hello world")

- url mapping
  create products -> urls.py
  from django.urls import path
  from . import views
  urlpattterns = [
  path('', views.index)
  ]

- set url for app
  import include from django.urls
  pyshop -> urls.py
  add path('products/', include('products.urls)) #products.urls is a path to module

  add new view 'new' in products -> views.py
  add path in products -> urls.py

- Create a Model
  products -> models.py
  class Product(models.model):
  name = models.CharField(max_length=255)
  price = models.FloatField()
  stock = models.IntegerField()
  image_url = models.CharField(max_length=2083)

- Migrations
  python manage.py makemigrations -> no changes detected
  get config file name from products -> apps.py (ProductsConfig)
  pyshop -> settings.py
  add config into INSTALLED_APPS = [..., 'products.apps.ProductsConfig']
  python manage.py makemigrations -> migration created...
  python manage.py migrate -> migrations ran
  python manage.py migrate -> no migrations to apply

- Create new class for Discount
  products -> models.py
  create class Offer(models.Model): ...

- Create Migration
  python manage.py makemigraions
  Run Migration
  python manage.py migrate

- Admin
  python manage.py createsuperuser -> set username, email, pass
  products -> admin.py
  from .models import Product
  create class ProductAdmin(admin.ModelAdmin): list_display("name", "price", "stock")
  admin.site.register(Product, ProductAdmin)

- Template
  products -> views.py
  from .models import Product

  in class index:
  products = Product.objects.all() -- returns all objects
  products = Product.objects.filter() -- filter on objects
  products = Product.objects.get() -- get single object
  return render(request, 'index.html', {'products': products})

  products -> templates (new folder)
  products -> templates -> index.html (for index class)

- DJANGO HTML
  no indentation
  {% for product in products %} = template tag
  {% endfor %} = close for loop in template tag
  {{ dynamic rendering }}

- Bootstrap -- https://getbootstrap.com/
  copy start template from documentation
  home folder create a templates folder

  - pyshop -> settings
    TEMPLATES = [{"DIRS": [os.path.join(BASE_DIR, 'templates')]}]
    django -> templates -> base.html
    {% block content %}

- creates an empty spot for other html
- content is block name
  {% endblock %}

products -> templates -> index.html
{% extends "base.html %}
{% block content %}
-HTML
-bootstrap components -> card (copy html)
{% endblock %}

templates -> base.html

<div class="container"></div>
-bootstrap components -> navbar

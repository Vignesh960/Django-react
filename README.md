# Django-react


create virtual env before creating django project
	pip install pipenv
activate the venv
	pipenv shell(use this whenever u close terminal to activate venv)
	pipenv freeze
	pipenv install pytest
	pipenv freeze
then install django inside venv
	pipenv install django
then create django project
	pipenv django-admin startproject ecom
=>cd ecom
=>py manage.py makemigrations
=>py manage.py migrate
=>now u can able to create super user for django admin
	py manage.py createsuperuser
=> py manage.py runserver
							section-3
						----------------------------
Now add corsheader by installing should active venv
	=> pipenv install django-cors-headers
	then add them to settings.py

Django is a Python web framework that allows rapid web application development. Apps developed in Django may need to interact with other applications hosted on different domains (or even just different ports). For these requests to succeed, you’ll need to use cross-origin resource sharing (CORS) in your server.

Luckily, in Django there’s already a module that’s easy to install and configure to allow CORS requests and avoid errors. So, if you want to know more about CORS and how to enable it in your Django server, be sure to keep reading.

What Is CORS?
CORS is a mechanism to allow interaction with resources hosted on different domains. For instance, one of the most common scenarios to apply it is with Ajax requests.

In order to illustrate how CORS works, let’s assume you have a web application that lives in domain.com. But, to save user information, the app calls an API hosted in another URL—for example, api.domain.com. So, when a request to save data is sent to api.domain.com, the server evaluates the requests based on its headers and the request’s source.

If you allow the URL domain.com in the server, it will provide the proper response. If the domain is not allowed, the server provides an error. This information exchange occurs using HTTP headers.

Errors Involving CORS
CORS is a security feature that web clients (browsers) implement that can make requests to a specific server to fail. Some  possible server responses may include

An unauthorized status (403)

An error in a preflight request indicating which URLs can send CORS requests

As a clarification, a preflight request is a petition that browsers send to the server to discover what HTTP methods it accepts in requests. Then, the server can return an error status and a list of CORS-enabled URLs. If the server doesn’t include the domain making the request, the browser won’t even perform the actual data request.

As a rule of thumb, if you’re dealing with different domains, remember to be on the lookout for CORS issues. Also remember that using a different HTTP protocol or even a different port counts as a different domain. But there’s no need to worry, as current browsers’ tools are very helpful when diagnosing these issues.

Enabling CORS in Django
Since Django is a web framework, it’s very simple to enable CORS. So, here are the steps you must take to do so.

Install the CORS module:

python -m pip install django-cors-headers
 or 
pipenv install django-cors-headers

Once that’s done, enable the module in Django. This is done in the installed apps section. Oh, and don’t forget the trailing comma; otherwise, you’ll get an error.



INSTALLED_APPS = [
...
'corsheaders',
...
]
Next, add the middleware classes to listen in on server responses. Middleware classes hook on Django’s request/response processing. You can think of it as a plugin system to modify Django’s input or output.



MIDDLEWARE = [
...,
'corsheaders.middleware.CorsMiddleware',
'django.middleware.common.CommonMiddleware',
...,
]

I’d recommend that you place the class CorsMiddleware before any other middleware that can generate responses, such as CommonMiddleware. This is because any other class may prevent the module from generating the appropriate CORS headers.

Finally, configure at least one of the required settings and any of the optional settings that you’d like to. Let’s review those settings and the purpose of each in the next sections.

Required Settings
Required settings tell the module how to evaluate a request’s origin. From there, the module decides, based on the settings you defined, if the origin is valid in order to continue processing the request and to provide a response.

You can set the module to allow requests from specific domains, regular expressions, or all requests. What options you should configure will depend on your back end’s purpose. Sometimes all origins are valid, but in other cases, you’ll need to narrow them to only a few, as shown below.

CORS_ALLOWED_ORIGINS:
CORS_ALLOWED_ORIGINS is the list of origins authorized to make requests. For example, below I’ve specified four origins:


CORS_ALLOWED_ORIGINS = [
"https://domain.com",
"https://api.domain.com",
"http://localhost:8080",
"http://127.0.0.1:9000"
]
	OR

CORS_ORIGIN_ALLOW_ALL = True




02 DRFW Installation:(https://www.django-rest-framework.org/#installation)

to install DRFW:
	pipenv install djangorestframework (inside the Venv)
	(or)
	pip install djangorestframework

and add DRFW to settings.py inside the installed_apps
	INSTALLED_APPS=[
			'rest_framework',
    			'rest_framework.authtoken',
			]


		whereas 'rest_framework.authtoken' like used for the custom signup instead of admin signup


Add RESTFRAMEWORK and add  AUTHENTICATION_CLASSES and token authentication to settings.py at bottom:

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    # add authentication class
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # Token based Authentication
        'rest_framework.authentication.TokenAuthentication',
    ]
}


*Add the url drf to urls.py
	
	urlpatterns = [
    			...
    			path('api-auth/', include('rest_framework.urls'))
			]


=>	py manage.py makemigrations
=>	py manage.py migrate (this will applies authtoken)
=>	py manage.py runserver

-------------------------------
create folder inside project =/media

=>add the media folder inside the settings.py
	MEDIA_URL="/media/"
	MEDIA_ROOT=os.path.join(BASE_URL,"/media")
=> add the below like: urls.py
	from django.contrib import admin
	from django.urls import path, include
	from django.conf.urls.static import static
	from django.conf import settings
	urlpatterns = [
    		path('admin/', admin.site.urls),
    		path('api-auth/', include('rest_framework.urls')),
		]
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
-----------------------
now create app named with api for django where manage.py file existed folder
	=> django-admin startapp api
	=>cd api
structure of api:
	-category
	-order
	-payment
	-product
	-user
now change the directory to api which is created api app=>cd api
	=>django-admin startapp category
	=>django-admin startapp order
	=>django-admin startapp payment
	=>django-admin startapp product
	=>django-admin startapp user

		20 handling  API root
	-------------------------------------

Add your every created app (api is app) to settings.py which is at project level
	INSTALLED_APPS=[
			...
			'api'
			]
then create urls.py to your own custom app (inside app-api)

then config urls inside the urls.py which is at project level (ecom)
	urls.py:
		urlpatterns=[... 
				path('api',include(api.urls'))
			]

under the api/urls.py (app-level config)
	from django.urls import path,include
	from rest_framework.authtoken import views
	from .views import home # home is function name from views.py

api/views.py
-------------
from django.shortcuts import render
from django.http import JsonResponse
#now here declare views
def home(request):
	return JsonResponse({'id':1,'name':'Vignesh','Course':'Django with react'})

then runserver and request to localhost:8000/api

	
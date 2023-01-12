from django.contrib import admin

# Register your models here.

from .models import Voyage, Transport
#allows us to work with views inside admin app 
#register this model in admin 
admin.site.register(Voyage)
admin.site.register(Transport)
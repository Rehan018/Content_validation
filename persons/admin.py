from django.contrib import admin

# Register your models here.
from persons.models import subdomain, domain, Person

admin.site.register(subdomain)
admin.site.register(domain)
admin.site.register(Person)

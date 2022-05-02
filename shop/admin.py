from django.contrib import admin

from .models import product, contact
from .models import checkout, status

admin.site.register(product)
admin.site.register(contact)
admin.site.register(checkout)
admin.site.register(status)

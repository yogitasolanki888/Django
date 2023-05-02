from django.contrib import admin

from .models import Register
from .models import Contact
admin.site.register(Register)
admin.site.register(Contact)

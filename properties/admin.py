from django.contrib import admin
from properties.models import allproperties,Rooms,LivingArea,Balcony,Bathroom,Kitchen

# Register your models here.
admin.site.register(allproperties)
admin.site.register(Rooms)
admin.site.register(LivingArea)
admin.site.register(Kitchen)
admin.site.register(Balcony)
admin.site.register(Bathroom)

from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Product)
admin.site.register(Testimonial)
admin.site.register(CafeInfo)
admin.site.register(Gallery)
admin.site.register(About)

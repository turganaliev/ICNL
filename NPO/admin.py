from django.contrib import admin

# Register your models here.

from NPO.models import *

admin.site.register(News)
admin.site.register(NewsImage)
admin.site.register(TypeLaw)
admin.site.register(Law)
admin.site.register(Publication)
admin.site.register(Question)
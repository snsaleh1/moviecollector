from django.contrib import admin
# import your models here
from .models import Movie, Viewing, Photo

# Register your models here
admin.site.register(Movie)
admin.site.register(Viewing)
admin.site.register(Photo)
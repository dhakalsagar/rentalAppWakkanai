from django.contrib import admin
from .models import Post 

# Register your models here.
# from .models import House, Appart




# admin.site.register(House)
# admin.site.register(Appart)

# class houseadmin(admin.ModelAdmin):
# 	list_display = ("owner")
admin.site.register(Post)
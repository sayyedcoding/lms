from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     pass

class Video_TubularInline(admin.TabularInline):
    model = Video

class course_admin(admin.ModelAdmin):
    inlines = [Video_TubularInline]

# admin.site.register(CustomUser)
admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course,course_admin)
admin.site.register(Level)
admin.site.register(Lesson)

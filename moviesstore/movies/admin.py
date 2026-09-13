from django.contrib import admin
from .models import Movie, Review

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
# Gives filtering for reviews so admin can see the innapropriate deleted comments
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'user', 'comment', 'is_inappropriate', 'report_reason']
    list_filter = ['is_inappropriate']
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)

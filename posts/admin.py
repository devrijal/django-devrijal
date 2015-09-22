from django.contrib import admin

from .models import Posts


class PostsAdmin(admin.ModelAdmin):
	list_display = ('title', 'category_id', 'is_active', 'updated_date')
	list_filter = ['updated_date']
	search_fields = ['title']
	fieldsets = [('Post title', {'fields': ['title']}), ('Another Field', {'fields': ['content','category_id', 'is_active','slug']}),]

admin.site.register(Posts, PostsAdmin)
# Register your models here.

from django.contrib import admin
from feincms.admin import tree_editor

from aw.models import Category, Reporter, Application


class CategoryAdmin(tree_editor.TreeEditor):
    list_display = ('name', 'slug')
    list_filter = ('parent',)
    prepopulated_fields = {
        'slug': ('name',),
        }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Reporter)
admin.site.register(Application)


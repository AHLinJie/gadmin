# coding=utf-8
from django.contrib import admin
from .models import GovProAttrSyn, GovProAttrExclude


class GovProAttrSynAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'main_word',
                    'attribute_field',
                    'synonym_word',
                    'valid',
                    'created',
                    'modified')
    list_filter = ('created', 'valid',)
    search_fields = ['=id',
                     'main_word',
                     'attribute_field',
                     'synonym_word', ]
    date_hierarchy = 'created'


admin.site.register(GovProAttrSyn, GovProAttrSynAdmin)


class GovProAttrExcludeAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'main_word',
                    'attribute_field',
                    'exclude_word',
                    'valid',
                    'created',
                    'modified')
    list_filter = ('created', 'valid',)
    search_fields = ['=id',
                     'main_word',
                     'attribute_field',
                     'exclude_word', ]
    date_hierarchy = 'created'


admin.site.register(GovProAttrExclude, GovProAttrExcludeAdmin)

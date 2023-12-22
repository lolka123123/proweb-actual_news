from django.contrib import admin
from . import models
from django.utils.html import format_html
from ckeditor.widgets import CKEditorWidget
from django import forms

class ArticleAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание',widget=CKEditorWidget())

    class Meta:
        model = models.Article
        fields = '__all__'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']




@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']

    form = ArticleAdminForm


    # readonly_fields = ['thumbnail']
    #
    # def article_image(self, instance):
    #     return format_html(f'<img src="{instance.image.url}" class="thumbnail">')
    #
    # def thumbnail(self, instance):
    #     return format_html(f'<img src="{instance.image.url}" class="thumbnail">')
    #
    # class Media:
    #     css = {
    #         'all': ['styles/custom.css']
    #     }

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['id', 'user']


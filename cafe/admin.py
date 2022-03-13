from django import forms
from django.contrib import admin
from .models import Product, Dish, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class DishAdminForm(forms.ModelForm):
    list_display = ('title', 'category', 'price')
    search_fields = ('title', 'category')
    title = forms.CharField(label='Название блюда')
    description = forms.CharField(label='Описание блюда', widget=CKEditorUploadingWidget)
#product = forms.????
    flag_promotion = forms.Select()
    flag_popular = forms.Select()
    flag_novelty = forms.Select()

    class Meta:
        model = Dish
        fields = '__all__'


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    form = DishAdminForm


# Register your models here.
admin.site.register(Product)
#admin.site.register(Dish)
admin.site.register(Category)


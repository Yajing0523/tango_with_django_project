from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display=('title','category','url')

# class Category(models.Model):
#    name = models.CharField(max_length=128, unique=True)

#    class Meta:
#        verbose_name_plural = 'Categories'

#    def __str__(self):
#        return self.name

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category)
admin.site.register(Page)
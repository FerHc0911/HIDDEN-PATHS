from django.contrib import admin
from .models import Tours

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('nombre_tour','fecha','hora','estado','ciudad','costo','ganancias')
    search_fields = ('nombre_tour','estado')
    date_hierarchy = 'created'
    list_filter = ('estado','created')

# Register your models here.
admin.site.register(Tours,AdministrarModelo)



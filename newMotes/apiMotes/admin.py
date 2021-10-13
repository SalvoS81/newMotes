from django.contrib import admin
from newMotes.apiMotes.models import *

# Register your models here.

admin.site.register(SequenzaRiposi)

class LavoratoreAdmin(admin.ModelAdmin):
    list_display = ['nominativo', 'sequenza_riposi', 'data_per_sequenza', 'indice_per_sequenza']
    
admin.site.register(Lavoratore, LavoratoreAdmin)

class LineaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'polo']

admin.site.register(Linea, LineaAdmin)

class TurnoAdmin(admin.ModelAdmin):
    list_display = ['mansione', 'priorita', 'linea', 'ora_inizio', 'ora_fine']

class TurniInline(admin.StackedInline):
    model = Matrice.turni.through

admin.site.register(Turno, TurnoAdmin)

class MatriceAdmin(admin.ModelAdmin):
    # inlines = [
    #     TurniInline,
    # ]
    # exclude = ('turni',)
    pass
admin.site.register(Matrice, MatriceAdmin)
admin.site.register(Evento)


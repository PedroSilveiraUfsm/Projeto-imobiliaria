from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Imovel, Proprietario, Cliente, Corretor, Visita, Tipos, Status, Caracteristicas, Comodidades, Foto

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'get_proprietarios', 'endereco', 'valor', 'area_total', 'get_tipos', 'get_status', 'get_carateristicas', 'get_comodidades')
    search_fields = ('codigo', 'valor')

    def get_proprietarios(self, obj):
        return ', '.join([bb.nome for bb in Proprietario.objects.filter(imovel=obj.id)])
    get_proprietarios.short_description = 'Proprietários'

    def get_tipos(self, obj):
        return ', '.join([bb.descricao for bb in Tipos.objects.filter(imovel=obj.id)])
    get_tipos.short_description = 'Tipos'

    def get_status(self, obj):
        return ', '.join([bb.status for bb in Status.objects.filter(imovel=obj.id)])
    get_status.short_description = 'Status'
    
    def get_carateristicas(self, obj):
        return ', '.join([bb.caracteristicas for bb in Caracteristicas.objects.filter(imovel=obj.id)])
    get_carateristicas.short_description = 'Características'

    def get_comodidades(self, obj):
        return ', '.join([bb.comodidades for bb in Comodidades.objects.filter(imovel=obj.id)])
    get_comodidades.short_description = 'Comodidades'


@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'celular', 'email')
    search_fields = ('nome', 'celular')

@admin.register(Tipos)
class TiposAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
    search_fields = ('status',)

@admin.register(Caracteristicas)
class CaracteristicasAdmin(admin.ModelAdmin):
    list_display = ('caracteristicas',)
    search_fields = ('caracteristicas',)

@admin.register(Comodidades)
class ComodidadesAdmin(admin.ModelAdmin):
    list_display = ('comodidades',)
    search_fields = ('comodidades',)

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'foto', 'imovel')
    readonly_fields = ['fotografia']

    def fotografia(self, obj):
        return mark_safe('<img src="{url}" width="{width} height="{height}" />'.format(
            url = obj.foto.url,
            width = obj.foto.width,
            height = obj.foto.height,
        ))

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'celular', 'email')
    search_fields = ('nome', 'celular')

    def fotografia(self, obj):
        return mark_safe('<img src="{url}" width="{width} height="{height}" />'.format(
            url = obj.foto.url,
            width = obj.foto.width,
            height = obj.foto.height,
        ))

@admin.register(Corretor)
class CorretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'celular', 'email', 'foto')
    readonly_fields = ['fotografia']
    search_fields = ('nome',)

    def fotografia(self, obj):
        return mark_safe('<img src="{url}" width="{width} height="{height}" />'.format(
            url = obj.foto.url,
            width = obj.foto.width,
            height = obj.foto.height,
        ))

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'corretor', 'imovel', 'data_hora')


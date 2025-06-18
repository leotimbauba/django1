from django.contrib import admin

from .models import Produto, Cliente, OrdemServico


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modelo', 'preco', 'estoque')
    search_fields = ('nome', 'modelo')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cidade')
    search_fields = ('nome', 'email', 'telefone')
    

class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('Cliente', 'Produto', 'servico', 'status', 'data_da_entrada', 'data_da_saida')
    search_fields = ('Cliente__nome', 'Produto__nome', 'servico')
    list_filter = ('status', 'data_da_entrada', 'data_da_saida')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(OrdemServico, OrdemServicoAdmin)
# Register your models here.


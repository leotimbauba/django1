from django.urls import path

from .views import index, sobre, contato, produto, cliente

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
    path('produto/<int:pk>/', produto, name='produto'),
    path('cliente/<int:pk>/', cliente, name='cliente'),
    path('ordens_de_servico/', index, name='ordens_de_servico'),
    path('ordens_de_servico/<int:pk>/', index, name='ordem_de_servico_detail'),
]

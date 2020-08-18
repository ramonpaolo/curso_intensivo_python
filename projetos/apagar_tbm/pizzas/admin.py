from django.contrib import admin
from pizzas.modelos import Topicos,Entre
from lanches.lanches.modelo import Categoria, Especificacao

admin.site.register(Topicos)
admin.site.register(Entre)
admin.site.register(Categoria)
admin.site.register(Especificacao)
from django.urls import path
from .views import IndexView, ImoveisView, ImoveisAddView, ImoveisUpDateView, ImoveisDeleteView, \
        ProprietariosView, ProprietariosAddView, ProprietariosUpDateView, ProprietariosDeleteView, \
        ClientesView, ClientesAddView, ClientesUpDateView, ClientesDeleteView, \
        CorretoresView, CorretoresAddView, CorretoresUpDateView, CorretoresDeleteView, \
        VisitasView, VisitasAddView, VisitasUpDateView, VisitasDeleteView, \
        FotosView, FotosAddView, FotosUpDateView, FotosDeleteView

#os caminhos para cada nova página estão aqui
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('imoveis', ImoveisView.as_view(), name='imoveis'),
    path('imoveis/adicionar/', ImoveisAddView.as_view(), name='imovel_adicionar'),
    path('<int:pk>/imoveis/editar/', ImoveisUpDateView.as_view(), name='imovel_editar'),
    path('<int:pk>/imoveis/apagar/', ImoveisDeleteView.as_view(), name='imovel_apagar'),
    path('fotos', FotosView.as_view(), name='fotos'),
    path('fotos/adicionar', FotosAddView.as_view(), name='foto_adicionar'),
    path('<int:pk>/fotos/editar/', FotosUpDateView.as_view(), name='foto_editar'),
    path('<int:pk>/fotos/apagar/', FotosDeleteView.as_view(), name='foto_apagar'),
    path('proprietarios', ProprietariosView.as_view(), name='proprietarios'),
    path('proprietarios/adicionar', ProprietariosAddView.as_view(), name='proprietario_adicionar'),
    path('<int:pk>/proprietarios/editar/', ProprietariosUpDateView.as_view(), name='proprietario_editar'),
    path('<int:pk>/proprietarios/apagar/', ProprietariosDeleteView.as_view(), name='proprietario_apagar'),
    path('clientes', ClientesView.as_view(), name='clientes'),
    path('clientes/adicionar', ClientesAddView.as_view(), name='cliente_adicionar'),
    path('<int:pk>/clientes/editar/', ClientesUpDateView.as_view(), name='cliente_editar'),
    path('<int:pk>/clientes/apagar/', ClientesDeleteView.as_view(), name='cliente_apagar'),
    path('corretores', CorretoresView.as_view(), name='corretores'),
    path('corretores/adicionar', CorretoresAddView.as_view(), name='corretor_adicionar'),
    path('<int:pk>/corretores/editar/', CorretoresUpDateView.as_view(), name='corretor_editar'),
    path('<int:pk>/corretores/apagar/', CorretoresDeleteView.as_view(), name='corretor_apagar'),
    path('visitas', VisitasView.as_view(), name='visitas'),
    path('visitas/adicionar', VisitasAddView.as_view(), name='visita_adicionar'),
    path('<int:pk>/visitas/editar/', VisitasUpDateView.as_view(), name='visita_editar'),
    path('<int:pk>/visitas/apagar/', VisitasDeleteView.as_view(), name='visita_apagar'),
]
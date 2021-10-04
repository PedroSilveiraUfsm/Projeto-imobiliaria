from django.views.generic import TemplateView, ListView
from .models import Imovel, Proprietario, Cliente, Corretor, Visita, Foto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .forms import ImovelModelForm, FotoModelForm, ProprietarioModelForm, ClienteModelForm, CorretorModelForm, VisitaListForm
from .utils import HtmlToPdf
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['qtd_imoveis'] = Imovel.objects.count()
        context['qtd_proprietarios'] = Proprietario.objects.count()
        context['qtd_clientes'] = Cliente.objects.count()
        context['qtd_corretores'] = Corretor.objects.count()
        return context

# IMOVEIS
class ImoveisView(ListView):
    model = Imovel
    template_name = 'imoveis.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ImoveisView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(Q(codigo__icontains=buscar))
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='imoveis_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ImoveisView, self).get(*args, **kwargs)
    queryset = Imovel.objects.all()

class ImoveisAddView(CreateView):
    form_class = ImovelModelForm
    model = Imovel
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('imoveis')

class ImoveisUpDateView(UpdateView):
    form_class = ImovelModelForm
    model = Imovel
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('imoveis')

class ImoveisDeleteView(DeleteView):
    form_class = ImovelModelForm
    model = Imovel
    template_name = 'imovel_apagar.html'
    success_url = reverse_lazy('imoveis')

# FOTOS
class FotosView(ListView):
    model = Foto
    template_name = 'fotos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(FotosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(descricao__icontains=buscar)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='foto_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(FotosView, self).get(*args, **kwargs)
    queryset = Foto.objects.all()

class FotosAddView(CreateView):
    form_class = FotoModelForm
    model = Foto
    template_name = 'foto_form.html'
    success_url = reverse_lazy('fotos')

class FotosUpDateView(UpdateView):
    form_class = FotoModelForm
    model = Foto
    template_name = 'foto_form.html'
    success_url = reverse_lazy('fotos')

class FotosDeleteView(DeleteView):
    form_class = FotoModelForm
    model = Foto
    template_name = 'foto_apagar.html'
    success_url = reverse_lazy('fotos')

# PROPRIETARIOS
class ProprietariosView(ListView):
    model = Proprietario
    template_name = 'proprietarios.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ProprietariosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='proprietarios_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ProprietariosView, self).get(*args, **kwargs)
    queryset = Proprietario.objects.all()

class ProprietariosAddView(CreateView):
    form_class = ProprietarioModelForm
    model = Proprietario
    template_name = 'proprietario_form.html'
    success_url = reverse_lazy('proprietarios')

class ProprietariosUpDateView(UpdateView):
    form_class = ProprietarioModelForm
    model = Proprietario
    template_name = 'proprietario_form.html'
    success_url = reverse_lazy('proprietarios')

class ProprietariosDeleteView(DeleteView):
    form_class = ProprietarioModelForm
    model = Proprietario
    template_name = 'proprietario_apagar.html'
    success_url = reverse_lazy('proprietarios')

# CLIENTES
class ClientesView(ListView):
    model = Cliente
    template_name = 'clientes.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientesView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='cliente_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ClientesView, self).get(*args, **kwargs)
    queryset = Cliente.objects.all()

class ClientesAddView(CreateView):
    form_class = ClienteModelForm
    model = Cliente
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

class ClientesUpDateView(UpdateView):
    form_class = ClienteModelForm
    model = Cliente
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

class ClientesDeleteView(DeleteView):
    form_class = ClienteModelForm
    model = Cliente
    template_name = 'cliente_apagar.html'
    success_url = reverse_lazy('clientes')

# CORRETORES
class CorretoresView(ListView):
    model = Cliente
    template_name = 'corretores.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(CorretoresView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='corretor_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(CorretoresView, self).get(*args, **kwargs)
    queryset = Corretor.objects.all()

class CorretoresAddView(CreateView):
    form_class = CorretorModelForm
    model = Corretor
    template_name = 'corretor_form.html'
    success_url = reverse_lazy('corretores')

class CorretoresUpDateView(UpdateView):
    form_class = CorretorModelForm
    model = Corretor
    template_name = 'corretor_form.html'
    success_url = reverse_lazy('corretores')

class CorretoresDeleteView(DeleteView):
    form_class = CorretorModelForm
    model = Corretor
    template_name = 'corretor_apagar.html'
    success_url = reverse_lazy('corretores')

# VISITAS
class VisitasView(ListView):
    model = Visita
    template_name = 'visitas.html'

    def get_context_data(self, **kwargs):
        context = super(VisitasView, self).get_context_data(**kwargs)

        if self.request.GET:
            form = VisitaListForm(self.request.GET)
        else:
            form = VisitaListForm()

        context['form'] = form
        return context

    def get_queryset(self):
        qs = super(VisitasView, self).get_queryset()
        
        if self.request.GET:
            form = VisitaListForm(self.request.GET)
            if form.is_valid():
                cliente = form.cleaned_data.get('cliente')
                corretor = form.cleaned_data.get('corretor')
                imovel = form.cleaned_data.get('imovel')
                if cliente:
                    qs = qs.filter(cliente=cliente)
                if corretor:
                    qs = qs.filter(corretor=corretor)
                if imovel:
                    qs = qs.filter(imovel=imovel)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='visita_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(VisitasView, self).get(*args, **kwargs)
        queryset = Visita.objects.all()

class VisitasAddView(CreateView):
    form_class = VisitaListForm
    model = Visita
    template_name = 'visita_form.html'
    success_url = reverse_lazy('visitas')

class VisitasUpDateView(UpdateView):
    form_class = VisitaListForm
    model = Visita
    template_name = 'visita_form.html'
    success_url = reverse_lazy('visitas')

class VisitasDeleteView(DeleteView):
    form_class = VisitaListForm
    model = Visita
    template_name = 'visita_apagar.html'
    success_url = reverse_lazy('visitas')



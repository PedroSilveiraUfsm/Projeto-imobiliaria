from django import forms
from agenda.models import Imovel, Foto, Proprietario, Cliente, Corretor, Visita
class ImovelModelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o codigo do imovel'}),
            'valor': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o valor do imovel'}),
            'status': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o status do imovel'}),
        }

class FotoModelForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = '__all__'
        widgets = {
            'descricao': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a descrição da Foto'}),
            'foto': forms.FileInput(
                attrs={'class': 'input', 'type': 'file'}),
        }
        imovel = forms.ModelChoiceField(label='Imóvel:',
                                      widget=forms.Select(attrs={'class': 'select is-fullwidth'}),
                                      queryset=Imovel.objects.all(), required=False)

class ProprietarioModelForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do Proprietário'}),
            'celular': forms.TextInput(
                attrs={'class': 'input', 'type': 'tel', 'placeholder': 'Digite o telefone do proprietario'}),
            'email': forms.EmailInput(
                attrs={'class': 'input', 'type': 'mail', 'placeholder': 'Digite o email  do proprietario'}),
        }

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do Cliente'}),
            'celular': forms.TextInput(
                attrs={'class': 'input', 'type': 'tel', 'placeholder': 'Digite o telefone do Cliente'}),
            'email': forms.EmailInput(
                attrs={'class': 'input', 'type': 'mail', 'placeholder': 'Digite o email  do Cliente'}),
        }

class CorretorModelForm(forms.ModelForm):
    class Meta:
        model = Corretor
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do Corretor'}),
            'celular': forms.TextInput(
                attrs={'class': 'input', 'type': 'tel', 'placeholder': 'Digite o telefone do Corretor'}),
            'email': forms.EmailInput(
                attrs={'class': 'input', 'type': 'mail', 'placeholder': 'Insira o email  do Corretor'}),
            'foto': forms.FileInput(
                attrs={'class': 'input', 'type': 'file'}),
        }

class VisitaListForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'
        clientes = forms.CharField(label='Clientes:',
                                          widget=forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder':'Nome do cliente'}), required=False)
        corretores = forms.ModelChoiceField(label='Corretores:',
                                      widget=forms.Select(attrs={'class': 'select is-fullwidth'}),
                                      queryset=Corretor.objects.all(), required=False)
        imoveis = forms.ModelChoiceField(label='Imóveis:',
                                            widget=forms.Select(attrs={'class': 'select is-fullwidth'}),
                                            queryset=Imovel.objects.all(), required=False)
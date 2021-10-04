from django.db import models
from stdimage import StdImageField

class Proprietario(models.Model):
    nome = models.CharField('Nome', max_length=35, help_text='Informe o nome')
    celular = models.CharField('Celular', max_length=16, help_text='Informe o telefone Ex.:(xx)xxxxx-xxxx')
    email = models.EmailField('Email', max_length=100, help_text='Informe o email')

    class Meta:
        verbose_name = 'Proprietário'
        verbose_name_plural = 'Proprietários'

    def __str__(self):
        return self.nome

class Tipos(models.Model):
    descricao = models.CharField('Descrição', max_length=35, help_text='Informe a descrição do imóvel')

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.descricao

class Status(models.Model):
    status = models.CharField('Status', max_length=35, help_text='Informe a status do imóvel')

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.status

class Caracteristicas(models.Model):
    caracteristicas = models.CharField('Caracteristicas', max_length=35, help_text='Informe as características do imóvel')

    class Meta:
        verbose_name = 'Caracteristica'
        verbose_name_plural = 'Caracteristicas'

    def __str__(self):
        return self.caracteristicas

class Comodidades(models.Model):
    comodidades = models.CharField('Comodidades', max_length=35, help_text='Informe as comodidades do imóvel')

    class Meta:
        verbose_name = 'Comodidade'
        verbose_name_plural = 'Comodidades'

    def __str__(self):
        return self.comodidades

class Imovel(models.Model):
    codigo = models.CharField('Codigo', max_length=7, help_text='Informe o código do imóvel', unique=True)
    endereco = models.CharField('Endereço', max_length=100, help_text='Informe o endereço')
    proprietario = models.ManyToManyField('agenda.Proprietario')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, help_text='Informe o Valor do Imóvel')
    iptu = models.DecimalField('IPTU', max_digits=10, decimal_places=2, help_text='Informe o IPTU')
    condominio = models.DecimalField('Condomínio', max_digits=5, decimal_places=2, help_text='Informe o valor do condominio')
    area_total = models.DecimalField('Área Total', max_digits=5, decimal_places=2, help_text='Informe a área total do imóvel')
    descricao = models.CharField('Descrição', max_length=14, help_text='Descrição do Imóvel')
    quarto = models.DecimalField('Quartos', max_digits=5, decimal_places=2, help_text='Quantidade de quartos')
    banheiro = models.DecimalField('Banheiros', max_digits=5, decimal_places=2, help_text='Quantidade de banheiros')
    garagem = models.DecimalField('Garagem', max_digits=5, decimal_places=2, help_text='Vagas na Garagem')
    tipo = models.ManyToManyField('agenda.Tipos')
    statu = models.ManyToManyField('agenda.Status')
    caracteristica = models.ManyToManyField('agenda.Caracteristicas')
    comodidade = models.ManyToManyField('agenda.Comodidades')
    # foto = models.ForeignKey('agenda.Foto', related_name='foto_fk', verbose_name='Fotos', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'

    @property
    def proprietarios(self):
        return Proprietario.objects.filter(imovel=self)

    @property
    def tipos(self):
        return Tipos.objects.filter(imovel=self)

    @property
    def status(self):
        return Status.objects.filter(imovel=self)

    @property
    def caracteristicas(self):
        return Caracteristicas.objects.filter(imovel=self)

    @property
    def comodidades(self):
        return Comodidades.objects.filter(imovel=self)

    # def foto(self):
    #     return self.foto

    def __str__(self):
        return self.codigo

class Foto(models.Model):
    descricao = models.CharField('Descrição', max_length=35, help_text='Informe a descrição do imóvel')
    foto = StdImageField('Foto', upload_to='fotos', variations={'thumb': {'width': 200, 'height': 200, 'crop': True}})
    # imovel = models.OneToOneField('agenda.Imovel', on_delete=models.CASCADE)
    imovel = models.ForeignKey('agenda.Imovel', verbose_name='Imóvel', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __str__(self):
        return self.foto.url

    def imovel(self):
        return self.imovel

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=35, help_text='Informe o nome')
    celular = models.CharField('Celular', max_length=14, help_text='Informe o telefone Ex.:(xx)xxxxx-xxxx')
    email = models.EmailField('Email', max_length=100, help_text='Informe o email')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

class Corretor(models.Model):
    nome = models.CharField('Nome', max_length=35, help_text='Informe o nome')
    celular = models.CharField('Celular', max_length=14, help_text='Informe o telefone Ex.:(xx)xxxxx-xxxx')
    email = models.EmailField('Email', max_length=100, help_text='Informe o email')
    foto = StdImageField('Foto', upload_to='corretores', variations={'thumb': {'width': 200, 'height': 200, 'crop': True}})

    class Meta:
        verbose_name = 'Corretor'
        verbose_name_plural = 'Corretores'

    def __str__(self):
        return self.nome

class Visita(models.Model):
    cliente = models.ForeignKey('agenda.Cliente', verbose_name='Cliente', on_delete=models.CASCADE)
    corretor = models.ForeignKey('agenda.Corretor', verbose_name='Corretor', on_delete=models.CASCADE)
    imovel = models.ForeignKey('agenda.Imovel', verbose_name='Imóvel', on_delete=models.CASCADE)
    data_hora = models.DateTimeField('Data e Hora', help_text='Data e hora da visita')


    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'

    # @property
    def imovel(self):
        return self.imovel

    # def __str__(self):
    #     return f'{self.cliente} - {self.corretor} - {Visita.imovel.__str__()}'
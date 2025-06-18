from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)  # Nome do produto
    modelo = models.CharField('Modelo', max_length=100)  # Modelo do produto
    descricao = models.TextField('Descrição')  # Descrição do produto
    preco = models.DecimalField(
        'Preço', max_digits=10, decimal_places=2)    # Preço do produto
    # Quantidade em estoque do produto
    estoque = models.IntegerField('Quantidade em Estoque')
    imagem = models.ImageField(
        'Imagem', upload_to='produtos/', blank=True, null=True)  # Imagem do produto

    def __str__(self):
        return f"{self.nome} ({self.modelo}) - R$ {self.preco:.2f}"


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)  # Nome do cliente
    sobrenome = models.CharField(
        'Sobrenome', max_length=100)  # Sobrenome do cliente
    endereco = models.CharField(
        'Endereço', max_length=200)  # Endereço do cliente
    estado = models.CharField('Estado', max_length=50)  # Estado do cliente
    cidade = models.CharField('Cidade', max_length=100)  # Cidade do cliente
    email = models.EmailField('E-mail', max_length=100)  # E-mail do cliente
    telefone = models.CharField(
        'Telefone', max_length=15, blank=True, null=True)  # Telefone do cliente

    def __str__(self):
        return f'{self.nome} {self.endereco} {self.telefone}'


class OrdemServico(models.Model):
    id = models.AutoField(primary_key=True)  # ID da ordem de serviço
    # Chave estrangeira para o cliente
    Cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='ordens_de_servico')
    # Chave estrangeira para o produto
    Produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name='ordens_de_servico')
    servico = models.CharField(
        'Serviço', max_length=100, blank=True, null=True)  # Serviço do cliente
    observacao = models.TextField(
        'Observação', blank=True, null=True)  # Observação do cliente
    valor_pecas = models.DecimalField('Valor das Peças', max_digits=10,
                                      decimal_places=2, blank=True, null=True)  # Valor das peças do cliente
    valor_mao_de_obra = models.DecimalField(
        # Valor da mão de obra do cliente
        'Valor da Mão de Obra', max_digits=10, decimal_places=2, blank=True, null=True)
    valor_galho = models.DecimalField(
        # Valor do galho do cliente
        'Valor do Galho', max_digits=10, decimal_places=2, blank=True, null=True)
    data_da_entrada = models.DateField(
        'Data', blank=True, null=True)  # Data da entrada do cliente
    data_da_saida = models.DateField(
        'Data de Saída', blank=True, null=True)  # Data da saída do cliente

    status = models.CharField('Status', max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ], default='pendente')  # Status da ordem de serviço

    def valor_total(self):
        total = 0
        if self.valor_pecas:
            total += self.valor_pecas
        if self.valor_mao_de_obra:
            total += self.valor_mao_de_obra
        if self.valor_galho:
            total += self.valor_galho
        return total

    @property
    def total(self):
        return self.valor_total()

    @property
    def status_display(self):
        choices = self._meta.get_field('status').choices
        choices_dict = {key: value for key, value in choices} # type: ignore
        return choices_dict.get(self.status, 'Pendente')

    @property
    def data_entrada_formatada(self):
        return self.data_da_entrada.strftime('%d/%m/%Y') if self.data_da_entrada else 'N/A'

    @property
    def data_saida_formatada(self):
        return self.data_da_saida.strftime('%d/%m/%Y') if self.data_da_saida else 'N/A'

    def __str__(self):
        return f'Ordem de Serviço {self.id} - {self.Cliente.nome} {self.Cliente.sobrenome}'

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'
        ordering = ['-data_da_entrada']

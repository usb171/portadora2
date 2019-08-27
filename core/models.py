from django.db import models
from django.contrib.auth.models import User


TIPO_STREAM = (
    ('1', 'TX'),
    ('2', 'RX'),
)

class ServidorStream(models.Model):
    ativo = models.BooleanField(default=True, help_text="Flag de ativação do Servidor")
    nome = models.CharField(max_length=500, help_text='* URL')

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, verbose_name='* Acesso', null=True)
    nome = models.CharField(max_length=120, editable=False)
    tipoStream = models.CharField(max_length=2, choices=TIPO_STREAM, verbose_name='* Tipo do Stream')

    def save(self, *args, **kwargs):
        self.nome = self.user.first_name + " " + self.user.last_name
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Sala(models.Model):
    nome = models.CharField(max_length=500, help_text='* Nome da Sala')
    server = models.ForeignKey(ServidorStream, on_delete=models.SET_NULL, null=True)
    tx = models.OneToOneField(Usuario, related_name='TX', help_text='Aquele que Fala', on_delete=models.SET_NULL, null=True)
    rx = models.OneToOneField(Usuario, related_name='RX', help_text='Aquele que Escuta', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome




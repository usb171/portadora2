# Generated by Django 2.2.4 on 2019-08-26 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190826_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServidorStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=True, help_text='Flag de ativação do Servidor')),
                ('nome', models.CharField(help_text='* URL', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(editable=False, max_length=120),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='* Acesso'),
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='* Nome da Sala', max_length=500)),
                ('rx', models.ForeignKey(help_text='Aquele que Escuta', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RX', to='core.Usuario')),
                ('server', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.ServidorStream')),
                ('tx', models.ForeignKey(help_text='Aquele que Fala', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='TX', to='core.Usuario')),
            ],
        ),
    ]

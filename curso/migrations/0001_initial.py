# Generated by Django 4.1.3 on 2022-11-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monitores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga horária')),
                ('data', models.DateField()),
                ('numero_vagas', models.IntegerField(verbose_name='Quantidade de vagas')),
                ('prublco_alvo', models.CharField(max_length=255, verbose_name='Público alvo')),
                ('inicio_matriculas', models.DateTimeField(verbose_name='Início das matrículas')),
                ('fim_matriculas', models.DateTimeField(verbose_name='Encerramento das matrículas')),
                ('minitores', models.ManyToManyField(to='monitores.monitor', verbose_name='Monitores')),
            ],
        ),
    ]

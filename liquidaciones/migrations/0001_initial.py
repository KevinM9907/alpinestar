# Generated by Django 5.2 on 2025-04-03 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manicuristas', '0001_initial'),
        ('semanas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liquidacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('bonificacion', models.IntegerField()),
                ('manicurista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manicuristas.manicurista')),
                ('semana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semanas.semana')),
            ],
        ),
    ]

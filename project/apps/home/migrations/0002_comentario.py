# Generated by Django 4.2.2 on 2023-06-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=150)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-15 15:51

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('latin', models.CharField(max_length=255)),
                ('otro', models.CharField(blank=True, max_length=255, null=True)),
                ('resumen', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('siglas', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Glosary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('termino', models.CharField(max_length=255)),
                ('resumen', models.CharField(max_length=255)),
                ('definicion', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Término',
                'verbose_name_plural': 'Glosary de términos',
            },
        ),
        migrations.CreateModel(
            name='Dpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('division', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('arbol', models.TextField(blank=True, null=True)),
                ('division_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.Dpt')),
            ],
            options={
                'verbose_name': 'División político territorial',
                'verbose_name_plural': 'División político territorial',
            },
        ),
    ]

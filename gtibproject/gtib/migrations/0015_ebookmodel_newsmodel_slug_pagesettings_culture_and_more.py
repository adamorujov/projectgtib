# Generated by Django 4.0.5 on 2022-07-22 10:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtib', '0014_youthorganizationmodel_alter_volunteermodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Şəkil')),
                ('title', models.CharField(max_length=256, verbose_name='Başlıq')),
                ('description', models.TextField(verbose_name='Haqqında')),
                ('slug', models.SlugField(max_length=256, verbose_name='Sluq')),
            ],
            options={
                'verbose_name': 'Elektron kitab',
                'verbose_name_plural': 'Elektron kitablar',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True, verbose_name='Sluq'),
        ),
        migrations.AddField(
            model_name='pagesettings',
            name='culture',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Mədəniyyət'),
        ),
        migrations.AddField(
            model_name='pagesettings',
            name='karabakh',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Qarabağ Azərbaycandır!'),
        ),
        migrations.AddField(
            model_name='pagesettings',
            name='tourism',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Turizm'),
        ),
    ]

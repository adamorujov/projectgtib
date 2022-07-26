# Generated by Django 4.0.5 on 2022-07-26 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtib', '0021_photomodel_videomodel_alter_ideamodel_idea'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='Meta izah'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='meta_keyword',
            field=models.TextField(blank=True, null=True, verbose_name='Meta açar sözlər'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='meta_title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Meta başlıq'),
        ),
    ]
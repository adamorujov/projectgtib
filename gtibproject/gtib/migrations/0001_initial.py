# Generated by Django 4.0.5 on 2022-06-23 15:10

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='Sual')),
                ('answer', models.TextField(verbose_name='Cavab')),
            ],
            options={
                'verbose_name': 'Sual',
                'verbose_name_plural': 'Tez-tez verilən suallar',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='FormmModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.CharField(max_length=256, verbose_name='Sorğu')),
                ('is_highlighted', models.BooleanField(default=False, verbose_name='Önə çıxan')),
            ],
            options={
                'verbose_name': 'Sorğu',
                'verbose_name_plural': 'Sorğular',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='NewsCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Kateqoriya')),
            ],
            options={
                'verbose_name': 'Kateqoriya',
                'verbose_name_plural': 'Xəbər kateqoriyaları',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='NewsTypeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Növ')),
            ],
            options={
                'verbose_name': 'Növ',
                'verbose_name_plural': 'Xəbər növləri',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='OfferQuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ad Soyad')),
                ('email', models.EmailField(max_length=256, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Mesaj')),
            ],
            options={
                'verbose_name': 'Təklif/Sual',
                'verbose_name_plural': 'Təklif və Suallar',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='PageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Loqo')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ikon')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Əsas səhifə başlığı')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Əsas səhifə meta izahı')),
                ('keywords', models.TextField(blank=True, null=True, verbose_name='Əsas səhifə açar sözləri')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Telefon')),
                ('email', models.EmailField(max_length=256, verbose_name='Email')),
                ('address', models.TextField(verbose_name='Ünvan')),
                ('about', models.TextField(blank=True, null=True, verbose_name='Haqqımızda')),
                ('charter', models.TextField(blank=True, null=True, verbose_name='Nizamnamə')),
            ],
            options={
                'verbose_name': 'Parametr',
                'verbose_name_plural': 'Parametrlər',
            },
        ),
        migrations.CreateModel(
            name='VolunteersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ad soyad')),
                ('email', models.EmailField(max_length=256, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefon')),
                ('address', models.CharField(max_length=256, verbose_name='Ünvan')),
                ('message', models.TextField(verbose_name='Mesaj')),
            ],
            options={
                'verbose_name': 'Könüllü',
                'verbose_name_plural': 'Könüllülər',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='SocialMediaAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Ad')),
                ('link', models.URLField(max_length=256, verbose_name='Link')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialmediaaccounts', to='gtib.pagesettings')),
            ],
            options={
                'verbose_name': 'Sosial Media Hesabı',
                'verbose_name_plural': 'Sosial Media Hesabları',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Başlıq şəkli')),
                ('title', models.CharField(max_length=300, verbose_name='Başlıq')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Mövzu')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Nəşr olunma tarixi')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Yenilənmə tarixi')),
                ('categories', models.ManyToManyField(related_name='categorynews', to='gtib.newscategorymodel')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='typenews', to='gtib.newstypemodel')),
            ],
            options={
                'verbose_name': 'Xəbər',
                'verbose_name_plural': 'Xəbərlər',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='FormmChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=256, verbose_name='Seçim')),
                ('vote_number', models.IntegerField(default=0, verbose_name='Səs sayı')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formchoices', to='gtib.formmmodel')),
            ],
            options={
                'verbose_name': 'Seçim',
                'verbose_name_plural': 'Sorğu seçimləri',
                'ordering': ('-id',),
            },
        ),
    ]
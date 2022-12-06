# Generated by Django 2.2.24 on 2022-12-06 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20221206_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(max_length=200, verbose_name='Кто жаловался')),
                ('complaint', models.TextField(verbose_name='Текст жалобы')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='сomplaints', to='property.Flat', verbose_name='Адрес')),
            ],
        ),
    ]
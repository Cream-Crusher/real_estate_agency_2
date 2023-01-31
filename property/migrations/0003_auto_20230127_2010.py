# Generated by Django 2.2.24 on 2022-12-06 15:58

from django.db import migrations


def change_building_status(apps, Flat):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gt=2013).update(new_building=True)
    Flat.objects.filter(construction_year__lte=2013).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20230127_2008'),
    ]

    operations = [
        migrations.RunPython(change_building_status),
    ]
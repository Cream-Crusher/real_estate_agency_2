# Generated by Django 2.2.24 on 2022-12-07 14:47
import phonenumbers

from django.db import migrations


def normalization_number(apps, Flat):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all().iterator():

        phonenumber = flat.phonenumber
        phone_number = phonenumbers.parse(phonenumber, 'RU')

        if phonenumbers.is_possible_number(phone_number):
            flat.owner_pure_phone = phone_number

        elif phonenumbers.is_valid_number(phone_number):
            flat.owner_pure_phone = False

        else:
            flat.owner_pure_phone = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)

        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20221221_1905'),
    ]

    operations = [
        migrations.RunPython(normalization_number)
    ]
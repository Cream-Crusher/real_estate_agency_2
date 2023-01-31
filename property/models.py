from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Flat(models.Model):
    BUILDING_TYPES = (
        ('NEW_BUILDING', 'Новостройка'),
        ('OLD_BUILDING', 'Cтарое здание'),
        ('UNKNOWN', 'Неизвестно'),
    )

    new_building = models.BooleanField('Статус постройки здания', choices=BUILDING_TYPES, db_index=True, default='UNKNOWN', null=True)
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    liked_by = models.ManyToManyField(User, related_name="liked_apartments", verbose_name='лайки', blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200)
    phonenumber = models.CharField('Номер владельца', max_length=20)
    pure_phone = PhoneNumberField('Нормализованный номер владельца', blank=True, region="RU")
    apartments = models.ManyToManyField(Flat, verbose_name='Квартир(а\ы) в собственности', related_name="owners", blank=True)

    def __str__(self):
        return self.name


class UserComplaint(models.Model):
    flat = models.ForeignKey(Flat, null=True, on_delete=models.CASCADE, related_name='complaints', verbose_name='Адрес')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='complaints', verbose_name='Кто жаловался')
    text = models.TextField(verbose_name='Текст жалобы')

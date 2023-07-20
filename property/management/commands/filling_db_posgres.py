import psycopg2

from config import dbname, user, password, host
from django.core.management.base import BaseCommand
from ...models import Flat


conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host
    )
cursor = conn.cursor()


def filling_models_complaint(flatid, ownerid, wordsСomplaint):

    cursor.execute(f'''INSERT INTO complaint (
        flatid,
        ownerid,
        wordsСomplaint
        ) VALUES (
        {flatid},
        {ownerid},
        '{wordsСomplaint}'
        )''')
    conn.commit()


def filling_models_likeby(flatid, ownerid):
    cursor.execute(f'''INSERT INTO likeby (
        flatid,
        ownerid
        ) VALUES (
        {flatid},
        {ownerid}
        )''')
    conn.commit()


def filling_models_owner(owner):
    cursor.execute(f'''INSERT INTO apartmentowner (
        nameowner,
        phonenumber,
        apartments
        ) VALUES (
        '{owner.name}',
        '{owner.pure_phone}',
        '{owner.apartments.first()}'
        )''')
    conn.commit()


def filling_models_flat(flat, ownerid):
    cursor.execute(f'''INSERT INTO flat (
        newbuilding,
        description,
        price,
        town,
        towndistrict,
        address,
        floornumber,
        roomsnumber,
        hasbalcony,
        active,
        constructionyear,
        createdat,
        ownerid
        ) VALUES (
        {flat.new_building},
        '{flat.description}',
        '{flat.price}',
        '{flat.town}',
        '{flat.town_district}',
        '{flat.address}',
        {flat.floor},
        {flat.rooms_number},
        {flat.has_balcony},
        {flat.active},
        {flat.construction_year},
        now(),
        {ownerid}
        )''')
    conn.commit()


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument('flat', nargs='?', type=str)  # TODO ТУТ БУДЕТ СПОСОБ ДОАБВЛЕНИЯ НОВЫХ данных

    def handle(self, *args, **options):

        flats = Flat.objects.all()
        ownerid = 14628  # начало ownerid(после многих перезапусков)
        flatid = 197371  # начало flatid(после многих перезапусков)

        for flat in flats:
            try:
                owner = flat.owners.first()
                wordsСomplaint = 'тут жалоба'
                filling_models_owner(owner)
                filling_models_flat(flat, ownerid)
                filling_models_likeby(flatid, ownerid)
                filling_models_complaint(flatid, ownerid, wordsСomplaint)
                ownerid += 1
                flatid += 1
            except:
                continue

        conn.close()
        cursor.close()

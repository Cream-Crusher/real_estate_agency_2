import psycopg2

from django.shortcuts import render
from config import dbname, user, password, host

conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host
    )
cursor = conn.cursor()


def format_price(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def get_activ_towns():
    query = 'SELECT DISTINCT town FROM Flat WHERE newbuilding ORDER BY town'
    cursor.execute(query)
    query_towns = cursor.fetchall()

    return list(zip(*query_towns))[0]


def get_filter_flats(town, min_price, max_price, new_building):
    query = ("SELECT * FROM Flat WHERE True ")

    if town:
        query += f" AND town='{town}'"
    if min_price:
        query += f" AND price>{min_price}"
    if max_price:
        query += f" AND price<{max_price}"
    if new_building:
        query += f" AND newbuilding={new_building}"

    cursor.execute(query)

    return cursor.fetchall()


def show_flats(request):
    flats = []
    town = request.GET.get('town')
    min_price = format_price(request.GET.get('min_price'))
    max_price = format_price(request.GET.get('max_price'))
    new_building = request.GET.get('new_building') == '1'

    towns = get_activ_towns()
    query_flats = get_filter_flats(town, min_price, max_price, new_building)

    for flat in query_flats:
        flats.append(
            {
                'new_building': flat[1],
                'description': flat[2],
                'price': flat[3],
                'town': flat[4],
                'town_district': flat[5],
                'address': flat[6],
                'floor_number': flat[7],
                'rooms_number': flat[8],
                'hasbalcony': flat[9],
                'active': flat[10],
                'construction_year': flat[11],
                'createdat': flat[12],
            }
        )

    return render(request, 'flats_list.html', {
        'flats': flats[:10],
        'towns': towns,
        'active_town': town,
        'max_price': max_price,
        'min_price': min_price,
        'new_building': new_building})
